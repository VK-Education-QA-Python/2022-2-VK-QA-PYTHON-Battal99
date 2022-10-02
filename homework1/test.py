from random import choice, randint

from string import ascii_letters

import pytest

from homework1.locators import *
from homework1.base import BaseCase

import time


class TestMyTarget(BaseCase):
    login: str = "batal990@mail.ru"
    password: str = "9Gq*686vJcYRtK"

    @pytest.mark.UI
    def test_login(self):
        """ Тест входа в аккаунт"""
        successful_login = self.log_in(self.login, self.password)
        time.sleep(2)
        assert successful_login is True
        assert self.find(*MAIL_LOCATOR).is_displayed() is True

    @pytest.mark.UI
    def test_logout(self):
        """ Тест выхода из аккаунта """
        self.log_in(self.login, self.password)
        time.sleep(2)
        logout = self.logout()
        time.sleep(3)
        assert logout is True
        assert self.find(*PROMO_MAIN_PAGE).is_displayed() is True

    @pytest.mark.UI
    def test_invalid_email_login(self):
        """ Негативный тест на авторизацию """
        self.log_in("battal@mail.ru", self.password)
        element_error_title = self.find(*ERROR_LOGIN)
        assert element_error_title.text == 'Error'

    @pytest.mark.UI
    def test_invalid_password_login(self):
        """ Негативный тест на авторизацию """
        self.log_in(self.login, "1234")
        element_error_title = self.find(*ERROR_LOGIN)
        assert element_error_title.text == 'Error'

    @pytest.mark.UI
    def test_edit_profile(self):
        """ Тест на редактирование профиля """
        self.log_in(self.login, self.password)

        random_size_str: int = randint(1, 100)
        random_str: str = ''.join(choice(ascii_letters) for _ in range(random_size_str))
        time.sleep(4)
        element_profile = self.find(*PROFILE_LOCATOR)
        element_profile.click()

        # time.sleep(3)

        element_input_fio = self.find(*INPUT_FIO)
        element_input_fio.clear()
        element_input_fio.send_keys(random_str)

        element_button_save = self.find(*BUTTON_SAVE)
        element_button_save.click()
        # time.sleep(2)

        assert element_input_fio.get_attribute('value') == random_str

    # @pytest.mark.UI
    # @pytest.mark.parametrize("page, locator",
    #                          [(BILLING_LOCATOR, BUTTON_PAYMENT_SUBMIT),
    #                           (STATISTICS_LOCATOR, STATISTICS_LOCATOR_ON_PAGE_INFO)]
    #                          )
    # def test_page_transition(self, page, locator):
    #     """ Тест на переход на страницы портала через кнопки в шапке меню """
    #     self.log_in(self.login, self.password)
    #     time.sleep(5)
    #     element_page_1 = self.find(*page)
    #     element_page_1.click()
    #     time.sleep(5)
    #     page_locator = self.find(*locator)
    #     assert page_locator.is_displayed() is True

    @pytest.mark.UI
    @pytest.mark.parametrize("page_1, page_2, locator_1, locator_2",
                             [(BILLING_LOCATOR, STATISTICS_LOCATOR, BUTTON_PAYMENT_SUBMIT,
                               STATISTICS_LOCATOR_ON_PAGE_INFO),
                              (SEGMENTS_LOCATOR, TOOLS_LOCATOR, SEGMENTS_LOCATOR_ON_PAGE_INSTRUCTION,
                               TOOLS_LOCATOR_ON_PAGE_INSTRUCTION)]
                             )
    def test_page_transition(self, page_1, page_2, locator_1, locator_2):
        """ Тест на переход на страницы портала через кнопки в шапке меню """
        self.log_in(self.login, self.password)
        time.sleep(4)
        assert self.page_transition(page_1, locator_1).is_displayed() is True
        assert self.page_transition(page_2, locator_2).is_displayed() is True

