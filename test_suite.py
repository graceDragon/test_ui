# coding:utf-8
import unittest
from youli_app.test_case import case01_login as youli_login
from zhiyu_app.test_case import case01_login as zhiyu_login

suite = unittest.TestSuite()

# 运行单个case
suite.addTest(youli_login.LogIn('test_login'))
# suite.addTest(zhiyu_login.LogIn('test_login'))

# 运行一组case
# suite.addTest(unittest.makeSuite(youli_login.LogIn))
# suite.addTest(unittest.makeSuite(zhiyu_login.LogIn))

