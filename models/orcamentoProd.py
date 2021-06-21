from datetime import datetime
import sys

sys.path.insert(0, './')
from utility.FDB_handler import FDBModel, Column

class BudgetProd(FDBModel):
    __tablename__ = 'ORCAMENTOPROD'
    
    CODORCPROD = Column(is_primary_key=True, use_generator='SEQ_CODORCPROD')
    
    #Main Components
    CODORC = Column()
    CODPROD = Column()
    QUANTIDADE = Column()
    VALORUNITARIO = Column()
    PRECOTABELA = Column()
    ALIQDESCONTOITEM = Column()
    VALORDESCONTOITEM = Column()
    ALIQACRESCIMOITEM = Column()
    VALORACRESCIMOITEM = Column()
    VALORTOTAL = Column()
    DATAINCLUSAO = Column()
    CODCFOP = Column() #Important
    DESCRICAOPRODUTO = Column()
    CUSTOREAL = Column() #What is this?
    CODCALCULOICMS = Column() #Important
    CODSITUACAOTRIBUTARIA = Column() #Important
    CODCLASSIFICACAOFISCAL = Column() #Important
    NUMEROITEM = Column()
    
    #Fixed components
    BASEICMS = Column()
    VALORICMS = Column()
    BASEIPI = Column()
    ALIQIPI = Column()
    VALORIPI = Column()
    ALIQISS = Column()
    VALORISS = Column()
    BASESUBSTTRIBUTARIA = Column()
    VALORSUBSTTRIBUTARIA = Column()
    VALORFRETERATEADO = Column()
    VALORSEGURORATEADO = Column()
    VALOROUTRASDESPRATEADO = Column()
    VALORACRESCIMORATEADO = Column()
    VALORDESCONTORATEADO = Column()
    FLAG1 = Column()
    FLAG2 = Column()
    FLAG3 = Column()
    BASECOFINS = Column()
    ALIQCOFINS = Column()
    VALORCOFINS = Column()
    BASEPIS = Column()
    ALIQPIS = Column()
    VALORPIS = Column()
    FLAGCANCELADO = Column()
    FLAGITEMCANCELADO = Column()
    ALIQTRIBUTACAO = Column()
    ALIQFCP = Column()
    VALORFCP = Column()
    VALORFCPSUBSTTRIBUTARIA = Column()
    ALIQFCP_ST_UF_DESTINO = Column()
    QUANTIDADEEMBALAGEM = Column()
    FLAGTIPOACRESCIMOITEM = Column()
    FLAGTIPODESCONTOITEM = Column()
    ALIQICMS = Column()
    
    #Var data
    CODEMPRESA = Column()
    CODPRECO = Column()
    
    def __init__(self,
                CODORCPROD,
                CODORC,
                CODPROD,
                
                QUANTIDADE = None,
                VALORUNITARIO = None,
                PRECOTABELA = None,
                ALIQDESCONTOITEM = None,
                VALORDESCONTOITEM = None,
                ALIQACRESCIMOITEM = None,
                VALORACRESCIMOITEM = None,
                VALORTOTAL = None,
                DATAINCLUSAO = None,
                CODCFOP = None,
                DESCRICAOPRODUTO = None,
                CUSTOREAL = None,
                CODCALCULOICMS = None,
                CODSITUACAOTRIBUTARIA = None,
                CODCLASSIFICACAOFISCAL = None,
                NUMEROITEM = None,
                
                BASEICMS = None,
                VALORICMS = None,
                BASEIPI = None,
                ALIQIPI = None,
                VALORIPI = None,
                ALIQISS = None,
                VALORISS = None,
                BASESUBSTTRIBUTARIA = None,
                VALORSUBSTTRIBUTARIA = None,
                VALORFRETERATEADO = None,
                VALORSEGURORATEADO = None,
                VALOROUTRASDESPRATEADO = None,
                VALORACRESCIMORATEADO = None,
                VALORDESCONTORATEADO = None,
                FLAG1 = None,
                FLAG2 = None,
                FLAG3 = None,
                BASECOFINS = None,
                ALIQCOFINS = None,
                VALORCOFINS = None,
                BASEPIS = None,
                ALIQPIS = None,
                VALORPIS = None,
                FLAGCANCELADO = None,
                FLAGITEMCANCELADO = None,
                ALIQTRIBUTACAO = None,
                ALIQFCP = None,
                VALORFCP = None,
                VALORFCPSUBSTTRIBUTARIA = None,
                ALIQFCP_ST_UF_DESTINO = None,
                QUANTIDADEEMBALAGEM = None,
                FLAGTIPOACRESCIMOITEM = None,
                FLAGTIPODESCONTOITEM = None,
                ALIQICMS = None,
                
                CODEMPRESA = None,
                CODPRECO = None) -> None:
        
        self.CODORCPROD = CODORCPROD
        
        self.CODORC = CODORC
        self.CODPROD = CODPROD
        self.QUANTIDADE = QUANTIDADE
        self.VALORUNITARIO = VALORUNITARIO
        self.PRECOTABELA = PRECOTABELA
        self.ALIQDESCONTOITEM = ALIQDESCONTOITEM
        self.VALORDESCONTOITEM = VALORDESCONTOITEM
        self.ALIQACRESCIMOITEM = ALIQACRESCIMOITEM
        self.VALORACRESCIMOITEM = VALORACRESCIMOITEM
        self.VALORTOTAL = VALORTOTAL
        self.DATAINCLUSAO = DATAINCLUSAO
        self.CODCFOP = CODCFOP
        self.DESCRICAOPRODUTO = DESCRICAOPRODUTO
        self.CUSTOREAL = CUSTOREAL
        self.CODCALCULOICMS = CODCALCULOICMS
        self.CODSITUACAOTRIBUTARIA = CODSITUACAOTRIBUTARIA
        self.CODCLASSIFICACAOFISCAL = CODCLASSIFICACAOFISCAL
        self.NUMEROITEM = NUMEROITEM
        
        self.BASEICMS = BASEICMS if BASEICMS != None else 0.0
        self.VALORICMS = VALORICMS if VALORICMS != None else 0.0
        self.BASEIPI = BASEIPI if BASEIPI != None else 0.0
        self.ALIQIPI = ALIQIPI if ALIQIPI != None else 0.0
        self.VALORIPI = VALORIPI if VALORIPI != None else 0.0
        self.ALIQISS = ALIQISS if ALIQISS != None else 0.0
        self.VALORISS = VALORISS if VALORISS != None else 0.0
        self.BASESUBSTTRIBUTARIA = BASESUBSTTRIBUTARIA if BASESUBSTTRIBUTARIA != None else 0.0
        self.VALORSUBSTTRIBUTARIA = VALORSUBSTTRIBUTARIA if VALORSUBSTTRIBUTARIA != None else 0.0
        self.VALORFRETERATEADO = VALORFRETERATEADO if VALORFRETERATEADO != None else 0.0
        self.VALORSEGURORATEADO = VALORSEGURORATEADO if VALORSEGURORATEADO != None else 0.0
        self.VALOROUTRASDESPRATEADO = VALOROUTRASDESPRATEADO if VALOROUTRASDESPRATEADO != None else 0.0
        self.VALORACRESCIMORATEADO = VALORACRESCIMORATEADO if VALORACRESCIMORATEADO != None else 0.0
        self.VALORDESCONTORATEADO = VALORDESCONTORATEADO if VALORDESCONTORATEADO != None else 0.0
        self.FLAG1 = FLAG1 if FLAG1 != None else 'Y'
        self.FLAG2 = FLAG2 if FLAG2 != None else 'Y'
        self.FLAG3 = FLAG3 if FLAG3 != None else 'N'
        self.BASECOFINS = BASECOFINS if BASECOFINS != None else 0.0
        self.ALIQCOFINS = ALIQCOFINS if ALIQCOFINS != None else 0.0
        self.VALORCOFINS = VALORCOFINS if VALORCOFINS != None else 0.0
        self.BASEPIS = BASEPIS if BASEPIS != None else 0.0
        self.ALIQPIS = ALIQPIS if ALIQPIS != None else 0.0
        self.VALORPIS = VALORPIS if VALORPIS != None else 0.0
        self.FLAGCANCELADO = FLAGCANCELADO if FLAGCANCELADO != None else 'N'
        self.FLAGITEMCANCELADO = FLAGITEMCANCELADO if FLAGITEMCANCELADO != None else 'N'
        self.ALIQTRIBUTACAO = ALIQTRIBUTACAO if ALIQTRIBUTACAO != None else 0.0 #Valor muda em operações fora do estado?
        self.ALIQFCP = ALIQFCP if ALIQFCP != None else 0.0
        self.VALORFCP = VALORFCP if VALORFCP != None else 0.0
        self.VALORFCPSUBSTTRIBUTARIA = VALORFCPSUBSTTRIBUTARIA if VALORFCPSUBSTTRIBUTARIA != None else 0.0
        self.ALIQFCP_ST_UF_DESTINO = ALIQFCP_ST_UF_DESTINO if ALIQFCP_ST_UF_DESTINO != None else 0.0
        self.QUANTIDADEEMBALAGEM = QUANTIDADEEMBALAGEM if QUANTIDADEEMBALAGEM != None else 0.0
        self.FLAGTIPOACRESCIMOITEM = FLAGTIPOACRESCIMOITEM if FLAGTIPOACRESCIMOITEM != None else 'V'
        self.FLAGTIPODESCONTOITEM = FLAGTIPODESCONTOITEM if FLAGTIPODESCONTOITEM != None else 'V'
        self.ALIQICMS = ALIQICMS if ALIQICMS != None else 0.0
        
        self.CODEMPRESA = CODEMPRESA if CODEMPRESA != None else 3
        self.CODPRECO = CODPRECO if CODPRECO != None else "000000001"
        
    def _on_insert(self):
        self.DATAINCLUSAO = datetime.now()
    
