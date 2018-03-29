# coding:utf-8

from public import public_method
from ..page import page_wode
from .page_action_login import LogIn
from .page_action_home import Home


class WoDe(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(driver)
        self.login = LogIn(driver)
        self.home = Home(driver)

    def judge_wode_page(self):
        self.pm.assert_el_by_name(page_wode.wode_mywallet)

    def click_setting(self):
        self.pm.click_by_id(page_wode.wode_setting)

    def click_login(self):
        self.pm.click_by_name(page_wode.wode_login)

    def check_user(self, user):
        user_phone = self.pm.read_element_txt_by_id(page_wode.wode_user)
        if user_phone == user:
            print '用户已登录！'
            return True
        elif user_phone != user:
            print '用户未登录！'
            return False

    # --------------------设置页面------------------------
    def judge_setting_page(self):
        self.pm.assert_el_by_name(page_wode.setting_title)

    def logout_judge(self):
        if self.pm.find_element_name(page_wode.wode_login):
            print '未登录'
        else:
            print '退出当前用户！'
            self.click_setting()
            self.logout()

    def logout(self):
        self.pm.click_by_name(page_wode.setting_logout)
        self.pm.click_by_name(page_wode.confirm)  # 返回到‘我的’首页

    def login_judge(self, user, pwd):
        if self.pm.find_element_name(page_wode.wode_login):
            print "去登录！"
            self.click_login()
            self.login.login(user, pwd)
        else:
            if self.check_user(user):
                pass
            else:
                print '退出当前用户！'
                self.click_setting()
                self.logout()
                self.click_login()
                self.login.login(user, pwd)
        self.home.click_tab_home()  # 回到首页

    def login_login(self, user, pwd):
        if self.pm.find_element_name(page_wode.wode_login):
            print "直接登录！"
        else:
            print '先退出当前用户！'
            self.click_setting()
            self.logout()
        self.click_login()
        self.login.login(user, pwd)










