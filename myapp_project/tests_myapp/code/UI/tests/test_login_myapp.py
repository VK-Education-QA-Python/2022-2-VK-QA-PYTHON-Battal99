import allure

from base import BaseCase
from settings import USERNAME, PASSWORD


class TestLogin(BaseCase):

    @allure.step("Login in myapp")
    @allure.issue("UI test")
    @allure.description("Test to login in app")
    def test_login(self):

        self.login_page.login(USERNAME, PASSWORD)

        assert self.login_page.find(
            self.login_page.locator.login_success_locator
        ).is_displayed()

