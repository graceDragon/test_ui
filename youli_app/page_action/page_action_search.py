# coding:utf-8

from public import public_method
from ..page import page_search


class Search(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(self.driver)

    def judge_search(self):
        self.pm.assert_el_by_name(page_search.search_input02)

    def search_input(self, r):
        self.pm.click_by_id(page_search.search_input)
        self.pm.send_keys_by_id(r, page_search.search_input)

    def search_pipei(self):
        pass

    def search_cancel(self):
        self.pm.click_by_name(page_search.search_cancel)

    # 搜索页流程
    def search_page(self, r):
        self.judge_search()
        self.search_input(r)
        # 键盘搜索键
        self.pm.presscode(84)