# fixedData = {
#     "BASEICMS": 0.0000,
#     "VALORICMS": 0.0000,
#     "BASEIPI": 0.0000,
#     "ALIQIPI": 0.0000,
#     "VALORIPI": 0.0000,
#     "ALIQISS": 0.0000,
#     "VALORISS": 0.0000,
#     "BASESUBSTTRIBUTARIA": 0.0000,
#     "VALORSUBSTTRIBUTARIA": 0.0000,
#     "VALORFRETERATEADO": 0.0000,
#     "VALORSEGURORATEADO": 0.0000,
#     "VALOROUTRASDESPRATEADO": 0.0000,
#     "VALORACRESCIMORATEADO": 0.0000,
#     "VALORDESCONTORATEADO": 0.0000,  # Pesquisar como funciona
#     "FLAG1": "Y",
#     "FLAG2": "Y",  # O que significam essas flags?
#     "FLAG3": "N",
#     "BASECOFINS": 0.0000,
#     "ALIQCOFINS": 0.0000,
#     "VALORCOFINS": 0.0000,
#     "BASEPIS": 0.0000,
#     "ALIQPIS": 0.0000,
#     "VALORPIS": 0.0000,
#     "FLAGCANCELADO": "N",
#     "FLAGITEMCANCELADO": "N",
#     "ALIQTRIBUTACAO": 0.0000,
#     "ALIQFCP": 0.0000,
#     "VALORFCP": 0.0000,
#     "VALORFCPSUBSTTRIBUTARIA": 0.0000,
#     "ALIQFCP_ST_UF_DESTINO": 0.0000,
#     "GTIN": "",
#     "GTINTRIB": "",
#     "UNIDADETRIB": "",
#     "QUANTIDADEEMBALAGEM": 0.0000,
#     "FLAGTIPOACRESCIMOITEM": "V",
#     "FLAGTIPODESCONTOITEM": "V",
#     "COMPLEMENTO": ""
# }

