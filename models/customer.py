
import sys

sys.path.insert(0, './')

from utility.FDB_handler import Column, FDBModel

class Customer(FDBModel):
    __tablename__ = "CLIENTE"
    
    CODCLI = Column(is_primary_key=True)
    CODIGO = Column()
    NOMECLI = Column()
    ENDERECO = Column()
    BAIRRO = Column()
    CIDADE = Column()
    ESTADO = Column()
    CEP = Column()
    TELEFONE = Column()
    CNPJ = Column()
    CPF = Column()
    INSCR = Column()
    FLAGFISICA = Column()
    DATCAD = Column()
    LAST_CHANGE = Column()
    EMAIL = Column()
    CONJFANTASIA = Column()
    NUMEROLOGRADOURO = Column()
    COMPLEMENTOLOGRADOURO = Column()
    
    def __init__(self,
                CODCLI,
                CODIGO,
                NOMECLI,
                ENDERECO,
                BAIRRO,
                CIDADE,
                ESTADO,
                CEP,
                TELEFONE,
                CNPJ,
                CPF,
                INSCR,
                FLAGFISICA,
                DATCAD,
                LAST_CHANGE,
                EMAIL,
                CONJFANTASIA,
                NUMEROLOGRADOURO,
                COMPLEMENTOLOGRADOURO) -> None:
        
        self.CODCLI = CODCLI
        self.CODIGO = CODIGO
        self.NOMECLI = NOMECLI
        self.ENDERECO = ENDERECO
        self.BAIRRO = BAIRRO
        self.CIDADE = CIDADE
        self.ESTADO = ESTADO
        self.CEP = CEP
        self.TELEFONE = TELEFONE
        self.CNPJ = CNPJ
        self.CPF = CPF
        self.INSCR = INSCR
        self.FLAGFISICA = FLAGFISICA
        self.DATCAD = DATCAD
        self.LAST_CHANGE = LAST_CHANGE
        self.EMAIL = EMAIL
        self.CONJFANTASIA = CONJFANTASIA
        self.NUMEROLOGRADOURO = NUMEROLOGRADOURO
        self.COMPLEMENTOLOGRADOURO = COMPLEMENTOLOGRADOURO
        
    def json(self) -> str:
        return self.convert_to_JSON({
            'CODCLI': self.CODCLI,
            'CODIGO': self.CODIGO,
            'NOMECLI': self.NOMECLI,
            'ENDERECO': self.ENDERECO,
            'BAIRRO': self.BAIRRO,
            'CIDADE': self.CIDADE,
            'ESTADO': self.ESTADO,
            'CEP': self.CEP,
            'TELEFONE': self.TELEFONE,
            'CNPJ': self.CNPJ,
            'CPF': self.CPF,
            'INSCR': self.INSCR,
            'FLAGFISICA': self.FLAGFISICA,
            'DATCAD': self.DATCAD,
            'LAST_CHANGE': self.LAST_CHANGE,
            'EMAIL': self.EMAIL,
            'CONJFANTASIA': self.CONJFANTASIA,
            'NUMEROLOGRADOURO': self.NUMEROLOGRADOURO,
            'COMPLEMENTOLOGRADOURO': self.COMPLEMENTOLOGRADOURO
        })

customer = Customer.find_by_key('00016226')
print(type(customer.json()))
   
# import datetime


# def parseDictFromFlag(flag):
#     if(flag == 'Y'):
#         return {
#             'CNPJ': '',
#             'INSCR': '',
#             'CONJFANTASIA': ''
#         }
#     else:
#         return {
#             'CPF': ''
#         }


# def parseData(data):
#     def customReplace(text):
#         return text.replace('.', '').replace('/', '').replace('(', '').replace(')', '').replace('-', '')

#     def getIndDest():
#         if(data['FLAGFISICA'] == 'Y'):
#             return '9'
#         else:
#             if(data['INSCR']):
#                 return '1'

#     newData = data
#     newData['CPF'] = customReplace(newData['CPF'])
#     newData['CNPJ'] = customReplace(newData['CNPJ'])
#     newData['INSCR'] = customReplace(newData['INSCR'])
#     newData['CEP'] = customReplace(newData['CEP'])
#     newData['TELEFONE'] = customReplace(newData['TELEFONE'])
#     newData['INDIEDEST'] = getIndDest()

#     return newData


# def queryToDict(sqlQuery):
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

#     cur = con.cursor()
#     cur.execute(sqlQuery)
#     data = cur.fetchall()
#     return [{desc[0]:convertToText(desc[1], row[index]) for index, desc in enumerate(cur.description)} for row in data]


# def getByNameOrCode(text):
#     def buildInteliSearch():
#         searchQuery = ''
#         searchedText = text.split()
#         for index, wordText in enumerate(searchedText):
#             searchQuery += f"NOMECLI SIMILAR TO '%{wordText}%'"
#             if((index + 1) < len(searchedText)):
#                 searchQuery += " AND "
#         return searchQuery

#     def getSearchColumns():
#         if(text):
#             try:
#                 int(text)
#                 return f"""
#             WHERE (CODIGO SIMILAR TO '%{text}%' OR CPF SIMILAR TO '%{text}%' OR CNPJ SIMILAR TO '%{text}%' OR ({buildInteliSearch()}))
#             """
#             except:
#                 return f" WHERE ({ buildInteliSearch() })"
#         return ""

