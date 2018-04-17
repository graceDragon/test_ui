# coding:utf-8

import unittest
from public import driver
from youli_app.page_action import page_action_fangyuan_list, page_action_home


class HouseList(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app_youli()
        self.list = page_action_fangyuan_list.FangyuanList(self.driver)
        self.home = page_action_home.Home(self.driver)

    def tearDown(self):
        self.driver.quit()

    # def test_houselist_zheng(self):
    #     self.home.judge_homepage()
    #     self.home.click_zhengzu()
    #     self.list.judge_zhengzu_list()

    def test_houselist_he(self):
        self.home.judge_homepage()
        self.home.click_hezu()
        self.list.judge_hezu_list()


if __name__ == '__main__':
    # unittest.main()
    HouseList().test_houselist_he()








