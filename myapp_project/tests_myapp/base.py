import os

import allure
import pytest

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reg_page import RegPage


class BaseCase:
    driver = None
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, logger, config):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = BasePage(driver=driver)
        self.login_page: LoginPage = LoginPage(driver=driver)
        self.reg_page: RegPage = RegPage(driver=driver)
        self.main_page: MainPage = MainPage(driver=driver)

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            self.driver.save_screenshot(filename=screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)
