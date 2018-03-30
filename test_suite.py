# coding:utf-8
import unittest
from youli_app.test_case import case01_login as youli_login

from zhiyu_app.test_case import case01_login as zhiyu_login
from zhiyu_app.test_case import case11_house_signtocheckout_fensan_flow
from zhiyu_app.test_case import case12_house_signtocheckout_fensan_flow02
from zhiyu_app.test_case import case13_house_signtocheckout_fensan_flow03
from zhiyu_app.test_case import case14_house_signtocheckout_jizhong_flow
from zhiyu_app.test_case import case15_house_signtocheckout_jizhong_flow02
from zhiyu_app.test_case import case16_house_signtocheckout_jizhong_flow03


suite = unittest.TestSuite()

# 运行单个case
suite.addTest(youli_login.LogIn('test_login'))
# suite.addTest(zhiyu_login.LogIn('test_login'))

# 运行一组case
# 优粒租房app是测试包
# suite.addTest(unittest.makeSuite(youli_login.LogIn))

# 智寓伙伴app是生产包
# suite.addTest(unittest.makeSuite(zhiyu_login.LogIn))
# suite.addTest(unittest.makeSuite(case11_house_signtocheckout_fensan_flow.SignToCheckout))
# suite.addTest(unittest.makeSuite(case12_house_signtocheckout_fensan_flow02.SignToCheckout))
# suite.addTest(unittest.makeSuite(case13_house_signtocheckout_fensan_flow03.SignToCheckout))
# suite.addTest(unittest.makeSuite(case14_house_signtocheckout_jizhong_flow.SignToCheckout))
# suite.addTest(unittest.makeSuite(case15_house_signtocheckout_jizhong_flow02.SignToCheckout))
# suite.addTest(unittest.makeSuite(case16_house_signtocheckout_jizhong_flow03.SignToCheckout))
