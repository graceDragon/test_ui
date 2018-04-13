# coding:utf-8

"""
公用方法封装
"""

from config.settings import BASE_PATH
import os
import time
import re
from time import sleep
from PIL import Image
import pytesseract
from selenium.webdriver.common.action_chains import ActionChains
# from appium.webdriver.mobilecommand import MobileCommand


class PublicMethod(object):

    def __init__(self, driver):
        self.d = driver

    def find_element_name(self, r):
        try:
            self.d.find_element_by_name(r)
            return True
        except Exception as e:
            # print(e)
            return False

    def find_element_id(self, r):
        try:
            self.d.find_element_by_id(r)
            return True
        except Exception as e:
            # print(e)
            return False

    def find_element_class_name(self, r):
        try:
            self.d.find_element_by_class_name(r)
            return True
        except Exception as e:
            # print(e)
            return False

    def find_element_xpath(self, r):
        try:
            self.d.find_element_by_xpath(r)
            return True
        except Exception as e:
            # print(e)
            return False

    def click_by_name(self, r):
        self.d.find_element_by_name(r).click()

    def click_by_names(self, r, i):
        self.d.find_elements_by_name(r)[i].click()

    def click_by_id(self, r):
        self.d.find_element_by_id(r).click()

    def click_by_ids(self, r, i):
        self.d.find_elements_by_id(r)[i].click()

    def click_by_class_name(self, r):
        self.d.find_element_by_class_name(r).click()

    def click_by_xpath(self, r):
        self.d.find_element_by_xpath(r).click()

    def click_element(self, r):
        if self.find_element_name(r):
            self.d.find_element_by_name(r).click()
        elif self.find_element_id(r):
            self.d.find_element_by_id(r).click()
        elif self.find_element_class_name(r):
            self.d.find_element_by_class_name(r).click()
        elif self.find_element_xpath(r):
            self.d.find_element_by_xpath(r).click()
        else:
            print '没有找到元素：', r

    def send_keys_by_name(self, r, key):
        self.d.find_element_by_name(r).send_keys(key)

    def send_keys_by_names(self, r, i, j):
        self.d.find_elements_by_name(r)[j].send_keys(i)

    def send_keys_by_id(self, r, key):
        self.d.find_element_by_id(r).send_keys(key)

    def send_keys_by_ids(self, r, i, j):
        self.d.find_elements_by_id(r)[j].click()
        self.d.find_elements_by_id(r)[j].send_keys(i)

    def send_keys_by_class_name(self, r, i):
        self.d.find_element_by_class_name(r).send_keys(i)

    def send_keys_by_xpath(self, r, i):
        self.d.find_element_by_xpath(r).send_keys(i)

    def send_keys_element(self, r, i):
        if self.find_element_name(r):
            self.d.find_element_by_name(r).send_keys(i)
        elif self.find_element_id(r):
            self.d.find_element_by_id(r).send_keys(i)
        elif self.find_element_class_name(r):
            self.d.find_element_by_class_name(r).send_keys(i)
        elif self.find_element_xpath(r):
            self.d.find_element_by_xpath(r).send_keys(i)
        else:
            print '没有找到元素：', r

    # 鼠标停留在某个元素上
    def stay_mouse_xpath(self, r):
        ele = self.d.find_element_by_xpath(r)
        ActionChains(self.d).move_to_element(ele).perform()

    # 鼠标移动
    def move_mouse(self, x, y):
        ActionChains(self.d).move_by_offset(x, y).perform()

    # 鼠标移动到坐标出并点击
    def move_mouse_click(self, x, y):
        ActionChains(self.d).move_by_offset(x, y).click().perform()
        print '鼠标移动点击完成！'

    # 鼠标右击元素
    def right_click_el_xpath(self, xpath):
        el = self.d.find_element_by_xpath(xpath)
        ActionChains(self.d).context_click(el).perform()

    # 双击元素
    def double_click_el_xpath(self, xpath):
        el = self.d.find_element_by_xpath(xpath)
        ActionChains(self.d).double_click(el).perform()

    def scrollbar_web(self, r):
        # web页面滚动条
        # r是滚动的距离 r=10000移动到最底部，r=0移动到顶部
        r = str(r)
        browser_name = self.d.name
        print '浏览器:', browser_name
        if browser_name == 'chrome':
            js = "var q=document.body.scrollTop=" + r
        else:
            js = "var q=document.documentElement.scrollTop=" + r
        print(js)
        return self.d.execute_script(js)

    def scrollbar_web_02(self):
        js = "window.scrollTo(0,0)"
        self.d.execute_script(js)
        print 'scroll2'

    def read_element_txt_by_name(self, r):
        txt = self.d.find_element_by_name(r).text
        return txt

    def read_element_txt_by_names(self, r, i):
        txt = self.d.find_elements_by_name(r)[i].text
        return txt

    def read_element_txt_by_id(self, r):
        txt = self.d.find_element_by_id(r).text
        return txt

    def read_element_txt_by_ids(self, r, i):
        txt = self.d.find_elements_by_id(r)[i].text
        return txt

    def read_element_txt_by_xpath(self, r):
        txt = self.d.find_element_by_xpath(r).text
        return txt

    def read_element_txt(self, r):
        # 读取元素的文本信息
        if self.find_element_name(r):
            txt = self.d.find_element_by_name(r).text
        elif self.find_element_id(r):
            txt = self.d.find_element_by_id(r).text
        elif self.find_element_class_name(r):
            txt = self.d.find_element_by_class_name(r).text
        elif self.find_element_xpath(r):
            txt = self.d.find_element_by_xpath(r).text
        else:
            print '没有找到元素：', r
        return txt

    def read_and_judge_element_txt_by_name(self, e, r):
        txt = self.d.find_element_by_name(e).text
        if txt == r:
            print '元素信息正确：', txt, r
            return True
        else:
            print '元素信息不不不正确：', txt, r
            self.screen_shot()
            return False

    def read_and_judge_element_txt_by_id(self, e, r):
        txt = self.d.find_element_by_id(e).text
        # unicode类型转换成str类型
        txt = txt.encode(encoding='utf-8')
        if txt == r:
            print '元素信息正确：', txt, r
            return True
        else:
            print '元素信息不不不正确：', txt, '!=', r
            self.screen_shot()
            return False

    def read_and_judge_element_txt_by_xpath(self, r, i):
        txt = self.d.find_element_by_xpath(r).text
        if txt == i:
            print '元素信息正确：', txt, i
            return True
        else:
            print '元素信息不不不正确：', txt, i
            self.screen_shot()
            return False

    def read_and_judge_element_txt(self, r, i):
        # 读取元素的文本信息,并判断是否正确
        if self.find_element_name(r):
            txt = self.d.find_element_by_name(r).text
        elif self.find_element_id(r):
            txt = self.d.find_element_by_id(r).text
        elif self.find_element_class_name(r):
            txt = self.d.find_element_by_class_name(r).text
        elif self.find_element_xpath(r):
            txt = self.d.find_element_by_xpath(r).text
        else:
            print '没有找到元素：', r
        if txt == i:
            print '元素信息正确：', txt, i
            return True
        else:
            print '元素信息不不不正确：', txt, i
            self.screen_shot()
            return False

    def assert_el_by_name(self, r):
        if self.find_element_name(r):
            pass
        else:
            self.screen_shot()
            print '*******************'
            print '没有找到元素：', r
            print '*******************'
            assert True is False

    def assert_el_by_xpath(self, r):
        if self.find_element_xpath(r):
            pass
        else:
            self.screen_shot()
            print '*******************'
            print '没有找到元素：', r
            print '*******************'
            assert True is False

    def assert_el_by_id(self, r):
        if self.find_element_id(r):
            pass
        else:
            self.screen_shot()
            print '*******************'
            print '没有找到元素：', r
            print '*******************'
            assert True is False

    def assert_element(self, r):
        # 断言元素是否存在，否则截屏
        if self.find_element_name(r):
            pass
        elif self.find_element_id(r):
            pass
        elif self.find_element_class_name(r):
            pass
        elif self.find_element_xpath(r):
            pass
        else:
            self.screen_shot()
            print '*******************'
            print '没有找到元素：', r
            print '*******************'
            assert True is False

    def screen_shot(self):
        # 按日期新建文件夹
        dir_day = time.strftime('%Y%m%d', time.localtime(time.time()))
        dir_path = os.path.join(BASE_PATH, 'reports\screen_shot', dir_day)
        if os.path.exists(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        # 截屏并以当前时间来命名图片
        time_now = self.time_now()
        pic_name = time_now + '.png'
        filename = os.path.join(BASE_PATH, 'reports\screen_shot', dir_path, pic_name)
        self.d.save_screenshot(filename)

    def time_now(self):
        # 时间格式为：20171102_151926
        time_str = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        return time_str

    def image_yzm(self, r):
        # 获取图形验证码 r:控件的名字
        if self.find_element_name(r):
            a = self.d.find_element_by_name(r)
        elif self.find_element_id(r):
            a = self.d.find_element_by_id(r)
        elif self.find_element_xpath(r):
            a = self.d.find_element_by_xpath(r)
        elif self.find_element_class_name(r):
            a = self.d.find_element_by_class_name(r)
        startx = int(a.location.get('x'))
        starty = int(a.location.get('y'))
        width = int(a.size.get('width'))
        height = int(a.size.get('height'))
        endx = startx + width
        endy = starty + height
        u'''''获取验证码
                （startx, xstarty）---------------------------------
                                  |     要截取的图片范围             |
                                  |                               |
                                  ---------------------------------- (endx, endy)
                '''
        # 截取整个屏幕
        pic_name = 'screen_shot.jpg'
        screen_img = os.path.join(BASE_PATH, 'test_data\image_screen', pic_name)
        self.d.get_screenshot_as_file(screen_img)
        img_file = Image.open(screen_img)
        sleep(2)
        box = (startx, starty, endx, endy)
        img = img_file.crop(box)
        # a = a.filter(ImageFilter.EDGE_ENHANCE)  # 边缘增强
        # a = a.filter(ImageFilter.DETAIL)  # 细节增强滤波
        # a.save('E:\\android\\imgVerificaton' + '\\zengqiang.jpg')
        # a = ImageEnhance.Sharpness(a).enhance(1)  # 图像锐度增强
        # a = ImageEnhance.ConimgVerificatontrast(a).enhance(1)  # 图像对比度
        imgL = img.convert('L')  # 转化为灰度图像
        pic_gray_name = 'pic_gray.jpg'
        pic_gray_path = os.path.join(BASE_PATH, 'test_data\image_screen', pic_gray_name)
        imgL.save(pic_gray_path)
        threshold = 140  # 噪声去除掉。。#阈值为什么是140呢？试出来的，或者参考直方图。
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        img_out = imgL.point(table, '1')
        img_out_name = 'img_out.jpg'
        img_out_path = os.path.join(BASE_PATH, 'test_data\image_screen', img_out_name)
        img_out.save(img_out_path)
        # img = Image.open(img_out_path)
        # img.show()
        text = pytesseract.image_to_string(img_out)
        # code_file_path = os.path.join(BASE_PATH, 'test_data\image_screen', 'code.txt')
        # code_file = os.open(code_file_path, 'w')
        # os.write(code_file, text)

        print '##################'
        print '读取的图形验证码：', text
        print '##################'
        return text

    def presscodes(self, m, n):
        self.d.press_keycode(m, n)

    def presscode(self, i):
        self.d.press_keycode(i)  # 84是搜索按键

    def clear_keycode(self, element):  # 模拟键盘清空输入框- 删除键 112
        element.click()
        time.sleep(2)
        self.d.press_keycode(29, 28672)  # ctrl+a 全选输入框内容
        time.sleep(2)
        self.d.press_keycode(112)  # 删除键 112

    def screenSlide_by_zuobiao(self, x1, y1, x2, y2, x, y):
        # （x1,y1）滑动的起始位置，（x2,y2）滑动的结束位置，（x,y）屏幕的大小，数值要为浮点数比如：2.0
        # 600.0, 1500.0, 600.0, 900.0, 1080.0, 1920.0
        # 600.0, 1500.0, 600.0, 900.0, 1440.0, 2560.0
        a1 = x1/x  # (a1,b1)是起始位置的相对坐标，（a2,b2）是结束位置的相对坐标
        b1 = y1/y
        a2 = x2/x
        b2 = y2/y
        z = self.d.get_window_size()  # 获取当前屏幕的大小
        # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        # print "当前屏幕大小：", z
        # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        x1 = a1*z['width']
        y1 = b1*z['height']
        x2 = a2*z['width']
        y2 = b2*z['height']
        print x1, y1, x2, y2
        time.sleep(2)  # 划屏之前先sleep(2)一段时间
        self.d.swipe(start_x=x1, start_y=y1, end_x=x2, end_y=y2, duration=2000)

    # 正则表达式-只取数字包括小数点
    def regular_num(self, r):
        num = re.findall(("\d+\.*\d*"), r)
        print '正则之后的数字：', num
        return num  # 结果是列表格式['2.45']

    # 正则表达式-只取数字包括小数点
    def regular_num_new(self, r):
        num = re.findall(("\d+\.*\d*"), r)
        num = num[0]
        num = float(num)
        print '正则之后的数字：', num
        return num  # 结果是float类型数字

    # 切换iframe
    def change_iframe(self, frame):
        self.d.switch_to.frame(frame)

    # 返回frame
    def back_iframe(self):
        self.d.switch_to.default_content()








