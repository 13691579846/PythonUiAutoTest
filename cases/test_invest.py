"""
------------------------------------
@Time : 2019/7/13 20:01
@Auth : linux超
@File : test_invest.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import unittest
import inspect

from cases.unit_test.unit_test import MyUnitTest
from datas.invest_datas import InvestData
from libs.ddt import ddt, data
from common.record_log import logger


# TODO: perfect success test cases
@ddt
class TestInvest(MyUnitTest):
    """投资用例"""
    test_data = InvestData

    def setUp(self):
        self.login_page.open_url()
        self.login_page.login(self.test_data.user_password['phone'],
                              self.test_data.user_password['pwd'])
        self.home_page.click_knock_invest_button()

    @data(*test_data.invest_amount_singular)
    def test_amount_singular(self, value):
        self.loan_page.invest(value['amount'])
        actual = self.loan_page.get_error_info
        try:
            self.assertEqual(value['expect'], actual)
        except AssertionError as e:
            logger.error("投资用例{}测试失败{}".format(inspect.stack()[0][1], e))
            raise e
        else:
            logger.info("投资用例{}测试通过".format(inspect.stack()[0][1]))

    @data(*test_data.invest_amount_error)
    def test_amount_error(self, value):
        self.loan_page.invest(value['amount'])
        actual = self.loan_page.get_error_alert
        try:
            self.assertEqual(value['expect'], actual)
        except AssertionError as e:
            logger.error("投资用例{}测试失败{}".format(inspect.stack()[0][1], e))
            raise e
        else:
            logger.info("投资用例{}测试通过".format(inspect.stack()[0][1]))

    def tearDown(self):
        self.driver.delete_all_cookies()


if __name__ == '__main__':
    unittest.main()
