# coding:utf-8
"""
分散式-退房
"""

import unittest
from public import driver
from test_data import data
from zhiyu_app.page_action import page_action_login, page_action_house_status
from zhiyu_app.page_action import page_action_home, page_action_orders, page_action_checkout


class HouseJizhongSignFlow(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app()
        self.plogin = page_action_login.LogIn(self.driver)
        self.phome = page_action_home.HomePage(self.driver)
        self.phs = page_action_house_status.HouseStatus(self.driver)
        self.pac = page_action_checkout.CheckOut(self.driver)
        self.pao = page_action_orders.PageActionOrders(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_house_jizhong_sign_flow(self):
        self.plogin.login_judge(data.user_01, data.pwd_01)
        self.phome.click_tab_house_status()
        self.phs.select_community_room_fensan02(data.district_fengtai, data.street_liuliqiao,
                                                data.community_fensan_02, data.room_no_201,)
        self.phs.room_checkout()
        self.pac.checkout_flow_easy(data.item_bed, data.reason_bed, data.room_status)


if __name__ == '__main__':
    unittest.main()



