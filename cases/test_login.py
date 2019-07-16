"""
------------------------------------
@Time : 2019/7/13 20:01
@Auth : linux超
@File : test_login.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import unittest
from selenium import webdriver

from pages.LoginPage import LoginPage
from datas.LoginDatas import LoginData
from libs.ddt import ddt, data


@ddt
class TestLogin(unittest.TestCase):
    """登录测试用例"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.login = LoginPage(cls.driver)

    def setUp(self):
        self.login.open_url()

    @data(*LoginData.login_success_data)
    def test_login_success(self, value):
        self.login.login(value['user'], value['pwd'])
        actual = self.login.get_login_success_info()
        self.assertEqual(value['expect'], actual, msg='断言失败')

    @data(*LoginData.login_format_data)
    def test_login_format_error(self, value):
        self.login.login(value['user'], value['pwd'])
        actual = self.login.get_phone_pwd_format_info()
        self.assertEqual(value['expect'], actual, msg='断言失败')

    @data(*LoginData.login_account_error_data)
    def test_login_account_error(self, value):
        self.login.login(value['user'], value['pwd'])
        actual = self.login.get_phone_pwd_error_info()
        self.assertEqual(value['expect'], actual, msg='断言失败')

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
