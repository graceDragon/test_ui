# coding:utf-8

from ..page import page_house_detail
from public import public_method
from time import sleep
import page_action_fangyuan_list
import page_action_wode


class HouseDetail(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(driver)
        self.list = page_action_fangyuan_list.FangyuanList(self.driver)
        self.wode = page_action_wode.WoDe(self.driver)

    def click_confirm(self):
        self.pm.click_by_name(page_house_detail.confirm)

    def click_cancel(self):
        self.pm.click_by_name(page_house_detail.cancel)

    def judge_house_detail(self):
        self.pm.assert_el_by_name(page_house_detail.detail_phone)

    def click_back(self):
        self.pm.click_by_id(page_house_detail.detail_back)

    def click_collect(self):
        self.pm.click_by_id(page_house_detail.detail_collect)

    def click_share(self):
        self.pm.click_by_id(page_house_detail.detail_share)

    def click_pay_way(self):
        self.pm.click_by_id(page_house_detail.detail_pay_way)

    def click_yuyue(self):
        if self.pm.find_element_name(page_house_detail.detail_yuyue):
            pass
        elif self.pm.find_element_name(page_house_detail.detail_yuyue_cancel):
            self.pm.click_by_name(page_house_detail.detail_yuyue_cancel)
            self.pm.click_by_name(page_house_detail.confirm)
            sleep(1)
        self.pm.click_by_name(page_house_detail.detail_yuyue)

    def click_yuyue_cancel(self):
        self.pm.click_by_name(page_house_detail.detail_yuyue_cancel)

    def click_phone(self):
        self.pm.click_by_name(page_house_detail.detail_phone)

    # -------------预约页面------------
    def judge_yuyue_page(self):
        self.pm.assert_el_by_name(page_house_detail.yuyue_confirm)

    def click_yuyue_time(self):
        self.pm.click_by_name(page_house_detail.yuyue_time_select)

    def yuyue_confirm(self):
        self.pm.click_by_name(page_house_detail.yuyue_confirm)

    # -------------预约流程------------
    def yuyue_page_flow(self):
        self.judge_house_detail()
        sleep(1)
        self.click_yuyue()
        self.judge_yuyue_page()
        self.click_yuyue_time()
        self.click_confirm()
        self.yuyue_confirm()
        self.wode.judge_yuyue_page()  # 返回到我的预约











