import sys
from datetime import date, datetime

sys.path.insert(0, './')

from utility.FDB_handler import FDBModel, Column
from models.orcamentoProd import BudgetProd

class Budget(FDBModel):
    __tablename__ = "ORCAMENTO"
    
    CODORC = Column(is_primary_key=True, use_table_codigo=9)
    NUMEROORCAMENTO = Column(is_primary_key=True, use_table_codigo=9)
    
    #Main components
    CODCLI = Column()
    CODVENDED = Column()
    DATA = Column()
    FLAGCLI = Column()
    NOMECLI = Column()
    OBS = Column()
    VALORTOTAL = Column()
    ALIQDESCONTO = Column()
    VALORFRETE = Column()
    VALORACRESCIMO = Column()
    HORA = Column()
    OBSNOTAFISCAL = Column()
    CODCFOP = Column()
    VALORDESCONTO = Column()
    ALIQACRESCIMO = Column()
    VALORTOTALORCAMENTO = Column()
    VALORTOTALPRODUTOS = Column()
    CODTIPOMOVIMENTO = Column()
    TEMPO = Column()
    DATACADASTRO = Column()

    #Adicionals
    IDENTIFICADORDESTINO = Column()
    VALORENTRADA = Column()
    CAMPOVALOR1 = Column()
    VALORTOTALIPI = Column()
    FLAGFRETE = Column()
    VALORICMS = Column()
    BASEICMS = Column()
    VALOROUTRASDESPESAS = Column()
    VALORSUBSTTRIBUTARIA = Column()
    BASESUBSTTRIBUTARIA = Column()
    VALORSEGURO = Column()
    FLAGDELIVERY = Column()
    FLAGSTATUS = Column()
    FLAGPALM = Column()
    RENTABILIDADE = Column()
    QUANTIDADEVOLUMES = Column()
    INDPRESENCA = Column()
    VALORFCP = Column()
    VALORFCPSUBSTTRIBUTARIA = Column()
    VALORTOTALPIS = Column()
    VALORTOTALCOFINS = Column()
    FLAGESTOQUELIBERADO = Column()
    FLAGDESCAUTORIZADO = Column()
    FLAGIMPRESSO = Column()
    VALORTOTALISS = Column()
    FLAGRESERVADO = Column()
    
    
    #The variables
    CODPRECO = Column()
    CODEMPRESA = Column()
    CODUSER = Column()
    CODSETORESTOQUE = Column()
    
    def __init__(self,
                CODORC,
                NUMEROORCAMENTO,
    
                CODCLI = None,
                CODVENDED = None,
                DATA = None,
                FLAGCLI = None,
                NOMECLI = None,
                OBS = None,
                VALORTOTAL = None,
                ALIQDESCONTO = None,
                VALORFRETE = None,
                VALORACRESCIMO = None,
                HORA = None,
                OBSNOTAFISCAL = None,
                CODCFOP = None,
                VALORDESCONTO = None,
                ALIQACRESCIMO = None,
                VALORTOTALORCAMENTO = None,
                VALORTOTALPRODUTOS = None,
                CODTIPOMOVIMENTO = None,
                TEMPO = None,
                DATACADASTRO = None,

                IDENTIFICADORDESTINO = None,
                VALORENTRADA = None,
                CAMPOVALOR1 = None,
                VALORTOTALIPI = None,
                FLAGFRETE = None,
                VALORICMS = None,
                BASEICMS = None,
                VALOROUTRASDESPESAS = None,
                VALORSUBSTTRIBUTARIA = None,
                BASESUBSTTRIBUTARIA = None,
                VALORSEGURO = None,
                FLAGDELIVERY = None,
                FLAGSTATUS = None,
                FLAGPALM = None,
                RENTABILIDADE = None,
                QUANTIDADEVOLUMES = None,
                INDPRESENCA = None,
                VALORFCP = None,
                VALORFCPSUBSTTRIBUTARIA = None,
                VALORTOTALPIS = None,
                VALORTOTALCOFINS = None,
                FLAGESTOQUELIBERADO = None,
                FLAGDESCAUTORIZADO = None,
                FLAGIMPRESSO = None,
                VALORTOTALISS = None,
                FLAGRESERVADO = None,

                CODPRECO = None,
                CODEMPRESA = None,
                CODUSER = None,
                CODSETORESTOQUE = None):
        self.CODORC = CODORC
        self.NUMEROORCAMENTO = NUMEROORCAMENTO
        
        #Main components
        self.CODCLI = CODCLI
        self.CODVENDED = CODVENDED
        self.DATA = DATA
        self.FLAGCLI = FLAGCLI
        self.NOMECLI = NOMECLI
        self.OBS = OBS
        self.VALORTOTAL = VALORTOTAL
        self.ALIQDESCONTO = ALIQDESCONTO
        self.VALORFRETE = VALORFRETE
        self.VALORACRESCIMO = VALORACRESCIMO
        self.HORA = HORA
        self.OBSNOTAFISCAL = OBSNOTAFISCAL
        self.CODCFOP = CODCFOP
        self.VALORDESCONTO = VALORDESCONTO
        self.ALIQACRESCIMO = ALIQACRESCIMO
        self.VALORTOTALORCAMENTO = VALORTOTALORCAMENTO
        self.VALORTOTALPRODUTOS = VALORTOTALPRODUTOS
        self.CODTIPOMOVIMENTO = CODTIPOMOVIMENTO
        self.TEMPO = TEMPO
        self.DATACADASTRO = DATACADASTRO

        #Adicionals
        self.IDENTIFICADORDESTINO = IDENTIFICADORDESTINO if IDENTIFICADORDESTINO != None else "1"
        self.VALORENTRADA = VALORENTRADA if VALORENTRADA != None else 0.0
        self.CAMPOVALOR1 = CAMPOVALOR1 if CAMPOVALOR1 != None else 100.0
        self.VALORTOTALIPI = VALORTOTALIPI if VALORTOTALIPI != None else 0.0
        self.FLAGFRETE = FLAGFRETE if FLAGFRETE != None else "D"
        self.VALORICMS = VALORICMS if VALORICMS != None else 0.0
        self.BASEICMS = BASEICMS if BASEICMS != None else 0.0
        self.VALOROUTRASDESPESAS = VALOROUTRASDESPESAS if VALOROUTRASDESPESAS != None else 0.0
        self.VALORSUBSTTRIBUTARIA = VALORSUBSTTRIBUTARIA if VALORSUBSTTRIBUTARIA != None else 0.0
        self.BASESUBSTTRIBUTARIA = BASESUBSTTRIBUTARIA if BASESUBSTTRIBUTARIA != None else 0.0
        self.VALORSEGURO = VALORSEGURO if VALORSEGURO != None else 0.0
        self.FLAGDELIVERY = FLAGDELIVERY if FLAGDELIVERY != None else "N"
        self.FLAGSTATUS = FLAGSTATUS if FLAGSTATUS != None else "O"
        self.FLAGPALM = FLAGPALM if FLAGPALM != None else "0"
        self.RENTABILIDADE = RENTABILIDADE if RENTABILIDADE != None else 0.0
        self.QUANTIDADEVOLUMES = QUANTIDADEVOLUMES if QUANTIDADEVOLUMES != None else 0
        self.INDPRESENCA = INDPRESENCA if INDPRESENCA != None else "0"
        self.VALORFCP = VALORFCP if VALORFCP != None else 0.0
        self.VALORFCPSUBSTTRIBUTARIA = VALORFCPSUBSTTRIBUTARIA if VALORFCPSUBSTTRIBUTARIA != None else 0.0
        self.VALORTOTALPIS = VALORTOTALPIS if VALORTOTALPIS != None else 0.0
        self.VALORTOTALCOFINS = VALORTOTALCOFINS if VALORTOTALCOFINS != None else 0.0
        self.FLAGESTOQUELIBERADO = FLAGESTOQUELIBERADO if FLAGESTOQUELIBERADO != None else 'Y'
        self.FLAGDESCAUTORIZADO = FLAGDESCAUTORIZADO if FLAGDESCAUTORIZADO != None else 'N'
        self.FLAGIMPRESSO = FLAGIMPRESSO if FLAGIMPRESSO != None else 'N'
        self.VALORTOTALISS = VALORTOTALISS if VALORTOTALISS != None else 0.0
        self.FLAGRESERVADO = FLAGRESERVADO if FLAGRESERVADO != None else 'N'

        #The variables
        self.CODPRECO = CODPRECO if CODPRECO != None else "000000001"
        self.CODEMPRESA = CODEMPRESA if CODEMPRESA != None else 3
        self.CODUSER = CODUSER if CODUSER != None else "000000010" #Importante, deve ser analisado no futuro
        self.CODSETORESTOQUE = CODSETORESTOQUE if CODSETORESTOQUE != None else "000000001"
        
    def get_all_budget_prod(self):
        if self.CODORC:
            return(BudgetProd.find_by_columns(CODORC = self.CODORC))
        return []
        
    def _on_insert(self):
        self.DATA = datetime.now().date()
        self.HORA = datetime.now().time()
        self.DATACADASTRO = datetime.now().date()
        self.ALIQDESCONTO = self.ALIQDESCONTO if self.ALIQDESCONTO != None else 0.0
        self.VALORACRESCIMO = self.VALORACRESCIMO if self.VALORACRESCIMO != None else 0.0
        self.VALORDESCONTO = self.VALORDESCONTO if self.VALORDESCONTO != None else 0.0
        self.ALIQACRESCIMO = self.ALIQACRESCIMO if self.ALIQACRESCIMO != None else 0.0

