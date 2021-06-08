import unittest
from datetime import date

import sys
sys.path.insert(0, './')

from models.userInfo2 import UserInfo

class TestUserInfo(unittest.TestCase):
    def test_get_month_range(self):
        result = UserInfo.get_month_range(date(2021, 4, 15))
        self.assertEqual(result, (date(2021, 3, 16), date(2021, 4, 15)))

    def test_get_month_range_on_last_month_day(self):
        result = UserInfo.get_month_range(date(2021, 3, 31))
        self.assertEqual(result, (date(2021, 3, 1), date(2021, 3, 31)))

    def test_get_month_range_on_first_month_day(self):
        result = UserInfo.get_month_range(date(2021, 3, 1))
        self.assertEqual(result, (date(2021, 2, 2), date(2021, 3, 1)))

    def test_get_month_range_with_less_than_today(self):
        result = UserInfo.get_month_range(date(2021, 3, 5), True)
        self.assertEqual(result, (date(2021, 6, 6), date(2021, 7, 5)))

    # def test_get_month_range_with_more_than_today(self):
    #     result = UserInfo.get_month_range(date(2021, 3, 15))
    #     self.assertEqual(result, (date(2021, 5, 16), date(2021, 6, 15)))

if __name__ == '__main__':
    unittest.main(verbosity=2)