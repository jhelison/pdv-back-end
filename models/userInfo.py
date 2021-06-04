from datetime import datetime
import datetime as dt
from FDBHandler import con


def getDateRange(dataDate):
    def subtractMonth(date):
        try:
            return date.replace(day=1, month=date.month - 1)
        except:
            return date.replace(day=1, month=12, year=date.year - 1)

    def addMonth(date):
        try:
            return date.replace(day=1, month=date.month + 1)
        except:
            return date.replace(day=1, month=1, year=date.year + 1)

    def setDayOfMonth(date, day, down=False):
        day = day
        while True:
            try:
                return date.replace(day=day)
            except:
                if(down):
                    day -= 1
                else:
                    return addMonth(date)
                    
    day = dataDate.day
    now = datetime.now().date()

    if day >= now.day:
        return setDayOfMonth(subtractMonth(now), day + 1, False), setDayOfMonth(now, day, True)
    else:
        return setDayOfMonth(now, day + 1, False), setDayOfMonth(addMonth(now), day, True)


def getCount(user, startDate, endDate):
    query = f"""
    SELECT 
        COUNT(*)
    FROM 
        MOVENDA
    WHERE 
        DATA >= '{startDate}' AND 
        DATA <= '{endDate}' AND 
        MOVENDA.CODVENDED = '{user.codvend}'
    """
    movenda = con.cursor().execute(query).fetchone()

    query = f"""
    SELECT
        COUNT(MOVENDA.CODVENDED)
    FROM
        MOVENDADEVOLUCAO
    LEFT JOIN
        MOVENDAPROD ON 
            MOVENDADEVOLUCAO.CODMOVPROD = MOVENDAPROD.CODMOVPROD
    LEFT JOIN 
        MOVENDA ON 
            MOVENDAPROD.CODMOVENDA = MOVENDA.CODMOVENDA
    WHERE 
        MOVENDADEVOLUCAO.DATA >= '{startDate}' AND
        MOVENDADEVOLUCAO.DATA <= '{endDate}' AND
        MOVENDA.CODVENDED = '{user.codvend}'
    """
    returns = con.cursor().execute(query).fetchone()

    return movenda[0], returns[0]


