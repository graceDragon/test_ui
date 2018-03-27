# coding:utf-8

import unittest
from public import driver
from zhiyu_app.page_action import page_action_login
from test_data import data


class LogIn(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app()
        self.p = page_action_login.LogIn(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 正常登录
        from public import input_method
        self.p.login_judge(data.user_01, data.pwd_01)
        # import time
        # from zhiyu_app.page import page_home
        # self.driver.find_element_by_id(page_home.search_text).click()
        # print '键盘输入'
        # # self.driver.press_keycode(12)
        # # self.driver.press_keycode(7)
        # # self.driver.press_keycode(8)
        # input_method.InputMethod().input_method_baidu()
        # time.sleep(3)
        # self.driver.find_element_by_id(page_home.search_text).send_keys('123243254')
        #
        # # self.driver.press_keycode(67)  # 删除
        # print '输入完成'
        #
        # # input_method.InputMethod().input_method_baidu()
        # time.sleep(10)
        # # self.driver.press_keycode('KEYCODE_NUMPAD_ENTER')  # 回车
        # # self.driver.press_keycode('KEYCODE_ENTER')  # 回车
        # self.driver.press_keycode(66)  # 回车
        # # self.driver.keyevent(66)
        # # self.driver.press_keycode(84)  # 搜索
        # time.sleep(3)
        # input_method.InputMethod().input_method_appium()
        # time.sleep(5)

    def test_login_username_error(self):
        # 用户名错误
        self.p.logout_judge()
        self.p.judge_login()
        self.p.login(data.user_01_err, data.pwd_01)
        self.p.judge_login()

    def test_login_pwd_error(self):
        # 密码错误
        self.p.logout_judge()
        self.p.judge_login()
        self.p.login(data.user_01, data.pwd_01_err)
        self.p.judge_login()

    def test_user_long(self):
        # 判断手机号输入框允许输入最长字符
        self.p.logout_judge()
        self.p.judge_login()
        user_read = self.p.read_text_user(data.user_01)
        print '读取的数据：', user_read
        if user_read == data.user_01:
            pass
        else:
            assert True is False

    def test_user_long01(self):
        # 判断手机号输入框允许输入最长字符
        self.p.logout_judge()
        self.p.judge_login()
        user_read = self.p.read_text_user(data.user_01_long)
        print '读取的数据：', user_read
        if user_read == data.user_01:
            pass
        else:
            assert True is False


if __name__ == '__main__':
    LogIn().test_login_username_error()













