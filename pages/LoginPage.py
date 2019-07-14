"""
------------------------------------
@Time : 2019/7/13 19:55
@Auth : linux超
@File : LoginPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from base.base import Base


class LoginPage(Base):

    phone_input = ('xpath', '//input[@name = "phone"]')
    password_input = ('xpath', '// input[@name = "password"]')
    v_code = ('xpath', '//input[@name = "vcode"]')
    v_code_img = ('xpath', '//img[@class ="verify-img"]')
    login_button = ('xpath', '//button[text()="登录"]')

    def login(self, phone: str, password: str):
        self.input_user(phone)
        self.input_password(password)
        self.click_login()

    def input_user(self, phone: str):
        self.send_keys(*self.phone_input, phone)

    def input_password(self, password: str):
        self.send_keys(*self.password_input, password)

    def click_login(self):
        self.click(*self.login_button)

    def assert_error_info(self):
        pass


if __name__ == '__main__':
    from selenium import webdriver
    from pages.HomePage import HomePage
    driver = webdriver.Firefox()
    home = HomePage(driver)
    login = LoginPage(driver)
    driver.get('http://120.78.128.25:8765/')
    home.click_login()
    login.login('13691579841', 'python')
