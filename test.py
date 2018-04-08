# coding:utf-8
from selenium import webdriver
import unittest



class Test(unittest.TestCase):
    def test_01(self):
        driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver2.33.exe')
        driver.get('http://t.efang100.cc')
        driver.maximize_window()
        driver.implicitly_wait(3)


if __name__ == '__main__':
    Test().test_01()











