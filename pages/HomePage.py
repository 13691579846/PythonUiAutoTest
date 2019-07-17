"""
------------------------------------
@Time : 2019/7/17 22:14
@Auth : linux超
@File : HomePage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from base.base import Base
from common.ParseConfig import ParseConfig
from config.config import LOCATOR_PATH


class HomePage(Base):
    """首页"""
    config = ParseConfig(LOCATOR_PATH)
    knock_invest_button = config('HomePage', 'knock_invest_button')

    @property
    def invest_button(self):
        return self.find_elements(*self.knock_invest_button)[0]

    def click_knock_invest_button(self):
        self.invest_button.click()


if __name__ == '__main__':
    pass
