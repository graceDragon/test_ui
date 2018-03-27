# coding:utf-8
"""
财务处理部分
"""

# 财务入口
finance_enter = '//span[contains(text(),"财务")]'
# finance_orders_manage = '//a[@class="orders" and contains(text(),"订单管理")]'
finance_orders_manage = '/html/body/div[1]/ul/li[4]/ul/li[1]/a'
# finance_orders_manage_btn = '//a[@class="menu_3 cw_orders_lists" and contains(text(),"订单管理")]'
finance_orders_manage_btn = '/html/body/div[1]/ul/li[4]/ul/li[1]/ul/li[1]/a'
finance_orders_manage_house_id = '/html/body/div/div[1]/form/div[2]/div[1]/div/input'
# finance_orders_manage_house_id = '//input[@name="house_no"]'
finance_orders_manage_chaxun = '//input[@value="查询"]'
finance_orders_manage_iframe_id = 'fRight'
finance_orders_manage_iframe_url = 'http://t.efang100.cc/cw_orders_lists'
# driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
finance_orders_manage_confirm = '//a[contains(text(),"[确认]")]'
finance_orders_manage_confirm_1 = '//input[@value="确认"]'
finance_orders_manage_confirm_2 = '//a[contains(text(),"确认")]'

finance_orders_manage_kaipiao = '//a[contains(text(),"开票")]'
finance_orders_manage_submit = '//input[@value="提交"]'





