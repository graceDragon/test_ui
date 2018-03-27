# coding:utf-8

import unittest
from public import driver
from test_data import data
from zhiyu_app.page_action import page_action_login, page_action_house_status
from zhiyu_app.page_action import page_action_home, page_action_orders
from time import sleep


class HouseJizhongSignFlow(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app()
        self.plogin = page_action_login.LogIn(self.driver)
        self.phome = page_action_home.HomePage(self.driver)
        self.phs = page_action_house_status.HouseStatus(self.driver)
        self.pao = page_action_orders.PageActionOrders(self.driver)

    def tearDown(self):
        pass

    def test_house_fensan_sign_flow(self):
        self.plogin.login_judge(data.user, data.pwd)
        self.phome.click_tab_house_status()
        self.phs.house_status_flow_fensan(data.district_dongcheng, data.street_longtan, data.community_fensan_01,
                                          data.room_no_01, data.user, data.rent_time_3, method='季付', fee1='房屋租金',
                                          zhouqi1='周期费用', day=1, addmoney='1000', furniture1='床', model1='1.2米床',
                                          num1=3, mendian='江大门店', saleman='张爱东', fapiao='No'
                                          )
        self.phome.click_tab_order()
        self.pao.order_flow(data.community_fensan_01, data.room_no_01)

if __name__ == '__main__':
    unittest.main()



