# coding:utf-8

from public import public_method
from ..page import page_fangyuan


class FangyuanList(object):
    def __init__(self, driver):
        self.driver = driver
        self.pm = public_method.PublicMethod(self.driver)

    def find_fangyuan(self, name):
        # 滑动屏幕直到找到这个房源
        for i in range(5):
            if self.pm.find_element_name(name):
                # 如果这个房源的部分信息被屏幕遮挡，需要滑动屏幕
                tag = 1
                break
            else:
                self.pm.screenSlide_by_zuobiao(600.0, 1700.0, 600.0, 320.0, 1080.0, 1920.0)



