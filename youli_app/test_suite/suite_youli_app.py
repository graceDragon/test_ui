# coding:utf-8

import unittest
from ..test_case import case01_login


suite = unittest.TestSuite()
# 运行单个case
suite.addTest(case01_login.LogIn('test_login'))

# 运行一组case
# suite.addTest(unittest.makeSuite(case01_login.LogIn))









