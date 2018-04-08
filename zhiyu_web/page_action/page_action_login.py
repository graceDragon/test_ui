# coding:utf-8
"""
登录页-方法封装
"""
from ..page import page_login
from ..page import page_home
from public import public_method
from time import sleep
from test_data.data import *
from zhiyu_web.page_action import page_action_home
from selenium.webdriver import ActionChains


class PageActionLogin(object):

    def __init__(self, driver):
        self.m = public_method.PublicMethod(driver)
        self.l = page_login
        self.d = driver
        self.homeAc = page_action_home.Home(self.d)

    def assert_login_title(self):
        # 断言跳转到登录页
        self.m.assert_element(self.l.login_title_xpath)

    def input_user(self, i):
        # 输入用户名
        self.m.send_keys_element(self.l.user_input_name, i)

    def input_password(self, i):
        # 输入密码
        self.m.send_keys_element(self.l.pwd_input_name, i)

    # def img_yzm(self):
    #     img_yzm = self.m.image_yzm(self.l.yzm_pic_class)
    #     return img_yzm

    def input_yzm(self):
        # 输入验证码
        # img_yzm = self.m.image_yzm(self.l.yzm_pic_class)
        # 验证码临时设置成随意输入，不需要读取
        img_yzm = '1234'
        self.m.send_keys_element(self.l.yzm_input_name, img_yzm)

    def click_login(self):
        # 点击登录
        self.m.click_element(self.l.login_btn_class)

    def click_forget_pwd(self):
        # 点击忘记密码
        self.m.click_element(self.l.forget_pwd_class)

    def stay_forget_pwd_btn(self):
        # 鼠标停留在忘记密码按钮上
        ActionChains(self.d).move_to_element('forgetPass')
        sleep(10)

    def mouse_stay(self,ele):
        # 鼠标停留在某个元素上
        ActionChains(self.d).move_to_element(ele).perform()
        sleep(2)

    # 登录
    def login_page_action(self, user, pwd):
        if self.m.find_element_xpath(self.l.login_title_xpath):
            self.assert_login_title()
            self.input_user(user)
            self.input_password(pwd)
            # self.stay_forget_pwd_btn()
            self.input_yzm()
            self.click_login()
        elif self.m.find_element_xpath(page_home.home_tab_home):
            if self.homeAc.read_user(user):
                pass
            else:
                # 退出当前帐号重新登录
                self.logout()
                self.input_user(user)
                self.input_password(pwd)
                # self.stay_forget_pwd_btn()
                self.input_yzm()
                self.click_login()
        self.homeAc.judge_home_page()
        print "登录成功！"

    def login_page_action_cookies(self):
        self.d.add_cookie(cookies_dict)
        self.d.refresh()

    def logout(self):
        self.homeAc.judge_home_page()
        self.mouse_stay(page_home.home_setting)
        self.m.click_by_xpath(page_login.logout)
        self.assert_login_title()












