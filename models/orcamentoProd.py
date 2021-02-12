from firebirdConnection import con

fixedData = {
    "BASEICMS" : 0.0000,
    "VALORICMS" : 0.0000,
    "BASEIPI" : 0.0000,
    "ALIQIPI" : 0.0000,
    "VALORIPI" : 0.0000,
    "ALIQISS" : 0.0000,
    "VALORISS" : 0.0000,
    "BASESUBSTTRIBUTARIA" : 0.0000,
    "VALORSUBSTTRIBUTARIA" : 0.0000,
    "VALORFRETERATEADO" : 0.0000,
    "VALORSEGURORATEADO" : 0.0000,
    "VALOROUTRASDESPRATEADO" : 0.0000,
    "VALORACRESCIMORATEADO" : 0.0000,
    "VALORDESCONTORATEADO" : 0.0000, #Pesquisar como funciona
    "FLAG1" : "Y",
    "FLAG2" : "Y", #O que significam essas flags?
    "FLAG3" : "N",
    "BASECOFINS" : 0.0000,
    "ALIQCOFINS" : 0.0000,
    "VALORCOFINS" : 0.0000,
    "BASEPIS" : 0.0000,
    "ALIQPIS" : 0.0000,
    "VALORPIS" : 0.0000,
    "FLAGCANCELADO" : "N",
    "FLAGITEMCANCELADO" : "N",
    "ALIQTRIBUTACAO" : 0.0000,
    "ALIQFCP" : 0.0000,
    "VALORFCP" : 0.0000,
    "VALORFCPSUBSTTRIBUTARIA" : 0.0000,
    "ALIQFCP_ST_UF_DESTINO" : 0.0000,
    "GTIN" : "",
    "GTINTRIB" : "",
    "UNIDADETRIB" : "",
    "QUANTIDADEEMBALAGEM" : 0.0000,
    "FLAGTIPOACRESCIMOITEM" : "V",
    "FLAGTIPODESCONTOITEM" : "V",
    "COMPLEMENTO" : ""
}

varData = {
    "CODEMPRESA" : 3,
    "CODPRECO" : "000000001",
}

def basicQueryToDict(sqlQuery):
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
    return [{desc[0]:convertToText(desc[1],row[index]) for index, desc in enumerate(cur.description)} for row in data]

def queryToDict(sqlQuery, flagAdmin):
    def convertToText(typeClass, num):
        if('string' not in str(typeClass)):
            try:
                if(str(num) == 'None'):
                    return ''
                return str(num)
            except:
                return ''
        else:
            return num
        
    def addExtraInfo(productDict):
        def addDecimal(val):
            try:
                return "{:.2f}".format(float(val))
            except:
                return val
                    
        return {
        'CODPROD': productDict['CODPROD'],
        'CODIGO' : productDict['CODIGO'],
        'QUANTIDADE': "{:.1f}".format(float(productDict['QUANTIDADE'])),
        'VALORUNITARIO': addDecimal(float(productDict['VALORTOTAL']) / float(productDict['QUANTIDADE'])),
        'PRECOTABELA': addDecimal(productDict['PRECOTABELA']),
        'ALIQDESCONTOITEM': addDecimal(productDict['ALIQDESCONTOITEM']),
        'VALORDESCONTOITEM': addDecimal(productDict['VALORDESCONTOITEM']),
        'ALIQACRESCIMOITEM': addDecimal(productDict['ALIQACRESCIMOITEM']),
        'VALORACRESCIMOITEM': addDecimal(productDict['VALORACRESCIMOITEM']),
        'VALORTOTAL': addDecimal(productDict['VALORTOTAL']),
        'NOMEPROD': productDict['NOMEPROD'],
        'UNIDADE': productDict['UNIDADE'],
        'DESCMAXIMO': productDict['DESCMAXIMO'] if not flagAdmin else 100.0,
        'ESTATU': productDict['ESTATU']
        }
        
    cur = con.cursor()
    cur.execute(sqlQuery)
    data = cur.fetchall()
    return [addExtraInfo({desc[0]:convertToText(desc[1],row[index]) for index, desc in enumerate(cur.description)}) for row in data]

def getNextCod():
    query = """
    SELECT SKIP ((SELECT COUNT(*) FROM ORCAMENTOPROD) - 1)
    CODORCPROD FROM ORCAMENTOPROD
    ORDER BY CODORCPROD
    """
    res = basicQueryToDict(query)[0]
    res['CODORCPROD'] = int(res['CODORCPROD']) + 1
    
    while True:
        CODORCPRODtring = res['CODORCPROD']
        CODORCPRODtring = f'{CODORCPRODtring:09}'
        query = f"SELECT CODORCPROD FROM ORCAMENTOPROD WHERE CODORCPROD = '{CODORCPRODtring}'"
        ans = basicQueryToDict(query)
        if(len(ans) == 0):
            break
        res['CODORCPROD'] = res['CODORCPROD'] + 1
    
    CODORCPROD = res['CODORCPROD']
    return f'{CODORCPROD:09}'

