# coding:utf-8
import math
import operator
import os
import random
import time
from datetime import timedelta, date
import MySQLdb
import pytesseract
import re
from PIL import Image
from appium.webdriver.mobilecommand import MobileCommand
from public import saveScreen
from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from uiautomator import Device   # 为了监听弹框-多台手机可以
# from uiautomator import device as d  # 为了监听弹框-uiautomator在使用的时候都要初始化一个d对象，单个手机可以通过
# from pyocr import pyocr
# import pyocr.builders

"""
cmd配置appium
appium -a 127.0.0.1 -p 4726 --bootstrap-port 4780 --session-override --log "E:/appium" --command-timeout 600

"""


class Method():
    def __init__(self, driver):
        self.driver = driver

    """
    def setup(self):
        # a = os.system('adb connect 10.129.222.118:5555')  # 如果无线连接手机，先执行连接，防止掉线
        # print a  # 用线连接手机就注释掉这块
        self.appium()
        desired_caps = {}
        desired_caps['deviceName'] = param.devicename  # adb devices查到的设备名 #0815f83cb8390c01  #91QEBPL69452
        desired_caps['udid'] = param.devicename  # 多线程要加这个
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'  # 5.1  6.0.1
        desired_caps['appPackage'] = 'com.gomejr.myf2'  # 被测App的包名
        # desired_caps['appActivity'] = '.module.launcher.SelectUrlActivity'  # 启动时的Activity
        desired_caps['appActivity'] = '.module.launcher.WelcomeActivity'  # 启动时的Activity
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver = webdriver.Remote(param.address, desired_caps)  # 10.129.39.76
        self.driver.implicitly_wait(10)
        return self.driver

    def setup_xiaoguan(self):
        # a = os.system('adb connect 10.129.222.118:5555')  # 如果无线连接手机，先执行连接，防止掉线
        # print a  # 用线连接手机就注释掉这块
        self.appium()
        desired_caps = {}
        desired_caps['deviceName'] = '0815f83cb8390c01'  # adb devices查到的设备名 #0815f83cb8390c01  #91QEBPL69452
        desired_caps['udid'] = '0815f83cb8390c01'  # 多线程要加这个
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'  # 5.1  6.0.1
        desired_caps['appPackage'] = 'com.gomejr.myf'  # 被测App的包名
        desired_caps['appActivity'] = '.welcome.WelcomeActivity'  # 启动时的Activity
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        return self.driver
    """

    # def appium(self):
    #     self.stop_appium("4723")
    #     time.sleep(3)
    #     self.start_appium()
    """
    def qidong(self):
        for i in range(10):
            if self.ckname("允许"):
                self.finduname("允许").click()  # 点掉手机权限
            else:
                break
        if self.ckname("SIT"):
            self.finduname("SIT").click()  # 选择sit环境
        for i in range(10):
            if self.ckname("即刻申请"):
                self.finduname("即刻申请").click()
                self.judgename("产品")
                self.finduname("产品").click()
                break
            elif self.ckname("美易分优质产品"):  # 判断是否在首页
                break
            elif self.ckname(loginout.lg_denglu_name):  # 登录
                break
            else:
                self.screenSlide_by_zuobiao(900.0, 1000.0, 100.0, 1000.0, 1080.0, 1920.0)  # 滑掉屏幕的提示页
        print "跳出启动循环..."
        """

    def teardown(self):
        self.driver.quit()  # quit结束的是session,assert结束的是代码
        # pass

    """
    def start_appium(self):  # 启动appium
        os.system("E:\\gitcode\\uasc-develop\\uasc\\frame\\project_ui\\config\\appium_start_mf3.bat")
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
    """
    # 随机生成16位数（导购单号）
    def shoppingNum(self):
        num = "".join(random.choice("1234567890") for i in range(16))
        print num
        return num

    # 随机生成手机号码
    def createPhone(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    # 随机生成身份证号
    def getdistrictcode(self):
        FILE_PATH = "E:\\android\\districtcode.txt"
        with open(FILE_PATH) as file:
            data = file.read()
            districtlist = data.split('\n')
        for node in districtlist:
            # print node
            if node[10:11] != ' ':
                state = node[10:].strip()
            if node[10:11] == ' ' and node[12:13] != ' ':
                city = node[12:].strip()
            if node[10:11] == ' ' and node[12:13] == ' ':
                district = node[14:].strip()
                code = node[0:6]
                codelist.append({"state": state, "city": city, "district": district, "code": code})

    # 随机生成身份证号
    def gennerator(self):
        global codelist
        codelist = []
        if not codelist:
            self.getdistrictcode()  # 调用getdistrictcode
        id = codelist[random.randint(0, len(codelist))]['code']  # 地区项
        id = id + str(random.randint(1930, 2013))  # 年份项
        da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
        id = id + da.strftime('%m%d')
        id = id + str(random.randint(100, 300))  # 顺序号简单处理
        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
        id = id + checkcode[str(count % 11)]  # 算出校验码
        return id

    def js(self,r):
        return self.driver.execute_script(r)

    def pressHome(self, m):  # 按home键，并打开应用
        self.driver.press_keycode(3)
        tag = 0
        for i in range(3):
            if self.driver.find_element_by_name(m):
                self.driver.find_element_by_name(m).click()
                tag = 1
                break
            else:
                self.screenSlide_by_zuobiao(1100.0, 500.0, 200.0, 500.0, 1430.0, 2550.0)
        if tag == 0:
            for i in range(3):
                if self.driver.find_element_by_name(m):
                    self.driver.find_element_by_name(m).click()
                    break
                else:
                    self.screenSlide_by_zuobiao(200.0, 500.0, 1100.0, 500.0, 1430.0, 2550.0)

    def presscodes(self, m, n):
        self.driver.press_keycode(m, n)

    def presscode(self, i):
        self.driver.press_keycode(i)

    def clear_keycode(self, element):  # 模拟键盘清空输入框- 删除键 112
        element.click()
        time.sleep(2)
        self.driver.press_keycode(29, 28672)  # ctrl+a 全选输入框内容
        time.sleep(2)
        self.driver.press_keycode(112)  # 删除键 112

    def longPress(self, x, time):  # 长按
        action = TouchAction(self.driver)
        el = self.driver.find_element_by_id(x)
        return action.long_press(el).wait(time).perform()

    def ckid(self, x):
        try:
            self.driver.find_element_by_id(x)
        except:
            print u'未发现'+x
            return False
        return True

    def ckname(self, y):
        try:
            self.driver.find_element_by_name(y)
        except:
            print u'未发现'+y
            return False
        return True

    def ckclass(self,r):
        try:
            self.driver.find_element_by_class_name(r)
        except:
            print u'未发现'+r
            return False
        return True

    def ckxpath(self, z):
        try:
            self.driver.find_element_by_xpath(z)
        except:
            print u'页面跳转失败'
            return False
        return True

    def findclass(self,r):
        return self.driver.find_element_by_class_name(r)

    def findsclass(self,r):
        return self.driver.find_elements_by_class_name(r)

    def finduid(self, r):
        return self.driver.find_element_by_id(r)

    def finduids(self, r):
        return self.driver.find_elements_by_id(r)

    def finduname(self, s):
        return self.driver.find_element_by_name(s)

    def findunames(self, s):
        return self.driver.find_elements_by_name(s)

    def finduxpath(self, r):
        return self.driver.find_element_by_xpath(r)

    def finduxpaths(self, r):
        return self.driver.find_elements_by_xpath(r)

    def clickbyzuobiao(self, a):
        return self.driver.tap(a)

    # 页面跳转,等待加载完成
    def wait_page(self, element):
        for i in range(5):
            if self.ckname(element):
                break
            else:
                time.sleep(2)

    def read_zuobiao_by_xpath(self, r):  # 获取控件坐标--根据xpath
        a = self.driver.find_element_by_xpath(r)
        startx = int(a.location.get('x'))
        starty = int(a.location.get('y'))
        width = int(a.size.get('width'))
        height = int(a.size.get('height'))
        endx = startx + width
        endy = starty + height
        centrex = (startx + endx) / 2
        centrey = (starty + endy) / 2
        # print a
        return startx, starty, width, height, endx, endy, centrex, centrey

    def read_zuobiao_by_id(self, r):  # 获取控件坐标--根据id
        a = self.driver.find_element_by_id(r)
        startx = int(a.location.get('x'))
        starty = int(a.location.get('y'))
        width = int(a.size.get('width'))
        height = int(a.size.get('height'))
        endx = startx + width
        endy = starty + height
        centrex = (startx + endx) / 2
        centrey = (starty + endy) / 2
        # print a
        return startx, starty, width, height, endx, endy, centrex, centrey

    def imageVerification(self, startx, starty, endx, endy):  # 获取图形验证码
        u'''''获取验证码
                （startx，xstarty）----------------------------------
                                  |     要截取的图片范围              |
                                  |                                |
                                  ---------------------------------- (endx,endy)
                '''
        self.driver.get_screenshot_as_file('E:\\android\\imgVerificaton' + '\\image_web.jpg')  # 截屏
        imGetScreen = Image.open('E:\\android\\imgVerificaton' + '\\image_web.jpg')
        time.sleep(2)
        box = (startx, starty, endx, endy)
        # imIndentigy = imGetScreen.crop(box)
        a = imGetScreen.crop(box)
        # a = a.filter(ImageFilter.EDGE_ENHANCE)  # 边缘增强
        # a = a.filter(ImageFilter.DETAIL)  # 细节增强滤波
        # a.save('E:\\android\\imgVerificaton' + '\\zengqiang.jpg')
        # a = ImageEnhance.Sharpness(a).enhance(1)  # 图像锐度增强
        # a = ImageEnhance.ConimgVerificatontrast(a).enhance(1)  # 图像对比度
        imgL = a.convert('L')      # 转化为灰度图像
        imgL.save('E:\\android\\imgVerificaton' + '\\indent_web.jpg')
        threshold = 140            # 噪声去除掉。。#阈值为什么是140呢？试出来的，或者参考直方图。
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        out =imgL.point(table, '1')
        out.save('E:\\android\\' + '\\indentL_web.jpg')
        # img = Image.open('E:\\android\\imgVerificaton\\indentL_web.jpg')
        # img.show()
        text = pytesseract.image_to_string(out)
        print "#####################"
        print text
        print "#####################"
        # strCommand = 'tesseract.exe ' + 'E:\\android\\imgVerificaton' + '\\indentL_web.jpg ' + 'E:\\android\\imgVerificaton' + '\\indet_web.txt'
        # print strCommand
        # os.system(strCommand)
        # rfindet = open('E:\\android\\imgVerificaton' + '\\indet_web.txt.txt', 'r')
        # strIndet = rfindet.readline()
        # print strIndet
        return text

    def imageVerification_code(self, r, i):  # 获取图形验证码 r:控件的名字，i:控件是按id/name/xpath查找
        if i == "id":
            a = self.driver.find_element_by_id(r)
        elif i == "name":
            a = self.driver.find_element_by_name(r)
        else:
            a = self.driver.find_element_by_xpath(r)
        startx = int(a.location.get('x'))
        starty = int(a.location.get('y'))
        width = int(a.size.get('width'))
        height = int(a.size.get('height'))
        endx = startx + width
        endy = starty + height
        centrex = (startx + endx) / 2
        centrey = (starty + endy) / 2
        # print a
        # return startx, starty, width, height, endx, endy, centrex, centrey

        u'''''获取验证码
                （startx，xstarty）---------------------------------
                                  |     要截取的图片范围             |
                                  |                               |
                                  ---------------------------------- (endx,endy)
                '''
        self.driver.get_screenshot_as_file('E:\\android\\imgVerificaton' + '\\image_web.jpg')  # 截屏
        imGetScreen = Image.open('E:\\android\\imgVerificaton' + '\\image_web.jpg')
        time.sleep(2)
        box = (startx, starty, endx, endy)
        # imIndentigy = imGetScreen.crop(box)
        a = imGetScreen.crop(box)
        # a = a.filter(ImageFilter.EDGE_ENHANCE)  # 边缘增强
        # a = a.filter(ImageFilter.DETAIL)  # 细节增强滤波
        # a.save('E:\\android\\imgVerificaton' + '\\zengqiang.jpg')
        # a = ImageEnhance.Sharpness(a).enhance(1)  # 图像锐度增强
        # a = ImageEnhance.ConimgVerificatontrast(a).enhance(1)  # 图像对比度
        imgL = a.convert('L')      # 转化为灰度图像
        imgL.save('E:\\android\\imgVerificaton' + '\\indent_web.jpg')
        threshold = 140            # 噪声去除掉。。#阈值为什么是140呢？试出来的，或者参考直方图。
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        out =imgL.point(table, '1')
        out.save('E:\\android\\' + '\\indentL_web.jpg')
        # img = Image.open('E:\\android\\imgVerificaton\\indentL_web.jpg')
        # img.show()
        text = pytesseract.image_to_string(out)
        print "#####################"
        print text
        print "#####################"
        # strCommand = 'tesseract.exe ' + 'E:\\android\\imgVerificaton' + '\\indentL_web.jpg ' + 'E:\\android\\imgVerificaton' + '\\indet_web.txt'
        # print strCommand
        # os.system(strCommand)
        # rfindet = open('E:\\android\\imgVerificaton' + '\\indet_web.txt.txt', 'r')
        # strIndet = rfindet.readline()
        # print strIndet
        return text

    def capture(self, what):  # waht是webelement    capture:捕获
        tmp = 'E:/android/imgVerificaton'
        begin = what.location
        size = what.size
        start_x = begin['x']
        start_y = begin['y']
        end_x = start_x + size['width']
        end_y = start_y + size['height']
        name = str(start_x) + '_' + str(start_y) + '_' + str(end_x) + '_' + str(end_y)
        box = (start_x, start_y, end_x, end_y)
        self.driver.get_screenshot_as_file(tmp + '/' + 'full_screen.png')
        image = Image.open(tmp + '/' + 'full_screen.png')  # tmp是临时文件夹
        newimage = image.crop(box)
        newimage.save(tmp + '/' + name + '.png')
        os.popen('rm %s/full_screen.png' % tmp)
        a = tmp + '/' + name + '.png'
        imIndentigy = a.convert('L')      #转化为灰度图像
        imIndentigy.save('E:\\android\\imgVerificaton' + '\\indentSave.jpg')
        threshold = 140            # 噪声去除掉。。#阈值为什么是140呢？试出来的，或者参考直方图。
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        out =imIndentigy.point(table, '1')
        out.save('E:\\android\\imgVerificaton' + '\\indentSave1.jpg')
        strCommand = 'tesseract.exe ' + 'E:\\android\\imgVerificaton' + '\\indentSave1.jpg ' + 'E:\\android\\imgVerificaton' + '\\indetSave.txt'
        print strCommand
        os.system(strCommand)
        rfindet = open('E:\\android\\imgVerificaton' + '\\indetSave.txt.txt', 'r')
        strIndet = rfindet.readline()
        return strIndet

    # 图像对比 image1截取图像 image2本地图像
    def same_as(self, image1,image2, percent):
        # 对比图片，percent值设为0(值为整型、浮点型)，则100%相似时返回True，设置的值越大，相差越大
        # image1的格式不能为字符串。要为：image1 = Image.open(***)
        histogram1 = image1.histogram()
        histogram2 = image2.histogram()
        # print type(histogram1)
        # print type(histogram2)
        differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
        print '图片相似度结果：', differ
        if differ <= percent:
            return True
        else:
            return False

    def find_toast(self, message):
            # 判断toast信息
            try:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
                return True
            except:
                return False

    def is_chinese(self, uchar):
        # """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False

    def judgetext(self, x, y):
        if not (x == y):
                saveScreen.saveScreen(self.driver, x)
                print x + u'页面跳转失败'
                assert (x == y) == True
        else:
            None

    def judgetitle(self, x, t):
        if self.ckid(t):
            y = self.driver.find_element_by_id(t).get_attribute('text')
            self.judgetext(x, y)
        else:
            print '这一步断言会执行'
            # self.assertTrue(self.ckid(t))
            assert self.ckid(t) == True

    def judgeid(self, x):  # 如果没有这个元素才报错
        if self.ckid(x):
            None
        else:
            saveScreen.saveScreen(self.driver, x)
            print '****************'
            print '没有找到元素：'+x
            print '****************'
            assert self.ckid(x) == True
            # self.assertTrue(self.ckid(x))  # 这样断言可以终止程序

    def judgeid1(self, x):  # 如果有这个元素就报错
        if self.ckid(x):
            saveScreen.saveScreen(self.driver, x)
            print '****************'
            print '找到元素：' + x + "case失败"
            print '****************'
            assert self.ckid(x) == True
        else:
            None

    def judgexpath(self, r):
        if self.ckxpath(r):
            None
        else:
            saveScreen.saveScreen(self.driver, r)
            print '****************'
            print '没有找到元素：' + r
            print '****************'
            assert self.ckxpath(r) == True

    def judgexpaths(self,x,y):
        if self.ckxpath(x) or self.ckxpath(y):
            None
        else:
            print x or y + '没有找到'
            assert (self.ckxpath(x) or self.ckxpath(y)) == True

    def judgeandids(self, x, y):
        if (self.ckid(x) and self.ckid(y)):
            None
        else:
            saveScreen.saveScreen(self.driver, x+y)
            print '****************'
            print '没有找到元素：' + x + 'and' + y
            print '****************'
            assert (self.ckid(x) and self.ckid(y)) == True
            # self.assertTrue(self.ckid(x))  # 这样断言可以终止程序

    def judgeorids(self, x, y):
        if (self.ckid(x) or self.ckid(y)):
            None
        else:
            saveScreen.saveScreen(self.driver, x+y)
            print '****************'
            print '没有找到元素：' + x + 'or' + y
            print '****************'
            assert (self.ckid(x) or self.ckid(y)) == True
            # self.assertTrue(self.ckid(x))  # 这样断言可以终止程序

    def judgethreeorids(self, x, y, z):
        if (self.ckid(x) or self.ckid(y) or self.ckid(z)):
            return True
        else:
            saveScreen.saveScreen(self.driver, x + y + z)
            print '****************'
            print '没有找到元素：' + x + 'or' + y + 'or'+ '自动定位成功。。。'
            print '****************'
            return False
            # assert (self.ckid(x) or self.ckid(y) or self.ckid(z)) == True

    def judgename(self, x):
        if self.ckname(x):
            None
        else:
            saveScreen.saveScreen(self.driver, x)
            print '****************'
            print '没有找到元素：' + x
            print '****************'
            assert (self.ckname(x)) == True

    def judgename_no(self, x):
        if self.ckname(x):
            saveScreen.saveScreen(self.driver, x)
            print '****************'
            print '找到元素：' + x + "跳转失败"
            print '****************'
            assert (self.ckname(x)) == True
        else:
            None

    def judgename1(self, x):
        if (self.ckname(x)):
            print '默认首付比例50%'
        else:
            saveScreen.saveScreen(self.driver, x)
            print '****************'
            print '首付比例没有默认50%：' + x
            print '****************'
            assert (self.ckname(x)) == True

    def judgeandnames(self, x, y):
        if (self.ckname(x) and self.ckname(y)):
            None
        else:
            saveScreen.saveScreen(self.driver, x + y)
            print '****************'
            print '没有找到元素：' + x + 'and' + y
            print '****************'
            assert (self.ckname(x) and self.ckname(y)) == True

    def judgeornames(self, x, y):
        if not (self.ckname(x) or self.ckname(y)):
            None
        else:
            saveScreen.saveScreen(self.driver, x + y)
            print '****************'
            print '没有找到元素：' + x + 'or' + y
            print '****************'
            assert (self.ckname(x) or self.ckname(y)) == True

    def judgeorthreenames(self, x, y, z):
        if (self.ckname(x) or self.ckname(y) or self.ckname(z)):
            None
        else:
            saveScreen.saveScreen(self.driver, x + y + z)
            print '****************'
            print '没有找到元素：' + x + 'or' + y + 'or' + z
            print '****************'
            assert (self.ckname(x) or self.ckname(y) or self.ckname(z)) == True

    def judgeandthreenames(self, x, y, z):
        if (self.ckname(x) and self.ckname(y) and self.ckname(z)):
            None
        else:
            saveScreen.saveScreen(self.driver, x + y + z)
            print '****************'
            print '没有找到元素：' + x + 'and' + y + 'and' + z
            print '****************'
            assert (self.ckname(x) and self.ckname(y) and self.ckname(z)) == True

    def judgefname(self, x):
        if (self.ckname(x)):
            None
        else:
            saveScreen.saveScreen(self.driver, x)
            print '****************'
            print '没有找到元素：' + x
            print '****************'
            assert (self.ckname(x)) == False

    def judgeclass(self, x): # 通过class名字找元素
        if (self.ckclass(x)):
            None
        else:
            saveScreen.saveScreen(self.driver, x)
            print '****************'
            print '没有找到元素：' + x
            print '****************'
            assert (self.ckclass(x)) == True

    def waitById(self, y):  # 显性等待
        try:
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_id(y))
        except:
            print '没有找到：' + y

    def wait_invisible(self):  # 隐性等待
        self.driver.implicitly_wait(15)

    def compare(self, a, b):  # 对比
        if a == b:
            return True
        else:
            return False

    def compare1(self, a, b):  # 对比
        if a == b:
            pass
        else:
            saveScreen.saveScreen(self.driver, a)
            assert True == False

    # ------------H5定位元素
    def findH5Id(self,r):
        return self.driver.find_element_by_id(r)

    def printH5(self):
        a = self.driver.contexts
        print a[1]
        return a[1]

    def switch_H5(self,r):  # 能够确定name是哪个就用这个
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT,{'name':r})  # 你的H5的content:WEBVIEW_com.gomejr.myf2

    def switch_app(self,r,s):  # 不能确定name是哪个就用这个判断
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT,{'name':r})  # Native_App

    def screenSize(self):  # 获取屏幕大小
        a = self.driver.get_window_size()
        return a  # {u'width':1080,u'height':1920}

    def readContext(self, r):  # 获取控件的内容
        a = self.driver.find_element_by_id(r).get_attribute('text')
        # print a
        return a

    def readBoundsById(self, r):  # 获取控件坐标
        a = self.driver.find_element_by_id(r)
        startx = int(a.location.get('x'))
        starty = int(a.location.get('y'))
        width = int(a.size.get('width'))
        height = int(a.size.get('height'))
        # print a
        return startx, starty, width, height

    def readBoundsByClass(self, r):  # 获取控件坐标
        a = self.driver.find_element_by_class_name(r)
        startx = int(a.location.get('x'))
        starty = int(a.location.get('y'))
        width = int(a.size.get('width'))
        height = int(a.size.get('height'))
        endx = startx + width
        endy = starty + height
        centrex = (startx + endx) / 2
        centrey = (starty + endy) / 2
        # print a
        return startx, starty, width, height, endx, endy, centrex, centrey
    # get_attribute
    # name(返回 content-desc 或 text)
    # text(返回 text)
    # className(返回 class，只有 API=>18 才能支持)
    # resourceId(返回 resource-id，只有 API=>18 才能支持)
    # bounds（可通过get_position来获取其中部分内容）
    # 获取元素的坐标
    '''
        # 选择相册-相对坐标
            x0 = 450.0/1080 # 相对x
            y0 = 900.0/1920 # 相对y
            print x0
            print y0
            z = ct.screenSize()
            x = x0 * z['width']
            y = y0 * z['height']
            ct.screenswipe(x,y,x,y,1000) # 选择图像
            ct.finduname('确定').click()  # 点确定
        '''
    '''
     def relative_By_Position(self,x1,y1,x2,y2): #
            a0 = x1 / y1  #
            b0 = x1 / y1  #
            b1 = x2 / y2  #
            print a0
            print b0
            print b1
            z = param.ock.screenSize()
            x = x0 * z['width']
            y2 = y0 * z['height']
            y3 = y1 * z['height']
            param.ock.screenswipe(x, y2, x, y3, 1000)  # 选择选项
    '''

    def screenswipe(self, e, f, g, h, i):
        return self.driver.swipe(start_x=e, start_y=f, end_x=g, end_y=h, duration=i)

    def screenSlide_by_zuobiao(self, x1, y1, x2, y2, x, y):
        # （x1,y1）滑动的起始位置，（x2,y2）滑动的结束位置，（x,y）屏幕的大小，数值要为浮点数比如：2.0
        # 600.0, 1500.0, 600.0, 900.0, 1080.0, 1920.0
        # 600.0, 1500.0, 600.0, 900.0, 1440.0, 2560.0
        a1 = x1/x  # (a1,b1)是起始位置的相对坐标，（a2,b2）是结束位置的相对坐标
        b1 = y1/y
        a2 = x2/x
        b2 = y2/y
        z = self.screenSize()  # 获取当前屏幕的大小
        # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        # print "当前屏幕大小：", z
        # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        x1 = a1*z['width']
        y1 = b1*z['height']
        x2 = a2*z['width']
        y2 = b2*z['height']
        print x1, y1, x2, y2
        time.sleep(2)
        self.screenswipe(x1, y1, x2, y2, 1000)  # 划屏之前先sleep(2)一段时间

    def mysql_connect(self, localhost, user, password, db, sql):  # 连接数据库
        conn = MySQLdb.connect(host=localhost, user=user, passwd=password, db=db, charset='utf8')
        cursor = conn.cursor()  # 鼠标游标
        cursor.execute(sql)  # 执行sql语句  select等sql语句
        # cursor.scroll(0, mode='absolute')
        time.sleep(3)
        try:
            b = cursor.fetchone()[0]  # 读取列表里第一个
        except Exception as e:
            print u"错误信息：", e
            assert True is False
        print b
        return b

    def mysql_connect01(self, localhost, user, password, db, sql):  # 连接数据库，只执行sql语句不需要返回值
        conn = MySQLdb.connect(host=localhost, user=user, passwd=password, db=db, charset='utf8')
        cursor = conn.cursor()  # 鼠标游标
        cursor.execute(sql)  # 执行sql语句  update等sql语句
        conn.commit()  # 执行完之后commit

    def mysql_connect_code(self):  # 遇到需要验证码的地方直接拷贝过去用
        sql = "SELECT content FROM `T_SMS_SEND_TASK` WHERE dest_mobile = '18211078897' ORDER BY create_time DESC;"
        yzm_text = self.st.mysql_connect("10.143.117.21", "sms", "A5ELDU2r", "sms", sql)
        yzm = self.st.read_yanzhengma(yzm_text)
        self.st.finduid("et_pwd").send_keys(yzm)

    def read_yanzhengma(self, r):  # 读取前6位数字（正则表达式）
        a = re.findall(r"\d", r)  # 读取字符串中的数字---生成列表
        b = ''.join(a)  # 列表变成一串数字
        c = b[0]+b[1]+b[2]+b[3]+b[4]+b[5]
        print c
        return c

    def read_num(self, r):  # 读取文本中数字，带小数点  正则表达式
        a = re.findall(("\d+\.*\d*"), r)
        print "正则之后的结果", a
        return a

    # everMonthPay = round(everMonthPay, 2)  保留两位小数
    def read_num_01(self, r):  # 读取纯数字
        a = re.findall("\d+", r)
        print a
        return a

    def yanzhengma(self):
        cursor = MySQLdb.connect('10.143.117.24', 'myfang_sit', 'HrP2Cfxr', 'myfang_sit', \
                 "SELECT vcode FROM t_sms_verifycode WHERE telephone = 15233129197 ORDER BY sms_time DESC")
        cursor.scroll(0, mode='absolute')
        a = cursor.fetchone()
        smscode = a[0]
        return smscode

    def quanxian(self):  # 允许手机权限
        for i in range(10):
            if self.ckname("允许"):
                self.finduname("允许").click()  # 点掉手机权限
            else:
                break
    """
    def log_in(self, user, pwd):  # 登录
        if self.ckname(loginout.lg_denglu_name):  # 登录
            self.judgename(loginout.lg_denglu_name)  # 登录
            self.finduids(loginout.lg_phoneinput_id)[0].click()  # 手机号
            element = self.finduids(loginout.lg_phoneinput_id)[0]
            self.clear_keycode(element)
            self.finduids(loginout.lg_phoneinput_id)[0].send_keys(user)
            time.sleep(2)
            self.finduids(loginout.lg_phoneinput_id)[1].click()
            self.finduids(loginout.lg_phoneinput_id)[1].send_keys(pwd)
            self.finduname(loginout.lg_denglu_name).click()
        else:
            self.judgename(homepage.hp_tab04_name)
            self.finduname(homepage.hp_tab04_name).click()
            # text = self.finduid("tv_phone").text
            # print text
            # print user
            if self.ckname(mycenter.mc_pleaselogin_name):
                self.finduname(mycenter.mc_pleaselogin_name).click()
                self.judgename(loginout.lg_denglu_name)  # 登录
                self.finduids(loginout.lg_phoneinput_id)[0].click()  # 手机号
                element = self.finduids(loginout.lg_phoneinput_id)[0]
                self.clear_keycode(element)
                self.finduids(loginout.lg_phoneinput_id)[0].send_keys(user)
                time.sleep(2)
                self.finduids(loginout.lg_phoneinput_id)[1].click()
                self.finduids(loginout.lg_phoneinput_id)[1].send_keys(pwd)
                self.finduname(loginout.lg_denglu_name).click()
            elif self.finduid("tv_phone").text == "182****8893" and user == "18211078893":
                pass
            else:
                self.judgeid(mycenter.mc_setting_id)
                self.finduid(mycenter.mc_setting_id).click()
                self.finduid(mycenter.mc_logout_id).click()
                self.finduid(mycenter.mc_yeslogout_id).click()
                self.judgename(loginout.lg_denglu_name)  # 停留在登录界面
                self.judgename(loginout.lg_denglu_name)  # 登录
                self.finduids(loginout.lg_phoneinput_id)[0].click()  # 手机号
                element = self.finduids(loginout.lg_phoneinput_id)[0]
                self.clear_keycode(element)
                self.finduids(loginout.lg_phoneinput_id)[0].send_keys(user)
                time.sleep(2)
                self.finduids(loginout.lg_phoneinput_id)[1].click()
                self.finduids(loginout.lg_phoneinput_id)[1].send_keys(pwd)
                self.finduname(loginout.lg_denglu_name).click()
        # self.judgename(loginout.lg_denglu_name)  # 登录
        # self.finduids(loginout.lg_phoneinput_id)[0].click()  # 手机号
        # element = self.finduids(loginout.lg_phoneinput_id)[0]
        # self.clear_keycode(element)
        # self.finduids(loginout.lg_phoneinput_id)[0].send_keys(user)
        # time.sleep(2)
        # self.finduids(loginout.lg_phoneinput_id)[1].click()
        # self.finduids(loginout.lg_phoneinput_id)[1].send_keys(pwd)
        # self.finduname(loginout.lg_denglu_name).click()
        self.finduname(homepage.hp_tab01_name).click()  # 点击产品，登录成功后点击到首页
        self.judgename(homepage.hp_introduce_name)  # 判断停留在首页

    def log_out(self):  # 退出登录
        self.finduname(homepage.hp_tab04_name).click()
        if self.ckname(mycenter.mc_pleaselogin_name):
            pass
        else:
            self.judgeid(mycenter.mc_setting_id)
            self.finduid(mycenter.mc_setting_id).click()
            self.finduid(mycenter.mc_logout_id).click()
            self.finduid(mycenter.mc_yeslogout_id).click()
            self.judgename(loginout.lg_denglu_name)  # 停留在登录界面
            self.finduid(loginout.lg_back_id).click()
        self.finduname(homepage.hp_tab01_name).click()  # 停留在首页
        self.judgename(homepage.hp_introduce_name)  # 判断停留在首页

    def log_in_xiaoguan(self, user, pwd):  # 销管登录
        self.judgeclass("android.widget.EditText")
        element = self.findsclass("android.widget.EditText")[0]
        self.clear_keycode(element)
        self.findsclass("android.widget.EditText")[0].send_keys(user)
        self.findsclass("android.widget.EditText")[1].click()
        if self.ckid("iv_clear"):
            self.finduid("iv_clear").click()
        self.findsclass("android.widget.EditText")[1].send_keys(pwd)
        self.finduname("登 录").click()
        self.judgename("打卡")  # 判断登录成功
    """

    # 切换不同的app,就是切换Activity
    def wait_activity(self, activity, timeout, interval=1):

        """
        Wait for an activity: block until target activity presents
            or time out.

            This is an Android-only method.

             :Agrs:
            - activity - target activity
              - timeout - max wait time, in seconds
             - interval - sleep interval between retries, in seconds
        """

        try:

            WebDriverWait(self, timeout, interval).until(lambda d: d.current_activity == activity)
            return True

        except:
            return False

    # '''
    """ 封装post方法 """

    # def _post(self, data=None, json=None, files=None, **kwargs):
        # testData = None
        # if not data is None:
        #     testData = data
        # if not json is None:
        #     testData = json
        # # # /value格式
        # if '{' in self.url:
        #     paramsRe = re.compile("\{(.+?)\}")  # 正则表达式
        #     paramsList = paramsRe.findall(self.url)  # 找到url里所以需要替换的字段
        #     for par in paramsList:
        #         parH = '{' + par + '}'
        #         parT = testData[par]
        #         self.url = self.url.replace(parH, parT)
        #         del testData[par]
        #     if testData == {}:
        #         data = None
        #     # print '最终请求的data：',testData
        #     print '最终请求的url为：', self.url

        # logs().info(
        #     '[{0}] url:{1}'
        #     '\n请求方式:{2}'
        #     '\ndata参数:{3}  data数据类型:{4}'
        #     '\njson参数:{5} json参数数据类型:{6}'
        #     '\nheaders参数:{7}'
        #     '\ncookies参数:{8}'
        #     '\n其他参数:{9}'.format(
        #         threading.currentThread().getName(), self.url, 'POST', data, type(data),
        #         json, type(json), self.headers, self.cookies, kwargs))
    def _post(self, url, data=None, json=None, files=None, **kwargs):
        import requests
        try:
            resp = requests.post(url, data, json, files=files, headers=self.headers, cookies=self.cookies, **kwargs)
            return resp
        except Exception as e:
            # logs().error(e)
            raise e

    def one():








        if requestMethod.lower() == 'post':
            pic_path = os.path.join(ProjectFileDir(PROJECT), caseData['picture'])
            del caseData['picture']
            m = MultipartEncoder(
                fields={
                    'loanApplySerialNo': caseData['loanApplySerialNo'],
                    'type': caseData['type'],
                    'picture': ('006.jpg', open(pic_path, 'rb'), 'image/jpeg')
                }
            )
            content_type = {
                'Authorization': token,
                'Content-Type': m.content_type,
            }
            http.set_headers(**content_type)
            response = http.post(params=m)
        # '''


















