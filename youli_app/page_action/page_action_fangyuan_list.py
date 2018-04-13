# coding:utf-8

from public import public_method
from ..page import page_fangyuan_list


class FangyuanList(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(self.driver)

    def click_confirm(self):
        self.pm.click_by_name(page_fangyuan_list.confirm)

    def judge_fangyuanlist_page(self):
        self.pm.assert_el_by_name(page_fangyuan_list.choose_price_name)

    def click_limit(self):
        self.pm.click_by_id(page_fangyuan_list.choose_limit)

    def click_location(self):
        self.pm.click_by_id(page_fangyuan_list.choose_location)

    def click_more(self):
        self.pm.click_by_id(page_fangyuan_list.choose_more)

    def click_price(self):
        self.pm.click_by_id(page_fangyuan_list.choose_more)

    # 选择几室(整租)
    def select_howmany_zheng(self, r):
        self.pm.click_by_names(r, 0)

    # 选择几室(合租)
    def select_howmany_he(self, r):
        self.pm.click_by_names(r, 1)

    # 选择品牌公寓
    def select_apartment(self, r):
        tag = 0
        for i in range(5):
            last_apartment = self.pm.read_element_txt_by_ids(page_fangyuan_list.choose_name, -1)
            if self.pm.find_element_name(r):
                self.pm.click_by_name(r)
                tag = 1
                break
            else:
                self.pm.screenSlide_by_zuobiao(600.0, 1300.0, 600.0, 600.0, 1080.0, 1920.0)
                last_apartment_again = self.pm.read_element_txt_by_ids(page_fangyuan_list.choose_name, -1)
                if last_apartment_again == last_apartment:
                    print '已经滑动到了最底部！没有找到"', r, '"公寓'
                    break
        if tag == 1:
            pass
        elif tag == 0:
            for i in range(5):
                last_apartment = self.pm.read_element_txt_by_ids(page_fangyuan_list.choose_name, 0)
                if self.pm.find_element_name(r):
                    self.pm.click_by_name(r)
                    tag = 1
                    break
                else:
                    self.pm.screenSlide_by_zuobiao(600.0, 700.0, 600.0, 1300.0, 1080.0, 1920.0)
                    last_apartment_again = self.pm.read_element_txt_by_ids(page_fangyuan_list.choose_name, 0)
                    if last_apartment_again == last_apartment:
                        print '已经滑动到了最顶部！没有找到"', r, '"公寓'
                        break
        if tag == 1:
            pass
        else:
            print '划到最顶部还么找到此公寓，直接退出程序'
            assert True is False

    # 选择商圈
    def select_location(self, l1, l2, l3):
        self.pm.click_by_name(l1)
        if l1 == '附近':
            pass
        elif l1 == '区域':
            for i in range(5):
                location_name = self.pm.read_element_txt_by_ids(page_fangyuan_list.location_middle, -1)
                if self.pm.find_element_name(l2):
                    self.pm.click_by_name(l2)
                    break
                else:
                    self.pm.screenSlide_by_zuobiao(600.0, 1500.0, 600.0, 700.0, 1080.0, 1920.0)
                    location_name_again = self.pm.read_element_txt_by_ids(page_fangyuan_list.location_middle, -1)
                    if location_name_again == location_name:
                        print '选择位置不存在！”', l2, '“不存在'
                        assert True is False
            for i in range(5):
                location_name = self.pm.read_element_txt_by_ids(page_fangyuan_list.location_right, -1)
                if self.pm.find_element_name(l3):
                    self.pm.click_by_name(l3)
                    break
                else:
                    self.pm.screenSlide_by_zuobiao(900.0, 1500.0, 900.0, 700.0, 1080.0, 1920.0)
                    location_name_again = self.pm.read_element_txt_by_ids(page_fangyuan_list.location_right, -1)
                    if location_name_again == location_name:
                        print '选择位置不存在！”', l3, '“不存在'
                        assert True is False
        else:
            print '选择位置不存在！”', l1, '“不存在'
            assert True is False

    # 选择装修情况
    def select_zhuangxiu(self, r):
        self.pm.screenSlide_by_zuobiao(600.0, 1500.0, 600.0, 700.0, 1080.0, 1920.0)
        if self.pm.find_element_name(r):
            self.pm.click_by_name(r)
        else:
            print r, '装修情况不存在！'
            assert True is False

    # 滑动屏幕直到找到这个房源
    def find_click_fangyuan(self, r):
        for i in range(5):
            house_name = self.pm.read_element_txt_by_ids(page_fangyuan_list.fangyuan_name, -1)
            if self.pm.find_element_name(r):
                self.pm.click_by_name(r)
                break
            else:
                # 1700-1010坐标划过2个房源
                self.pm.screenSlide_by_zuobiao(600.0, 1700.0, 600.0, 1010.0, 1080.0, 1920.0)
                house_name_again = self.pm.read_element_txt_by_ids(page_fangyuan_list.fangyuan_name, -1)
                if house_name_again == house_name:
                    print '房源"', r, '"不存在'
                    assert True is False

    # -------------房源列表页-------------
    def fangyuan_list_flow(self, zheng, he, pinpai, l1, l2, l3, zhuangxiu, house):
        self.judge_fangyuanlist_page()
        self.click_limit()
        self.select_howmany_zheng(zheng)
        self.select_howmany_he(he)
        self.select_apartment(pinpai)
        self.click_confirm()
        self.click_location()
        self.select_location(l1, l2, l3)
        self.click_more()
        self.select_zhuangxiu(zhuangxiu)
        self.click_confirm()
        self.find_click_fangyuan(house)

    def zhengzu_flow(self, house):
        self.judge_fangyuanlist_page()
        self.find_click_fangyuan(house)











