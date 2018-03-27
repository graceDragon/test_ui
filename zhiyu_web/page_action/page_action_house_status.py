# coding:utf-8

from ..page.page_house_status_now import *
from public import public_method
from test_data.data import *


class PageActionHouseStatus(object):
    def __init__(self, driver):
        self.m = public_method.PublicMethod(driver)

    def house_status_01(self):
        # 点击 房态-实时房态-集中式房态
        # self.m.stay_element(house_status_xpath)
        # self.m.stay_element(house_status_now_xpath)
        # self.m.stay_element(house_status_concentrate_xpath)
        self.m.click_element(house_status_xpath)
        self.m.click_element(house_status_now_xpath)
        self.m.click_element(house_status_concentrate_xpath)
        self.m.move_mouse(100, 100)

    def house_site_judge(self, r):
        # 判断所在的公寓地址是否正确
        self.m.read_and_judge_element_txt(select_site_xpath, r)

    def scrollbar_web(self, r):
        self.m.scrollbar_web(r)














