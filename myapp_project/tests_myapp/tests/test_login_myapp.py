import allure

from base import BaseCase
import pytest
from settings import USERNAME, PASSWORD, LOGIN_URL, REG_URL


class TestLogin(BaseCase):

    @allure.step("Login in myapp")
    @allure.issue("UI test")
    @allure.description("Test to login in app")
    @pytest.mark.UI
    def test_login(self):

        self.login_page.login(USERNAME, PASSWORD)

        assert self.login_page.find(
            self.login_page.locator.login_success_locator
        ).is_displayed()

    @allure.step("incorrect login in myapp")
    @allure.issue("UI test")
    @allure.description("Test to incorrect credentials login in app")
    @pytest.mark.UI
    def test_login_incorrect(self):
        """ Тест на несуществующего пользователя """
        self.login_page.login('Inccorectname', "1234")

        assert self.driver.current_url == LOGIN_URL or "http://myapp:83/login"

        assert self.login_page.find(self.login_page.locator.INVALID_USER)

    @allure.step("Registration link  in myapp")
    @allure.issue("UI test")
    @allure.description("Test to reg link")
    @pytest.mark.UI
    def test_create_account_link(self):
        """ Тест на ссылку регистрации """
        self.login_page.find(self.login_page.locator.LINK_REG).click()

        assert self.driver.current_url == REG_URL or "http://myapp:83/reg"

