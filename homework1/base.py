import pytest

from homework1 import locators

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

from retry import retry


class BaseCase:
    driver: WebElement = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        """ Фикстура драйвера """
        self.driver = driver

    def find_wait(self, by: By, what: str) -> WebElement:
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((by, what)))

    @retry(NoSuchElementException, tries=10, delay=0.5)
    def find(self, by: By, what: str) -> WebElement:
        return self.driver.find_element(by, what)

    def log_in(self, login: str, password: str) -> bool:
        """ Метод входа входа в аккаунт """
        try:
            self.find_wait(*locators.QUERY_LOCATOR).click()
            element_login_input = self.find_wait(*locators.INPUT_LOGIN)
            element_login_input.send_keys(login)
            element_password_input = self.find_wait(*locators.INPUT_PASSWORD)
            element_password_input.send_keys(password)
            element_password_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            return False
        return True

    def logout(self) -> bool:
        """ метод выхода с аккаунта """
        try:
            elem_1 = self.find(*locators.MAIL_LOCATOR)
            self.click_element(elem_1)
            elem_exit = self.find(*locators.EXIT_BUTTON)
            self.click_element(elem_exit)
        except NoSuchElementException:
            return False
        return True

    def page_transition(self, page, locator) -> WebElement:
        """ Метод перехода на страницы """
        element_page = self.find_wait(*page)
        element_page.click()
        page_locator = self.find_wait(*locator)
        return page_locator

    @retry(WebDriverException, tries=10, delay=0.5)
    def click_element(self, element: WebElement):
        if element.is_displayed():
            element.click()
