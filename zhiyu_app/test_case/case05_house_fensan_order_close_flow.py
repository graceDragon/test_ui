# coding:utf-8
"""
预定-提交-财务打回-分散式
"""

import unittest
from public import driver
from test_data import data
from zhiyu_app.page_action import page_action_login, page_action_house_status
from zhiyu_app.page_action import page_action_home, page_action_orders


class HouseJizhongSignFlow(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app()
        self.plogin = page_action_login.LogIn(self.driver)
        self.phome = page_action_home.HomePage(self.driver)
        self.phs = page_action_house_status.HouseStatus(self.driver)
        self.pao = page_action_orders.PageActionOrders(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_house_jizhong_sign_flow(self):
        self.plogin.login_judge(data.user_01, data.pwd_01)
        self.phome.click_tab_house_status()
        self.phs.house_status_fensan_order_close_flow(data.district_fengtai, data.street_liuliqiao,
                                                      data.community_fensan_02, data.room_no_402,
                                                      data.user_01)
        self.phome.click_tab_home()
        self.pao.click_wait_pay()
        self.pao.refress_screen()
        # self.pao.close_order_wait_pay(data.community_fensan_02, data.room_no_402)
        self.pao.confirm_order_wait_pay(data.community_fensan_02, data.room_no_402)
        self.pao.fee_page_flow(money_1=100, remark=data.remark)
        self.pao.caiwu_pay_dahui(data.community_fensan_02, data.room_no_402)
        self.pao.click_wait_pay()
        self.pao.refress_screen()
        self.pao.close_order_wait_pay(data.community_fensan_02, data.room_no_402)
        self.pao.confirm()


if __name__ == '__main__':
    unittest.main()