# varData = {
#     "CODEMPRESA": 3,
#     "CODPRECO": "000000001",
# }


# def basicQueryToDict(sqlQuery):
#     def convertToText(typeClass, num):
#         if('string' not in str(typeClass)):
#             try:
#                 return str(num)
#             except:
#                 return ''
#         else:
#             return num

#     cur = con.cursor()
#     cur.execute(sqlQuery)
#     data = cur.fetchall()
#     return [{desc[0]:convertToText(desc[1], row[index]) for index, desc in enumerate(cur.description)} for row in data]


# def queryToDict(sqlQuery, flagAdmin):
#     def convertToText(typeClass, num):
#         if('string' not in str(typeClass)):
#             try:
#                 if(str(num) == 'None'):
#                     return ''
#                 return str(num)
#             except:
#                 return ''
#         else:
#             return num

#     def addExtraInfo(productDict):
#         def addDecimal(val):
#             try:
#                 return "{:.2f}".format(float(val))
#             except:
#                 return val

#         return {
#             'CODPROD': productDict['CODPROD'],
#             'CODIGO': productDict['CODIGO'],
#             'QUANTIDADE': "{:.1f}".format(float(productDict['QUANTIDADE'])),
#             'VALORUNITARIO': addDecimal(float(productDict['VALORTOTAL']) / float(productDict['QUANTIDADE'])),
#             'PRECOTABELA': addDecimal(productDict['PRECOTABELA']),
#             'ALIQDESCONTOITEM': addDecimal(productDict['ALIQDESCONTOITEM']),
#             'VALORDESCONTOITEM': addDecimal(productDict['VALORDESCONTOITEM']),
#             'ALIQACRESCIMOITEM': addDecimal(productDict['ALIQACRESCIMOITEM']),
#             'VALORACRESCIMOITEM': addDecimal(productDict['VALORACRESCIMOITEM']),
#             'VALORTOTAL': addDecimal(productDict['VALORTOTAL']),
#             'NOMEPROD': productDict['NOMEPROD'],
#             'UNIDADE': productDict['UNIDADE'],
#             'DESCMAXIMO': productDict['DESCMAXIMO'] if not flagAdmin else 100.0,
#             'ESTATU': productDict['ESTATU']
#         }

