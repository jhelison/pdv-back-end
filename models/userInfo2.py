from datetime import date, datetime
from FDBHandler import FDBHandler
from typing import Tuple

class UserInfo:
    def __init__(self):
        pass


    @staticmethod
    def get_month_range(input_date : datetime, this_month : bool = False) -> Tuple[date, date]:
        """
        Return the month range based on day starting on day + 1 as a tuple. 
        If this_month is used, returns the date range based on now.date.
        
        get_month_range(date(2021, 4, 15)) returns (date(2021, 3, 16), date(2021, 4, 15))
        get_month_range(date(2021, 3, 31)) returns (date(2021, 3, 1), date(2021, 3, 31))
        get_month_range(date(2021, 3, 1)) returns (date(2021, 2, 2), date(2021, 3, 1)))
        """

        def secure_replace_date(d : date, year=None, month=None, day=None):
            new_date = d
            if year:
                new_date = new_date.replace(year=year)
            if month:
                try:
                    new_date = new_date.replace(month=month)
                except:
                    new_date = new_date.replace(month=1, year=new_date.year + 1)
            if day:
                try:
                    new_date = new_date.replace(day=day)
                except:
                    new_date = next_month(new_date)
            return new_date

        def last_month(d):
            #Try to set last month on day 1. If not possible (<1) return last month on last year.
            try:
                return d.replace(day=1, month = d.month - 1)
            except:
                return d.replace(day=1, month=12, year=d.year - 1)

        def next_month(d):
            #Try to set next month on day 1. If not possible (>12) return first month on next year.
            try:
                return d.replace(day=1, month=d.month + 1)
            except:
                return d.replace(day=1, month=1, year=d.year + 1)


        if this_month:
            if input_date.day < date.today().day:
                input_date = secure_replace_date(input_date, month=date.today().month + 1)
            else:
                input_date = secure_replace_date(input_date, month=date.today().month  + 1)
                # try:
                #     input_date.replace(month=input_date.month + 1)
                # except:
                #     input_date.replace(month=1, year=input_date.year + 1)
            
            # else


            # try:
            #     input_date = date.today().replace(day=input_date.day)
            # except:
            #     input_date = date
            

        
        first_date = secure_replace_date(last_month(input_date), day=input_date.day + 1)
        last_date = secure_replace_date(input_date, day=input_date.day)

        return first_date, last_date

                        
        # day = input_date.day
        # now = datetime.now().date()

        # if day >= now.day:
        #     return set_day_month(subtract_month(now), day + 1, False), set_day_month(now, day, True)
        # else:
        #     return set_day_month(now, day + 1, False), set_day_month(add_month(now), day, True)
