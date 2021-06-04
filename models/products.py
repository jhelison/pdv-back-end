from FDBHandler import con


def queryToDict(sqlQuery, flagAdmin):
    def convertToText(typeClass, num):
        if('string' not in str(typeClass)):
            try:
                return str(num)
            except:
                return ''
        else:
            return num

    def addExtraInfo(productDict):
        try:
            price = "{:.2f}".format(float(productDict['PRECO']))
        except:
            price = "0.00"

        return {
            'CODPROD': productDict['CODPROD'],
            'CODIGO': productDict['CODIGO'],
            'QUANTIDADE': '1.0',
            'VALORUNITARIO': price,
            'PRECOTABELA': price,
            'ALIQDESCONTOITEM': '0.00',
            'VALORDESCONTOITEM': '0.00',
            'ALIQACRESCIMOITEM': '0.00',
            'VALORACRESCIMOITEM': '0.00',
            'VALORTOTAL': price,
            'NOMEPROD': productDict['NOMEPROD'],
            'UNIDADE': productDict['UNIDADE'],
            'DESCMAXIMO': productDict['DESCMAXIMO'] if not flagAdmin else 100.0,
            'ESTATU': productDict['ESTATU']
        }

    cur = con.cursor()
    cur.execute(sqlQuery)
    data = cur.fetchall()
    return [addExtraInfo({desc[0]:convertToText(desc[1], row[index]) for index, desc in enumerate(cur.description)}) for row in data]


def getByNameOrCode(text, flagAdmin):
    text = text.replace('\'', '\'\'')

    def buildInteliSearch():
        searchQuery = ''
        searchedText = text.split()
        for index, wordText in enumerate(searchedText):
            searchQuery += f"PRODUTO.NOMEPROD SIMILAR TO '%{wordText}%'"
            if((index + 1) < len(searchedText)):
                searchQuery += " AND "
        return searchQuery

    def getSearchColumns():
        if(text):
            try:
                int(text)
                return f"AND (PRODUTO.CODIGO SIMILAR TO '%{text}%' OR ({buildInteliSearch()}))"
            except:
                return f"AND ({ buildInteliSearch() })"
        return ""

    query = f"""
    SELECT FIRST 50 PRODUTO.CODPROD, PRODUTO.CODIGO, PRODUTO.NOMEPROD, PRODUTO.UNIDADE, PRODUTO.DESCMAXIMO, PRODUTOESTOQUE.ESTATU, PRODUTOPRECO.PRECO 
    FROM PRODUTO
    LEFT JOIN PRODUTOESTOQUE ON PRODUTO.CODPROD = PRODUTOESTOQUE.CODPROD
    LEFT JOIN PRODUTOPRECO ON PRODUTO.CODPROD = PRODUTOPRECO.CODPROD
    WHERE PRODUTO.FLAGINATIVO = 'N'
    AND PRODUTOESTOQUE.CODEMPRESA = 1
    AND PRODUTOPRECO.CODPRECO = '000000001'
    {getSearchColumns()}
    ORDER BY PRODUTOPRECO.PRECO 
    """
    res = queryToDict(query, flagAdmin)
    return res