budgets = Budget.find_by_columns(exact=False, NOMECLI="jhelis")

for budget in budgets:
    print(budget.NOMECLI)
    prods = budget.get_all_budget_prod()
    print(len(prods))    


# from models.orcamentoProd import buildBudgetProductData, getORCAMENTOPRODCodes

# fixedData = {
#     "IDENTIFICADORDESTINO": "1",
#     "VALORENTRADA": 0.0000,
#     "CAMPOVALOR1": 100.0000,
#     "VALORTOTALIPI": 0.0000,
#     "FLAGFRETE": "D",
#     "VALORICMS": 0.0000,
#     "BASEICMS": 0.0000,
#     "VALOROUTRASDESPESAS": 0.0000,
#     "VALORSUBSTTRIBUTARIA": 0.0000,
#     "BASESUBSTTRIBUTARIA": 0.0000,
#     "VALORSEGURO": 0.0000,
#     "FLAGDELIVERY": "N",
#     "FLAGSTATUS": "O",
#     "FLAGPALM": "0",
#     "RENTABILIDADE": 0.0000,
#     "QUANTIDADEVOLUMES": 0,
#     "INDPRESENCA": "0",
#     "VALORFCP": 0.0000,
#     "VALORFCPSUBSTTRIBUTARIA": 0.0000
# }

