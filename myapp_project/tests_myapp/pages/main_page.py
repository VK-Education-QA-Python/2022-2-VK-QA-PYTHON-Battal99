from typing import Tuple

import allure
from selenium.webdriver.common.action_chains import ActionChains

from locators.myapp_locators import MainPageLocators
from pages.login_page import LoginPage
from settings import APP_HOST, APP_PORT


class MainPage(LoginPage):
    main_page_url = f"http://{APP_HOST}:{APP_PORT}/welcome/"
    url_logout = f"http://{APP_HOST}:{APP_PORT}/logout"
    main_page_locators = MainPageLocators()

    @allure.step("logout method")
    def logout(self):
        logout_button = self.find(self.main_page_locators.LOGOUT)
        logout_button.click()

    @allure.step("open links method")
    @allure.description("open links in main page headers")
    def open_links(self, main_locator: Tuple[str, str], link_locator: Tuple[str, str]):
        home_locator = self.find(main_locator)
        ActionChains(self.driver).move_to_element(home_locator).perform()
        self.find(link_locator).click()
