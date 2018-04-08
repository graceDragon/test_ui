# coding:utf-8
from ..page import page_house_yuan
from public import public_method
from . import page_action_login
from time import sleep


class FangYuan(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(self.driver)
        self.fangyuan = page_house_yuan
        self.login = page_action_login.PageActionLogin(self.driver)

    def click_jizhong_community(self):
        self.pm.stay_mouse_xpath(self.fangyuan.house_tab_fangyuan)
        self.pm.stay_mouse_xpath(self.fangyuan.house_tab_shequchanpin)
        self.pm.stay_mouse_xpath(self.fangyuan.house_tab_jizhongshequ)
        self.pm.click_by_xpath(self.fangyuan.house_tab_jizhongshequ)
        self.pm.move_mouse(100, 100)

    def click_edit_ui(self):
        self.pm.click_by_xpath(self.fangyuan.house_jizhongshequ_ui_edit)

    def click_ui_test(self):
        self.pm.change_iframe('fRight')
        self.pm.click_by_xpath(self.fangyuan.house_community_edit_ui)
        sleep(5)

    def read_test(self):
        text = self.pm.read_element_txt_by_xpath(self.fangyuan.house_community_edit_ui2)
        print text, 'UI'
        return text

    def community_open(self):
        self.pm.click_by_xpath(self.fangyuan.house_community_open)

    def community_close(self):
        self.pm.click_by_xpath(self.fangyuan.house_community_close)

    def community_edit_save(self):
        self.pm.click_by_xpath(self.fangyuan.house_community_edit_save)

    def open_community(self, user, pwd):
        self.login.login_page_action(user, pwd)
        self.click_jizhong_community()
        # 切换iframe
        self.pm.change_iframe('fRight')
        self.click_edit_ui()
        sleep(3)
        # self.pm.back_iframe()
        self.pm.scrollbar_web(10000)
        # self.pm.scrollbar_web_02(self.fangyuan.house_community_edit_save)
        # sleep(5)
        # self.pm.scrollbar_web(200)
        # self.pm.scrollbar_web_02()
        sleep(3)
        self.community_open()
        # sleep(5)
        # self.community_close()
        sleep(2)
        self.community_edit_save()

    def close_community(self, user, pwd):
        self.login.login_page_action(user, pwd)
        self.click_jizhong_community()
        # 切换iframe
        self.pm.change_iframe('fRight')
        self.click_edit_ui()
        self.pm.scrollbar_web(10000)
        sleep(3)
        self.community_close()
        sleep(2)
        self.community_edit_save()






