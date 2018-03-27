# coding:utf-8

import unittest
from public import driver
from test_data import data
from zhiyu_app.page_action import page_action_login, page_action_house_status
from zhiyu_app.page_action import page_action_home


class HouseJizhongSignFlow(unittest.TestCase):
    def setUp(self):
        self.driver = driver.Driver().driver_app()
        self.plogin = page_action_login.LogIn(self.driver)
        self.phome = page_action_home.HomePage(self.driver)
        self.phs = page_action_house_status.HouseStatus(self.driver)

    def test_house_jizhong_sign_flow(self):
        self.plogin.login_judge(data.user, data.pwd)
        self.phome.click_tab_house_status()
        self.phs.house_status_flow(data.community_name, data.loudong_name, data.user, rent_time=6, method='季付',
                                   day=1, fee1='房屋租金', zhouqi1='周期费用',  fee2='物业费', zhouqi2='一次性',
                                   fee3='燃气费', zhouqi3='抄表', addmoney1='1000', addmoney2='100', addmoney3='10',
                                   biaodi='22', furniture1='床', model1='1.2米床', num1=3, furniture2='空调',
                                   model2='奥克斯空调', num2=2, mendian='江大门店', saleman='张爱东',
                                   no=data.house_id, fapiao='No')


if __name__ == '__main__':
    unittest.main()



