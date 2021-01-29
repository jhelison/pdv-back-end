import fdb

path = r'C:\CPlus\CPLUS.FDB'
con = fdb.connect(path, 'SYSDBA', 'masterkey')

def queryToDict(sqlQuery):
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
        
    cur = con.cursor()
    cur.execute(sqlQuery)
    data = cur.fetchall()
    return [{desc[0]:convertToText(desc[1],row[index]) for index, desc in enumerate(cur.description)} for row in data]

def getAllSellers():
    query = """
    SELECT CODVENDED, NOMEVENDED
    FROM VENDEDOR
    WHERE INATIVO = 'N'
    """
    
    return queryToDict(query)