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
import inspect

from pages.LoginPage import LoginPage
# from datas.LoginDatas import LoginData
from libs.ddt import ddt, data
from common.RecordLog import logger
from common.ParseExcel import do_excel


@ddt
class TestLogin(unittest.TestCase):
    """登录测试用例"""

    login_success_data = do_excel('TestLoginSucess')
    login_format_data = do_excel('TestFormatLoginFail')
    login_account_error_data = do_excel('TestAccountLoginFail')

    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = webdriver.Firefox()
            cls.driver.maximize_window()
        except Exception as e:
            logger.error('打开浏览器失败:{}', format(e))
        else:
            logger.info("打开浏览器:{}".format(cls.driver.name))
        cls.login = LoginPage(cls.driver)

    def setUp(self):
        self.login.open_url()

    # @data(*LoginData.login_success_data)
    @data(*login_success_data)
    def test_login_success(self, value):
        self.login.login(value['user'], value['pwd'])
        actual = self.login.get_login_success_info()
        try:
            self.assertEqual(value['expect'], actual, msg='断言失败')
        except AssertionError as e:
            logger.error("测试{}失败:{}".format(inspect.stack()[0][3], e))
            raise e
        else:
            logger.info("测试{}通过".format(inspect.stack()[0][3]))

    # @data(*LoginData.login_format_data)
    @data(*login_format_data)
    def test_login_format_error(self, value):
        self.login.login(value['user'], value['pwd'])
        actual = self.login.get_phone_pwd_format_info()
        try:
            self.assertEqual(value['expect'], actual, msg='断言失败')
        except AssertionError as e:
            logger.error("测试{}失败:{}".format(inspect.stack()[0][3], e))
            raise e
        else:
            logger.info("测试{}通过".format(inspect.stack()[0][3]))

    # @data(*LoginData.login_account_error_data)
    @data(*login_account_error_data)
    def test_login_account_error(self, value):
        print(value['user'], value['pwd'])
        self.login.login(value['user'], value['pwd'])
        actual = self.login.get_phone_pwd_error_info()
        try:
            self.assertEqual(value['expect'], actual, msg='断言失败')
        except AssertionError as e:
            logger.error("测试{}失败:{}".format(inspect.stack()[0][3], e))
            raise e
        else:
            logger.info("测试{}通过".format(inspect.stack()[0][3]))

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logger.info("关闭浏览器")


if __name__ == '__main__':
    unittest.main()
