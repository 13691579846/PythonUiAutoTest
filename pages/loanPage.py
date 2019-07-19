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
from pages.base.base import Base
from common.parse_config import ParseConfig
from config.config import LOCATOR_PATH


class LoanPage(Base):
    """标详情页"""
    config = ParseConfig(LOCATOR_PATH)
    amount_element = config('LoanPage', 'invest_amount')  # 金额输入框
    invest_loan_btn = config('LoanPage', 'invest_loan_btn')  # 投标按钮
    invest_error_alert = ('xpath', '//div[@class="text-center"]')  # 投资失败的弹窗

    def invest(self, value):
        """投标"""
        self.logger.info('开始投标')
        self.execute_window_scroll('0', '300')
        self.input_amount(value)  # 输入金额
        self.click_invest_button()  # 确认投标

    def input_amount(self, amount):
        """输入投资金额"""
        self.logger.info('输入投资金额:{}'.format(amount))
        action = self.move_to_element_click(*self.amount_element)
        self.send_keys(*self.amount_element, amount)
        action.release().perform()

    def click_invest_button(self):
        """点击投标按钮"""
        self.logger.info("点击投资按钮")
        self.click(*self.invest_loan_btn)

    @property
    def get_error_info(self):
        """投资失败时投资按钮显示信息"""
        return self.get_element_text(*self.invest_loan_btn)

    @property
    def get_error_alert(self):
        """投资失败时弹窗信息"""
        return self.get_element_text(*self.invest_error_alert)

    @property
    def get_remain_amount(self):
        """获取剩余金额"""
        remain_amount = self.find_element(*self.amount_element).get_attribute('data-amount')
        return remain_amount


if __name__ == '__main__':
    pass
