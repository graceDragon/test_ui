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

    def click_confirm(self):
        self.pm.click_by_name(page_wode.confirm)

    def judge_wode_page(self):
        self.pm.assert_el_by_name(page_wode.wode_mywallet)

    def click_message(self):
        self.pm.click_by_id(page_wode.wode_message)

    def click_setting(self):
        self.pm.click_by_id(page_wode.wode_setting)

    # 待办
    def click_waitdo(self):
        self.pm.click_by_id(page_wode.wode_waitdo)

    def click_yuyue(self):
        self.pm.click_by_name(page_wode.wode_yuyue)

    def click_login(self):
        self.pm.click_by_name(page_wode.wode_login)

    def check_user(self, user):
        user_phone = self.pm.read_element_txt_by_id(page_wode.wode_phone)
        print user, user_phone, type(user), type(user_phone)
        if user_phone == user:
            print '用户已登录！'
            return True
        elif user_phone != user:
            print '用户未登录！'
            return False

    # --------------------消息中心------------------------
    def judge_message_page(self):
        self.pm.assert_el_by_name(page_wode.message_title)

    def click_back(self):
        self.pm.click_by_id(page_wode.back_id)

    def click_mes_all(self):
        self.pm.click_by_name(page_wode.message_tab_all)

    def click_mes_sign(self):
        self.pm.click_by_name(page_wode.message_tab_sign)

    def click_mes_tui(self):
        self.pm.click_by_name(page_wode.message_tab_tui)

    def click_mes_repair(self):
        self.pm.click_by_name(page_wode.message_tab_repair)

    def click_mes_zhuangxiu(self):
        self.pm.click_by_name(page_wode.message_tab_zhuangxiu)

    def click_mes_ai(self):
        self.pm.click_by_name(page_wode.message_tab_ai)

    def click_mes_fee(self):
        self.pm.click_by_name(page_wode.message_tab_fee)

    def click_mes_other(self):
        self.pm.click_by_name(page_wode.message_tab_other)

    def wode_message_flow(self):
        self.judge_wode_page()
        self.click_message()
        self.judge_message_page()
        self.click_mes_ai()
        self.click_mes_all()
        self.click_back()
        self.judge_wode_page()

    # --------------------设置页面------------------------
    def judge_setting_page(self):
        self.pm.assert_el_by_name(page_wode.setting_title)

    def setting_back(self):
        self.pm.click_by_id(page_wode.setting_back)

    def setting_click_zhengjian(self):
        self.pm.click_by_name(page_wode.setting_zhengjian)

    def setting_click_modifypwd(self):
        self.pm.click_by_name(page_wode.setting_modifypwd)

    def setting_click_idea(self):
        self.pm.click_by_name(page_wode.setting_idea)

    def setting_click_aboutme(self):
        self.pm.click_by_name(page_wode.setting_aboutme)

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

    # --------------------待办事项------------------------
    def judge_waitdo_title(self):
        self.pm.assert_el_by_name(page_wode.waitdo_title)

    def wode_waitdo_flow(self):
        self.judge_wode_page()
        self.click_waitdo()
        self.judge_waitdo_title()
        self.click_back()
        self.judge_wode_page()

    # --------------------预约看房------------------------
    def judge_yuyue_page(self):
        self.pm.assert_el_by_name(page_wode.yuyue_title)

    def click_yuyue_all(self):
        self.pm.click_by_name(page_wode.yuyue_all)

    def click_yuyue_nosee(self):
        self.pm.click_by_name(page_wode.yuyue_seehouse_no)

    def click_yuyue_yetsee(self):
        self.pm.click_by_name(page_wode.yuyue_seehouse_yet)

    def click_yuyue_cancelsee(self):
        self.pm.click_by_name(page_wode.yuyue_seehouse_cancel)

    def click_yuyue_delete(self):
        self.pm.click_by_name(page_wode.yuyue_delete)
        self.pm.click_by_name(page_wode.confirm_ren)

    def delete_all_orders(self):
        while self.pm.find_element_name(page_wode.yuyue_delete):
            self.click_yuyue_delete()










