# coding:utf-8

import unittest
from public import driver
from youli_app.page_action import page_action_wode, page_action_home, page_action_login
from test_data import data


class LogIn(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app_youli()
        self.wode = page_action_wode.WoDe(self.driver)
        self.home = page_action_home.Home(self.driver)
        self.login_page = page_action_login.LogIn(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.home.judge_homepage()
        self.home.click_tab_wode()
        self.wode.login_judge(data.user, data.pwd)

    def test_login_usererror(self):
        self.home.judge_homepage()
        self.home.click_tab_wode()
        self.wode.login_login(data.user_e, data.pwd)
        self.login_page.judge_login_page()

    def test_login_pwderror(self):
        self.home.judge_homepage()
        self.home.click_tab_wode()
        self.wode.login_login(data.user, data.pwd_e)
        self.login_page.judge_login_page()




if __name__ == '__main__':
    unittest.main()








