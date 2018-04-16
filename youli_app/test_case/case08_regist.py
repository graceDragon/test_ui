# coding:utf-8

import unittest
from public import driver
from youli_app.page_action import page_action_wode, page_action_home, page_action_regist
from youli_app.page_action import page_action_login
from test_data import data


class Regist(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app_youli()
        self.wode = page_action_wode.WoDe(self.driver)
        self.home = page_action_home.Home(self.driver)
        self.regist = page_action_regist.Regist(self.driver)
        self.login = page_action_login.LogIn(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_regist(self):
        self.home.click_tab_wode()
        self.wode.judge_wode_page()
        self.wode.logout_judge()
        self.wode.click_login()
        self.login.judge_login_page()
        self.login.click_regist()
        self.regist.regist_flow(data.user, data.pwd)
        self.regist.judge_regist_page()


if __name__ == '__main__':
    # unittest.main()
    Regist().test_regist()








