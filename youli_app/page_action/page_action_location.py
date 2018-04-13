# coding:utf-8

from public import public_method
from ..page import page_location


class ChangeCity(object):
    def __init__(self, driver):
        # 登录判断在我的里边
        self.driver = driver
        self.pm = public_method.PublicMethod(driver)

    def judge_title(self):
        self.pm.assert_el_by_name(page_location.city_title)

    def back_home(self):
        self.pm.click_by_id(page_location.city_back)

    def select_city(self, r):
        self.pm.click_by_name(r)

    def read_location_city(self):
        city = self.pm.read_element_txt_by_id(page_location.city_location)
        return city













