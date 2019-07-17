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
from selenium import webdriver
import inspect

from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.LoanPage import LoanPage
from datas.InvestDatas import InvestData
from libs.ddt import ddt, data
from common.RecordLog import logger
from common.ParseExcel import do_excel


@ddt
class TestLogin(unittest.TestCase):
    """登录测试用例"""

    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = webdriver.Firefox()
            cls.driver.maximize_window()
        except Exception as e:
            logger.error('打开浏览器失败:{}', format(e))
        else:
            logger.info("打开浏览器:{}".format(cls.driver.name))
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.loan_page = LoanPage(cls.driver)

    def setUp(self):
        self.login_page.open_url()
        self.login_page.login('18684720553 ', 'python')
        self.home_page.click_knock_invest_button()

    @data(*InvestData.invest_amount_singular)
    def test_amount_singular(self, value):
        """测试投资金额为大于0的单数"""
        self.loan_page.invest(value['amount'])
        actual = self.loan_page.get_error_info
        self.assertEqual(value['expect'], actual)

    @data(*InvestData.invest_amount_error)
    def test_amount_error(self, value):
        self.loan_page.invest(value['amount'])
        actual = self.loan_page.get_error_alert
        self.assertEqual(value['expect'], actual)

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        logger.info("关闭浏览器")


if __name__ == '__main__':
    unittest.main()
