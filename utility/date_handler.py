from __future__ import annotations

from datetime import datetime, date
import calendar
from typing import Union, Tuple


class DateHandler:
    def __init__(self, input_date: Union[date, datetime]) -> None:
        if isinstance(input_date, datetime):
            self._input_date = input_date.date()
        else:
            self._input_date = input_date

    @property
    def date(self):
        return self._input_date

    @date.setter
    def date(self, input_date):
        if isinstance(input_date, datetime):
            self._input_date = input_date.date()
        else:
            self._input_date = input_date

    def set_year(self, year: int) -> None:
        """
        Set the year of the date.
        """
        try:
            self._input_date = self._input_date.replace(year=year)
        except:
            last_day_month = self.get_last_day_month(
                year, self._input_date.month)
            self._input_date = self._input_date.replace(
                day=last_day_month, year=year)

    def set_month(self, input_month: int, overflow: bool = True) -> None:
        """
        Set the day of the month.
        If overflow is setted, it will overflow month to years.
        Month > 12 will overflow to year + 1.
        Month < 1 will overflow to year - 1.

        If overflow is false it will set month as a valid month on the same year.
        """
        year = self._input_date.year
        month = input_month
        day = self._input_date.day

        if overflow:
            if month < 1:
                month = 12
                year = year - 1
            elif month > 12:
                month = 1
                year = year + 1
        else:
            if month < 1:
                month = 1
            elif month > 12:
                month = 12

        last_month_day = self.get_last_day_month(year, month)

        if day > last_month_day:
            day = last_month_day

        self._input_date = self._input_date.replace(
            year=year,
            month=month,
            day=day
        )

    def set_day(self, day: int, overflow: bool = True) -> None:
        params_day = self._input_date.day
        params_month = self._input_date.month
        params_year = self._input_date.year

        last_month_day = self.get_last_day_month(params_year, params_month)

        if overflow:
            if day < 1:
                params_month -= 1
                if params_month < 1:
                    params_month = 12
                    params_year -= 1
                params_day = self.get_last_day_month(params_year, params_month)
            elif day > last_month_day:
                params_month += 1
                if params_month > 12:
                    params_month = 1
                    params_year += 1
                params_day = 1
            else:
                params_day = day
        else:
            if day < 1:
                params_day = 1
            elif day > last_month_day:
                params_day = last_month_day
            else:
                params_day = day

        self._input_date = self._input_date.replace(
            year=params_year,
            month=params_month,
            day=params_day
        )

    def range_on_month(self) -> Tuple[date, date]:
        """
        Get a month range as a tuple.

        Return:
        start_date as day + 1, month - 1.
        End_date as day, month.

        If this_month is used, returns the date range based on now.date.

        get_month_range(date(2021, 4, 15)) returns (date(2021, 3, 16), date(2021, 4, 15))
        get_month_range(date(2021, 3, 31)) returns (date(2021, 3, 1), date(2021, 3, 31))
        get_month_range(date(2021, 3, 1)) returns (date(2021, 2, 2), date(2021, 3, 1)))
        """
        return self._calculate_first_date(self._input_date), self._input_date

    def range_on_month_including_today(self) -> Tuple[date, date]:
        """
        Same as range_on_month, but includes today inside the range.
        It negates the month of the date, replacing it with a range that includes today.
        """
        today = date.today()

        objective_date = DateHandler(self._input_date)
        objective_date.set_year(today.year)

        if self._input_date.day < today.day:
            objective_date.set_month(today.month + 1)
        else:
            objective_date.set_month(today.month)

        return self._calculate_first_date(objective_date.date), objective_date.date

    def range_on_month_for_month(self, 
                                 month: int,
                                 year: int = None) -> Tuple[date, date]:
        """
        Get a range of dates based on certain specified month or year.
        """
        objective_date = DateHandler(self._input_date)
        if year:
            objective_date.set_year(year)
            
        objective_date.set_month(month)

        return self._calculate_first_date(objective_date.date), objective_date.date

    @staticmethod
    def get_last_day_month(year: int, month: int) -> int:
        return calendar.monthrange(year, month)[1]

    def _calculate_first_date(self, input_date: date) -> date:
        first_date = DateHandler(input_date)
        first_date.set_month(input_date.month - 1)
        first_date.set_day(self._input_date.day + 1)

        return first_date.date

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(Year={self._input_date.year}, Month={self._input_date.month}, Day={self._input_date.day})"
    
    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(Year={self._input_date.year}, Month={self._input_date.month}, Day={self._input_date.day})"
