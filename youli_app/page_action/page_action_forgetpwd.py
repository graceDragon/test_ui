# coding:utf-8
"""
忘记密码页
"""
from public import public_method
from ..page import page_forgetpwd


class ForgetPwd(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(self.driver)
        self.db = public_method.DataBase()

    def click_person(self):
        self.pm.click_by_name(page_forgetpwd.forgetpwd_person)

    def click_company(self):
        self.pm.click_by_name(page_forgetpwd.forgetpwd_company)

    def input_phone(self, phone):
        self.pm.send_keys_by_name(page_forgetpwd.forgetpwd_phone, phone)

    def click_getcode(self):
        self.pm.click_by_name(page_forgetpwd.forgetpwd_getcode)

    def input_code(self, sql):
        code = self.db.connect_database_youli(sql)
        self.pm.send_keys_by_name(page_forgetpwd.forgetpwd_inputcode, code)

    def input_pwd(self, pwd):
        self.pm.send_keys_by_id(page_forgetpwd.forgetpwd_inputpwd, pwd)

    def click_confirm(self):
        self.pm.click_by_name(page_forgetpwd.forgetpwd_confirm)

    def forgetpwd_flow(self, phone, sql, pwd):
        self.input_phone(phone)
        self.click_getcode()
        self.input_code(sql)
        self.input_pwd(pwd)
        self.click_confirm()  # 返回到登陆首页




