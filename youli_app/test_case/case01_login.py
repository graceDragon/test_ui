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

    def test_login_user_long(self):
        self.home.judge_homepage()
        self.home.click_tab_wode()
        self.wode.judge_wode_page()
        # 判断手机号输入框允许输入最长字符
        self.wode.logout_judge()
        self.wode.judge_wode_page()
        self.wode.click_login()
        self.login_page.send_keys_user(data.user_01_long)
        user_read = self.login_page.read_user()
        print '读取的数据：', user_read
        if user_read == data.user_01:
            pass
        else:
            assert True is False




if __name__ == '__main__':
    unittest.main()








