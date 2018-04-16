# coding:utf-8

from public import public_method
from ..page import page_login, page_wode
import page_action_qidong, page_action_home, page_action_wode


class LogIn(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(self.driver)
        self.qidong = page_action_qidong.QiDong(self.driver)
        self.home = page_action_home.Home(self.driver)
        self.wode = page_action_wode.WoDe(self.driver)

    def judge_login_page(self):
        self.pm.assert_el_by_name(page_login.login_confirm)

    def send_keys_user(self, user):
        self.pm.send_keys_by_id(page_login.login_user, user)

    def read_user(self):
        # 读取用户名
        user_read = self.pm.read_element_txt_by_id(page_login.login_user)
        return user_read

    def click_regist(self):
        self.pm.click_by_name(page_login.login_register)

    def login(self, user, pwd):
        self.pm.send_keys_by_id(page_login.login_user, user)
        self.pm.send_keys_by_id(page_login.login_pwd, pwd)
        self.pm.click_by_name(page_login.login_confirm)  # 回到我的首页

    def login_01(self, user, pwd):
        if self.pm.find_element_name(page_wode.wode_login):
            print "直接登录！"
        else:
            print '先退出当前用户！'
            self.wode.click_setting()
            self.wode.logout()
        self.wode.click_login()
        self.login(user, pwd)

    def login_judge(self, user, pwd):
        if self.pm.find_element_name(page_wode.wode_login):
            print "去登录！"
            self.wode.click_login()
            self.login(user, pwd)
        else:
            if self.wode.check_user(user):
                pass
            else:
                print '退出当前用户！'
                self.wode.click_setting()
                self.wode.logout()
                self.wode.click_login()
                self.login(user, pwd)
        self.home.click_tab_home()  # 回到首页

    # 启动app到登录的过程
    def login_login(self, user, pwd):
        self.qidong.qidong_flow()
        self.home.judge_homepage()
        self.home.click_tab_wode()
        self.login_judge(user, pwd)












