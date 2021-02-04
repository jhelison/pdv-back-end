from datetime import datetime
import datetime as dt
from firebirdConnection import con

def getMonthRange():
    now = datetime.now().date()
    
    if now.day > 28:
        now = now.replace(day=28)
        
    try:
        return now.replace(month=now.month-1), now
    except:
        return now.replace(month=12, year=now.year - 1), now

def getTopItems(codvend):
    start, end = getMonthRange()
    
    query = f"""
    SELECT FIRST 10 MOVENDAPROD.DESCRICAOPRODUTO
    FROM MOVENDAPROD
    INNER JOIN MOVENDA ON MOVENDAPROD.CODMOVENDA = MOVENDA.CODMOVENDA AND DATA >= '2020-10-27' AND DATA <= '2020-11-27' AND MOVENDA.CODVENDED = '{codvend}'
    GROUP BY MOVENDAPROD.DESCRICAOPRODUTO
    ORDER BY COUNT(*) DESC
    """
    res = con.cursor().execute(query).fetchall()
    res = [item[0] for item in res]

    return res