def getComission(user, startDate, endDate):
    query = f"""
    SELECT 
        COALESCE(SUM(CAST(MOVENDAPROD.VALORTOTAL AS DOUBLE PRECISION)  * (CAST(PRODUTO.COMISSAO AS DOUBLE PRECISION) / 100)),0) + COALESCE(SUM((COALESCE((CAST(MOVENDA.VALORACRESCIMO AS DOUBLE PRECISION) / NULLIF((CASE WHEN MOVENDA.VALORTOTALPRODUTOS = 0 THEN CAST(MOVENDA.VALORTOTALNOTA AS DOUBLE PRECISION) ELSE CAST(MOVENDA.VALORTOTALPRODUTOS AS DOUBLE PRECISION) END), 0)),0) - COALESCE((CAST(MOVENDA.VALORDESCONTO AS DOUBLE PRECISION) / NULLIF((CASE WHEN MOVENDA.VALORTOTALPRODUTOS = 0 THEN CAST(MOVENDA.VALORTOTALNOTA AS DOUBLE PRECISION) ELSE CAST(MOVENDA.VALORTOTALPRODUTOS AS DOUBLE PRECISION) END), 0)),0) * CAST(MOVENDAPROD.VALORTOTAL AS DOUBLE PRECISION)) * (CAST(PRODUTO.COMISSAO AS DOUBLE PRECISION) / 100)),0) AS saleFinalComission,
        COALESCE(SUM(CAST(MOVENDAPROD.VALORTOTAL AS DOUBLE PRECISION)),0) AS saleBruteTotal,
        COALESCE(SUM(CASE WHEN CAST(PRODUTO.COMISSAO AS DOUBLE PRECISION) != 0 THEN CAST(MOVENDAPROD.VALORTOTAL AS DOUBLE PRECISION) END),0) AS saleLiquidTotal,
        COALESCE(SUM((COALESCE((CAST(MOVENDA.VALORACRESCIMO AS DOUBLE PRECISION) / NULLIF((CASE WHEN MOVENDA.VALORTOTALPRODUTOS = 0 THEN CAST(MOVENDA.VALORTOTALNOTA AS DOUBLE PRECISION) ELSE CAST(MOVENDA.VALORTOTALPRODUTOS AS DOUBLE PRECISION) END), 0)),0) - COALESCE((CAST(MOVENDA.VALORDESCONTO AS DOUBLE PRECISION) / NULLIF((CASE WHEN MOVENDA.VALORTOTALPRODUTOS = 0 THEN CAST(MOVENDA.VALORTOTALNOTA AS DOUBLE PRECISION) ELSE CAST(MOVENDA.VALORTOTALPRODUTOS AS DOUBLE PRECISION) END), 0)),0) * CAST(MOVENDAPROD.VALORTOTAL AS DOUBLE PRECISION)) * (CAST(PRODUTO.COMISSAO AS DOUBLE PRECISION))),0) AS saleBudgetDifer
    FROM 
        MOVENDAPROD
    INNER JOIN 
        MOVENDA ON 
            MOVENDAPROD.CODMOVENDA = MOVENDA.CODMOVENDA AND 
            DATA >= '{startDate}' AND DATA <= '{endDate}' AND 
            MOVENDA.CODVENDED = '{user.codvend}'
    LEFT JOIN 
        PRODUTO ON 
            MOVENDAPROD.CODPROD = PRODUTO.CODPROD
    """
    sales = con.cursor().execute(query).fetchone()

    query = f"""
    SELECT 
        COALESCE(SUM(((MOVENDAPROD.VALORTOTAL / MOVENDAPROD.QUANTIDADE) * MOVENDADEVOLUCAO.QUANTIDADEDEVOLUCAO + (COALESCE((MOVENDA.VALORACRESCIMO / MOVENDA.VALORTOTALPRODUTOS),0) - COALESCE((MOVENDA.VALORDESCONTO / MOVENDA.VALORTOTALPRODUTOS),0) * MOVENDAPROD.VALORTOTAL)) * (PRODUTO.COMISSAO / 100)),0) AS FINALTOTAL,
        COALESCE(SUM((MOVENDAPROD.VALORTOTAL / MOVENDAPROD.QUANTIDADE) * MOVENDADEVOLUCAO.QUANTIDADEDEVOLUCAO),0) AS TOTALRETURNS,
        COALESCE(SUM(CASE WHEN PRODUTO.COMISSAO != 0 THEN (MOVENDAPROD.VALORTOTAL / MOVENDAPROD.QUANTIDADE) * MOVENDADEVOLUCAO.QUANTIDADEDEVOLUCAO END),0) AS TOTALRETURNSCOMISSION,
        COALESCE(SUM((COALESCE((MOVENDA.VALORACRESCIMO / MOVENDA.VALORTOTALPRODUTOS),0) - COALESCE((MOVENDA.VALORDESCONTO / MOVENDA.VALORTOTALPRODUTOS),0) * MOVENDAPROD.VALORTOTAL) * (PRODUTO.COMISSAO)),0) AS BUDGETVALUE
    FROM 
        MOVENDADEVOLUCAO
    LEFT JOIN 
        MOVENDAPROD ON
            MOVENDADEVOLUCAO.CODMOVPROD = MOVENDAPROD.CODMOVPROD
    LEFT JOIN 
        PRODUTO ON
            MOVENDAPROD.CODPROD = PRODUTO.CODPROD
    LEFT JOIN 
        MOVENDA ON
            MOVENDAPROD.CODMOVENDA = MOVENDA.CODMOVENDA
    WHERE
        MOVENDADEVOLUCAO.DATA >= '{startDate}' AND 
        MOVENDADEVOLUCAO.DATA <= '{endDate}' AND 
        MOVENDA.CODVENDED = '{user.codvend}' AND 
        MOVENDA.DATA >= '2021-01-01'
    """
    returns = con.cursor().execute(query).fetchone()
    return {
        'saleFinalComission': float(sales[0]),
        'saleBruteTotal': float(sales[1]),
        'saleLiquidTotal': float(sales[2]),
        'saleBudgetDifer': float(sales[3]),
        'returnFinalComission': float(returns[0]),
        'returnBruteTotal': float(returns[1]),
        'returnLiquidTotal': float(returns[2]),
        'returnBudgetDifer': float(returns[3]),
        'finalComission': float(sales[0]) - float(returns[0])
    }


