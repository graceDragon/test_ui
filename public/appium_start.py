# -*- coding:utf-8 -*-
import os
import time
from config.settings import BASE_PATH_BAT


class AppiumStart:
    def __init__(self):
        print 'start appium....'
        # pass

    def start_appium(self, path):  # 启动appium
        os.system(path)
        # os.system("C:\\JKS\\workspace\\myfen-android\\gitcode\\meiyifen\\config\\appium_start_mf3.bat")
        print "启动Appium..."
        print "等待启动完成..."
        time.sleep(10)
        print "开始执行脚本..."

    def stop_appium(self, port):  # 杀死appium
        dos = 'netstat -aon|findstr ' + port
        a = os.popen(dos).readline()
        try:
            a = a.split()[4]
        except:
            pass
        cmd = 'taskkill /f /pid ' + a
        print cmd
        os.system(cmd)

    def appium(self, port, path):
        self.stop_appium(port)
        time.sleep(3)
        self.start_appium(path)

    def appium_youli(self):
        port = "4723"
        pt = os.path.join(BASE_PATH_BAT, 'appium_start_youli.bat')
        print 'bat路径：', pt
        self.appium(port, pt)

    def appium_meiyifen_xg(self):
        port = "4725"
        pt = os.path.join(BASE_PATH, 'config/bat/appium_start_youli.bat')
        print 'bat路径：', pt
        self.appium(port, pt)

    def appium_meiyifang(self):
        port = "4725"
        pt = os.path.join(BASE_PATH, 'appium_start_meiyifang.bat')
        print 'bat路径：', pt
        self.appium(port, pt)

if __name__ == '__main__':
    AppiumStart().stop_appium('4723')