# # All those values should change in future updates
# varData = {
#     "CODPRECO": "000000001",
#     "CODEMPRESA": 3,
#     "CODUSER": "000000010",
#     "CODSETORESTOQUE": "000000001",
# }


# def queryToDict(sqlQuery):
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


# def getNextCod():
#     query = "SELECT SKIP ((SELECT count(*) - 1 FROM ORCAMENTO)) CODORC, NUMEROORCAMENTO FROM ORCAMENTO ORDER BY CODORC"
#     res = queryToDict(query)[0]
#     res['CODORC'] = int(res['CODORC'])
#     res['NUMEROORCAMENTO'] = int(res['NUMEROORCAMENTO'])

#     while True:
#         CODORCtring = res['CODORC']
#         CODORCtring = f'{CODORCtring:09}'
#         query = f"SELECT CODORC FROM ORCAMENTO WHERE CODORC = '{CODORCtring}'"
#         ans = queryToDict(query)
#         if(len(ans) == 0):
#             break
#         res['CODORC'] = res['CODORC'] + 1

#     while True:
#         res['NUMEROORCAMENTO'] = res['NUMEROORCAMENTO'] + 1
#         NUMEROORCAMENTOString = res['NUMEROORCAMENTO']
#         NUMEROORCAMENTOString = f'{NUMEROORCAMENTOString:09}'
#         query = f"SELECT NUMEROORCAMENTO FROM ORCAMENTO WHERE NUMEROORCAMENTO = '{NUMEROORCAMENTOString}'"
#         ans = queryToDict(query)
#         if(len(ans) == 0):
#             break