def getComissionObjectDay(user, totalComission, startDate, endDate):
    workingHours = [8.5, 8.5, 8.5, 8.5, 8.5, 6.5, 0]

    step = dt.timedelta(days=1)

    totalComission = float(totalComission)

    leftMonthHours = 0
    while startDate <= endDate:
        leftMonthHours += workingHours[startDate.weekday()]
        startDate += step

    if user.comissionObjective:
        objective = ((user.comissionObjective - totalComission) /
                     leftMonthHours) * workingHours[datetime.now().weekday()]
        return objective
    else:
        return 0


def getUserInfo(user):
    now = datetime.now().date()
    startDate, endDate = getDateRange(user.startedDate)

    daylyComission = getComission(user, now, now)
    monthComission = getComission(user, startDate, endDate)

    daylySales, daylyReturns = getCount(user, now, now)
    monthSales, monthReturns = getCount(user, startDate, endDate)

    data = {
        'name': user.nomeVend,
        'lastUpdate': str(datetime.now()),
        'salary': ("%.2f" % user.salary),
        'salaryDate': str(endDate) + ' 19:59:59',
        'comissionMult': str(user.comissionMult),
        'today': {
            'totalSales': str(daylySales),
            'objective': ("%.2f" % getComissionObjectDay(user, monthComission['finalComission'], now, endDate)),
            'returns': str(daylyReturns),
            'saleFinalComission': ("%.2f" % daylyComission['saleFinalComission']),
            'saleBruteTotal': ("%.2f" % daylyComission['saleBruteTotal']),
            'saleLiquidTotal': ("%.2f" % daylyComission['saleLiquidTotal']),
            'saleBudgetDifer': ("%.2f" % daylyComission['saleBudgetDifer']),
            'returnFinalComission': ("%.2f" % daylyComission['returnFinalComission']),
            'returnBruteTotal': ("%.2f" % daylyComission['returnBruteTotal']),
            'returnLiquidTotal': ("%.2f" % daylyComission['returnLiquidTotal']),
            'returnBudgetDifer': ("%.2f" % daylyComission['returnBudgetDifer']),
            'finalComission': ("%.2f" % daylyComission['finalComission'])
        },
        'month': {
            'totalSales': str(monthSales),
            'objective': ("%.2f" % user.comissionObjective),
            'returns': str(monthReturns),
            'saleFinalComission': ("%.2f" % monthComission['saleFinalComission']),
            'saleBruteTotal': ("%.2f" % monthComission['saleBruteTotal']),
            'saleLiquidTotal': ("%.2f" % monthComission['saleLiquidTotal']),
            'saleBudgetDifer': ("%.2f" % monthComission['saleBudgetDifer']),
            'returnFinalComission': ("%.2f" % monthComission['returnFinalComission']),
            'returnBruteTotal': ("%.2f" % monthComission['returnBruteTotal']),
            'returnLiquidTotal': ("%.2f" % monthComission['returnLiquidTotal']),
            'returnBudgetDifer': ("%.2f" % monthComission['returnBudgetDifer']),
            'finalComission': ("%.2f" % monthComission['finalComission'])
        },
        'notice': "\"  \""
    }
    return data
