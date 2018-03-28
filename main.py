# coding:utf-8

from config import HTMLTestRunner
import time
from config.settings import BASE_PATH, BASE_PATH_HTML
import os
from public import appium_start
from config.configEmail import MyEmail
from zhiyu_web.test_suite import suite_zhiyu_web
from zhiyu_app.test_suite import suite_zhiyu_app


if __name__ == '__main__':
    # 加appium命令行启动，加app和web的判断执行
    appium_start.AppiumStart().appium_youli()

    # 按日期新建文件夹
    dir_day = time.strftime('%Y%m%d', time.localtime(time.time()))
    dir_path = os.path.join(BASE_PATH, 'reports\html_report', dir_day)
    # 按精确时间命名html文件
    time_str = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    filename = time_str + '.html'
    filename_path = os.path.join(BASE_PATH, 'reports\html_report', dir_day, filename)
    # 测试报告路径写入文本
    f_path = open(BASE_PATH_HTML, 'w')
    f_path.write(filename_path)
    f_path.close()
    if os.path.exists(dir_path):
        pass
    else:
        os.mkdir(dir_path)
    f = open(filename_path, 'wb')
    # """
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title=u'系统持续集成-功能测试结果',
        description=u'测试报告'
    )
    # """
    # runner.run(suite_zhiyu_web.suite)
    runner.run(suite_zhiyu_app.suite)
    f.close()
    # send test report by email
    send_email = MyEmail.get_email()
    on_off = 'on'
    if on_off == 'on':
        print '开始发送邮件...'
        send_email.send_email()
        print '邮件发送完成...'
    elif on_off == 'off':
        print "不需要发动邮件给任何人！"
    else:
        print "是否发送邮件的状态码书写错误！"