#     cur = con.cursor()
#     cur.execute(sqlQuery)
#     data = cur.fetchall()
#     return [addExtraInfo({desc[0]:convertToText(desc[1], row[index]) for index, desc in enumerate(cur.description)}) for row in data]


# def getNextCod():
#     query = """
#     SELECT SKIP ((SELECT COUNT(*) FROM ORCAMENTOPROD) - 1)
#     CODORCPROD FROM ORCAMENTOPROD
#     ORDER BY CODORCPROD
#     """
#     res = basicQueryToDict(query)[0]
#     res['CODORCPROD'] = int(res['CODORCPROD']) + 1

#     while True:
#         CODORCPRODtring = res['CODORCPROD']
#         CODORCPRODtring = f'{CODORCPRODtring:09}'
#         query = f"SELECT CODORCPROD FROM ORCAMENTOPROD WHERE CODORCPROD = '{CODORCPRODtring}'"
#         ans = basicQueryToDict(query)
#         if(len(ans) == 0):
#             break
#         res['CODORCPROD'] = res['CODORCPROD'] + 1

#     CODORCPROD = res['CODORCPROD']
#     return f'{CODORCPROD:09}'


# def getORCAMENTOPRODCodes(quantity):
#     codes = []

#     query = """
#     SELECT NEXT VALUE FOR SEQ_CODORCPROD FROM RDB$DATABASE;
#     """

#     for num in range(quantity):
#         code = con.cursor().execute(query).fetchone()[0]
#         codes.append(f'{code:09}')

#     return codes


# def buildBudgetProductData(budgetProduct, index, orcData):
#     CODPROD = budgetProduct['CODPROD']
#     query = f"""
#     SELECT CODCALCULOICMS, CODCLASSIFICACAOFISCAL, UNIDADE, CFOPDENTROUF, CFOPFORAUF, CODTRIBUTACAOECF, CODIGO, CUSTOREAL
#     FROM PRODUTO 
#     WHERE CODPROD = '{CODPROD}'
#     """
#     PRODUTO = basicQueryToDict(query)[0]

