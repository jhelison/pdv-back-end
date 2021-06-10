from calendar import month
import unittest
from datetime import date
import sys

sys.path.insert(0, './')

from utility.date_handler import DateHandler

class TestDateHandler(unittest.TestCase):
    def test_set_year(self):
        test_date = date(2020, 2, 29)
        date_handler = DateHandler(test_date)

        date_handler.set_year(2021)

        self.assertEqual(date_handler.date, date(2021, 2, 28))

    def test_set_month_below_range(self):
        test_date = date(2020, 2, 29)
        date_handler = DateHandler(test_date)

        date_handler.set_month(-1)

        self.assertEqual(date_handler.date, date(2019, 12, 29))

    def test_set_month_after_range(self):
        test_date = date(2020, 2, 29)
        date_handler = DateHandler(test_date)

        date_handler.set_month(13)

        self.assertEqual(date_handler.date, date(2021, 1, 29))

    def test_set_month_day_out_range(self):
        test_date = date(2020, 12, 31)
        date_handler = DateHandler(test_date)

        date_handler.set_month(11)

        self.assertEqual(date_handler.date, date(2020, 11, 30))

    def test_set_day(self):
        test_date = date(2020, 12, 31)
        date_handler = DateHandler(test_date)

        date_handler.set_day(11)

        self.assertEqual(date_handler.date, date(2020, 12, 11))

    def test_set_day_below_range(self):
        test_date = date(2020, 12, 31)
        date_handler = DateHandler(test_date)

        date_handler.set_day(-1)

        self.assertEqual(date_handler.date, date(2020, 11, 30))

    def test_set_day_after_range(self):
        test_date = date(2020, 11, 30)
        date_handler = DateHandler(test_date)

        date_handler.set_day(40)

        self.assertEqual(date_handler.date, date(2020, 12, 1))

    def test_set_day_below_range_month_1(self):
        test_date = date(2020, 1, 4)
        date_handler = DateHandler(test_date)

        date_handler.set_day(-1)

        self.assertEqual(date_handler.date, date(2019, 12, 31))

    def test_set_day_below_range_month_12(self):
        test_date = date(2020, 12, 4)
        date_handler = DateHandler(test_date)

        date_handler.set_day(50)

        self.assertEqual(date_handler.date, date(2021, 1, 1))

    def test_range_on_month_middle(self):
        test_date = date(2020, 1, 15)
        date_handler = DateHandler(test_date)

        self.assertEqual(date_handler.range_on_month(), (date(2019, 12, 16), date(2020, 1, 15)))

    def test_range_on_month_upper_extreme(self):
        test_date = date(2021, 1, 31)
        date_handler = DateHandler(test_date)

        self.assertEqual(date_handler.range_on_month(), (date(2021, 1, 1), date(2021, 1, 31)))


    def test_range_on_month_lower_extreme(self):
        test_date = date(2020, 1, 1)
        date_handler = DateHandler(test_date)
        
        date_handler.range_on_month_for_month()

        self.assertEqual(date_handler.range_on_month(), (date(2019, 12, 2), date(2020, 1, 1)))
        
    # def test_range_on_month_lower_extreme(self):
    #     test_date = date(2020, 1, 1)
    #     date_handler = DateHandler(test_date)
        
    #     date_handler.range_on_month_for_month()

    #     self.assertEqual(date_handler.range_on_month(), (date(2019, 12, 2), date(2020, 1, 1)))
        
    # def test_range_on_month_lower_extreme(self):
    #     test_date = date(2020, 1, 1)
    #     date_handler = DateHandler(test_date)
        
    #     date_handler.range_on_month_for_month()

    #     self.assertEqual(date_handler.range_on_month(), (date(2019, 12, 2), date(2020, 1, 1)))
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
