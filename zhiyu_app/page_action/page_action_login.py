# coding:utf-8

from zhiyu_app.page import page_login, page_home
from public import public_method
from zhiyu_app.page_action import page_action_home


class LogIn(object):
    def __init__(self, driver):
        self.driver = driver
        self.pl = page_login
        self.ph = page_home
        self.pah = page_action_home.HomePage(self.driver)
        self.pm = public_method.PublicMethod(self.driver)

    def judge_login(self):
        self.pm.assert_element(self.pl.login_submit)

    def read_text_user(self, user):
        self.pm.send_keys_by_id(self.pl.login_user, user)
        user_read = self.pm.read_element_txt_by_id(self.pl.login_user)
        return user_read

    def login(self, user, pwd):
        self.pm.send_keys_by_id(self.pl.login_user, user)
        self.pm.send_keys_by_id(self.pl.login_pwd, pwd)
        # 点掉虚拟键盘
        self.pm.screenSlide_by_zuobiao(300.0, 300.0, 300.0, 300.0, 1080.0, 1920.0)
        self.pm.click_by_id(self.pl.login_submit)

    def logout(self):
        self.pm.click_by_id(self.pl.my_center_logout)
        self.pm.click_by_name(self.pl.my_center_logout_confirm)

    # 判断是否是登录页面，否则退出现有登录帐号
    def logout_judge(self):
        if self.pm.find_element_id(self.pl.login_submit):
            print '是登录界面。'
            pass
        elif self.pm.find_element_name(self.ph.tab_myCenter):
            self.pah.click_my_center()
            self.logout()
            print "退出到登录页面"

    # 判断是否需要重新登录
    def login_judge(self, user, pwd):
        if self.pm.find_element_id(self.pl.login_submit):
            print '登录界面登录。'
            self.login(user, pwd)
        elif self.pm.find_element_name(self.ph.tab_myCenter):
            self.pah.click_my_center()
            text = self.pm.read_element_txt_by_id(self.pl.my_center_phone)
            if text == user:
                print '已经登录，无需重新登录。'
                self.pm.click_by_name(self.ph.tab_home)
            else:
                print '已经登录，需要重新登录。'
                self.logout()
                self.login(user, pwd)
        self.pm.assert_el_by_id(self.ph.home_notice)







