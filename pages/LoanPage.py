"""
------------------------------------
@Time : 2019/7/13 20:55
@Auth : linux超
@File : UserPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from base.base import Base
from common.ParseConfig import ParseConfig
from config.config import LOCATOR_PATH


class LoanPage(Base):
    """标详情页"""
    config = ParseConfig(LOCATOR_PATH)
    amount_element = config('LoanPage', 'invest_amount')
    invest_loan_btn = config('LoanPage', 'invest_loan_btn')
    inverst_error_alert = ('xpath', '//div[@class="text-center"]')

    def invest(self, value):
        """投标"""
        self.input_amount(value)  # 输入金额
        self.click_invest_button()

    def input_amount(self, amount):
        self.send_keys(*self.amount_element, amount)

    def click_invest_button(self):
        self.click(*self.invest_loan_btn)

    @property
    def get_error_info(self):
        return self.get_element_text(*self.invest_loan_btn)

    @property
    def get_error_alert(self):
        return self.get_element_text(*self.inverst_error_alert)


if __name__ == '__main__':
    pass
