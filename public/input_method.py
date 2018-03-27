# coding:utf-8

"""
切换输入法
"""

import os


class InputMethod(object):
    def __init__(self):
        # 列出所有的输入法
        self.commond_0 = 'adb shell ime list -s'
        # 查看默认的输入法
        self.commond_1 = 'adb shell settings get secure default_input_method'
        # 切换到华为百度输入法
        self.commond_2 = 'adb shell ime set com.baidu.input_huawei/.ImeService'
        # 切换到appium输入法
        self.commond_3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'
        # 切换到安卓默认输入法
        self.commond_4 = 'adb shell ime set com.android.inputmethod.latin/.LatinIME'

    def input_method_appium(self):
        # appium自带的输入法
        os.system(self.commond_3)

    def input_method_baidu(self):
        # 百度输入法
        os.system(self.commond_2)

    def input_method_android(self):
        # 安卓默认输入法
        os.system(self.commond_4)


if __name__ == '__main__':
    # InputMethod().input_method_appium()
    InputMethod().input_method_baidu()





















