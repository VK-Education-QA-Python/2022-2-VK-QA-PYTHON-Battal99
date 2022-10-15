# import pytest
from selenium.webdriver.common.by import By

from base import BaseCase


class TestAdvertisingCampaign(BaseCase):
    authorize = True

    def test_create_new_campaign(self):

        name_campaign = self.base_page.random_str()

        assert self.dashboard_page.create_new_campaign(name_campaign)
        assert self.dashboard_page.find((By.XPATH, "//a[contains(@class,'nameCell-module-campaignNameLink')]")) \
                   .get_attribute('title') == name_campaign
