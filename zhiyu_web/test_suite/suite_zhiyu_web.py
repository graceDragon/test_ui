# coding:utf-8

import unittest

from ..test_case import case_login


suite = unittest.TestSuite()
# 运行单个case
suite.addTest(case_login.LogIn('test_login'))

# 运行一组case
# suite.addTest(unittest.makeSuite(case_login.LogIn))









