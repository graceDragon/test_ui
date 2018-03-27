# coding:utf-8

"""
财务-订单管理
"""

import unittest
from zhiyu_web.page_action import page_action_login
from zhiyu_web.page_action import page_action_finance
from public import driver
from config.settings import *
from test_data.data import *


class FinanceOrderManage(unittest.TestCase):

    def setUp(self):
        self.driver = driver.Driver().driver_web_session(url_zhiyu_test)
        self.login = page_action_login.PageActionLogin(self.driver)
        self.finance = page_action_finance.Finance(self.driver)

    def tearDown(self):
        pass
        # self.driver.quit()

    def test_finance_order_manage(self):
        self.login.login_page_action(user, pwd)
        self.finance.order_manage_flow(house_id)


if __name__ == '__main__':
    FinanceOrderManage().test_finance_order_manage()


