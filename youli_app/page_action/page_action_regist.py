# coding:utf-8
"""
注册页
"""
from public import public_method
from ..page import page_regist


class Regist(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(self.driver)
        self.db = public_method.DataBase()

    def judge_regist_page(self):
        self.pm.assert_el_by_name(page_regist.re_confirm)

    def input_phone(self, phone):
        self.pm.send_keys_by_id(page_regist.re_phone, phone)

    def click_get_code(self):
        self.pm.click_by_name(page_regist.re_get_code)

    def input_code(self, sql):
        code = self.db.connect_database_youli(sql)
        self.pm.send_keys_by_name(page_regist.re_input_code, code)

    def input_pwd(self, pwd):
        self.pm.send_keys_by_id(page_regist.re_input_pwd, pwd)

    def click_pwd_see(self):
        self.pm.click_by_id(page_regist.re_pwd_see)

    def click_pact(self):
        self.pm.click_by_id(page_regist.re_pact_click)

    def click_regist(self):
        self.pm.click_by_name(page_regist.re_confirm)

    def click_login(self):
        self.pm.click_by_name(page_regist.re_back_login)

    # 查看注册协议
    def check_pact(self):
        self.pm.click_by_id(page_regist.re_pact)

    def regist_flow(self, user, pwd, sql):
        self.judge_regist_page()
        self.input_phone(user)
        self.click_get_code()
        self.input_code(sql)
        self.input_pwd(pwd)
        self.click_pwd_see()
        self.pm.read_and_judge_element_txt_by_id(page_regist.re_input_pwd, pwd)
        self.click_regist()




