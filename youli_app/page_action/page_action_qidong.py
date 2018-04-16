# coding:utf-8
"""
# 启动页
"""
from ..page import page_qidong
from public import public_method


class QiDong(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(self.driver)

    def judge_qidong(self):
        self.pm.assert_el_by_id(page_qidong.qidong_skip)

    def click_skip(self):
        self.pm.click_by_id(page_qidong.qidong_skip)

    # 启动页执行流程
    def qidong_flow(self):
        if self.pm.find_element_id(page_qidong.qidong_skip):
            self.click_skip()



