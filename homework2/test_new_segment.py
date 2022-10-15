import pdb
from random import choice, randint
from selenium.webdriver.common.by import By
import time
from base import BaseCase
from locators import basic_locators


class TestSegments(BaseCase):
    authorize = True

    def test_create_new_segment(self):
        name = self.segment_page.random_str()
        self.segment_page.add_new_segments()

        assert self.segment_page.create_new_segment(name)
        assert self.segment_page.find((By.XPATH, f"//a[@title='{name}']")).get_attribute('title') == name

    def test_add_new_segment_group(self):
        name = self.segment_page.random_str()

        assert self.segment_page.add_source_group()
        assert self.segment_page.find((By.XPATH, "//span[contains(@title, 'VK')]")).is_displayed()

        self.segment_page.create_segment_vk_group()

        assert self.segment_page.create_new_segment(name)
        assert self.segment_page.find((By.XPATH, f"//a[@title='{name}']")).get_attribute('title') == name

        # удалить сегмент и источник данных
        assert self.segment_page.delete_segment(name)
        assert self.segment_page.delete_vk_group()

