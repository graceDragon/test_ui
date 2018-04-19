# coding:utf-8

import unittest
from public import driver
from test_data import data
from youli_app.page_action import page_action_location, page_action_home


class Location(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app_youli()
        self.home = page_action_home.Home(self.driver)
        self.location = page_action_location.ChangeCity(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_location(self):
        self.home.judge_homepage()
        self.home.click_change_city()
        self.location.judge_title()
        self.location.select_city(data.city_bj)
        self.home.judge_city(data.city_bj)

if __name__ == '__main__':
    unittest.main()








