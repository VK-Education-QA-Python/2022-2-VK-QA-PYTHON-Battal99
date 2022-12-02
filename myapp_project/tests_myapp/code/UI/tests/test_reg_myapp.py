import allure
import pytest

from base import BaseCase


class TestReg(BaseCase):

    @allure.step("Create new user")
    @allure.issue("UI test")
    @allure.description("Test to create new user in app")
    @pytest.mark.UI
    def test_registration_valid(self):
        """ Тест на регистрацию пользователя
        Заполняем фейковой информацией
        Создаем
        """
        name = self.reg_page.random_str()
        surname = self.reg_page.random_str()
        middlename = self.reg_page.random_str()
        username = self.reg_page.random_str(digit=True)
        email = self.reg_page.random_str(digit=True, is_email=True)
        password = self.reg_page.random_str(digit=True)
        self.reg_page.create_user(
            name=name,
            surname=surname,
            middlename=middlename,
            username=username,
            email=email,
            password=password,
            password_confirm=password
        )

        assert self.driver.current_url != self.reg_page.url

        assert self.reg_page.find(
            self.reg_page.reg_locator.login_success_locator
        ).is_displayed()

    @allure.step("mismatched passwords")
    @allure.issue("UI test")
    @allure.description("Negative test for mismatched passwords")
    @pytest.mark.UI
    def test_invalid_password_confirm(self):
        """ Негативный тест на несопадающие пароли"""
        name = self.reg_page.random_str()
        surname = self.reg_page.random_str()
        middlename = self.reg_page.random_str()
        username = self.reg_page.random_str(digit=True)
        email = self.reg_page.random_str(digit=True, is_email=True)
        password = self.reg_page.random_str(digit=True)
        self.reg_page.create_user(
            name=name,
            surname=surname,
            middlename=middlename,
            username=username,
            email=email,
            password=password,
            password_confirm=self.reg_page.random_str(digit=True)
        )

        assert self.driver.current_url == self.reg_page.url

    @allure.step("Test username input")
    @allure.issue("UI test")
    @allure.description("Username less 6 characters")
    @pytest.mark.UI
    def test_invalid_username(self):
        """ Негативный тест username меньше 6 символов"""
        name = self.reg_page.random_str()
        surname = self.reg_page.random_str()
        middlename = self.reg_page.random_str()
        username = self.reg_page.random_str(size=5)
        email = self.reg_page.random_str(digit=True, is_email=True)
        password = self.reg_page.random_str(digit=True)
        self.reg_page.create_user(
            name=name,
            surname=surname,
            middlename=middlename,
            username=username,
            email=email,
            password=password,
            password_confirm=self.reg_page.random_str(digit=True)
        )

        assert self.driver.current_url == self.reg_page.url

    @allure.step("Incorrect email")
    @allure.issue("UI test")
    @allure.description("Negative test for incorrect email")
    @pytest.mark.UI
    def test_invalid_email(self):
        """ Негативный тест на email """
        name = self.reg_page.random_str()
        surname = self.reg_page.random_str()
        middlename = self.reg_page.random_str()
        username = self.reg_page.random_str(digit=True)
        email = self.reg_page.random_str(digit=True)
        password = self.reg_page.random_str(digit=True)
        self.reg_page.create_user(
            name=name,
            surname=surname,
            middlename=middlename,
            username=username,
            email=email,
            password=password,
            password_confirm=self.reg_page.random_str(digit=True)
        )

        assert self.driver.current_url == self.reg_page.url

        assert self.reg_page.find(
            self.reg_page.reg_locator.FLASH_INVALID_EMAIL
        ).is_displayed()

