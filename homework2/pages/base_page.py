import pytest
from retry import retry
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.basic_locators import BasePageLocators


class BasePage(object):

    locators = BasePageLocators()
    # url = "https://target-sandbox.my.com/"

    def __init__(self, driver):
        self.driver = driver

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        """ Фикстура драйвера """
        self.driver = driver

    def wait(self, timeout=None) -> WebDriverWait:
        if timeout is None:
            timeout = 15
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def log_out(self) -> bool:
        """ метод выхода с аккаунта """
        try:
            if self.find(self.locators.MAIN_CONTENT).is_displayed():
                elem_1 = self.find(self.locators.MAIL_LOCATOR)
                self.click_element(elem_1)
                elem_exit = self.find(self.locators.EXIT_BUTTON)
                self.click_element(elem_exit)
        except NoSuchElementException:
            return False

        return True

    def page_transition(self, page, locator) -> WebElement:
        """ Метод перехода на страницы """
        element_page = self.find(page)
        element_page.click()
        page_locator = self.find(locator)

        return page_locator

    @retry(WebDriverException, tries=10, delay=0.5)
    def click_element(self, element: WebElement):
        if element.is_displayed():
            element.click()
