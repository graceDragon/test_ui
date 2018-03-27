# coding:utf-8
import unittest
from public import date, public_method
from time import strftime, localtime
from datetime import timedelta
import datetime
import re

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test01(self):
        d = '2018-02-27'
        d1 = date.get_day_of_d(d, n=-1)
        print d1, type(d1)

    def test02(self):
        str = '2018-02-28至2018-03-27'
        str1 = str.split('至')
        print str1

    def test_03(self):
        str1 = '-￥5500.00'
        num = re.findall(("\d+\.*\d*"), str1)
        num = num[0]
        num = float(num)
        print '正则之后的数字：', num, type(num)

    def test_04(self):
        print '*************************'
        print '*************************'
        str1 = '2018-8-31'
        str1_list = str1.split('-')
        str1_list[1] = '0' + str1_list[1]
        str2 = '-'.join(str1_list)
        print str1_list, str1, str2

if __name__ == '__main__':
    Test().test_03()