#     CODORC = res['CODORC']
#     NUMEROORCAMENTO = res['NUMEROORCAMENTO']
#     res['CODORC'] = f'{CODORC:09}'
#     res['NUMEROORCAMENTO'] = f'{NUMEROORCAMENTO:09}'

#     return res


# def buildData(data, codvend):
#     def timeFromMs(val):
#         h = f'{int(val / 60 / 60):02}'
#         m = f'{int((val / 60) % 60):02}'
#         s = f'{int(val % (60)):02}'
#         return f'{h}:{m}:{s}'

#     now = datetime.datetime.now()

#     def getCODCLI():
#         if data['customer']['fromDatabase']:
#             return {'CODCLI': data['customer']['data']['CODCLI']}
#         return {}

#     dataBuilded = {
#         "DATA": now.date(),
#         "FLAGCLI": "Y" if data['customer']['fromDatabase'] else "N",
#         "NOMECLI": data['customer']['data']['NOMECLI'],
#         "CODVENDED": codvend,
#         "OBS": data['OBS'],
#         "ALIQDESCONTO": 0.0000,  # Fixed
#         "VALORFRETE": float(data['VALORFRETE']),
#         "VALORACRESCIMO": 0.0000,
#         "OBSNOTAFISCAL": data['OBSNOTAFISCAL'],
#         "CODCFOP": "5102" if data['customer']['data']['ESTADO'] == 'MA' or data['customer']['data']['ESTADO'] == '' else "6102",
#         "VALORDESCONTO": 0.0000,  # Fixed
#         "ALIQACRESCIMO": 0.0000,  # Fixed
#         "VALORTOTALORCAMENTO": sum([float(product["VALORTOTAL"]) for product in data['products']]) + float(data['VALORFRETE']),
#         "VALORTOTALPRODUTOS": sum([float(product["VALORTOTAL"]) for product in data['products']]),
#         "CODTIPOMOVIMENTO": data['movimento'],
#         "TEMPO": timeFromMs(data["TEMPO"] / 1000)
#     }

#     return {**dataBuilded, **varData, **fixedData, **getNextCod(), **getCODCLI()}


# def addNewBudget(data, codvend):
#     start = datetime.datetime.now()
#     buildedData = buildData(data, codvend)

#     columnsQuery = '('
#     valuesQuery = '('
#     for item in buildedData.items():
#         columnsQuery += item[0] + ', '
#         valuesQuery += f"'{item[1]}'" + ', '
#     columnsQuery = columnsQuery[:-2] + ')'
#     valuesQuery = valuesQuery[:-2] + ')'

#     query = f"""
#     INSERT INTO ORCAMENTO {columnsQuery}
#     VALUES {valuesQuery}
#     """

#     con.cursor().execute(query)

#     codes = getORCAMENTOPRODCodes(len(data['products']))
#     for index, budgetProduct in enumerate(data['products']):
#         CODORCPROD = {'CODORCPROD': codes[index]}
#         buildedProductData = {
#             **buildBudgetProductData(budgetProduct, index + 1, buildedData), **CODORCPROD}

#         columnsQuery = '('
#         valuesQuery = '('
#         for item in buildedProductData.items():
#             columnsQuery += item[0] + ', '
#             valuesQuery += f"'{item[1]}'" + ', '
#         columnsQuery = columnsQuery[:-2] + ')'
#         valuesQuery = valuesQuery[:-2] + ')'

#         query = f"""
#         INSERT INTO ORCAMENTOPROD {columnsQuery}
#         VALUES {valuesQuery}
#         """
#         con.cursor().execute(query)

#     if(data['fromBudget']):
#         budgetCode = data['fromBudget']
#         query = f"""
#         SELECT DATAFATURADO FROM ORCAMENTO WHERE CODORC = '{budgetCode}'
#         """
#         res = con.cursor().execute(query).fetchone()

#         if not res[0]:
#             query = f"""
#             DELETE FROM ORCAMENTOPROD
#             WHERE CODORC = '{budgetCode}'
#             """
#             con.cursor().execute(query)

#             query = f"""
#             UPDATE ORCAMENTO
#             SET VALORFRETE = '0'
#             WHERE CODORC = '{budgetCode}'
#             """
#             con.cursor().execute(query)

#     con.commit()
