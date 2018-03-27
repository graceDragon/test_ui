# coding:utf-8

from zhiyu_app.page import page_home
from public import public_method
from time import sleep


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.ph = page_home
        self.pm = public_method.PublicMethod(self.driver)

    # 断言是首页
    def judge_home_page(self):
        self.pm.assert_element(self.ph.home_notice)

    # 点击我的
    def click_my_center(self):
        self.pm.click_by_name(self.ph.tab_myCenter)

    # 点击首页
    def click_tab_home(self):
        self.pm.click_element(self.ph.tab_home)

    # 点击房态
    def click_tab_house_status(self):
        self.pm.click_by_name(self.ph.tab_house_status)

    # # 点击订单
    # def click_tab_order(self):
    #     # 循环等待网页刷新
    #     for i in range(10):
    #         if self.pm.find_element_name(self.ph.tab_order):
    #             self.pm.click_by_name(self.ph.tab_order)
    #         else:
    #             sleep(2)

    # 点击客户
    def click_tab_customer(self):
        self.pm.click_element(self.ph.tab_customer)

    # 点击确认合同
    def click_confirm_hetong(self):
        self.pm.click_by_name(self.ph.home_hetong)

    # 点击订单收款
    def click_order_pay(self):
        self.pm.click_by_name(self.ph.home_shoukuan)

    # 点击收款确认-财务
    def click_confirm_pay(self):
        self.pm.screenSlide_by_zuobiao(600.0, 1500.0, 600.0, 600.0, 1080.0, 1920.0)
        self.pm.click_by_name(self.ph.home_confirm_pay)

