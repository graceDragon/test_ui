# coding:utf-8

from public import public_method
from ..page import page_login


class LogIn(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(driver)

    def judge_login_page(self):
        self.pm.assert_el_by_name(page_login.login_confirm)

    def login(self, user, pwd):
        self.pm.send_keys_by_id(page_login.login_user, user)
        self.pm.send_keys_by_id(page_login.login_pwd, pwd)
        self.pm.click_by_name(page_login.login_confirm)  # 回到我的首页








