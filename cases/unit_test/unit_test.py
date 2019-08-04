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

from common.record_log import logger
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from pages.loanPage import LoanPage
from pages.memberPage import MemberPage


class MyUnitTest(unittest.TestCase):

    driver = None
    logger = logger

    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
        except Exception as e:
            cls.logger.error('打开浏览器失败:{}', format(e))
            raise e
        else:
            cls.logger.info("打开浏览器:{}".format(cls.driver.name))
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.loan_page = LoanPage(cls.driver)
        cls.member_page = MemberPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logger.info("关闭浏览器")


if __name__ == '__main__':
    unittest.main()