#     query = f"""
#     SELECT FIRST 25 CODCLI, CODIGO, NOMECLI, ENDERECO ,BAIRRO, CIDADE, ESTADO, CEP, TELEFONE, CNPJ, CPF, INSCR, FLAGFISICA, DATCAD, LAST_CHANGE, EMAIL, CONJFANTASIA, NUMEROLOGRADOURO, COMPLEMENTOLOGRADOURO
#     FROM CLIENTE
#     {getSearchColumns()}"""
#     res = queryToDict(query)
#     return res


# def getByCode(code):
#     query = f"""
#     SELECT CODCLI, CODIGO, NOMECLI, ENDERECO ,BAIRRO, CIDADE, ESTADO, CEP, TELEFONE, CNPJ, CPF, INSCR, FLAGFISICA, DATCAD, LAST_CHANGE, EMAIL, CONJFANTASIA, NUMEROLOGRADOURO, COMPLEMENTOLOGRADOURO
#     FROM CLIENTE
#     WHERE CODCLI = '{code}'
#     """
#     return queryToDict(query)[0]


# def getByName(name):
#     query = f"""
#     SELECT CODCLI, CODIGO, NOMECLI, ENDERECO ,BAIRRO, CIDADE, ESTADO, CEP, TELEFONE, CNPJ, CPF, INSCR, FLAGFISICA, DATCAD, LAST_CHANGE, EMAIL, CONJFANTASIA, NUMEROLOGRADOURO, COMPLEMENTOLOGRADOURO
#     FROM CLIENTE
#     WHERE NOMECLI = '{name}'
#     """
#     return queryToDict(query)[0]


# def checkIfUnique(data):
#     if(data['NOMECLI']):
#         name = data['NOMECLI']
#         query = f"SELECT NOMECLI FROM CLIENTE WHERE NOMECLI = '{name}'"
#         res = queryToDict(query)
#         if(len(res) != 0):
#             return False, 'NOMECLI'

#         if(data['FLAGFISICA'] == 'Y'):
#             if(data['CPF']):
#                 cpf = data['CPF']
#                 query = f"SELECT CPF FROM CLIENTE WHERE CPF = '{cpf}'"
#                 res = queryToDict(query)
#                 if(len(res) != 0):
#                     return False, 'CPF'
#         else:
#             if(data['CNPJ']):
#                 cnpj = data['CNPJ']
#                 query = f"SELECT CNPJ FROM CLIENTE WHERE CNPJ = '{cnpj}'"
#                 res = queryToDict(query)
#                 if(len(res) != 0):
#                     return False, 'CNPJ'
#         return True, ''
#     return False, 'NOMECLI'


# def getNextCod():
#     query = "SELECT SKIP ((SELECT count(*) - 1 FROM CLIENTE)) CODCLI, CODIGO FROM CLIENTE ORDER BY CODCLI"
#     res = queryToDict(query)[0]
#     res['CODCLI'] = int(res['CODCLI'])
#     res['CODIGO'] = int(res['CODIGO'])

#     while True:
#         CODCLItring = res['CODCLI']
#         CODCLItring = f'{CODCLItring:08}'
#         query = f"SELECT CODCLI FROM CLIENTE WHERE CODCLI = '{CODCLItring}'"
#         ans = queryToDict(query)
#         if(len(ans) == 0):
#             break
#         res['CODCLI'] = res['CODCLI'] + 1

#     while True:
#         res['CODIGO'] = res['CODIGO'] + 1
#         CODIGOString = res['CODIGO']
#         CODIGOString = f'{CODIGOString:06}'
#         query = f"SELECT CODIGO FROM CLIENTE WHERE CODIGO = '{CODIGOString}'"
#         ans = queryToDict(query)
#         if(len(ans) == 0):
#             break

#     CODCLI = res['CODCLI']
#     CODIGO = res['CODIGO']
#     res['CODCLI'] = f'{CODCLI:08}'
#     res['CODIGO'] = f'{CODIGO:06}'

#     return res


# def insertNewCustomer(data):
#     now = datetime.datetime.now()
#     dates = {'DATCAD': now.date(), 'LAST_CHANGE': now.strftime(
#         "%Y-%m-%d %H:%M:%S")}

#     dataWithDate = {**parseData(data), **dates, **
#                     parseDictFromFlag(data['FLAGFISICA'])}

#     columnsQuery = '('
#     valuesQuery = '('
#     for item in dataWithDate.items():
#         if(item[1]):
#             columnsQuery += item[0] + ', '
#             valuesQuery += f"'{item[1]}'" + ', '
#     columnsQuery = columnsQuery[:-2] + ')'
#     valuesQuery = valuesQuery[:-2] + ')'

#     query = f"""
#     INSERT INTO CLIENTE {columnsQuery}
#     VALUES {valuesQuery}
#     """

#     con.cursor().execute(query)
#     con.commit()


# def updateCustomer(data):
#     now = datetime.datetime.now()
#     nowDict = {'LAST_CHANGE': now.strftime("%Y-%m-%d %H:%M:%S")}

#     newData = {**parseData(data), **nowDict, **
#                parseDictFromFlag(data['FLAGFISICA'])}

#     dataQuery = ''
#     for item in newData.items():
#         if(item[1]):
#             dataQuery += item[0] + ' = ' + f"'{item[1]}', "
#     dataQuery = dataQuery[:-2]

#     cod = data['CODCLI']

#     query = f"""
#     UPDATE CLIENTE
#     SET {dataQuery}
#     WHERE CODCLI = '{cod}'
#     """

#     con.cursor().execute(query)
#     con.commit()
