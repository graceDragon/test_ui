# coding:utf-8


import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_PATH_BAT = os.path.join(BASE_PATH, 'config', 'bat')

BASE_PATH_HTML = os.path.join(BASE_PATH, 'config', 'test_report_path.txt')

url_zhiyu_test = 'http://t.efang100.cc'

url_zhiyu_online = 'http://www.efang100.cc'

chrome_driver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver2.33.exe'

print BASE_PATH, BASE_PATH_HTML

"""
---邮件发送给个人还是群组,
---test代表发送给我自己，online代表发送给测试组
"""
# SendEmail = 'test'
SendEmail = 'online'


