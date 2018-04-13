# coding:utf-8

import unittest
from public import driver
from test_data import data
from youli_app.page_action import page_action_wode, page_action_home


class WodeMessage(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app_youli()
        self.wode = page_action_wode.WoDe(self.driver)
        self.home = page_action_home.Home(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_message(self):
        self.home.judge_homepage()
        self.home.click_tab_wode()
        self.wode.judge_wode_page()
        self.wode.login_judge(data.user, data.pwd)
        self.home.click_tab_wode()
        self.wode.wode_waitdo_flow()


if __name__ == '__main__':
    unittest.main()








