# coding:utf-8

"""
智寓首页
"""

from public import public_method
from zhiyu_web.page import page_home


class Home(object):

    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(self.driver)

    def judge_home_page(self):
        self.pm.assert_el_by_xpath(page_home.home_tab_home)

    def read_user(self, user):
        self.pm.read_and_judge_element_txt_by_xpath(page_home.home_user, user)










