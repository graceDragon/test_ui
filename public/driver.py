# coding:utf-8

"""
封装driver
"""

from selenium import webdriver as sw
from config.settings import *
from test_data.data import *
from appium import webdriver as aw


class Driver(object):
    def __init__(self):
        pass

    def driver_web(self, url):
        # 谷歌浏览器
        driver = sw.Chrome(chrome_driver_path)
        # 火狐浏览器
        # driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(3)
        return driver

    def driver_web_session(self, url):
        # 谷歌浏览器
        driver = sw.Chrome(chrome_driver_path)
        # 火狐浏览器
        # driver = webdriver.Firefox()
        driver.get(url)
        driver.add_cookie(cookies_dict)
        driver.refresh()
        driver.maximize_window()
        driver.implicitly_wait(3)
        return driver

    def driver_app(self):
        desired_caps = {}
        desired_caps['deviceName'] = 'R8V7N15604006646'
        desired_caps['udid'] = 'R8V7N15604006646'  # 多线程要加这个
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        # desired_caps['appPackage'] = 'com.ncf.mango_manager.dev'  # 测试包
        # desired_caps['appActivity'] = 'com.ncf.mango_manager.activity.SplashActivity'
        desired_caps['appPackage'] = 'com.ncf.mango_manager'  # 生产包
        desired_caps['appActivity'] = '.activity.SplashActivity'
        desired_caps["unicodeKeyboard"] = "True"  # 使用 Unicode 输入法。默认值false
        desired_caps["resetKeyboard"] = "True"
        # resetKeyBoard在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。
        # 如果单独使用，将会被忽略。默认值 false
        desired_caps["noReset"] = "True"  # 不要在会话前重置应用状态。默认值false。
        driver = aw.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        return driver

    def driver_app_youli(self):
        desired_caps = {}
        desired_caps['deviceName'] = 'R8V7N15604006646'
        desired_caps['udid'] = 'R8V7N15604006646'  # 多线程要加这个
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['appPackage'] = 'com.ncf.ulive_client'  # 测试包
        desired_caps['appActivity'] = '.activity.SplashActivity'
        # desired_caps['appPackage'] = 'com.ncf.mango_manager'  # 生产包
        # desired_caps['appActivity'] = '.activity.SplashActivity'
        desired_caps["unicodeKeyboard"] = "True"  # 使用 Unicode 输入法。默认值false
        desired_caps["resetKeyboard"] = "True"
        # resetKeyBoard在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。
        # 如果单独使用，将会被忽略。默认值 false
        desired_caps["noReset"] = "True"  # 不要在会话前重置应用状态。默认值false。
        driver = aw.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        return driver

























