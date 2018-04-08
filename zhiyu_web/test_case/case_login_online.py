# coding:utf-8

import unittest
from zhiyu_web.page_action import page_action_login
from config.settings import *
from public import driver
from test_data.data import *


class LogIn(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_web(url_zhiyu_online)
        self.pa = page_action_login.PageActionLogin(self.driver)

    def tearDown(self):
        pass

    def test_login_online(self):
        self.pa.login_page_action(user_01, pwd_01)


if __name__ == '__main__':
    LogIn().test_login_online()

