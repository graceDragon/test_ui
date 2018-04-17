# coding:utf-8

import unittest
from public import driver
from youli_app.page_action import page_action_wode, page_action_home, page_action_forgetpwd
from youli_app.page_action import page_action_login
from test_data import data


class ForgetPwd(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app_youli()
        self.wode = page_action_wode.WoDe(self.driver)
        self.home = page_action_home.Home(self.driver)
        self.login = page_action_login.LogIn(self.driver)
        self.forgetpwd = page_action_forgetpwd.ForgetPwd(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_forgetpwd(self):
        self.home.judge_homepage()
        self.home.click_tab_wode()
        self.wode.logout_judge()
        self.wode.click_login()
        self.login.judge_login_page()
        self.login.click_forgetpwd()
        self.forgetpwd.forgetpwd_flow(data.user, data.sql_yzm, data.pwd)
        self.login.judge_login_page()


if __name__ == '__main__':
    # unittest.main()
    ForgetPwd().test_forgetpwd()








