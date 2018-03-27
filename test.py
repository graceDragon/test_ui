# coding:utf-8

from selenium import webdriver
from test_data.data import *
from config.settings import *
from time import sleep
# 谷歌浏览器
driver = webdriver.Chrome(chrome_driver_path)
# 火狐浏览器
# driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get(url_zhiyu_test)
driver.add_cookie(cookies_dict)
driver.refresh()
# driver.get('http://blog.csdn.net/qq_36482772/article/details/53328558')

sleep(5)
driver.find_element_by_xpath('//span[contains(text(),"首页")]').click()
sleep(5)
# 切换iframe  //*[@id="fRight"]
# js = "var q=document.documentElement.scrollTop=10000"
js = 'window.scrollBy(0,200)'
print(js)
driver.execute_script(js)
sleep(5)
driver.execute_script("var q=document.documentElement.scrollTop=0")
sleep(5)
driver.execute_script("var q=document.documentElement.scrollTop=1000")






class Test(object):
    def __init__(self):
        pass

    def check_str(self):
        a = '空置'
        b = '空置3天'
        if a in b:
            print 'pass'
        else:
            print 'fault'

if __name__ == '__main__':
    Test().check_str()

    



















