# from pages.dashboard_page import DashboardPage
# import pytest
# from _pytest.fixtures import FixtureRequest
#
# from base import BaseCase
# from pages.dashboard_page import LoginPage




# class LoginPage(BasePage):
#
#     def log_in(self, login: str, password: str):
#         """ Метод входа входа в аккаунт """
#         try:
#             self.click_element(self.find(self.locators.LOGIN_LOCATOR))
#             element_login_input = self.find(self.locators.INPUT_LOGIN)
#             element_login_input.send_keys(login)
#             element_password_input = self.find(self.locators.INPUT_PASSWORD)
#             element_password_input.send_keys(password)
#             element_password_input.send_keys(Keys.ENTER)
#         except NoSuchElementException:
#             return False
#
#         return DashboardPage(driver=self.driver)
