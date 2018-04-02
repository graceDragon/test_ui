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

    def test_judge_zhengzu(self):
        self.home.judge_zhengzu()

    def test_judge_hezu(self):
        self.home.judge_hezu()

    def test_judge_pinpai(self):
        self.home.judge_pinpai()


if __name__ == '__main__':
    unittest.main()








