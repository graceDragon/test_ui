# coding:utf-8

from config import HTMLTestRunner
import time
from config.settings import BASE_PATH
import os
from zhiyu_web.test_suite import suite_zhiyu_web
from zhiyu_app.test_suite import suite_zhiyu_app


if __name__ == '__main__':
    # 按日期新建文件夹
    dir_day = time.strftime('%Y%m%d', time.localtime(time.time()))
    dir_path = os.path.join(BASE_PATH, 'reports\html_report', dir_day)
    # 按精确时间命名html文件
    time_str = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    filename = time_str + '.html'
    filename_path = os.path.join(BASE_PATH, 'reports\html_report', dir_day, filename)

    if os.path.exists(dir_path):
        pass
    else:
        os.mkdir(dir_path)
    f = open(filename_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title=u'系统持续集成-功能测试结果',
        description=u'测试报告'
    )
    # 加appium命令行启动，加app和web的判断执行
    # runner.run(suite_zhiyu_web.suite)
    runner.run(suite_zhiyu_app.suite)





