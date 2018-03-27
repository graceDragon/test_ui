# coding:utf-8

from ..page import page_finance
from public import public_method
from time import sleep


class Finance(object):

    def __init__(self, driver):
        self.driver = driver
        self.finance = page_finance
        self.pm = public_method.PublicMethod(self.driver)

    # 点击财务入口
    def click_finance_enter(self):
        self.pm.click_by_xpath(self.finance.finance_enter)

    # 点击订单管理
    def click_orders_manage(self):
        self.pm.click_by_xpath(self.finance.finance_orders_manage)

    # 点击订单管理按钮
    def click_orders_manage_btn(self):
        self.pm.click_by_xpath(self.finance.finance_orders_manage_btn)

    # 输入房间号
    def input_houseid(self, num):
        self.pm.send_keys_by_xpath(self.finance.finance_orders_manage_house_id, num)

    # 点击查询
    def click_chaxun(self):
        self.pm.click_by_xpath(self.finance.finance_orders_manage_chaxun)

    # 点击财务确认
    def click_confirm(self):
        self.pm.click_by_xpath(self.finance.finance_orders_manage_confirm)

    # 点击财务确认提交
    def click_confirm_submit(self):
        self.pm.click_by_xpath(self.finance.finance_orders_manage_confirm_1)

    # 点击财务确认提交2
    def click_confirm_submit2(self):
        self.pm.click_by_xpath(self.finance.finance_orders_manage_confirm_2)

    # 点击开票
    def click_kaipiao(self):
        self.pm.click_by_xpath(self.finance.finance_orders_manage_kaipiao)

    # 财务订单管理流程
    def order_manage_flow(self, num):
        self.click_finance_enter()
        self.click_orders_manage()
        self.click_orders_manage_btn()
        # self.pm.move_mouse_click(100, 100)
        # 移除订单管理的鼠标焦点
        self.pm.move_mouse(100, 100)
        self.pm.change_iframe(self.finance.finance_orders_manage_iframe_id)
        self.input_houseid(num)
        self.click_chaxun()
        self.click_confirm()
        self.click_confirm_submit()
        self.click_confirm_submit2()


