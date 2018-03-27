# coding:utf-8

"""
签约到退房整体流程--集中式
"""

import unittest
from public import driver
from test_data import data
from config.settings import *
from zhiyu_app.page_action import page_action_login as login_a
from zhiyu_app.page_action import page_action_home
from zhiyu_app.page_action import page_action_house_status
from zhiyu_app.page_action import page_action_checkout
from zhiyu_app.page_action import page_action_orders
from zhiyu_web.page_action import page_action_login as login_w
from zhiyu_web.page_action import page_action_finance


class SignToCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = driver.Driver().driver_app()
        self.login = login_a.LogIn(self.driver)
        self.home = page_action_home.HomePage(self.driver)
        self.houseStatus = page_action_house_status.HouseStatus(self.driver)
        self.checkout = page_action_checkout.CheckOut(self.driver)
        self.orders = page_action_orders.PageActionOrders(self.driver)
        self.driver_web = driver.Driver().driver_web_session(url_zhiyu_test)
        self.login_web = login_w.PageActionLogin(self.driver_web)
        self.finance = page_action_finance.Finance(self.driver_web)

    def tearDown(self):
        self.driver.quit()
        self.driver_web.quit()

    def test_sign_checkout(self):
        # app端签约
        self.login.login_judge(data.user, data.pwd)
        self.home.click_tab_house_status()
        self.houseStatus.house_status_flow(data.community_name, data.loudong_name, data.user, rent_time=6, method='季付',
                                           day=1, fee1='房屋租金', zhouqi1='周期费用', fee2='物业费', zhouqi2='一次性',
                                           fee3='燃气费', zhouqi3='抄表', addmoney1='1000', addmoney2='100', addmoney3='10',
                                           biaodi='22', furniture1='床', model1='1.2米床', num1=3, furniture2='空调',
                                           model2='奥克斯空调', num2=2, mendian='江大门店', saleman='张爱东',
                                           no=data.house_id, fapiao='No')
        self.houseStatus.bill_plan_flow()
        self.home.click_tab_order()
        self.orders.order_confirm_flow(data.community_name, data.house_id, data.remark)
        # 转到web端财务确认
        # self.driver_web = driver.Driver().driver_web_session(url_zhiyu_test)
        # self.login_web = login_w.PageActionLogin(self.driver_web)
        # self.finance = page_action_finance.Finance(self.driver_web)
        self.login_web.login_page_action(data.user, data.pwd)
        self.finance.order_manage_flow(data.house_id)
        # 转到app执行退房
        self.home.click_tab_house_status()
        self.houseStatus.select_community_room_jizhong(data.community_name, data.loudong_name, data.house_id)
        self.houseStatus.room_checkout()
        self.checkout.checkout_flow(data.item, data.reason, data.room_status, data.fee_type_water, data.money_water)
        self.houseStatus.judege_house_status()
        self.home.click_tab_order()
        self.orders.click_wait_pay()
        self.orders.refress_screen()
        self.orders.confirm_order_wait_pay(data.community_name, data.house_id)
        self.orders.judge_fee_title()
        self.orders.fee_page_flow(data.remark)
        # 转到web端财务确认
        self.driver_web = driver.Driver().driver_web_session(url_zhiyu_test)
        self.login_web = login_w.PageActionLogin(self.driver_web)
        self.finance = page_action_finance.Finance(self.driver_web)
        self.login_web.login_page_action(data.user, data.pwd)
        self.finance.order_manage_flow(data.house_id)
        # 退房完成

if __name__ == "__main__":
    SignToCheckout().test_sign_checkout()













