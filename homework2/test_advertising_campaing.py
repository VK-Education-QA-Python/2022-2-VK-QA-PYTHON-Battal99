# import pytest
from selenium.webdriver.common.by import By

# from homework2.ui.pages.base_page import BasePage
from base import BaseCase
from pages.dashboard_page import LoginPage


class TestLogin(BaseCase):
    authorize = False

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.log_in("batal990@mail.ru", "9Gq*686vJcYRtK")


class TestAdvertisingCampaign(BaseCase):

    def test_create_new_campaign(self):
        name_campaign = 'Test'
        # login_page = LoginPage(self.driver)
        # login_page.log_in("batal990@mail.ru", "9Gq*686vJcYRtK")
        assert self.dashboard_page.create_new_campaign()
        assert self.dashboard_page.find((By.XPATH, "//a[contains(@class,'nameCell-module-campaignNameLink')]"))\
                   .get_attribute('title') == name_campaign

    def test_create_new_campaign_2(self):
        name_campaign = 'Test'

        assert self.dashboard_page.create_new_campaign()
        assert self.dashboard_page.find((By.XPATH, "//a[contains(@class,'nameCell-module-campaignNameLink')]")) \
                   .get_attribute('title') == name_campaign
