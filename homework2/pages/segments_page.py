import allure

from locators import basic_locators

from pages.base_page import BasePage
from settings import VK_EDUCATION
from selenium.webdriver.common.by import By


class SegmentsPageException(Exception):
    ...


class SegmentPage(BasePage):

    locator_segment = basic_locators.SegmentsLocator()
    url = "https://target-sandbox.my.com/segments"

    def open_segment_page(self):
        segment_page = self.find(self.locator_segment.SEGMENTS_LOCATOR)
        segment_page.click()
        return True

    def create_segment_button(self):
        """Кнопка создания сегмента """
        button_create_segment = self.find(self.locator_segment.button_create_segment)
        button_create_segment.click()
        return True

    def add_submit_segment(self):
        """ кнопка добавления сегмента """
        add_segment = self.find(self.locator_segment.ADD_SEGMENT)
        add_segment.click()
        return True

    def input_check_box(self, locator):
        """ Нажатие на checkbox"""
        check_box = self.find(locator)
        check_box.click()
        return True

    @allure.step("Step 2 - add new segment")
    def add_new_segments(self):

        try:
            self.open_segment_page()

            self.create_segment_button()

            app_and_games = self.find(self.locator_segment.APP_GAMES)
            app_and_games.click()

            self.input_check_box(self.locator_segment.CHECK_BOX)

            self.add_submit_segment()

        except SegmentsPageException as ex:
            return ex

        return True

    @allure.step("Step 3 - create new segment")
    def create_new_segment(self, name: str):
        try:
            name_segment = self.find(self.locator_segment.NAME_SEGMENT)
            name_segment.clear()
            name_segment.send_keys(name)

            self.find(self.locator_segment.BUTTON_CREATE_NEW_SEGMENT).click()
        except SegmentsPageException as ex:
            return ex

        return True

    @allure.step("Step 2 - add source VK Group")
    def add_source_group(self):

        try:
            self.open_segment_page()

            self.find(self.locator_segment.DATA_SOURCE_GROUP_VK).click()

            input_group = self.find(self.locator_segment.INPUT_GROUP_VK)
            input_group.send_keys(VK_EDUCATION)

            self.find(self.locator_segment.SHOW_GROUP_VK).click()
            self.find(self.locator_segment.VK_EDUCATION).click()

            submit_group = self.find(self.locator_segment.BUTTON_SUBMIT_GROUP)
            submit_group.click()

        except SegmentsPageException as ex:
            return ex

        return True

    @allure.step("Step 3 - create segment VK Group")
    def create_segment_vk_group(self):
        self.open_segment_page()

        self.create_segment_button()

        vk_group = self.find(self.locator_segment.ADD_SEGMENT_VK)
        vk_group.click()

        self.input_check_box(self.locator_segment.CHECK_BOX)

        self.add_submit_segment()

    @allure.step("Step 4 - delete segment VK Group")
    def delete_segment(self, name: str):

        if name:
            id_segment = self.find((By.XPATH, f"//a[@title='{name}']")).get_attribute("href")[-7:]
            if self.find((By.XPATH, f"//div[contains(@data-test,'{id_segment}')]")).is_displayed():
                search_segment = self.find(self.locator_segment.SEARCH_SEGMENT)
                search_segment.send_keys(id_segment)
                self.find((By.XPATH, f"//li[@data-test='{id_segment}']")).click()
                self.input_check_box(self.locator_segment.SEGMENTS_CHECKBOX)
                button_action = self.find(self.locator_segment.BUTTON_ACTION)
                button_action.click()
                delete_segment = self.find(self.locator_segment.DELETE_SEGMENT)
                delete_segment.click()
                return True

        return False

    @allure.step("Step 5 - delete source VK Group")
    def delete_vk_group(self):
        try:
            self.open_segment_page()
            self.find(self.locator_segment.DATA_SOURCE_GROUP_VK).click()
            remove_source_button = self.find(self.locator_segment.REMOVE_SOURCE)
            remove_source_button.click()
            confirm = self.find(self.locator_segment.BUTTON_REMOVE_SOURCE)
            confirm.click()
        except SegmentsPageException as ex:
            return ex

        return True
