# import pytest
from selenium.webdriver.common.by import By
import allure
from base import BaseCase


class TestAdvertisingCampaign(BaseCase):
    authorize = True

    @allure.step("Step 1 - Create new campaign")
    @allure.issue("Task 1")
    @allure.description("Write a test to create an advertising campaign "
                        "of any type and check that it is created")
    def test_create_new_campaign(self):

        name_campaign = self.base_page.random_str()

        assert self.dashboard_page.create_new_campaign(name_campaign)
        assert self.dashboard_page.find((By.XPATH, "//a[contains(@class,'nameCell-module-campaignNameLink')]")) \
                   .get_attribute('title') == name_campaign
