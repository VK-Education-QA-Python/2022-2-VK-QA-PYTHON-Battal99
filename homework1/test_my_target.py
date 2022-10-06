import time
from random import choice, randint
from string import ascii_letters

import pytest

from homework1 import locators
from homework1.base import BaseCase
from homework1.settings import INVALID_EMAIL, INVALID_PASSWORD, LOGIN, PASSWORD


class TestMyTarget(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        """ Тест входа в аккаунт"""
        successful_login: bool = self.log_in(LOGIN, PASSWORD)

        assert successful_login is True

        assert self.find(self.locators.MAIL_LOCATOR).is_displayed() is True

    @pytest.mark.UI
    def test_logout(self):
        """ Тест выхода из аккаунта """
        self.log_in(LOGIN, PASSWORD)
        time.sleep(3)
        logout = self.log_out()

        assert logout is True

        assert self.find(self.locators.PROMO_MAIN_PAGE).is_displayed() is True

    @pytest.mark.UI
    def test_invalid_email_login(self):
        """ Негативный тест на авторизацию """
        self.log_in(INVALID_EMAIL, PASSWORD)
        element_error_title = self.find(self.locators.ERROR_LOGIN)

        assert element_error_title.text == 'Error'

        assert self.find(self.locators.ERROR_LOCATOR).is_displayed() is True

    @pytest.mark.UI
    def test_invalid_password_login(self):
        """ Негативный тест на авторизацию """
        self.log_in(LOGIN, INVALID_PASSWORD)
        element_error_title = self.find(self.locators.ERROR_LOGIN)

        assert element_error_title.text == 'Error'

        assert self.find(self.locators.ERROR_LOCATOR).is_displayed() is True

    @pytest.mark.UI
    def test_edit_profile(self):
        """ Тест на редактирование профиля """
        self.log_in(LOGIN, PASSWORD)

        random_size_str: int = randint(1, 100)
        random_str: str = ''.join(choice(ascii_letters) for _ in range(random_size_str))
        element_profile = self.find(self.locators.PROFILE_LOCATOR)
        element_profile.click()
        element_input_fio = self.find(self.locators.INPUT_FIO)
        element_input_fio.clear()
        element_input_fio.send_keys(random_str)

        element_button_save = self.find(self.locators.BUTTON_SAVE)
        element_button_save.click()

        assert element_input_fio.get_attribute('value') == random_str

    @pytest.mark.UI
    @pytest.mark.parametrize('first_portal_page,'
                             'second_portal_page,'
                             'locator_on_first_page,'
                             'locator_on_second_page',

                             [(locators.BasePageLocators.BILLING_LOCATOR,
                               locators.BasePageLocators.STATISTICS_LOCATOR,
                               locators.BasePageLocators.BUTTON_PAYMENT_SUBMIT,
                               locators.BasePageLocators.STATISTICS_LOCATOR_ON_PAGE_INFO),
                              (locators.BasePageLocators.SEGMENTS_LOCATOR,
                               locators.BasePageLocators.TOOLS_LOCATOR,
                               locators.BasePageLocators.SEGMENTS_LOCATOR_ON_PAGE_INSTRUCTION,
                               locators.BasePageLocators.TOOLS_LOCATOR_ON_PAGE_INSTRUCTION)]
                             )
    def test_page_transition(self, first_portal_page, second_portal_page,
                             locator_on_first_page, locator_on_second_page):
        """ Тест на переход на страницы портала через кнопки в шапке меню """
        self.log_in(LOGIN, PASSWORD)

        assert self.page_transition(first_portal_page, locator_on_first_page) \
                   .is_displayed() is True

        assert self.page_transition(second_portal_page, locator_on_second_page) \
                   .is_displayed() is True
