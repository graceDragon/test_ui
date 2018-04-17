# coding:utf-8

import unittest
from public import driver
from youli_app.page_action import page_action_home


class Home(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app_youli()
        self.home = page_action_home.Home(self.driver)

    def tearDown(self):
        self.driver.quit()

    # def test_judge_zhengzu(self):
    #     self.home.judge_zhengzu()
    #
    # def test_judge_hezu(self):
    #     self.home.judge_hezu()
    #
    # def test_judge_pinpai(self):
    #     self.home.judge_pinpai()
    #
    # def test_judge_newhouse(self):
    #     self.home.judge_newhouse()
    #
    # def test_judge_youxuan(self):
    #     self.home.judge_youxuanhouse()

    def test_duwei(self):
        self.home.click_duwei()

    # def test_subway(self):
    #     self.home.click_subway()
    #
    # def test_south(self):
    #     self.home.click_south()
    #
    # def test_jingzhuang(self):
    #     self.home.click_jingzhuang()


if __name__ == '__main__':
    unittest.main()








