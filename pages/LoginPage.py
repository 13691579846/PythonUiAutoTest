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
from common.ParseConfig import ParseConfig
from config.config import CONFIG_PATH


class LoginPage(Base):

    config = ParseConfig(CONFIG_PATH)
    url = config('TestUrl', 'url')
    phone_input = config('LoginPage', 'phone_input')  # 用户名输入框
    password_input = config('LoginPage', 'password_input')  # 密码输入框
    login_button = config('LoginPage', 'login_button')  # 登录按钮

    login_success_info = config('LoginPage', 'login_success_info')
    format_error_info = config('LoginPage', 'format_error_info')  # 帐号或密码格式错误
    phone_password_error = config('LoginPage', 'phone_password_error')  # 帐号或密码错误

    def login(self, phone: str, password: str):
        self.input_user(phone)
        self.input_password(password)
        self.click_login()

    def open_url(self):
        self.open(self.url)

    def input_user(self, phone: str):
        self.send_keys(*self.phone_input, value=phone)

    def input_password(self, password: str):
        self.send_keys(*self.password_input, value=password)

    def click_login(self):
        self.click(*self.login_button)

    def get_phone_pwd_format_info(self):
        value = self.get_element_text(*self.format_error_info)
        return value

    def get_phone_pwd_error_info(self):
        value = self.get_element_text(*self.phone_password_error)
        return value

    def get_login_success_info(self):
        value = self.get_element_text(*self.login_success_info)
        return value


if __name__ == '__main__':
    pass
