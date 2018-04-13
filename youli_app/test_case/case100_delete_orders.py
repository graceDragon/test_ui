# coding:utf-8
"""
我的预约-删除订单
"""

import unittest
from public import driver
from test_data import data
from youli_app.page_action import page_action_wode, page_action_home, page_action_fangyuan_list


class YuYue(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app_youli()
        self.login = page_action_wode.WoDe(self.driver)
        self.home = page_action_home.Home(self.driver)
        self.wode = page_action_wode.WoDe(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_yuyue_flow(self):
        self.home.judge_homepage()
        self.home.click_tab_wode()
        self.login.login_judge(data.user, data.pwd)
        self.home.click_tab_wode()
        self.wode.click_yuyue()
        self.wode.delete_all_orders()


if __name__ == '__main__':
    unittest.main()








