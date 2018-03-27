# coding:utf-8

from ..page import page_orders
from public import public_method, input_method, date
from time import sleep
from . import page_action_home


class PageActionOrders(object):
    def __init__(self, driver):
        self.driver = driver
        self.po = page_orders
        self.pm = public_method.PublicMethod(self.driver)
        self.im = input_method.InputMethod()

    # 确定
    def confirm(self):
        self.pm.click_by_name(self.po.order_confirm)

    # 提交
    def submit(self):
        self.pm.click_by_name(self.po.order_submit)

    # 返回
    def back(self):
        self.pm.click_by_name(self.po.order_back)

    # 断言订单管理页
    def judge_order(self):
        self.pm.assert_el_by_name(self.po.order_title)

    # 点击搜索
    def order_search(self):
        self.pm.click_by_id(self.po.order_search)

    # 点击订单收款
    def click_wait_pay(self):
        page_action_home.HomePage(self.driver).click_order_pay()

    # 点击收款确认
    def click_home_pay_confirm(self):
        page_action_home.HomePage(self.driver).click_confirm_pay()

    # 点击待确认合同
    def click_wait_confirm_sign(self):
        self.pm.click_by_name(self.po.order_tab_wait_confirm_sign)

    # 点击历史订单
    def click_history_order(self):
        self.pm.click_by_name(self.po.order_tab_history_order)

    # 下拉屏幕刷新
    def refress_screen(self):
        self.pm.screenSlide_by_zuobiao(600.0, 700.0, 600.0, 1200.0, 1080.0, 1920.0)

    # 关闭待确认合同
    def close_wait_confirm_sign(self, communityName, houseId):
        for i in range(2):
            house_name = self.pm.read_element_txt_by_ids(self.po.order_house_name, i)
            if communityName in house_name and houseId in house_name:
                self.pm.click_by_names(self.po.order_close, i)
                break
            else:
                self.pm.screenSlide_by_zuobiao(600.0, 1560.0, 600.0, 500.0, 1080.0, 1920.0)

    # 签署待确认合同
    def sign_wait_confirm_sign(self, communityName, houseId):
        tag = 0
        # 等待生成pdf文档
        # sleep(10)
        for i in range(2):
            house_name = self.pm.read_element_txt_by_ids(self.po.order_house_name, i)
            print '房屋名称：', house_name
            if communityName in house_name and houseId in house_name:
                self.pm.click_by_names(self.po.order_sign_confirm, i)
                break
            else:
                self.pm.screenSlide_by_zuobiao(600.0, 1560.0, 600.0, 500.0, 1080.0, 1920.0)
        self.pm.click_by_name(self.po.order_confirm)
        sleep(10)
        # 再次判断签署是否成功
        house_name1 = self.pm.read_element_txt_by_id(self.po.order_house_name)
        print '房屋名称2：', house_name1
        if communityName in house_name1 and houseId in house_name1:
            # 递归执行函数，会执行返回操作，这一步执行了返回，下一步就不需要执行返回操作了
            self.sign_wait_confirm_sign(communityName, houseId)
            tag = 1
        if tag == 0:
            self.pm.click_by_name(self.po.order_back)  # 返回到首页

    # 关闭,待收款订单
    def close_order_wait_pay(self, communityName, houseId):
        for i in range(2):
            house_name = self.pm.read_element_txt_by_ids(self.po.order_house_name, i)
            if communityName in house_name and houseId in house_name:
                self.pm.click_by_names(self.po.order_close, i)
                break
            else:
                self.pm.screenSlide_by_zuobiao(600.0, 1560.0, 600.0, 500.0, 1080.0, 1920.0)

    # 收款,待收款订单
    def confirm_order_wait_pay(self, communityName, houseId):
        for i in range(2):
            house_name = self.pm.read_element_txt_by_ids(self.po.order_house_name, i)
            if communityName in house_name and houseId in house_name:
                self.pm.click_by_names(self.po.order_pay_confirm, i)
                break
            else:
                self.pm.screenSlide_by_zuobiao(600.0, 1560.0, 600.0, 500.0, 1080.0, 1920.0)

    # 财务收款确认
    def caiwu_confirm_order(self, communityName, houseId):
        for i in range(2):
            house_name = self.pm.read_element_txt_by_ids(self.po.order_house_name, i)
            if communityName in house_name and houseId in house_name:
                self.pm.click_by_names(self.po.order_confirm_01, i)
                break
            else:
                self.pm.screenSlide_by_zuobiao(600.0, 560.0, 600.0, 1500.0, 1080.0, 1920.0)

    # 财务打回
    def caiwu_dahui_order(self, communityName, houseId):
        for i in range(2):
            house_name = self.pm.read_element_txt_by_ids(self.po.order_house_name, i)
            if communityName in house_name and houseId in house_name:
                self.pm.click_by_names(self.po.order_dahui, i)
                break
            else:
                self.pm.screenSlide_by_zuobiao(600.0, 560.0, 600.0, 1500.0, 1080.0, 1920.0)

    # 财务打回页
    def caiwu_dahui_judge(self):
        self.pm.assert_el_by_name(self.po.caiwu_dahui_title)

    # 财务收费订单确认-标题
    def caiwu_page_judge(self):
        self.pm.assert_el_by_name(self.po.caiwu_order_confirm_title)

    # 财务收费订单实收确认
    def caiwu_money_total(self, money_t):
        money_total = self.pm.read_element_txt_by_id(self.po.caiwu_money_total)
        money_total = float(self.pm.regular_num(money_total)[0])
        money_order = self.pm.read_element_txt_by_id(self.po.caiwu_order_money)
        money_order = float(self.pm.regular_num(money_order)[0])
        self.pm.screenSlide_by_zuobiao(600.0, 1500.0, 600.0, 700.0, 1080.0, 1920.0)
        money_pay = self.pm.read_element_txt_by_id(self.po.caiwu_pay_money)
        money_pay = float(self.pm.regular_num(money_pay)[0])
        if money_t == money_total and money_t == money_order and money_t == money_pay:
            pass
        else:
            print '财务收费订单确认页，金额错误:', money_total, '!=', money_order, '!=', money_t, '!=', money_pay

    # 财务收费订单实收页-合同租期
    def caiwu_rent_time(self, n):
        text = self.pm.read_element_txt_by_id(self.po.caiwu_sign_time)
        text_list = text.split(u'至')
        date_start = text_list[0]
        date_end = text_list[1]
        date1 = date.today()
        date1 = str(date1)
        date2 = date.get_today_month(n)
        date2 = date.get_day_of_d(date2, n=-1)
        date2 = str(date2)
        if date1 == date_start and date2 == date_end:
            pass
        else:
            self.pm.screen_shot()
            print '财务收费确认页面，合同租期错误：', date1, date2, date_start, date_end
            assert True is False

    # 收费处理页-断言
    def judge_fee_title(self):
        self.pm.assert_el_by_name(self.po.order_fee_title)

    # 收费处理页-流程
    def fee_page_flow(self, money_1, remark):
        self.judge_fee_title()
        money = self.driver.find_element_by_id(self.po.order_pay_money).text
        print '订单金额：', money
        money = float(self.pm.regular_num(money)[0])
        print '处理后的订单金额：', money
        if money_1 == money:
            money = str(money)
            self.pm.send_keys_by_id(self.po.order_pay_input, money)
        else:
            self.pm.screen_shot()
            print '收费处理页金额错误:', money, '!=', money_1
            assert True is False
        self.pm.send_keys_by_id(self.po.order_mark, remark)
        self.submit()  # 提交完成停留在订单页
        self.back()  # 返回首页

    # 退费处理页
    def judge_refund_page(self):
        self.pm.assert_el_by_name(self.po.order_refund_title)

    # 退费处理页（财务确认页）
    def judge_refund_caiwu_page(self):
        self.pm.assert_el_by_name(self.po.order_refund_caiwu_title)

    # 订单收款-退费处理页-检查金额
    def refund_check_money(self, money_tui):
        money_tui = float(money_tui)
        refund_money = self.pm.read_element_txt_by_id(self.po.order_refund_money)
        refund_money = self.pm.regular_num_new(refund_money)
        # if refund_money == 9597.54:
        if refund_money == money_tui:
            pass
        else:
            self.pm.screen_shot()
            print '退费处理页，费用错误！'
            assert True is False

    # 退费方式
    def refund_way(self, way, mark, name, bank, count):
        self.pm.click_by_name(self.po.order_refund_way)
        if way == '转帐':
            pass
        elif way == '现金':
            self.pm.screenSlide_by_zuobiao(600.0, 1592.0, 600.0, 1510.0, 1080.0, 1920.0)
        self.confirm()
        if way == '转账':
            self.pm.send_keys_by_name(self.po.order_refund_name, name)
            self.pm.send_keys_by_name(self.po.order_refund_bank, bank)
            self.pm.send_keys_by_name(self.po.order_refund_count, count)
        self.pm.send_keys_by_id(self.po.order_mark, mark)
        self.submit()
        self.back()  # 返回到首页

    # 退费页流程
    def refund_page(self, way, mark, name, bank, count, money_tui=9597.54):
        self.judge_refund_page()
        self.refund_check_money(money_tui)
        self.refund_way(way, mark, name, bank, count)

    # 退费页流程
    def refund_page_jizhong(self, way, mark, name, bank, count, money_tui=6847.49):
        self.judge_refund_page()
        self.refund_check_money(money_tui)
        self.refund_way(way, mark, name, bank, count)

    # 订单操作流程-不提交
    def order_flow(self, communityName, houseId):
        self.judge_order()
        self.click_wait_confirm_sign()
        self.refress_screen()
        self.sign_wait_confirm_sign(communityName, houseId)
        self.confirm()
        self.click_wait_pay()
        sleep(3)
        self.refress_screen()
        self.confirm_order_wait_pay(communityName, houseId)
        self.back()
        self.close_order_wait_pay(communityName, houseId)
        self.confirm()

    # 订单操作流程-提交
    def order_confirm_flow(self, communityName, houseId, remark, money_1):
        self.judge_order()
        # self.click_wait_confirm_sign()
        self.refress_screen()
        self.sign_wait_confirm_sign(communityName, houseId)
        # self.confirm()
        self.click_wait_pay()
        sleep(3)
        self.refress_screen()
        self.confirm_order_wait_pay(communityName, houseId)
        self.fee_page_flow(money_1, remark)

    # 断言收款确认页
    def judge_shoukuan_page(self):
        self.pm.assert_el_by_name(self.po.order_shoukuan_title)

    # 财务收款确认
    def caiwu_pay_confirm(self, communityName, houseId, money_t, n=1):
        self.click_home_pay_confirm()
        self.judge_shoukuan_page()
        self.caiwu_confirm_order(communityName, houseId)
        # 添加金额时间判断
        self.caiwu_page_judge()
        self.pm.screenSlide_by_zuobiao(600.0, 500.0, 600.0, 1200.0, 1080.0, 1920.0)
        self.caiwu_money_total(money_t)
        self.pm.screenSlide_by_zuobiao(600.0, 500.0, 600.0, 1200.0, 1080.0, 1920.0)
        self.caiwu_rent_time(n)
        self.submit()
        self.back()  # 返回到首页

    # 财务打回
    def caiwu_pay_dahui(self, communityName, houseId):
        self.click_home_pay_confirm()
        self.judge_shoukuan_page()
        self.caiwu_dahui_order(communityName, houseId)
        # 添加金额时间判断
        self.caiwu_dahui_judge()
        self.submit()
        self.back()  # 返回到首页

    # 财务收款确认（退费）
    def caiwu_pay_confirm_tuifei(self, communityName, houseId, money_tui=9597.54):
        money_tui = float(money_tui)
        self.click_home_pay_confirm()
        self.judge_shoukuan_page()
        self.caiwu_confirm_order(communityName, houseId)
        self.judge_refund_caiwu_page()
        money = self.driver.find_element_by_id(self.po.order_checkout_money).text
        money = self.pm.regular_num_new(money)
        # if money == 9597.54:  # 1期1付的默认值
        if money == money_tui:
            pass
        else:
            self.pm.screen_shot()
            print '财务退费订单确认页，费用错误！'
            assert True is False
        self.pm.screenSlide_by_zuobiao(600.0, 1560.0, 600.0, 500.0, 1080.0, 1920.0)
        self.pm.send_keys_by_id(self.po.order_pay_input, str(money))
        self.submit()
        self.back()  # 返回到首页

    # 财务收款确认（退费）
    def caiwu_pay_confirm_tuifei_jizhong(self, communityName, houseId, money_tui=6847.49):
        money_tui = float(money_tui)
        self.click_home_pay_confirm()
        self.judge_shoukuan_page()
        self.caiwu_confirm_order(communityName, houseId)
        self.judge_refund_caiwu_page()
        money = self.driver.find_element_by_id(self.po.order_checkout_money).text
        money = self.pm.regular_num_new(money)
        # if money == 9597.54:  # 1期1付的默认值
        if money == money_tui:
            pass
        else:
            self.pm.screen_shot()
            print '财务退费订单确认页，费用错误！'
            assert True is False
        self.pm.screenSlide_by_zuobiao(600.0, 1560.0, 600.0, 500.0, 1080.0, 1920.0)
        self.pm.send_keys_by_id(self.po.order_pay_input, str(money))
        self.submit()
        self.back()  # 返回到首页