def getORCAMENTOPRODCodes(quantity):
    codes = []
    
    query = """
    SELECT NEXT VALUE FOR SEQ_CODORCPROD FROM RDB$DATABASE;
    """
    
    for num in range(quantity):
        code = con.cursor().execute(query).fetchone()[0]
        codes.append(f'{code:09}')
        
    return codes

def buildBudgetProductData(budgetProduct, index, orcData):
    CODPROD = budgetProduct['CODPROD']
    query = f"""
    SELECT CODCALCULOICMS, CODCLASSIFICACAOFISCAL, UNIDADE, CFOPDENTROUF, CFOPFORAUF, CODTRIBUTACAOECF, CODIGO, CUSTOREAL
    FROM PRODUTO 
    WHERE CODPROD = '{CODPROD}'
    """
    PRODUTO = basicQueryToDict(query)[0]
    
    CODTRIBUTACAOECF = PRODUTO['CODTRIBUTACAOECF']
    query = f"""
    SELECT TIPOTRIBUTACAO, CSOSN FROM TRIBUTACAOECF
    WHERE CODTRIBUTACAOECF = '{CODTRIBUTACAOECF}'
    """
    TRIBUTACAOECF = basicQueryToDict(query)[0]
    
    def getCFOP():
        if(orcData['CODCFOP'] == '5102'):
            if(PRODUTO['CFOPDENTROUF'] != 'None'):
                return '5' + PRODUTO['CFOPDENTROUF']
            else:
                return '5102'
        else:
            if(PRODUTO['CFOPFORAUF'] != 'None'):
                return '6' + PRODUTO['CFOPFORAUF']
            return '6102'
    
    inserData = {
        "CODORC" : orcData['CODORC'],
        "CODPROD" : budgetProduct['CODPROD'],
        "QUANTIDADE" : float(budgetProduct['QUANTIDADE']),
        "VALORUNITARIO" : float(budgetProduct['PRECOTABELA']),
        "ALIQDESCONTOITEM" : float(budgetProduct['ALIQDESCONTOITEM']),
        "VALORDESCONTOITEM" : float(budgetProduct['VALORDESCONTOITEM']),
        "ALIQACRESCIMOITEM" : float(budgetProduct['ALIQACRESCIMOITEM']),
        "VALORACRESCIMOITEM" : float(budgetProduct['VALORACRESCIMOITEM']),
        "VALORTOTAL" : float(budgetProduct['VALORTOTAL']),
        "DESCRICAOPRODUTO" : budgetProduct['NOMEPROD'].replace("'", "''"),
        "PRECOTABELA" : float(budgetProduct['PRECOTABELA']),
        "CODCFOP" : getCFOP(),
        "CUSTOREAL" : PRODUTO['CUSTOREAL'],
        "CSOSN" : TRIBUTACAOECF['CSOSN'],
        "NUMEROITEM" : index,
        "CODCALCULOICMS" : PRODUTO['CODCALCULOICMS'],
        "CODCLASSIFICACAOFISCAL" : PRODUTO['CODCLASSIFICACAOFISCAL'],
        "CODIGOPRODUTO" : PRODUTO['CODIGO'],
        "UNIDADE" : PRODUTO['UNIDADE'],
        "TIPOTRIBUTACAO" : TRIBUTACAOECF['TIPOTRIBUTACAO'],
        "NUMEROORCAMENTO" : orcData['NUMEROORCAMENTO'],
        "CODSITUACAOTRIBUTARIA" : "00 " if getCFOP() == '5102' else ''
    }
    
    return {**inserData, **fixedData, **varData}

def getByCodorc(val, flagAdmin):
    query = f"""
    SELECT ORCAMENTOPROD.CODPROD, PRODUTO.CODIGO, ORCAMENTOPROD.QUANTIDADE, ORCAMENTOPROD.VALORUNITARIO,
    ORCAMENTOPROD.PRECOTABELA, ORCAMENTOPROD.ALIQDESCONTOITEM, ORCAMENTOPROD.VALORDESCONTOITEM,
    ORCAMENTOPROD.ALIQACRESCIMOITEM, ORCAMENTOPROD.VALORACRESCIMOITEM, ORCAMENTOPROD.VALORTOTAL,
    PRODUTO.NOMEPROD, PRODUTO.UNIDADE, PRODUTO.DESCMAXIMO, PRODUTOESTOQUE.ESTATU
    FROM ORCAMENTOPROD
    LEFT JOIN PRODUTO ON ORCAMENTOPROD.CODPROD = PRODUTO.CODPROD
    LEFT JOIN PRODUTOESTOQUE ON PRODUTO.CODPROD = PRODUTOESTOQUE.CODPROD
    WHERE CODORC = '{val}'
    AND PRODUTOESTOQUE.CODEMPRESA = 1
    """
    
    return queryToDict(query, flagAdmin)