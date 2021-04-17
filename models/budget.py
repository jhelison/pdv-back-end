from firebirdConnection import con
import datetime

from models.orcamentoProd import buildBudgetProductData, getORCAMENTOPRODCodes

fixedData = {
    "IDENTIFICADORDESTINO": "1",
    "VALORENTRADA": 0.0000,
    "CAMPOVALOR1": 100.0000,
    "VALORTOTALIPI": 0.0000,
    "FLAGFRETE": "D",
    "VALORICMS": 0.0000,
    "BASEICMS": 0.0000,
    "VALOROUTRASDESPESAS": 0.0000,
    "VALORSUBSTTRIBUTARIA": 0.0000,
    "BASESUBSTTRIBUTARIA": 0.0000,
    "VALORSEGURO": 0.0000,
    "FLAGDELIVERY": "N",
    "FLAGSTATUS": "O",
    "FLAGPALM": "0",
    "RENTABILIDADE": 0.0000,
    "QUANTIDADEVOLUMES": 0,
    "INDPRESENCA": "0",
    "VALORFCP": 0.0000,
    "VALORFCPSUBSTTRIBUTARIA": 0.0000
}

# All those values should change in future updates
varData = {
    "CODPRECO": "000000001",
    "CODEMPRESA": 3,
    "CODUSER": "000000010",
    "CODSETORESTOQUE": "000000001",
}


def queryToDict(sqlQuery):
    def convertToText(typeClass, num):
        if('string' not in str(typeClass)):
            try:
                return str(num)
            except:
                return ''
        else:
            return num

    cur = con.cursor()
    cur.execute(sqlQuery)
    data = cur.fetchall()
    return [{desc[0]:convertToText(desc[1], row[index]) for index, desc in enumerate(cur.description)} for row in data]


def getNextCod():
    query = "SELECT SKIP ((SELECT count(*) - 1 FROM ORCAMENTO)) CODORC, NUMEROORCAMENTO FROM ORCAMENTO ORDER BY CODORC"
    res = queryToDict(query)[0]
    res['CODORC'] = int(res['CODORC'])
    res['NUMEROORCAMENTO'] = int(res['NUMEROORCAMENTO'])

    while True:
        CODORCtring = res['CODORC']
        CODORCtring = f'{CODORCtring:09}'
        query = f"SELECT CODORC FROM ORCAMENTO WHERE CODORC = '{CODORCtring}'"
        ans = queryToDict(query)
        if(len(ans) == 0):
            break
        res['CODORC'] = res['CODORC'] + 1

    while True:
        res['NUMEROORCAMENTO'] = res['NUMEROORCAMENTO'] + 1
        NUMEROORCAMENTOString = res['NUMEROORCAMENTO']
        NUMEROORCAMENTOString = f'{NUMEROORCAMENTOString:09}'
        query = f"SELECT NUMEROORCAMENTO FROM ORCAMENTO WHERE NUMEROORCAMENTO = '{NUMEROORCAMENTOString}'"
        ans = queryToDict(query)
        if(len(ans) == 0):
            break

    CODORC = res['CODORC']
    NUMEROORCAMENTO = res['NUMEROORCAMENTO']
    res['CODORC'] = f'{CODORC:09}'
    res['NUMEROORCAMENTO'] = f'{NUMEROORCAMENTO:09}'

    return res


def buildData(data, codvend):
    def timeFromMs(val):
        h = f'{int(val / 60 / 60):02}'
        m = f'{int((val / 60) % 60):02}'
        s = f'{int(val % (60)):02}'
        return f'{h}:{m}:{s}'

    now = datetime.datetime.now()

    def getCODCLI():
        if data['customer']['fromDatabase']:
            return {'CODCLI': data['customer']['data']['CODCLI']}
        return {}

    dataBuilded = {
        "DATA": now.date(),
        "FLAGCLI": "Y" if data['customer']['fromDatabase'] else "N",
        "NOMECLI": data['customer']['data']['NOMECLI'],
        "CODVENDED": codvend,
        "OBS": data['OBS'],
        "ALIQDESCONTO": 0.0000,  # Fixed
        "VALORFRETE": float(data['VALORFRETE']),
        "VALORACRESCIMO": 0.0000,
        "OBSNOTAFISCAL": data['OBSNOTAFISCAL'],
        "CODCFOP": "5102" if data['customer']['data']['ESTADO'] == 'MA' or data['customer']['data']['ESTADO'] == '' else "6102",
        "VALORDESCONTO": 0.0000,  # Fixed
        "ALIQACRESCIMO": 0.0000,  # Fixed
        "VALORTOTALORCAMENTO": sum([float(product["VALORTOTAL"]) for product in data['products']]) + float(data['VALORFRETE']),
        "VALORTOTALPRODUTOS": sum([float(product["VALORTOTAL"]) for product in data['products']]),
        "CODTIPOMOVIMENTO": data['movimento'],
        "TEMPO": timeFromMs(data["TEMPO"] / 1000)
    }

    return {**dataBuilded, **varData, **fixedData, **getNextCod(), **getCODCLI()}


def addNewBudget(data, codvend):
    start = datetime.datetime.now()
    buildedData = buildData(data, codvend)

    columnsQuery = '('
    valuesQuery = '('
    for item in buildedData.items():
        columnsQuery += item[0] + ', '
        valuesQuery += f"'{item[1]}'" + ', '
    columnsQuery = columnsQuery[:-2] + ')'
    valuesQuery = valuesQuery[:-2] + ')'

    query = f"""
    INSERT INTO ORCAMENTO {columnsQuery}
    VALUES {valuesQuery}
    """

    con.cursor().execute(query)

    codes = getORCAMENTOPRODCodes(len(data['products']))
    for index, budgetProduct in enumerate(data['products']):
        CODORCPROD = {'CODORCPROD': codes[index]}
        buildedProductData = {
            **buildBudgetProductData(budgetProduct, index + 1, buildedData), **CODORCPROD}

        columnsQuery = '('
        valuesQuery = '('
        for item in buildedProductData.items():
            columnsQuery += item[0] + ', '
            valuesQuery += f"'{item[1]}'" + ', '
        columnsQuery = columnsQuery[:-2] + ')'
        valuesQuery = valuesQuery[:-2] + ')'

        query = f"""
        INSERT INTO ORCAMENTOPROD {columnsQuery}
        VALUES {valuesQuery}
        """
        con.cursor().execute(query)

    if(data['fromBudget']):
        budgetCode = data['fromBudget']
        query = f"""
        SELECT DATAFATURADO FROM ORCAMENTO WHERE CODORC = '{budgetCode}'
        """
        res = con.cursor().execute(query).fetchone()

        if not res[0]:
            query = f"""
            DELETE FROM ORCAMENTOPROD
            WHERE CODORC = '{budgetCode}'
            """
            con.cursor().execute(query)

            query = f"""
            UPDATE ORCAMENTO
            SET VALORFRETE = '0'
            WHERE CODORC = '{budgetCode}'
            """
            con.cursor().execute(query)

    con.commit()
