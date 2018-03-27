# coding:utf-8

'''
# 集中式房源-续租
'''

import unittest
from public import driver
from test_data import data
from zhiyu_app.page_action import page_action_login, page_action_house_status
from zhiyu_app.page_action import page_action_home, page_action_orders, page_action_checkout


class HouseJizhongReletFlow(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app()
        self.plogin = page_action_login.LogIn(self.driver)
        self.phome = page_action_home.HomePage(self.driver)
        self.phs = page_action_house_status.HouseStatus(self.driver)
        self.pac = page_action_checkout.CheckOut(self.driver)
        self.pao = page_action_orders.PageActionOrders(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_house_jizhong_relet_flow(self):
        self.plogin.login_judge(data.user, data.pwd)
        self.phome.click_tab_house_status()
        self.phs.select_community_room_jizhong(data.community_name, data.loudong_name_order,
                                               data.room_no_checkout)
        self.phs.room_relet()
        self.phs.relet_fensan(data.rent_time_3, method='季付', day=1, biaodi=100, fee='房屋租金',
                              zhouqi='周期费用', addmoney1='1000', mendian='江大门店', saleman='张爱东')
        self.phs.judege_house_status()
        self.phome.click_tab_order()
        self.pao.order_flow(data.community_fensan_01, data.room_no_01)


if __name__ == '__main__':
    unittest.main()



