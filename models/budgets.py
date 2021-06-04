from FDBHandler import con
import datetime


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


def getAllBudgets(page, filters, codvend, flagAdmin):
    now = datetime.datetime.now()

    filtersQuery = ''
    if(not filters['ENVIADO']):
        filtersQuery += " AND (DATAFATURADO IS NOT NULL OR (SELECT COUNT(*) FROM ORCAMENTOPROD WHERE ORCAMENTO.CODORC = ORCAMENTOPROD.CODORC) = '0')"
    if(not filters['FATURADO']):
        filtersQuery += ' AND DATAFATURADO IS NULL'
    if(not filters['REFEITO']):
        filtersQuery += " AND (SELECT COUNT(*) FROM ORCAMENTOPROD WHERE ORCAMENTO.CODORC = ORCAMENTOPROD.CODORC) != '0'"

    sellerQuery = ''
    if not flagAdmin:
        sellerQuery = f"AND CODVENDED = '{codvend}'"

    query = f"""
    SELECT FIRST 30 SKIP {30 * (page - 1)}
    CODORC, DATA, NOMECLI, HORA, VALORTOTALORCAMENTO, NOMETIPOMOVIMENTO, DATAFATURADO, OBS, CODCLI, NUMEROORCAMENTO,
    OBSNOTAFISCAL, VALORFRETE, ORCAMENTO.CODTIPOMOVIMENTO, (SELECT COUNT(*) FROM ORCAMENTOPROD WHERE ORCAMENTO.CODORC = ORCAMENTOPROD.CODORC) AS QNTPRODS
    FROM ORCAMENTO
    LEFT JOIN TIPOMOVIMENTO ON ORCAMENTO.CODTIPOMOVIMENTO = TIPOMOVIMENTO.CODTIPOMOVIMENTO
    WHERE DATA = '{now.date()}'
    {sellerQuery}
    AND NUMCUPOM IS NULL
    {filtersQuery}
    ORDER BY DATA DESC, HORA DESC
    """
    return queryToDict(query)
