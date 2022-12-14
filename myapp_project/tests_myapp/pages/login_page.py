import allure

from pages.base_page import BasePage
from settings import APP_HOST, APP_PORT


class LoginPage(BasePage):
    url = f"http://{APP_HOST}:{APP_PORT}/login"

    @allure.step("login in app")
    def login(self, login, password):
        username = self.find(self.locator.INPUT_USERNAME)
        username.send_keys(login)
        self.find(self.locator.INPUT_PASSWORD).send_keys(password)

        self.find(self.locator.BUTTON_LOGIN).click()
