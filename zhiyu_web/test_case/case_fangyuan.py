# coding:utf-8
import unittest
from zhiyu_web.page_action import page_action_fangyuan
from zhiyu_web.page_action import page_action_login
from public import driver
from config import settings
from test_data import data


class FangYuan(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_web(settings.url_zhiyu_online)
        self.fangyuan = page_action_fangyuan.FangYuan(self.driver)
        self.login = page_action_login.PageActionLogin(self.driver)

    def tearDown(self):
        pass

    def test_on_community(self):
        # 启用/停用社区
        self.fangyuan.open_community(data.user_01, data.pwd_01)
        # self.login.login_page_action(data.user_01, data.pwd_01)
        # self.fangyuan.click_jizhong_community()
        # self.fangyuan.click_ui_test()
        # self.fangyuan.read_test()

    def test_off_community(self):
        # 启用/停用社区
        self.fangyuan.close_community(data.user_01, data.pwd_01)

    # def test_off_community(self):
    #     self.login.login_page_action(data.user_01, data.pwd_01)
    #     self.fangyuan.click_jizhong_community()
    #


if __name__ == '__main__':
    unittest.main()

