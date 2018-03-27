# coding:utf-8

import unittest
from public import driver
from config.settings import *
from test_data.data import *
from zhiyu_web.page_action import page_action_house_status
from time import sleep


class HoustStatus(unittest.TestCase):

    def setUp(self):
        self.driver = driver.Driver().driver_web_session(url_zhiyu_test)
        self.pa = page_action_house_status.PageActionHouseStatus(self.driver)

    def tearDown(self):
        pass

    # 实时房态
    def test_house_status_now(self):
        self.pa.house_status_01()
        self.pa.scrollbar_web(10000)
        sleep(3)
        self.pa.house_site_judge(house_site_mango)


if __name__ == '__main__':
    unittest.main()













