"""
------------------------------------
@Time : 2019/7/13 19:55
@Auth : linux超
@File : HomePage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from base.base import Base


class HomePage(Base):

    login_btn = ('xpath', '// div[@class ="center"]//a[text()="登录"]')

    def click_login(self):
        self.click(*self.login_btn)


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Firefox()
    home = HomePage(driver)
    driver.get('http://120.78.128.25:8765/')
    home.click_login()
