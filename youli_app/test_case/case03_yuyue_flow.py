# coding:utf-8
"""
预约流程-整租
"""

import unittest
from public import driver
from test_data import data
from youli_app.page_action import page_action_login, page_action_home, page_action_fangyuan_list
from youli_app.page_action import page_action_house_detail


class YuYue(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app_youli()
        self.login = page_action_login.LogIn(self.driver)
        self.home = page_action_home.Home(self.driver)
        self.list = page_action_fangyuan_list.FangyuanList(self.driver)
        self.detail = page_action_house_detail.HouseDetail(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_yuyue_flow(self):
        self.home.judge_homepage()
        self.home.click_tab_wode()
        self.login.login_judge(data.user, data.pwd)
        self.home.click_zhengzu()
        self.list.fangyuan_list_flow(data.two_house, data.one_house, data.mangguo, data.address,
                                     data.address_qu_chaoyang, data.address_jiedao_maizi, data.zhuangxiu_haohua,
                                     data.house_name_02)
        self.detail.yuyue_page_flow()


if __name__ == '__main__':
    unittest.main()








