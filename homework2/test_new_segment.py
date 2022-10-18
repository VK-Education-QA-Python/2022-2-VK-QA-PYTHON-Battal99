import allure
import pytest
from selenium.webdriver.common.by import By

from base import BaseCase


class TestSegments(BaseCase):
    authorize = True

    @pytest.mark.UI
    @allure.step("Step1 - Test create new segment")
    @allure.issue("Task 2")
    @allure.description("Test to create a segment in audiences with the type Apps and games "
                        "in social networks and check that the segment")
    def test_create_new_segment(self):
        name = self.segment_page.random_str()
        self.segment_page.add_new_segments()
        self.logger.info("create new segment")

        assert self.segment_page.create_new_segment(name)

        assert self.segment_page.find((By.XPATH, f"//a[@title='{name}']")).get_attribute('title') == name

    @pytest.mark.UI
    @allure.step("Step1 - Test create new segment group")
    @allure.issue("Task 3")
    @allure.description("Test for creating a segment by adding the VK education group to the data sources."
                        " After that, you need to create a segment with the Groups type OK and VK, check that it "
                        "exists, and then delete this particular segment and the added data source.")
    def test_create_new_segment_group(self):
        name = self.segment_page.random_str()
        title_vk = (By.XPATH, "//span[contains(@title, 'VK')]")

        assert self.segment_page.add_source_group()
        assert self.segment_page.find(title_vk).is_displayed()

        self.segment_page.create_segment_vk_group()

        assert self.segment_page.create_new_segment(name)
        assert self.segment_page.find((By.XPATH, f"//a[@title='{name}']")).get_attribute('title') == name

        # удалить сегмент и источник данных
        self.logger.info("deleted new group and segment")

        assert self.segment_page.delete_segment(name)
        assert self.segment_page.delete_vk_group()
