# coding:utf-8

"""
# 退房,费用结算页
"""

from ..page import page_checkout
from public import public_method, date
from time import sleep


class CheckOut(object):
    def __init__(self, driver):
        self.driver = driver
        self.pc = page_checkout
        self.pm = public_method.PublicMethod(self.driver)

    # 确定
    def confirm(self):
        self.pm.click_by_name(self.pc.checkout_confirm)

    # 确认
    def confirm_ren(self):
        self.pm.click_by_name(self.pc.checkout_confirm_ren)

    # 返回
    def click_back(self):
        self.pm.click_by_name(self.pc.checkout_back)

    # 断言房间检查页
    def judge_title(self):
        self.pm.assert_el_by_name(self.pc.checkout_title)

    # 点击其他维修项
    def click_fix(self):
        self.pm.click_by_name(self.pc.checkout_fix)

    # 维修项选项
    def select_fix(self, item, reason):
        if item == u'冰箱':
            if reason == u'断线了':
                pass
            elif reason == u'不制冷':
                self.pm.screenSlide_by_zuobiao(800.0, 1700.0, 800.0, 1620.0, 1080.0, 1920.0)
        elif item == u'电视':
            self.pm.screenSlide_by_zuobiao(300.0, 1700.0, 300.0, 1620.0, 1080.0, 1920.0)
        elif item == u'空调':
            for i in range(2):
                self.pm.screenSlide_by_zuobiao(300.0, 1700.0, 300.0, 1620.0, 1080.0, 1920.0)
        else:
            pass
        self.confirm()

    # 维修项选项-生产
    def select_fix_online(self, item, reason):
        if item == u'床':
            if reason == u'小床':
                pass
            elif reason == u'不制冷':
                self.pm.screenSlide_by_zuobiao(800.0, 1700.0, 800.0, 1620.0, 1080.0, 1920.0)
        elif item == u'电视':
            self.pm.screenSlide_by_zuobiao(300.0, 1700.0, 300.0, 1620.0, 1080.0, 1920.0)
        elif item == u'空调':
            for i in range(2):
                self.pm.screenSlide_by_zuobiao(300.0, 1700.0, 300.0, 1620.0, 1080.0, 1920.0)
        else:
            pass
        self.confirm()

    # 点击生成赔偿单
    def click_bill(self):
        self.pm.click_by_name(self.pc.checkout_bill)

    # 断言费用结算页
    def judge_fee_close(self):
        self.pm.assert_el_by_name(self.pc.checkout_feeclose_title)

    # 选择退房方式
    def select_checkout_way(self):
        self.pm.click_by_name(self.pc.checkout_way)
        self.confirm()

    # 选择房屋可租状态
    def checkout_rent_status(self, status):
        self.pm.click_by_name(self.pc.checkout_rent_status)
        if status == u'待租':
            pass
        elif status == u'配置中':
            self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080.0, 1920.0)
        self.confirm()

    # 添加费用
    def add_fees(self, fee):
        self.pm.click_by_name(self.pc.checkout_add_fee)
        if fee == '房屋租金':
            pass
        elif fee == '冷水费':
            self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080.0, 1920.0)
        self.confirm()

    # 添加费用金额
    def add_fee_money(self, i):
        self.pm.send_keys_by_name(self.pc.checkout_add_fee_money, i)

    # 划屏
    def swip_screen(self):
        self.pm.screenSlide_by_zuobiao(300.0, 1500.0, 300.0, 700.0, 1080.0, 1920.0)

    # 费用结算页-费用添加
    def add_fee(self):
        # 添加费用前先划屏
        print '费用结算页，输入金额。'
        tag = 0
        sleep(1)
        for i in range(3):
            self.pm.click_by_ids(self.pc.checkout_fee, 0)
            self.pm.send_keys_by_ids(self.pc.checkout_fee, 10, 0)
            text = self.pm.read_element_txt_by_ids(self.pc.checkout_fee, 0)
            print '*****'
            print 'text', text
            print '*****'
            try:
                if int(text) == 10:
                    tag = 1
                    break
            except Exception as e:
                print e
                print '费用结算页，费用输入有误或者压根没输进去！'
                # assert True is False
        if tag == 0:
            assert True is False
        # if int(text) == 10:
        #     pass
        # else:
        #     print '费用结算页，费用输入有误或者压根没输进去！'
        #     assert True is False
        self.pm.click_by_ids(self.pc.checkout_fee, 1)
        self.pm.send_keys_by_ids(self.pc.checkout_fee, -50, 1)
        self.pm.click_by_ids(self.pc.checkout_fee, 2)
        self.pm.send_keys_by_ids(self.pc.checkout_fee, -800, 2)
        self.pm.click_by_ids(self.pc.checkout_fee, 3)
        self.pm.send_keys_by_ids(self.pc.checkout_fee, -5000, 3)

    # 费用结算页-费用检查1期1付
    def check_fee(self,status_jiesuan,money_tui):
        money_tui = float(money_tui)
        ele_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 0)
        water_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 1)
        wuye_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 2)
        zujin_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 3)
        yajin_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 4)
        bingxiang_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 5)
        weixiu_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 6)
        weiyue_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 7)
        ele_fee = self.pm.regular_num_new(ele_fee)
        water_fee = self.pm.regular_num_new(water_fee)
        wuye_fee = self.pm.regular_num_new(wuye_fee)
        zujin_fee = self.pm.regular_num_new(zujin_fee)
        yajin_fee = self.pm.regular_num_new(yajin_fee)
        bingxiang_fee = self.pm.regular_num_new(bingxiang_fee)
        weixiu_fee = self.pm.regular_num_new(weixiu_fee)
        weiyue_fee = self.pm.regular_num_new(weiyue_fee)
        if status_jiesuan == '1_1':  # 1期1付
            if ele_fee == 2.45 and water_fee == 50.0 and wuye_fee == 800.0 and zujin_fee == 5000.0 and \
                            yajin_fee == 5500.0 and bingxiang_fee == 1000.0 and weixiu_fee == 0.01 and weiyue_fee == 2750.0:
                pass
            else:
                self.pm.screen_shot()
                print '费用结算页，费用详单错误！'
                assert True is False
        elif status_jiesuan == '6_3':  # 6期3付
            if ele_fee == 2.45 and water_fee == 50.0 and wuye_fee == 800.0 and zujin_fee == 5000.0 and \
                            yajin_fee == 4725.0 and bingxiang_fee == 1000.0 and weixiu_fee == 0.01 and weiyue_fee == 2362.5:
                pass
            else:
                self.pm.screen_shot()
                print '费用结算页，费用详单错误！'
                assert True is False
        elif status_jiesuan == '12_6':  # 12期6付
            if ele_fee == 2.45 and water_fee == 50.0 and wuye_fee == 800.0 and zujin_fee == 5000.0 and \
                            yajin_fee == 4000.0 and bingxiang_fee == 1000.0 and weixiu_fee == 0.01 and weiyue_fee == 2000.0:
                pass
            else:
                self.pm.screen_shot()
                print '费用结算页，费用详单错误！'
                assert True is False
        fee_total = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail_total, -1)
        fee_total = self.pm.regular_num_new(fee_total)
        # if fee_total == 9597.54: # 1期1付
        if fee_total == money_tui:
            pass
        else:
            self.pm.screen_shot()
            print '费用结算页，费用合计错误！'
            assert True is False

    # 费用结算页-费用检查1期1付
    def check_fee_jizhong(self, status_jiesuan, money_tui):
                money_tui = float(money_tui)
                ele_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 0)
                water_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 1)
                wuye_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 2)
                zujin_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 3)
                yajin_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 4)
                bingxiang_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 5)
                weixiu_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 6)
                weiyue_fee = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail, 7)
                ele_fee = self.pm.regular_num_new(ele_fee)
                water_fee = self.pm.regular_num_new(water_fee)
                wuye_fee = self.pm.regular_num_new(wuye_fee)
                zujin_fee = self.pm.regular_num_new(zujin_fee)
                yajin_fee = self.pm.regular_num_new(yajin_fee)
                bingxiang_fee = self.pm.regular_num_new(bingxiang_fee)
                weixiu_fee = self.pm.regular_num_new(weixiu_fee)
                weiyue_fee = self.pm.regular_num_new(weiyue_fee)
                if status_jiesuan == '1_1':  # 1期1付
                    if ele_fee == 2.5 and water_fee == 50.0 and wuye_fee == 800.0 and zujin_fee == 5000.0 and \
                                    yajin_fee == 9900.0 and bingxiang_fee == 1000.0 and weixiu_fee == 0.01 and \
                                    weiyue_fee == 9900.0:
                        pass
                    else:
                        self.pm.screen_shot()
                        print '费用结算页，费用详单错误！'
                        assert True is False
                elif status_jiesuan == '6_3':  # 6期3付
                    if ele_fee == 2.5 and water_fee == 50.0 and wuye_fee == 800.0 and zujin_fee == 5000.0 and \
                                    yajin_fee == 9405.0 and bingxiang_fee == 1000.0 and weixiu_fee == 0.01 and weiyue_fee == 9405.0:
                        pass
                    else:
                        self.pm.screen_shot()
                        print '费用结算页，费用详单错误！'
                        assert True is False
                elif status_jiesuan == '12_6':  # 12期6付
                    if ele_fee == 2.5 and water_fee == 50.0 and wuye_fee == 800.0 and zujin_fee == 5000.0 and \
                                    yajin_fee == 8910.0 and bingxiang_fee == 1000.0 and weixiu_fee == 0.01 and weiyue_fee == 8910.0:
                        pass
                    else:
                        self.pm.screen_shot()
                        print '费用结算页，费用详单错误！'
                        assert True is False
                fee_total = self.pm.read_element_txt_by_ids(self.pc.checkout_fee_detail_total, -1)
                fee_total = self.pm.regular_num_new(fee_total)
                # if fee_total == 9597.54: # 1期1付
                if fee_total == money_tui:
                    pass
                else:
                    self.pm.screen_shot()
                    print '费用结算页，费用合计错误！'
                    assert True is False

    # 费用结算页，检查日期
    def check_time_money(self, sign_n, rent_n):
        d2_sign = date.get_today_month(sign_n)
        d2_sign = date.get_day_of_d(d2_sign, n=-1)
        d2_sign = str(d2_sign)
        d2_rent = date.get_today_month(rent_n)
        d2_rent = date.get_day_of_d(d2_rent, n=-1)
        d2_rent = str(d2_rent)
        sign_end_time = self.pm.read_element_txt_by_ids(self.pc.checkout_sign_end_time, 0)
        rent_end_time = self.pm.read_element_txt_by_ids(self.pc.checkout_sign_end_time, 1)
        if d2_sign == sign_end_time and d2_rent == rent_end_time:
            pass
        else:
            self.pm.screen_shot()
            print '合同到期日，房租到期日错误：', sign_end_time, rent_end_time
            assert True is False

    # 退房流程-分散式
    def checkout_flow(self, item, reason, status, sign_n=1, rent_n=1,status_jiesuan='1_1', money_tui=9597.54):
        self.judge_title()
        self.click_fix()
        self.select_fix_online(item, reason)
        self.click_bill()
        self.judge_fee_close()
        self.select_checkout_way()
        self.checkout_rent_status(status)
        # self.add_fees(fee)
        # self.add_fee_money(money)
        # 检查日期金额是否正确
        self.check_time_money(sign_n, rent_n)
        self.pm.screenSlide_by_zuobiao(300.0, 1600.0, 300.0, 400.0, 1080.0, 1920.0)
        self.add_fee()
        self.pm.screenSlide_by_zuobiao(300.0, 1600.0, 300.0, 400.0, 1080.0, 1920.0)
        self.check_fee(status_jiesuan, money_tui)
        # self.swip_screen()
        self.confirm_ren()  # 确认之后回到房态首页

    # 退房流程(简单版)-分散式
    def checkout_flow_easy(self, item, reason, status):
        self.judge_title()
        self.click_fix()
        self.select_fix_online(item, reason)
        self.click_bill()
        self.judge_fee_close()
        self.select_checkout_way()
        self.checkout_rent_status(status)
        # self.confirm_ren()  # 确认之后回到房态首页
        self.click_back()
        self.click_back()  # 两次返回到房态首页

    # 退房流程(简单版)-分散式
    def checkout_flow_easy02(self, status):
        self.judge_title()
        self.click_bill()
        self.judge_fee_close()
        self.select_checkout_way()
        self.checkout_rent_status(status)
        self.confirm_ren()  # 确认之后回到房态首页

    # 退房流程-集中式
    def checkout_flow_jizhong(self, item, reason, status, sign_n=1, rent_n=1,status_jiesuan='1_1', money_tui=6847.49):
        self.judge_title()
        self.click_fix()
        self.select_fix_online(item, reason)
        self.click_bill()
        self.judge_fee_close()
        self.select_checkout_way()
        self.checkout_rent_status(status)
        # self.add_fees(fee)
        # self.add_fee_money(money)
        # 检查日期金额是否正确
        self.check_time_money(sign_n, rent_n)
        self.pm.screenSlide_by_zuobiao(300.0, 1600.0, 300.0, 400.0, 1080.0, 1920.0)
        self.add_fee()
        self.pm.screenSlide_by_zuobiao(300.0, 1600.0, 300.0, 400.0, 1080.0, 1920.0)
        self.check_fee_jizhong(status_jiesuan, money_tui)
        # self.swip_screen()
        self.confirm_ren()  # 确认之后回到房态首页

    # 退房流程-集中式
    def checkout_flow_jizhong_easy(self, status):
        self.judge_title()
        self.click_bill()
        self.judge_fee_close()
        self.select_checkout_way()
        self.checkout_rent_status(status)
        self.confirm_ren()  # 确认之后回到房态首页






























