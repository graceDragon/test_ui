# coding:utf-8

from ..page import page_home
from public import public_method


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(driver)

    def judge_homepage(self):
        self.pm.assert_el_by_name(page_home.home_newhouse)

    def judge_tab_home(self):
        self.pm.assert_el_by_name(page_home.home_tab_home)

    def click_tab_home(self):
        self.pm.click_by_name(page_home.home_tab_home)

    def click_tab_xinyuan(self):
        self.pm.click_by_name(page_home.home_tab_xinyuan)

    def click_tab_wode(self):
        self.pm.click_by_name(page_home.home_tab_wode)

    def click_change_city(self):
        self.pm.click_by_id(page_home.home_change_city)

    def read_city(self):
        city = self.pm.read_element_txt_by_id(page_home.home_change_city)
        return city

    def judge_city(self, r):
        if self.pm.read_and_judge_element_txt_by_id(page_home.home_change_city, r):
            pass
        else:
            print "定位异常"
            assert True is False

    def click_search(self):
        self.pm.click_by_id(page_home.home_search)

    def click_zhengzu(self):
        self.pm.click_by_name(page_home.home_zhengzu)

    def click_hezu(self):
        self.pm.click_by_name(page_home.home_hezu)

    def click_pinpai(self):
        self.pm.click_by_name(page_home.home_pinpai)

    def judge_zhengzu(self):
        self.pm.assert_el_by_name(page_home.home_zhengzu)

    def judge_hezu(self):
        self.pm.assert_el_by_name(page_home.home_hezu)

    def judge_pinpai(self):
        self.pm.assert_el_by_name(page_home.home_pinpai)

    def judge_newhouse(self):
        self.pm.assert_el_by_name(page_home.home_newhouse)

    def click_more(self):
        self.pm.click_by_id(page_home.home_more)

    def click_lookmore(self):
        self.pm.click_by_id(page_home.home_look_more)

    def judge_youxuanhouse(self):
        tag = 0
        for i in range(5):
            if self.pm.find_element_name(page_home.home_youxuan):
                self.pm.assert_el_by_name(page_home.home_youxuan)
                tag = 1
                break
            else:
                self.pm.screenSlide_by_zuobiao(600.0, 1500.0, 600.0, 700.0, 1080.0, 1920.0)
        if tag == 0:
            assert True is False

    def click_duwei(self):
        for i in range(7):
            self.pm.screenSlide_by_zuobiao(600.0, 1500.0, 600.0, 700.0, 1080.0, 1920.0)
        self.pm.click_by_names(page_home.home_duwei, -1)

    def click_subway(self):
        while not self.pm.find_element_name(page_home.home_subway):
            self.pm.screenSlide_by_zuobiao(600.0, 1500.0, 600.0, 700.0, 1080.0, 1920.0)
        self.pm.click_by_name(page_home.home_subway)

    def click_south(self):
        while not self.pm.find_element_name(page_home.home_south):
            self.pm.screenSlide_by_zuobiao(600.0, 1500.0, 600.0, 700.0, 1080.0, 1920.0)
        self.pm.click_by_name(page_home.home_south)

    def click_jingzhuang(self):
        while not self.pm.find_element_name(page_home.home_jingzhuang):
            self.pm.screenSlide_by_zuobiao(600.0, 1500.0, 600.0, 700.0, 1080.0, 1920.0)
        self.pm.click_by_name(page_home.home_jingzhuang)









