# coding:utf-8

from zhiyu_app.page import page_house_status
from public import public_method, input_method, date
from time import sleep


class HouseStatus(object):
    def __init__(self, driver):
        self.driver = driver
        self.phs = page_house_status
        self.pm = public_method.PublicMethod(self.driver)
        self.im = input_method.InputMethod()

    def judege_house_status(self):
        self.pm.assert_el_by_name(self.phs.tab_all)

    def change_house_staue_type(self):
        # 切换集中、分散(默认集中，点击切换到分散)
        self.pm.click_by_id(self.phs.room_status)

    def click_title_jizhong(self):
        # 集中式和分散式都是这个标题
        self.pm.click_by_id(self.phs.house_status_title)

    def select_community(self, community, loudong):
        # 选择社区、楼栋  集中式
        for i in range(10):
            if self.pm.find_element_name(community):
                self.pm.click_by_name(community)
                self.pm.click_by_name(loudong)
                break
            else:
                self.pm.screenSlide_by_zuobiao(300.0, 1580.0, 300.0, 500.0, 1080, 1920)

    # 分散式社区选择区域、街道
    def select_district_street_fensan(self, district, street):
        for i in range(10):
            if self.pm.find_element_name(district):
                self.pm.click_by_name(district)
                for j in range(10):
                    if self.pm.find_element_name(street):
                        self.pm.click_by_name(street)
                        break
                    else:
                        self.pm.screenSlide_by_zuobiao(900.0, 1580.0, 900.0, 700.0, 1080, 1920)
                break
            else:
                self.pm.screenSlide_by_zuobiao(300.0, 1580.0, 300.0, 700.0, 1080, 1920)

    def select_house(self, no=None):
        # 选择房间，如果给定房间号则直接选择该房间。如果没有给定房间号，则判断房间是否为空置，选择空置房间
        if no is None:
            pass
        elif no is not None:
            for i in range(10):
                if self.pm.find_element_name(no):
                    self.pm.click_by_name(no)
                    break
                else:
                    self.pm.screenSlide_by_zuobiao(300.0, 1300.0, 300.0, 700.0, 1080, 1920)

    def room_detail(self):
        # 点击详情
        self.pm.click_by_name(self.phs.room_tab_detail)

    def room_order(self):
        # 点击预订
        self.pm.click_by_name(self.phs.room_tab_order)

    def room_sign(self):
        # 点击签约
        self.pm.assert_el_by_name(self.phs.room_tab_sign)
        self.pm.click_by_name(self.phs.room_tab_sign)

    def room_checkout(self):
        # 点击退房
        self.pm.assert_el_by_name(self.phs.room_tab_checkout)
        self.pm.click_by_name(self.phs.room_tab_checkout)

    def room_relet(self):
        # 点击续租
        self.pm.assert_el_by_name(self.phs.room_tab_relet)
        self.pm.click_by_name(self.phs.room_tab_relet)

    # 签约页面
    def sign_judge(self):
        self.pm.assert_el_by_name(self.phs.sign_title)

    # 选择客户
    def sign_select_customer(self, customer):
        self.pm.click_by_name(self.phs.select_customer)
        self.im.input_method_baidu()
        sleep(3)
        self.pm.send_keys_by_name(self.phs.select_customer_input_text, customer)
        sleep(3)
        # 模拟键盘点击搜索/回车
        # self.pm.presscode(84)
        self.pm.presscode(66)
        sleep(1)
        self.im.input_method_appium()
        self.pm.click_by_name(self.phs.select_customer_submit)

    def rent_time(self, rent_time):
        # 租约起始截止日期
        if rent_time == 1:
            self.pm.click_by_id(self.phs.tv_time_1)
        elif rent_time == 3:
            self.pm.click_by_id(self.phs.tv_time_3)
        elif rent_time == 6:
            self.pm.click_by_id(self.phs.tv_time_6)
        elif rent_time == 12:
            self.pm.click_by_id(self.phs.tv_time_12)
        elif rent_time == 24:
            self.pm.click_by_id(self.phs.tv_time_24)
        else:
            print '租约起止日期输入错误！'

    def sign_time(self):
        # 选择签约日期
        self.pm.click_by_name(self.phs.sign_day)
        self.pm.click_by_name(self.phs.confirm)

    # 付款方式
    def pay_method(self, method):
        self.pm.click_by_name(self.phs.pay_method)
        if method == '月付':
            pass
        elif method == '季付':
            self.pm.screenSlide_by_zuobiao(600.0, 1592.0, 600.0, 1510.0, 1080, 1920)
        elif method == '半年付':
            for i in range(2):
                self.pm.screenSlide_by_zuobiao(600.0, 1592.0, 600.0, 1510.0, 1080, 1920)
        elif method == '年付':
            for i in range(3):
                self.pm.screenSlide_by_zuobiao(600.0, 1592.0, 600.0, 1510.0, 1080, 1920)
        elif method == '分期付':
            for i in range(4):
                self.pm.screenSlide_by_zuobiao(600.0, 1592.0, 600.0, 1510.0, 1080, 1920)
        self.pm.click_by_name(self.phs.confirm)

    # 付款日-提前、延后
    def pay_advance(self, day):
        self.pm.click_by_name(self.phs.pay_advance)
        self.pm.send_keys_by_id(self.phs.pay_advance_day, day)

    # 固定付款日-提前、延后
    def pay_fix_advance(self, month, day):
        self.pm.click_by_name(self.phs.pay_fix_advance)
        self.pm.send_keys_by_id(self.phs.pay_fix_advance_month, month)
        self.pm.send_keys_by_id(self.phs.pay_fix_advance_day, day)

    # 添加费用
    def add_fee(self, fee, zhouqi):
        self.pm.click_by_name(self.phs.add_fee)
        if fee == '房屋租金':
            pass
        elif fee == '冷水费':
            self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '电费':
            for i in range(2):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '物业费':
            for i in range(3):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '超期房租':
            for i in range(4):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '房租补差':
            for i in range(5):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '燃气费':
            for i in range(6):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '暖气费':
            for i in range(7):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '热水费':
            for i in range(8):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '车位费':
            for i in range(9):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '服务费':
            for i in range(10):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '美的空调使用费':
            for i in range(11):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '车位占用费':
            for i in range(12):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        if zhouqi == '一次性':
            pass
        elif zhouqi == '周期费用':
            self.pm.screenSlide_by_zuobiao(800.0, 1592.0, 800.0, 1510.0, 1080, 1920)
        elif zhouqi == '抄表':
            # 燃气费的抄表滑动一次，滑动两次也没关系
            for i in range(2):
                self.pm.screenSlide_by_zuobiao(800.0, 1592.0, 800.0, 1510.0, 1080, 1920)
        self.pm.click_by_name(self.phs.confirm)

    # 添加费用-生产
    def add_fee_online(self, fee, zhouqi):
        self.pm.click_by_name(self.phs.add_fee)
        if fee == '水费':
            pass
        elif fee == '电费':
            self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '物业费':
            for i in range(2):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        elif fee == '燃气费':
            for i in range(3):
                self.pm.screenSlide_by_zuobiao(300.0, 1592.0, 300.0, 1510.0, 1080, 1920)
        if zhouqi == '一次性':
            pass
        elif zhouqi == '周期费用':
            self.pm.screenSlide_by_zuobiao(800.0, 1592.0, 800.0, 1510.0, 1080, 1920)
        elif zhouqi == '抄表':
            # 燃气费的抄表滑动一次，滑动两次也没关系
            for i in range(2):
                self.pm.screenSlide_by_zuobiao(800.0, 1592.0, 800.0, 1510.0, 1080, 1920)
        self.pm.click_by_name(self.phs.confirm)

    # 租金，一次性或者周期
    def rent_money(self, money, j):
        self.pm.send_keys_by_names(self.phs.rent_money, money, j)

    # 租金，抄表
    def rent_money_caobiao(self, money, biaodi):
        self.pm.send_keys_by_id(self.phs.rent_money_caobiao, money)
        self.pm.send_keys_by_name(self.phs.rent_money_caobiao_biaodi, biaodi)

    # 添加配置
    def add_settings(self, furniture, model, j):
        self.pm.click_by_name(self.phs.add_setting)
        if furniture == '床':
            if model == '1.5米铁床':
                pass
            elif model == '1.2米床':
                for i in range(2):
                    self.pm.screenSlide_by_zuobiao(500.0, 1592.0, 500.0, 1510.0, 1080, 1920)
        elif furniture == '空调':
            for i in range(4):
                self.pm.screenSlide_by_zuobiao(150.0, 1592.0, 150.0, 1510.0, 1080, 1920)
            if model == '格力空调1.25匹':
                pass
            elif model == '奥克斯空调':
                for i in range(2):
                    self.pm.screenSlide_by_zuobiao(500.0, 1592.0, 500.0, 1510.0, 1080, 1920)
        for i in range(j - 1):
            # 滑动第三栏几个
            self.pm.screenSlide_by_zuobiao(900.0, 1592.0, 900.0, 1510.0, 1080, 1920)
        self.pm.click_by_name(self.phs.confirm)

    # 添加配置-生产
    def add_settings_online(self, furniture, model, j):
        self.pm.click_by_name(self.phs.add_setting)
        if furniture == '家电':
            if model == '电冰箱':
                pass
            elif model == '洗衣机':
                for i in range(1):
                    self.pm.screenSlide_by_zuobiao(500.0, 1592.0, 500.0, 1510.0, 1080, 1920)
        elif furniture == '家具':
            for i in range(1):
                self.pm.screenSlide_by_zuobiao(150.0, 1592.0, 150.0, 1510.0, 1080, 1920)
            if model == '三门衣柜':
                pass
            elif model == '二门衣柜':
                for i in range(1):
                    self.pm.screenSlide_by_zuobiao(500.0, 1592.0, 500.0, 1510.0, 1080, 1920)
        for i in range(j - 1):
            # 滑动第三栏几个
            self.pm.screenSlide_by_zuobiao(900.0, 1592.0, 900.0, 1510.0, 1080, 1920)
        self.pm.click_by_name(self.phs.confirm)

    def swip_screen(self):
        self.pm.screenSlide_by_zuobiao(600.0, 1580.0, 600.0, 700.0, 1080, 1920)

    # 出租门店
    def rent_shop(self, mendian):
        self.pm.click_by_name(self.phs.rent_shop)
        if mendian == '江大门店':
            pass
        elif mendian == '洪山家园门店':
            self.pm.screenSlide_by_zuobiao(600.0, 1592.0, 600.0, 1510.0, 1080, 1920)
        elif mendian == '分散式':
            for i in range(7):
                self.pm.screenSlide_by_zuobiao(600.0, 1592.0, 600.0, 1510.0, 1080, 1920)
        self.pm.click_by_name(self.phs.confirm)

    # 业务人员
    def saleman(self, saleman):
        self.pm.click_by_name(self.phs.saleman)
        if saleman == '张爱东':
            pass
        elif saleman == '刘美女管家-勿动':
            self.pm.screenSlide_by_zuobiao(600.0, 1592.0, 600.0, 1510.0, 1080, 1920)
        elif saleman == '18518757536':
            for i in range(2):
                self.pm.screenSlide_by_zuobiao(600.0, 1592.0, 600.0, 1510.0, 1080, 1920)
        self.pm.click_by_name(self.phs.confirm)

    def invoice(self, fapiao='No'):
        # 开具发票
        self.pm.click_by_name(self.phs.invoice)
        if fapiao == 'No':
            pass
        elif fapiao == 'Yes':
            self.pm.screenSlide_by_zuobiao(600.0, 1510.0, 600.0, 1592.0, 1080, 1920)
        self.pm.click_by_name(self.phs.confirm)

    def next_step(self):
        # 下一步
        self.pm.click_by_name(self.phs.next_step)

    # 确定不是确认
    def confirm(self):
        self.pm.click_by_name(self.phs.confirm)

    # 确认不是确定
    def confirm_ren(self):
        self.pm.click_by_name(self.phs.confirm_01)

    # 续租页面
    def judge_relet(self):
        self.pm.assert_el_by_name(self.phs.room_tab_relet)

    # 燃气费
    def gas_fee(self, biaodi):
        self.pm.send_keys_by_name(self.phs.gas_fee, biaodi)

    # 电费
    def electricity_fee(self, biaodi):
        self.pm.send_keys_by_name(self.phs.rent_money_caobiao_biaodi_2, biaodi)

    # 账单计划-续租页面之后
    def judge_bill_plan(self):
        self.pm.assert_el_by_name(self.phs.bill_plan)

    # 账单计划-判断账单总额
    def judge_bill_total_money(self, total_money):
        bill_total_money = self.pm.read_element_txt_by_id(self.phs.bill_total_money)
        print '读取出来的总额：', bill_total_money
        bill_total_money = self.pm.regular_num(bill_total_money)
        bill_total_money = float(bill_total_money[0])
        if bill_total_money == total_money:
            pass
        else:
            self.pm.screen_shot()
            print '账单总额错误：', bill_total_money, '!=', total_money
            assert True is False

    # 账单计划-判断首期收租日(等于第一期首款日)
    def judge_bill_payment_date(self, d1, status_fenqi):
        # 首期
        date_first = self.pm.read_element_txt_by_ids(self.phs.bill_payment_date, 0)
        # 第一期应收款日
        date_1 = self.pm.read_element_txt_by_ids(self.phs.bill_payment_date, 1)
        print 'd1的类型：', d1, type(d1)
        print 'date_first的类型：', date_first, type(date_first)
        print 'date_1的类型：', date_1, type(date_1)
        if date_first == d1 and date_1 == d1:
            pass
        else:
            self.pm.screen_shot()
            print '首期收款日期错误：', date_first, '!=', date_1, '!=', d1
            assert True is False
        if status_fenqi == '6_3':  # 如果有第2期（6期3月付）
            self.pm.screenSlide_by_zuobiao(700.0, 1600.0, 700.0, 600.0, 1080, 1920)
            date_2 = self.pm.read_element_txt_by_ids(self.phs.bill_payment_date, 2)
            d2 = date.get_today_month(3)
            d2 = date.get_day_of_d(d2, n=-1)
            d2 = str(d2)
            if date_2 == d2:
                pass
            else:
                self.pm.screen_shot()
                print '第二期日期错误：', date_2, '!=', d2
                assert True is False
        if status_fenqi == '12_6':  # 如果有第2期（12期6月付）
            self.pm.screenSlide_by_zuobiao(700.0, 1600.0, 700.0, 600.0, 1080, 1920)
            date_2 = self.pm.read_element_txt_by_ids(self.phs.bill_payment_date, 2)
            d2 = date.get_today_month(6)
            d2 = date.get_day_of_d(d2, n=-1)
            d2 = str(d2)
            if date_2 == d2:
                pass
            else:
                self.pm.screen_shot()
                print '第二期日期错误：', date_2, '!=', d2
                assert True is False

    # 账单计划-判断1期应收金额
    def judge_money_1(self, money, money2, tag):
        money_1 = self.pm.read_element_txt_by_ids(self.phs.bill_total_amount, 0)
        money_1 = self.pm.regular_num(money_1)
        money_1 = float(money_1[0])
        if money_1 == money:
            pass
        else:
            self.pm.screen_shot()
            print '收款金额错误：', money_1, '!=', money
            assert True is False
        if tag == 2:  # 如果有第2期
            money_2 = self.pm.read_element_txt_by_ids(self.phs.bill_total_amount, 1)
            money_2 = self.pm.regular_num_new(money_2)
            if money_2 == money2:
                pass
            else:
                self.pm.screen_shot()
                print '收款金额错误：', money_2, '!=', money2
                assert True is False

    # 账单计划-判断1期开始/截止日期
    def judge_start_end_date(self, date1, status_fenqi):
        if status_fenqi == '1_1':
            date2 = date.get_today_month(1)
            date2 = date.get_day_of_d(date2, n=-1)
            date2 = str(date2)
            start_date = self.pm.read_element_txt_by_id(self.phs.bill_start_date)
            end_date = self.pm.read_element_txt_by_id(self.phs.bill_end_date)
            if start_date == date1 and end_date == date2:
                pass
            else:
                self.pm.screen_shot()
                print '账期日期错误', date1, date2, start_date, end_date
                assert True is False
        if status_fenqi == '6_3':
            date2 = date.get_today_month(3)  # 第二期开始时间
            date3 = date.get_today_month(6)  # 第三期开始时间
            d1_end = date.get_day_of_d(date2, n=-1)
            d1_end = str(d1_end)
            d2_end = date.get_day_of_d(date3, n=-1)
            d2_end = str(d2_end)
            start_date_1 = self.pm.read_element_txt_by_ids(self.phs.bill_start_date, 0)
            start_date_2 = self.pm.read_element_txt_by_ids(self.phs.bill_start_date, 1)
            end_date_1 = self.pm.read_element_txt_by_ids(self.phs.bill_end_date, 0)
            end_date_2 = self.pm.read_element_txt_by_ids(self.phs.bill_end_date, 1)
            # 修改日期2018-8-01改成2018-08-01
            # end_date_2_list = end_date_2.split('-')
            # end_date_2_list[1] = '0' + end_date_2_list[1]
            # end_date_2 = '-'.join(end_date_2_list)
            # end_date_2 = date.modify_date(end_date_2)
            if start_date_1 == date1 and end_date_1 == d1_end and start_date_2 == date2 and end_date_2 == d2_end:
                pass
            else:
                self.pm.screen_shot()
                print '账期日期错误', date1, date2, d1_end, d2_end, start_date_1, start_date_2, end_date_1, end_date_2
                assert True is False
        if status_fenqi == '12_6':
            date2 = date.get_today_month(6)  # 第二期开始时间
            date3 = date.get_today_month(12)  # 第三期开始时间
            d1_end = date.get_day_of_d(date2, n=-1)
            d1_end = str(d1_end)
            d2_end = date.get_day_of_d(date3, n=-1)
            d2_end = str(d2_end)
            start_date_1 = self.pm.read_element_txt_by_ids(self.phs.bill_start_date, 0)
            start_date_2 = self.pm.read_element_txt_by_ids(self.phs.bill_start_date, 1)
            end_date_1 = self.pm.read_element_txt_by_ids(self.phs.bill_end_date, 0)
            end_date_2 = self.pm.read_element_txt_by_ids(self.phs.bill_end_date, 1)
            # 修改日期2018-8-01改成2018-08-01
            # end_date_2_list = end_date_2.split('-')
            # end_date_2_list[1] = '0' + end_date_2_list[1]
            # end_date_2 = '-'.join(end_date_2_list)
            # end_date_2 = date.modify_date(end_date_2)
            if start_date_1 == date1 and end_date_1 == d1_end and start_date_2 == date2 and end_date_2 == d2_end:
                pass
            else:
                self.pm.screen_shot()
                print '账期日期错误', date1, date2, d1_end, d2_end, start_date_1, start_date_2, end_date_1, end_date_2
                assert True is False

    # 账单计划-判断开始/截止日期(6期季付)
    def judge_start_end_date_6_1(self, date1):
        date2 = date.get_today_month(3)  # 第二期开始时间
        date3 = date.get_today_month(3)  # 第三期开始时间
        d1_end = date.get_day_of_d(date2, n=-1)
        d1_end = str(d1_end)
        d2_end = date.get_day_of_d(date3, n=-1)
        d2_end = str(d2_end)
        start_date_1 = self.pm.read_element_txt_by_ids(self.phs.bill_start_date,0)
        start_date_2 = self.pm.read_element_txt_by_ids(self.phs.bill_start_date,1)
        end_date_1 = self.pm.read_element_txt_by_ids(self.phs.bill_end_date,0)
        end_date_2 = self.pm.read_element_txt_by_ids(self.phs.bill_end_date,1)
        if start_date_1 == date1 and end_date_1 == d1_end and start_date_2 == date2 and end_date_2 == d2_end:
            pass
        else:
            self.pm.screen_shot()
            print '账期日期错误', date1, date2, d1_end, d2_end, start_date_1, start_date_2,end_date_1,end_date_2
            assert True is False

    # 账单计划-各种费用
    def bill_fee(self, fe1, fe2, fe3, fe4, fe5, tag):
        # 水费
        fee1 = self.pm.read_element_txt_by_ids(self.phs.bill_fee_amount, 0)
        fee1 = self.pm.regular_num(fee1)
        fee1 = float(fee1[0])
        # 物业费
        fee2 = self.pm.read_element_txt_by_ids(self.phs.bill_fee_amount, 1)
        fee2 = self.pm.regular_num(fee2)
        fee2 = float(fee2[0])
        # 房屋押金
        fee3 = self.pm.read_element_txt_by_ids(self.phs.bill_fee_amount, 2)
        fee3 = self.pm.regular_num(fee3)
        fee3 = float(fee3[0])
        # 房屋租金
        fee4 = self.pm.read_element_txt_by_ids(self.phs.bill_fee_amount, 4)
        fee4 = self.pm.regular_num(fee4)
        fee4 = float(fee4[0])
        # 电冰箱押金
        fee5 = self.pm.read_element_txt_by_ids(self.phs.bill_fee_amount, 5)
        fee5 = self.pm.regular_num(fee5)
        fee5 = float(fee5[0])
        if fee1 == fe1 and fee2 == fe2 and fee3 == fe3 and fee4 == fe4 and fee5 ==fe5:
            pass
        else:
            self.pm.screen_shot()
            print '费用错误'
            assert True is False
        if tag == 2:
            self.pm.screenSlide_by_zuobiao(600.0, 1500.0, 600.0, 1000.0, 1080.0, 1920.0)
            fee6 = self.pm.read_element_txt_by_ids(self.phs.bill_fee_amount, 6)
            fee7 = self.pm.read_element_txt_by_ids(self.phs.bill_fee_amount, 7)
            fee6 = self.pm.regular_num_new(fee6)
            fee7 = self.pm.regular_num_new(fee7)
            if fee6 == fe1 and fee7 == fe4:
                pass
            else:
                self.pm.screen_shot()
                print '费用错误'
                assert True is False

    # 账单计划页金额、时间检查流程（页面流程）
    def bill_plan_page_check(self, total_money, d1, money1, date1, fe1, fe2, fe3, fe4, fe5,
                             status_fenqi='',money2=0,tag=0,):
        self.judge_bill_plan()
        self.judge_bill_total_money(total_money)
        self.judge_bill_payment_date(d1, status_fenqi)
        self.judge_money_1(money1,money2, tag)
        self.judge_start_end_date(date1, status_fenqi)
        self.bill_fee(fe1, fe2, fe3, fe4, fe5,tag)
        self.confirm_ren()  # 确认完成返回房态页面

    # 账单计划页流程
    def bill_plan_flow(self):
        self.judge_bill_plan()
        self.confirm_ren()

    # 续租流程-分散式(集中式也一样)
    def relet_fensan(self, relettime, method, day, biaodi, fee, zhouqi, addmoney1, mendian, saleman):
        self.judge_relet()
        self.rent_time(relettime)
        self.pay_method(method)
        self.pay_advance(day)
        self.swip_screen()
        self.gas_fee(biaodi)
        self.add_fee(fee, zhouqi)
        self.rent_money(addmoney1, j=0)
        self.swip_screen()
        self.rent_shop(mendian)
        self.saleman(saleman)
        self.next_step()
        self.judge_bill_plan()
        self.confirm_ren()

    # 社区-房间选择-分散式
    def select_community_room_fensan(self, community, room):
        for i in range(10):
            if self.pm.find_element_name(community):
                if self.pm.find_element_name(room):
                    self.pm.click_by_name(room)
                else:
                    self.pm.click_by_name(community)
                    # 如果社区在屏幕下方，点开之后房间会被屏幕下方覆盖，所以要向上划屏
                    for j in range(10):
                        if self.pm.find_element_name(room):
                            self.pm.click_by_name(room)
                            break
                        else:
                            self.pm.screenSlide_by_zuobiao(700.0, 1380.0, 700.0, 1060.0, 1080, 1920)
                break
            else:
                self.pm.screenSlide_by_zuobiao(700.0, 1570.0, 700.0, 500.0, 1080, 1920)

    # 房态-集中式-预订页(分散式通用)
    def house_status_order(self, customer):
        self.pm.assert_el_by_name(self.phs.order_title)
        self.sign_select_customer(customer)
        self.pm.assert_el_by_name(self.phs.order_title)
        self.pm.click_by_name(self.phs.sign_day)
        self.confirm()
        self.pm.send_keys_by_id(self.phs.remark, u'没什么可备注的')
        self.confirm_ren()
        self.judege_house_status()  # 预订页确认之后回到房态首页

    # 房态-集中式-关闭预定单
    def house_status_order_close_flow(self, community, loudong, no, customer):
        self.judege_house_status()
        self.click_title_jizhong()
        self.select_community(community, loudong)
        self.select_house(no)
        self.room_order()
        self.house_status_order(customer)

    # 房态-集中式-签约流程
    def house_status_flow(self, community, loudong, customer, rent_time, method, day,
                          fee1, zhouqi1, addmoney1, furniture1, model1, num1, mendian,
                          saleman, fapiao, no=None):
        self.judege_house_status()
        self.click_title_jizhong()
        self.select_community(community, loudong)
        self.select_house(no)
        self.room_sign()
        self.sign_judge()
        self.sign_select_customer(customer)
        self.sign_judge()
        self.rent_time(rent_time)
        self.pay_method(method)
        # 付款日只能选一个
        self.pay_advance(day)
        self.swip_screen()  # 划屏
        self.electricity_fee(biaodi=5)
        # self.pay_fix_advance(month, fixday)
        self.add_fee_online(fee1, zhouqi1)
        self.rent_money(addmoney1, j=0)
        # self.add_fee(fee2, zhouqi2)
        # self.rent_money(addmoney2, j=0)
        # self.add_fee(fee3, zhouqi3)
        # self.rent_money_caobiao(addmoney3, biaodi)
        self.swip_screen()  # 划屏
        self.add_settings(furniture1, model1, num1)
        # self.add_settings(furniture2, model2, num2)
        self.rent_shop(mendian)
        self.saleman(saleman)
        self.swip_screen()  # 划屏
        self.invoice(fapiao)
        self.next_step()

    # 房态-分散式-预订-关闭
    def house_status_fensan_order_close_flow(self, district, street, community, room,
                                             customer):
        self.judege_house_status()
        self.change_house_staue_type()
        self.click_title_jizhong()
        self.select_district_street_fensan(district, street)
        self.select_community_room_fensan(community, room)
        self.room_order()
        self.house_status_order(customer)

    # 房态-分散式-签约流程
    def house_status_flow_fensan(self, district, street, community, room, customer,
                                 rent_time, method, fee1, zhouqi1, day, addmoney,
                                 furniture1, model1, num1, mendian, saleman, fapiao):
        self.judege_house_status()
        self.change_house_staue_type()
        self.click_title_jizhong()
        self.select_district_street_fensan(district, street)
        self.select_community_room_fensan(community, room)
        self.room_sign()
        self.sign_judge()
        self.sign_select_customer(customer)
        self.sign_judge()
        self.rent_time(rent_time)
        self.pay_method(method)
        # 付款日只能选一个
        self.pay_advance(day)
        # self.pay_fix_advance(month, fixday)
        # self.add_fee(fee1, zhouqi1)
        self.swip_screen()  # 划屏
        self.electricity_fee(biaodi=5)
        self.add_fee_online(fee1, zhouqi1)
        self.rent_money(addmoney, j=0)
        self.swip_screen()  # 划屏
        self.add_settings_online(furniture1, model1, num1)
        self.rent_shop(mendian)
        self.saleman(saleman)
        self.swip_screen()  # 划屏
        self.invoice(fapiao)
        self.next_step()
        # 增加账单计划页，金额时间的对比判断

        # self.confirm_ren()
        # 确认完成返回房态页面

    # 选择社区-房间-集中式
    def select_community_room_jizhong(self, community, loudong, room):
        self.judege_house_status()
        self.click_title_jizhong()
        self.select_community(community, loudong)
        self.select_house(room)

    # 选择社区-房间-分散式
    def select_community_room_fensan01(self, district, street, community, room):
        self.judege_house_status()
        # self.change_house_staue_type() #
        self.click_title_jizhong()
        self.select_district_street_fensan(district, street)
        self.select_community_room_fensan(community, room)

    # 选择社区-房间-分散式
    def select_community_room_fensan02(self, district, street, community, room):
        self.judege_house_status()
        self.change_house_staue_type()  # 需要点击房态切换到分散式
        self.click_title_jizhong()
        self.select_district_street_fensan(district, street)
        self.select_community_room_fensan(community, room)






