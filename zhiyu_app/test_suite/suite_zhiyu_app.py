# coding:utf-8

import unittest
from ..test_case import case01_login
from ..test_case import case11_house_signtocheckout_fensan_flow
from ..test_case import case12_house_signtocheckout_fensan_flow02
from ..test_case import case13_house_signtocheckout_fensan_flow03
from ..test_case import case14_house_signtocheckout_jizhong_flow
from ..test_case import case15_house_signtocheckout_jizhong_flow02
from ..test_case import case16_house_signtocheckout_jizhong_flow03


suite = unittest.TestSuite()
# 运行单个case
# suite.addTest(case01_login.LogIn('test_user_long01'))

# 运行一组case
suite.addTest(unittest.makeSuite(case01_login.LogIn))
suite.addTest(unittest.makeSuite(case11_house_signtocheckout_fensan_flow.SignToCheckout))
suite.addTest(unittest.makeSuite(case12_house_signtocheckout_fensan_flow02.SignToCheckout))
suite.addTest(unittest.makeSuite(case13_house_signtocheckout_fensan_flow03.SignToCheckout))
suite.addTest(unittest.makeSuite(case14_house_signtocheckout_jizhong_flow.SignToCheckout))
suite.addTest(unittest.makeSuite(case15_house_signtocheckout_jizhong_flow02.SignToCheckout))
suite.addTest(unittest.makeSuite(case16_house_signtocheckout_jizhong_flow03.SignToCheckout))









