# coding:utf-8

"""
签约到退房整体流程--分散式(6期-季付)
"""

import unittest
from public import driver, date
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
        # self.driver_web = driver.Driver().driver_web_session(url_zhiyu_test)
        # self.login_web = login_w.PageActionLogin(self.driver_web)
        # self.finance = page_action_finance.Finance(self.driver_web)

    def tearDown(self):
        self.driver.quit()
        # self.driver_web.quit()

    def test_sign_checkout(self):
        # app端签约
        self.login.login_judge(data.user_01, data.pwd_01)
        self.home.click_tab_house_status()
        # 测试环境
        # self.houseStatus.house_status_flow_fensan(data.district_dongcheng, data.street_longtan, data.community_fensan_01,
        #                                           data.room_no_07, data.user, data.rent_time_3, method='季付', fee1='房屋租金',
        #                                           zhouqi1='周期费用', day=1, addmoney='1000', furniture1='床', model1='1.2米床',
        #                                           num1=3, mendian='江大门店', saleman='张爱东', fapiao='No'
        #                                           )
        # 生产环境-丰台-丽新怡园-5
        self.houseStatus.house_status_flow_fensan(data.district_fengtai, data.street_liuliqiao,
                                                  data.community_fensan_02,
                                                  data.room_no_402, data.user_01, data.rent_time_6, method='季付',
                                                  fee1='物业费',
                                                  zhouqi1='一次性', day=1, addmoney='1000', furniture1='家电',
                                                  model1='电冰箱',
                                                  num1=1, mendian='测试门店1', saleman='用户四', fapiao='No'
                                                  )
        date_now = str(date.today())
        self.houseStatus.bill_plan_page_check(total_money=35435.0,d1=date_now,money1=21080.00,date1=date_now,
                                              fe1=180.00,fe2=1000.00,fe3=4725.00,fe4=14175.00,fe5=1000.00,
                                              money2=14355.00,tag=2,status_fenqi='6_3'
                                              )
        # self.houseStatus.confirm_ren()
        # self.houseStatus.bill_plan_flow()
        # self.home.click_tab_order()
        self.home.click_tab_home()
        self.home.click_confirm_hetong()
        self.orders.order_confirm_flow(data.community_fensan_02, data.room_no_402, data.remark, money_1=21080.00)
        """
        # 转到web端财务确认
        # self.driver_web = driver.Driver().driver_web_session(url_zhiyu_test)
        # self.login_web = login_w.PageActionLogin(self.driver_web)
        # self.finance = page_action_finance.Finance(self.driver_web)
        self.login_web.login_page_action(data.user, data.pwd)
        self.finance.order_manage_flow(data.room_no_07)
        """
        # app端财务确认
        self.orders.caiwu_pay_confirm(data.community_fensan_02, data.room_no_402, money_t=21080.00, n=6)
        # 转到app执行退房
        self.home.click_tab_house_status()
        self.houseStatus.select_community_room_fensan01(data.district_fengtai, data.street_liuliqiao,
                                                        data.community_fensan_02, data.room_no_402)
        self.houseStatus.room_checkout()
        self.checkout.checkout_flow(data.item_bed, data.reason_bed, data.room_status,sign_n=6,rent_n=3,
                                    status_jiesuan='6_3', money_tui=9210.04)
        # self.houseStatus.judege_house_status()
        self.home.click_tab_home()
        # self.home.click_tab_order()

        self.orders.click_wait_pay()
        self.orders.refress_screen()
        self.orders.confirm_order_wait_pay(data.community_fensan_02, data.room_no_402)
        # self.orders.judge_fee_title()
        # self.orders.fee_page_flow(data.remark)
        self.orders.refund_page(data.tuikuan_way_01, data.remark, data.bank_owner_name, data.bank_name, data.bank_count,money_tui=9210.04)
        """
        # 转到web端财务确认
        self.driver_web = driver.Driver().driver_web_session(url_zhiyu_test)
        self.login_web = login_w.PageActionLogin(self.driver_web)
        self.finance = page_action_finance.Finance(self.driver_web)
        self.login_web.login_page_action(data.user, data.pwd)
        self.finance.order_manage_flow(data.room_no_07)
        """
        # app财务退款确认
        self.orders.caiwu_pay_confirm_tuifei(data.community_fensan_02, data.room_no_402, money_tui=9210.04)
        # 退房完成

if __name__ == "__main__":
    SignToCheckout().test_sign_checkout()













