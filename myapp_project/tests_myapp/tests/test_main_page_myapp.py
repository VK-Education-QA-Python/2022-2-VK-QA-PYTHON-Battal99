from typing import Tuple

import allure
import pytest

from base import BaseCase
from locators.myapp_locators import MainPageLocators
from settings import (
    CENTOS,
    PYTHON_HISTORY,
    FLASK_DOC,
    WIRESHARK_NEWS,
    WIRESHARK_DOWNLOAD,
    TCPDUMP_EXAMPLES,
    API_LINK,
    FUTURE_INTERNET_LINK,
    SMTP_LINK
)


class TestMainPage(BaseCase):

    @allure.step("fixture login")
    @allure.description("login in my app")
    @pytest.fixture(scope='function', autouse=True)
    def login(self, login_ui):
        ...

    @allure.step("Test logout")
    @allure.issue("UI test")
    @allure.description("Test to logout button in main page")
    @pytest.mark.UI
    def test_logout_button(self):
        """ Тестирует кнопку выхода из аккаунта"""
        self.main_page.logout()

        assert self.driver.current_url == self.login_page.url

    @allure.step("Test open main page links")
    @allure.issue("UI test")
    @allure.description(
        "Test for the correctness of the links on"
        " the header of the site"
    )
    @pytest.mark.parametrize("main_locator, link_locator, link", [
        (
                MainPageLocators.LINUX,
                MainPageLocators.LINUX_REF,
                CENTOS
        ),
        (
                MainPageLocators.PYTHON,
                MainPageLocators.LINK_PYHTON_HIS,
                PYTHON_HISTORY
        ),
        (
                MainPageLocators.PYTHON,
                MainPageLocators.LINK_FLASK,
                FLASK_DOC
        ),
        (
                MainPageLocators.NETWORK,
                MainPageLocators.LINK_WIRESHARK_NEWS,
                WIRESHARK_NEWS
        ),
        (
                MainPageLocators.NETWORK,
                MainPageLocators.LINK_WIRESHARK_DOWNLOAD,
                WIRESHARK_DOWNLOAD
        ),
        (
                MainPageLocators.NETWORK,
                MainPageLocators.LINK_TCP_EXAMPLES,
                TCPDUMP_EXAMPLES
        )
    ])
    @pytest.mark.UI
    def test_open_main_page_links(
            self,
            main_locator: Tuple[str, str],
            link_locator: Tuple[str, str],
            link: str):
        """
        Параметризованный тест на корректность ссылок приложения
        :param main_locator: Локатор на главной странице приложения
        :param link_locator: Вкладка локатора с ссылкой
        :param link: Ссылка на которую должны перейти
        """
        self.main_page.open_links(main_locator, link_locator)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        assert self.driver.current_url == link

    @allure.step("Test icon")
    @allure.issue("UI test")
    @allure.description("Test icon links in main page")
    @pytest.mark.parametrize("icon_locator, link ", [
        (MainPageLocators.ICON_API, API_LINK),
        (MainPageLocators.ICON_FUTURE, FUTURE_INTERNET_LINK),
        (MainPageLocators.ICON_SMTP, SMTP_LINK)
    ])
    @pytest.mark.UI
    def test_icon_links(self, icon_locator: Tuple[str, str], link: str):
        """Параметризованный тест на корректность ссылок в иконках"""
        self.main_page.find(icon_locator).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

        assert self.driver.current_url == link
