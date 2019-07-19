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
import inspect

# from datas.LoginDatas import LoginData
from libs.ddt import ddt, data
from common.record_log import logger
from common.parse_excel import do_excel
from cases.unit_test.unit_test import MyUnitTest


@ddt
class TestLogin(MyUnitTest):
    """登录测试用例"""

    login_success_data = do_excel('TestLoginSuccess')
    login_format_data = do_excel('TestFormatLoginFail')
    login_account_error_data = do_excel('TestAccountLoginFail')

    def setUp(self):
        self.login_page.open_url()

    # @data(*LoginData.login_success_data)
    @data(*login_success_data)
    def test_login_success(self, value):
        self.login_page.login(value['user'], value['pwd'])
        actual = self.login_page.get_login_success_info
        try:
            do_excel.write_cell('TestLoginSuccess',
                                value['data_id'] + 1,
                                5,
                                actual)
            self.assertEqual(value['expect'], actual, msg='断言失败')
        except AssertionError as e:
            logger.error("测试{}失败:{}".format(inspect.stack()[0][3], e))
            do_excel.write_cell('TestLoginSuccess',
                                value['data_id'] + 1,
                                6,
                                'fail',
                                color='red')
            self.login_page.save_screen_shot('error')
            raise e
        else:
            logger.info("测试{}通过".format(inspect.stack()[0][3]))
            do_excel.write_cell('TestLoginSuccess',
                                value['data_id'] + 1,
                                6,
                                'pass',
                                color='green')

    # @data(*LoginData.login_format_data)
    @data(*login_format_data)
    def test_login_format_error(self, value):
        self.login_page.login(value['user'], value['pwd'])
        actual = self.login_page.get_phone_pwd_format_info
        try:
            do_excel.write_cell('TestFormatLoginFail',
                                value['data_id'] + 1,
                                5,
                                actual)
            self.assertEqual(value['expect'], actual, msg='断言失败')
        except AssertionError as e:
            logger.error("测试{}失败:{}".format(inspect.stack()[0][3], e))
            do_excel.write_cell('TestFormatLoginFail',
                                value['data_id'] + 1,
                                6,
                                'fail',
                                color='red')
            self.login_page.save_screen_shot('error')
            raise e
        else:
            logger.info("测试{}通过".format(inspect.stack()[0][3]))
            do_excel.write_cell('TestFormatLoginFail',
                                value['data_id'] + 1,
                                6,
                                'pass',
                                color='green')

    # @data(*LoginData.login_account_error_data)
    @data(*login_account_error_data)
    def test_login_account_error(self, value):
        self.login_page.login(value['user'], value['pwd'])
        actual = self.login_page.get_phone_pwd_error_info
        try:
            do_excel.write_cell('TestAccountLoginFail',
                                value['data_id'] + 1,
                                5,
                                actual)
            self.assertEqual(value['expect'], actual, msg='断言失败')
        except AssertionError as e:
            logger.error("测试{}失败:{}".format(inspect.stack()[0][3], e))
            do_excel.write_cell('TestAccountLoginFail',
                                value['data_id'] + 1,
                                6,
                                'fail',
                                color='red')
            self.login_page.save_screen_shot('error')
            raise e
        else:
            logger.info("测试{}通过".format(inspect.stack()[0][3]))
            do_excel.write_cell('TestAccountLoginFail',
                                value['data_id'] + 1,
                                6,
                                'pass',
                                color='green')

    def tearDown(self):
        self.driver.delete_all_cookies()


if __name__ == '__main__':
    unittest.main()
