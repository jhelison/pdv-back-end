from __future__ import annotations
from typing import List

from utility.FDB_handler import FDBHandler
from datetime import date, datetime, timedelta

from models.user import UserModel
from utility.date_handler import DateHandler
from utility.db_log import stopwatch

WEEK_HOURS = [8.5, 8.5, 8.5, 8.5, 8.5, 6.5, 0]

class UserInfo:
    def __init__(self, user: UserModel):
        self.user = user
        self.fdb_handler = FDBHandler()
        
    @stopwatch
    def sales_count(self, start_date: date = None, end_date: date = None) -> int:
        query = f"""
        SELECT 
            COUNT(1) AS SALES_COUNT
        FROM 
            MOVENDA
        WHERE 
            DATA >= ? AND 
            DATA <= ? AND 
            MOVENDA.CODVENDED = ?
        """
        if not start_date and not end_date:
            if not self.user.admissional_date:
                return None
            dh = DateHandler(self.user.admissional_date)
            start_date, end_date = dh.range_on_month_including_today()
        elif start_date and not end_date:
            end_date = start_date
            
        params = (start_date, end_date, self.user.cod_vend)
        
        res = self.fdb_handler.fetchone_as_dict(query, params)
        
        return res['SALES_COUNT']
    
    @stopwatch
    def devolution_count(self, start_date: date = None, end_date: date = None) -> int:
        query = f"""
        SELECT
            COUNT(1) AS DEV_COUNT
        FROM
            MOVENDADEVOLUCAO
        LEFT JOIN
            MOVENDAPROD ON 
                MOVENDADEVOLUCAO.CODMOVPROD = MOVENDAPROD.CODMOVPROD
        LEFT JOIN 
            MOVENDA ON 
                MOVENDAPROD.CODMOVENDA = MOVENDA.CODMOVENDA
        WHERE 
            MOVENDADEVOLUCAO.DATA >= ? AND
            MOVENDADEVOLUCAO.DATA <= ? AND
            MOVENDA.CODVENDED = ?
        """
        
        if not start_date and not end_date:
            if not self.user.admissional_date:
                return None
            dh = DateHandler(self.user.admissional_date)
            start_date, end_date = dh.range_on_month_including_today()
        elif start_date and not end_date:
            end_date = start_date
            
        params = (start_date, end_date, self.user.cod_vend)
        
        res = self.fdb_handler.fetchone_as_dict(query, params)
        
        return res['DEV_COUNT']
        
    @stopwatch
    def sales_comission(self, start_date: date = None, end_date: date = None) -> dict:
        query = """
        SELECT
	        SUM(CAST((VALORTOTAL_ITEM - (VALORTOTAL_ITEM * ACRS_DESC_PER_MONETARY)) * (PRODUTO.COMISSAO / 100) AS NUMERIC(18,2))) AS COMISSAO,
	        SUM(VALORTOTAL_ITEM) AS TOTAL_SALES
        FROM
            (
            SELECT
                CODPROD,
                VALORTOTAL_ITEM,
                VALORTOTALNOTA,
                CAST((VALORDESCONTO_NOTA - VALORACRESCIMO_NOTA) / VALORTOTALPRODUTOS AS NUMERIC(18,6)) AS ACRS_DESC_PER_MONETARY
            FROM
                (
                SELECT
                    MOVENDAPROD.CODPROD,
                    MOVENDAPROD.VALORTOTAL AS VALORTOTAL_ITEM,
                    MOVENDA.VALORTOTALNOTA,
                    COALESCE(MOVENDA.VALORDESCONTO, 0) AS VALORDESCONTO_NOTA, --Sometimes the desconto is null, if null return 0
                    COALESCE(MOVENDA.VALORACRESCIMO, 0) AS VALORACRESCIMO_NOTA, --Sometimes the acrescimo is null, if null return 0
                    COALESCE(NULLIF(MOVENDA.VALORTOTALPRODUTOS, 0), NULLIF(MOVENDA.VALORTOTALNOTA, 0)) AS VALORTOTALPRODUTOS --This columns can't be 0! Better null than zero.
                FROM
                    MOVENDAPROD
                INNER JOIN
                    MOVENDA ON
                        MOVENDA.CODMOVENDA = MOVENDAPROD.CODMOVENDA
                WHERE
                    MOVENDA.DATA >= ? AND MOVENDA.DATA <= ? AND
                    MOVENDA.CODVENDED = ?
                )
            ) AS SUBSET
        LEFT JOIN
            PRODUTO ON
                PRODUTO.CODPROD = SUBSET.CODPROD
        """
        
        if not start_date and not end_date:
            if not self.user.admissional_date:
                return None
            dh = DateHandler(self.user.admissional_date)
            start_date, end_date = dh.range_on_month_including_today()
        elif start_date and not end_date:
            end_date = start_date
            
        params = (start_date, end_date, self.user.cod_vend)
        
        res = self.fdb_handler.fetchone_as_dict(query, params)
        
        return res
        
    @stopwatch
    def devolution_comission(self, start_date: date = None, end_date: date = None) -> dict:
        query = """
        --This is the official devolution table, it calculates the price of each item that the sum is equals to VALORTOTALNOTA!
        --It don't take into consideration frete or others variables.
        SELECT
            SUM(CAST((VALORTOTAL_ITEM - (VALORTOTAL_ITEM * ACRS_DESC_PER_MONETARY)) * (PRODUTO.COMISSAO / 100) AS NUMERIC(18,2))) AS COMISSAO,
            SUM(VALORTOTAL_ITEM) AS TOTAL_DEVOLUTIONS
        FROM
            (
            SELECT
                CODPROD,
                VALORTOTALNOTA,
                CAST((VALORDESCONTO_NOTA - VALORACRESCIMO_NOTA) / VALORTOTALPRODUTOS AS NUMERIC(18,6)) AS ACRS_DESC_PER_MONETARY,
                CAST((VALORTOTAL / QUANTIDADE) * QUANTIDADEDEVOLUCAO AS NUMERIC(18,6)) AS VALORTOTAL_ITEM
            FROM
                (
                SELECT
                    MOVENDAPROD.CODPROD,
                    MOVENDAPROD.VALORTOTAL,
                    MOVENDAPROD.QUANTIDADE,
                    MOVENDADEVOLUCAO.QUANTIDADEDEVOLUCAO, --Especific for devolution.
                    MOVENDA.VALORTOTALNOTA,
                    COALESCE(MOVENDA.VALORDESCONTO, 0) AS VALORDESCONTO_NOTA, --Sometimes the desconto is null, if null return 0
                    COALESCE(MOVENDA.VALORACRESCIMO, 0) AS VALORACRESCIMO_NOTA, --Sometimes the acrescimo is null, if null return 0
                    COALESCE(NULLIF(MOVENDA.VALORTOTALPRODUTOS, 0), NULLIF(MOVENDA.VALORTOTALNOTA, 0)) AS VALORTOTALPRODUTOS --This columns can't be 0! Better null than zero.
                FROM
                    MOVENDADEVOLUCAO
                LEFT JOIN
                    MOVENDAPROD ON
                        MOVENDAPROD.CODMOVPROD = MOVENDADEVOLUCAO.CODMOVPROD
                INNER JOIN
                    MOVENDA ON
                        MOVENDA.CODMOVENDA = MOVENDAPROD.CODMOVENDA
                WHERE
                    MOVENDA.DATA >= ? AND MOVENDA.DATA <= ? AND
                    MOVENDA.CODVENDED = ?
                )
            ) AS SUBSET
        LEFT JOIN
            PRODUTO ON
                PRODUTO.CODPROD = SUBSET.CODPROD
        """
        
        if not start_date and not end_date:
            if not self.user.admissional_date:
                return None
            dh = DateHandler(self.user.admissional_date)
            start_date, end_date = dh.range_on_month_including_today()
        elif start_date and not end_date:
            end_date = start_date
            
        params = (start_date, end_date, self.user.cod_vend)
        
        res = self.fdb_handler.fetchone_as_dict(query, params)
        
        return res
        
        
    def comission_objective_today(self, total_comission: float, start_date: date, end_date: date) -> float:
        if self.user.comission_objective:
            comission_until_now = self.user.comission_objective - total_comission
            comission_left_in_month_per_hour = comission_until_now / self.working_hours_in_period(start_date, end_date)
            return comission_left_in_month_per_hour * WEEK_HOURS[date.today().weekday()] 
        else:
            return None
        
    def as_json(self):
        salary_date = None
        if self.user.admissional_date:
            dh = DateHandler(self.user.admissional_date)
            _, salary_date = dh.range_on_month_including_today()
                        
        data = {
            'user_Data': self.user.to_json(),
            'today': {
                'sales_count': self.sales_count(date.today()),
                'devolution_count': self.devolution_count(date.today()),
                'sales_values': {
                    **self.sales_comission(date.today())
                },
                'devolution_values': {
                    **self.devolution_comission(date.today())
                }
            },
            'month_range':{
                'sales_count': self.sales_count(),
                'devolution_count': self.devolution_count(),
                'sales_values': {
                    **self.sales_comission()
                },
                'devolution_values': {
                    **self.devolution_comission()
                }
            }
        }
        
        return FDBHandler.convert_to_JSON(data)
        
    @staticmethod
    def working_hours_in_period(start_date: date, end_date: date, week_hours: List = WEEK_HOURS) -> int:
        hours = 0
        while start_date <= end_date:
            hours += week_hours[start_date.weekday()]
            start_date += timedelta(days=1)
            
        return hours
            
        
            
        


