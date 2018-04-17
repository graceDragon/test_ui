# coding:utf-8
from selenium import webdriver
import unittest



class Test(unittest.TestCase):
    # def test_01(self):
    #     driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver2.33.exe')
    #     driver.get('http://t.efang100.cc')
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)

    def test_02(self):
        s = 'asv'
        s1 = u'asv'
        print type(s)
        print type(s1)
        s_type = s1.encode(encoding='utf-8')
        print type(s_type)


if __name__ == '__main__':
    Test().test_02()











