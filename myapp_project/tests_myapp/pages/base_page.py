from random import choice
from string import ascii_letters, digits

import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.myapp_locators import LoginPageLocators


class BasePage:
    locator = LoginPageLocators()

    def __init__(self, driver):
        self.driver = driver

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait(self, timeout=None) -> WebDriverWait:
        if timeout is None:
            timeout = 15
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    @staticmethod
    def random_str(
            size: int = 12,
            digit: bool = False,
            is_email: bool = False) -> str:
        string = ''.join(choice(ascii_letters) for _ in range(size))
        if digit:
            string += ''.join(choice(digits) for _ in range(3))
        if is_email:
            string += '@mail.ru'
        return string
