# coding:utf-8
import unittest
from zhiyu_web.test_case import case_fangyuan
from youli_app.test_case import case01_login as youli_login
from youli_app.test_case import case02_home
from youli_app.test_case import case03_yuyue_flow
from youli_app.test_case import case04_wode_message
from youli_app.test_case import case05_wode_waitdo
from youli_app.test_case import case06_location
from youli_app.test_case import case07_zhengzu_flow
from youli_app.test_case import case08_regist
from youli_app.test_case import case09_forgetpwd
from youli_app.test_case import case10_houselist

from zhiyu_app.test_case import case01_login as zhiyu_login
from zhiyu_app.test_case import case11_house_signtocheckout_fensan_flow
from zhiyu_app.test_case import case12_house_signtocheckout_fensan_flow02
from zhiyu_app.test_case import case13_house_signtocheckout_fensan_flow03
from zhiyu_app.test_case import case14_house_signtocheckout_jizhong_flow
from zhiyu_app.test_case import case15_house_signtocheckout_jizhong_flow02
from zhiyu_app.test_case import case16_house_signtocheckout_jizhong_flow03

suite = unittest.TestSuite()

# *************运行单个case
# suite.addTest(youli_login.LogIn('test_login'))
# suite.addTest(zhiyu_login.LogIn('test_login'))


# *************运行一组case
# ----------先打开社区（web端启用社区）
suite.addTest(case_fangyuan.FangYuan('test_on_community'))

# ----------优粒租房app------用的是测试包
suite.addTest(unittest.makeSuite(youli_login.LogIn))
suite.addTest(unittest.makeSuite(case02_home.Home))
suite.addTest(unittest.makeSuite(case03_yuyue_flow.YuYue))
suite.addTest(unittest.makeSuite(case04_wode_message.WodeMessage))
suite.addTest(unittest.makeSuite(case05_wode_waitdo.WodeWaitdo))
suite.addTest(unittest.makeSuite(case06_location.Location))
suite.addTest(unittest.makeSuite(case07_zhengzu_flow.ZhengZu))
suite.addTest(unittest.makeSuite(case08_regist.Regist))
suite.addTest(unittest.makeSuite(case09_forgetpwd.ForgetPwd))
suite.addTest(unittest.makeSuite(case10_houselist.HouseList))

# ---------智寓伙伴app-------用的是生产包
suite.addTest(unittest.makeSuite(zhiyu_login.LogIn))
suite.addTest(unittest.makeSuite(case11_house_signtocheckout_fensan_flow.SignToCheckout))
suite.addTest(unittest.makeSuite(case12_house_signtocheckout_fensan_flow02.SignToCheckout))
suite.addTest(unittest.makeSuite(case13_house_signtocheckout_fensan_flow03.SignToCheckout))
suite.addTest(unittest.makeSuite(case14_house_signtocheckout_jizhong_flow.SignToCheckout))
suite.addTest(unittest.makeSuite(case15_house_signtocheckout_jizhong_flow02.SignToCheckout))
suite.addTest(unittest.makeSuite(case16_house_signtocheckout_jizhong_flow03.SignToCheckout))

# ---------后关闭社区（web端停用社区）
suite.addTest(case_fangyuan.FangYuan('test_off_community'))






