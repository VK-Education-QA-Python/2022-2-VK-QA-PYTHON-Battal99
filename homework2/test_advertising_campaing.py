# import pytest
from selenium.webdriver.common.by import By

# from homework2.ui.pages.base_page import BasePage
# from base import BaseCase
from base import BaseCase
from pages.base_page import BasePage
from pages.dashboard_page import LoginPage, DashboardPage
# from pages.login_page import BaseCaseLogin
import pytest
from _pytest.fixtures import FixtureRequest


# class BaseCase:
#     driver = None
#     authorize = True
#
#     @pytest.fixture(scope='function', autouse=True)
#     def setup(self, driver, config, request: FixtureRequest):
#         self.driver = driver
#         self.config = config
#         # self.logger = logger
#
#         self.base_page: BasePage = BasePage(driver=driver)
#         self.dashboard_page: DashboardPage = DashboardPage(driver=driver)
#
#         self.login_page = LoginPage(driver)
#         if self.authorize:
#             cookies = request.getfixturevalue('cookies')
#             for cookie in cookies:
#                 self.driver.add_cookie(cookie)
#
#             self.driver.refresh()


# class TestLogin(BaseCase):
#     authorize = False
#
#     def test_login(self):
#         login_page = LoginPage(self.driver)
#         login_page.log_in("batal990@mail.ru", "9Gq*686vJcYRtK")


class TestAdvertisingCampaign(BaseCase):
    authorize = True

    def test_create_new_campaign(self):
        name_campaign = 'Test'

        assert self.dashboard_page.create_new_campaign()
        assert self.dashboard_page.find((By.XPATH, "//a[contains(@class,'nameCell-module-campaignNameLink')]")) \
                   .get_attribute('title') == name_campaign

    def test_create_new_campaign_2(self):
        name_campaign = 'Test'

        assert self.dashboard_page.create_new_campaign()
        assert self.dashboard_page.find((By.XPATH, "//a[contains(@class,'nameCell-module-campaignNameLink')]")) \
                   .get_attribute('title') == name_campaign
