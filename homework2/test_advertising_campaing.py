import allure
import pytest
from selenium.webdriver.common.by import By

from base import BaseCase


class TestAdvertisingCampaign(BaseCase):
    authorize = True

    @pytest.mark.UI
    @allure.step("Create new campaign")
    @allure.issue("Task 1")
    @allure.description("Test to create an advertising campaign "
                        "of any type and check that it is created")
    def test_create_new_campaign(self):

        name_campaign = self.base_page.random_str()
        title = (By.XPATH, "//a[contains(@class,'nameCell-module-campaignNameLink')]")

        assert self.dashboard_page.create_new_campaign(name_campaign)
        assert self.dashboard_page.find(title).get_attribute('title') == name_campaign
