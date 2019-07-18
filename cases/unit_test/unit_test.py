"""
------------------------------------
@Time : 2019/7/18 10:23
@Auth : linux超
@File : unit_test.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import unittest
from selenium import webdriver

from common.RecordLog import logger
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.LoanPage import LoanPage


class MyUnitTest(unittest.TestCase):

    driver = None

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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logger.info("关闭浏览器")


if __name__ == '__main__':
    unittest.main()
