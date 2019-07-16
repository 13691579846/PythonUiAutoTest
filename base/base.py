"""
------------------------------------
@Time : 2019/7/13 20:54
@Auth : linux超
@File : base.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (NoSuchElementException,
                                        TimeoutException,
                                        NoAlertPresentException,
                                        InvalidArgumentException)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from common.RecordLog import logger


class Base(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.base_url = 'http://120.78.128.25:8765'

    def _open(self, url=None):
        try:
            url = url or self.base_url
            self.driver.get(url)
        except InvalidArgumentException as e:
            logger.error('加载测试地址{}失败:{}'.format(url, e))
        else:
            logger.info('加载测试地址:{}'.format(url))

    def open(self, url=None):
        self._open(url)

    def find_element(self, by: str, location: str) -> WebElement:
        """
        find element by location
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: WebElement
        :Usage:
            locator = ("xpath", //*[@id="location"])
            element = driver.find_element(*locator)
        """
        try:
            by = by.lower()
            wait = WebDriverWait(self.driver, self.timeout)
            element = wait.until(lambda driver: driver.find_element(by, location))
        except (NoSuchElementException, TimeoutException) as e:
            logger.info('定位元素失败:{}'.format(e))
        else:
            return element

    def find_elements(self, by: str, location: str) -> list:
        """
        find elements with location
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: list of WebElement
        :Usage:
            locator = ("xpath", //*[@id="location"])
            elements = driver.find_elements(*locator)
        """
        try:
            by = by.lower()
            wait = WebDriverWait(self.driver, self.timeout)
            elements = wait.until(lambda driver: driver.find_elements(by, location))
        except (NoSuchElementException, TimeoutException) as e:
            logger.info('定位一组元素失败:{}'.format(e))
        else:
            return elements

    def is_element_exist(self, by: str, location: str) -> bool:
        """
        return True if element is exist else False
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: bool
        """
        self.timeout = 10
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            wait.until(ec.visibility_of_element_located((by, location)))
        except (NoSuchElementException, TimeoutException) as e:
            logger.debug('元素不存在:{}'.format(e))
            return False
        return True

    def is_alert_switch_to_alert(self):
        """
        switch to alert if alert is present
        :return: alert if alert is present else False
        """
        self.timeout = 10
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            alert = wait.until(ec.alert_is_present())
        except (TimeoutException, NoAlertPresentException) as e:
            logger.debug('alert 不存在:{}'.format(e))
            return False
        return alert

    def is_clickable(self, by: str, location: str):
        """
        return element if element is clickable else False
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return:
        """
        try:
            by = by.lower()
            wait = WebDriverWait(self.driver, self.timeout)
            element = wait.until(ec.element_to_be_clickable((by, location)))
        except (TimeoutException, NoSuchElementException) as e:
            logger.debug('元素{}不可点击:{}'.format(location, e))
            return False
        return element

    @property
    def get_alert_text(self):
        """
        get test of alert
        :return: text of alert
        """
        alert = self.is_alert_switch_to_alert()
        if alert:
            return alert.text

    def switch_to_frame(self, by: str, location: str) -> bool:
        """
        switch to iframe
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: bool
        """
        try:
            by = by.lower()
            wait = WebDriverWait(self.driver, self.timeout)
            wait.until(ec.frame_to_be_available_and_switch_to_it((by, location)))
        except (TimeoutException, NoSuchElementException) as e:
            logger.error("切换iframe失败：{}".format(e))
        else:
            return True

    def click(self, by: str, location: str):
        """
        click element
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: None
        """
        element = self.is_clickable(by, location)
        if element:
            element.click()
        else:
            logger.error('元素{}不可点击'.format(location))

    def send_keys(self, by: str, location: str, value: str) -> bool:
        """
        input the value to input box of element
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :param value: str
        :return: bool
        """
        try:
            element = self.find_element(by, location)
            element.clear()
            element.send_keys(value)
        except (NoSuchElementException, TimeoutException) as e:
            logger.error("{}输入数据{}失败:{}".format(location, value, e))
        else:
            logger.info("输入框{}输入数据{}".format(location, value))
            return True

    def get_element_text(self, by: str, location: str):
        """
        get text of element
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: str or bool
        """
        try:
            by = by.lower()
            element = self.find_element(by, location)
            value = element.text
        except (NoSuchElementException, TimeoutException) as e:
            logger.error("获取元素{}文本内容失败:{}".format(location, e))
        else:
            logger.info("获取元素文本内容:{}".format(value))
            return value

    def move_to_element(self, by: str, location: str):
        """
        move mouse to element
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: action
        """

        element = self.find_element(by, location)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        return action


if __name__ == '__main__':
    pass
