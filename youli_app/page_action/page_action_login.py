# coding:utf-8

from public import public_method
from ..page import page_login


class LogIn(object):
    def __init__(self, driver):
        # 登录判断在我的里边
        self.driver = driver
        self.pm = public_method.PublicMethod(driver)

    def judge_login_page(self):
        self.pm.assert_el_by_name(page_login.login_confirm)

    def send_keys_user(self, user):
        self.pm.send_keys_by_id(page_login.login_user, user)

    def read_user(self):
        # 读取用户名
        user_read = self.pm.read_element_txt_by_id(page_login.login_user)
        return user_read

    def login(self, user, pwd):
        self.pm.send_keys_by_id(page_login.login_user, user)
        self.pm.send_keys_by_id(page_login.login_pwd, pwd)
        self.pm.click_by_name(page_login.login_confirm)  # 回到我的首页