#     CODTRIBUTACAOECF = PRODUTO['CODTRIBUTACAOECF']
#     query = f"""
#     SELECT TIPOTRIBUTACAO, CSOSN FROM TRIBUTACAOECF
#     WHERE CODTRIBUTACAOECF = '{CODTRIBUTACAOECF}'
#     """
#     TRIBUTACAOECF = basicQueryToDict(query)[0]

#     def getCFOP():
#         if(orcData['CODCFOP'] == '5102'):
#             if(PRODUTO['CFOPDENTROUF'] != 'None'):
#                 return '5' + PRODUTO['CFOPDENTROUF']
#             else:
#                 return '5102'
#         else:
#             if(PRODUTO['CFOPFORAUF'] != 'None'):
#                 return '6' + PRODUTO['CFOPFORAUF']
#             return '6102'

#     inserData = {
#         "CODORC": orcData['CODORC'],
#         "CODPROD": budgetProduct['CODPROD'],
#         "QUANTIDADE": float(budgetProduct['QUANTIDADE']),
#         "VALORUNITARIO": float(budgetProduct['PRECOTABELA']),
#         "ALIQDESCONTOITEM": float(budgetProduct['ALIQDESCONTOITEM']),
#         "VALORDESCONTOITEM": float(budgetProduct['VALORDESCONTOITEM']),
#         "ALIQACRESCIMOITEM": float(budgetProduct['ALIQACRESCIMOITEM']),
#         "VALORACRESCIMOITEM": float(budgetProduct['VALORACRESCIMOITEM']),
#         "VALORTOTAL": float(budgetProduct['VALORTOTAL']),
#         "DESCRICAOPRODUTO": budgetProduct['NOMEPROD'].replace("'", "''"),
#         "PRECOTABELA": float(budgetProduct['PRECOTABELA']),
#         "CODCFOP": getCFOP(),
#         "CUSTOREAL": PRODUTO['CUSTOREAL'],
#         "CSOSN": TRIBUTACAOECF['CSOSN'],
#         "NUMEROITEM": index,
#         "CODCALCULOICMS": PRODUTO['CODCALCULOICMS'],
#         "CODCLASSIFICACAOFISCAL": PRODUTO['CODCLASSIFICACAOFISCAL'],
#         "CODIGOPRODUTO": PRODUTO['CODIGO'],
#         "UNIDADE": PRODUTO['UNIDADE'],
#         "TIPOTRIBUTACAO": TRIBUTACAOECF['TIPOTRIBUTACAO'],
#         "NUMEROORCAMENTO": orcData['NUMEROORCAMENTO'],
#         "CODSITUACAOTRIBUTARIA": "00 " if getCFOP() == '5102' else ''
#     }

#     return {**inserData, **fixedData, **varData}


# def getByCodorc(val, flagAdmin):
#     query = f"""
#     SELECT ORCAMENTOPROD.CODPROD, PRODUTO.CODIGO, ORCAMENTOPROD.QUANTIDADE, ORCAMENTOPROD.VALORUNITARIO,
#     ORCAMENTOPROD.PRECOTABELA, ORCAMENTOPROD.ALIQDESCONTOITEM, ORCAMENTOPROD.VALORDESCONTOITEM,
#     ORCAMENTOPROD.ALIQACRESCIMOITEM, ORCAMENTOPROD.VALORACRESCIMOITEM, ORCAMENTOPROD.VALORTOTAL,
#     PRODUTO.NOMEPROD, PRODUTO.UNIDADE, PRODUTO.DESCMAXIMO, PRODUTOESTOQUE.ESTATU
#     FROM ORCAMENTOPROD
#     LEFT JOIN PRODUTO ON ORCAMENTOPROD.CODPROD = PRODUTO.CODPROD
#     LEFT JOIN PRODUTOESTOQUE ON PRODUTO.CODPROD = PRODUTOESTOQUE.CODPROD
#     WHERE CODORC = '{val}'
#     AND PRODUTOESTOQUE.CODEMPRESA = 1
#     """

#     return queryToDict(query, flagAdmin)
