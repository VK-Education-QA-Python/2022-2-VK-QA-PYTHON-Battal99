import allure
from selenium.webdriver.common.keys import Keys

from utils import file_path
from locators import basic_locators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def log_in(self, login: str, password: str):
        """ Метод входа входа в аккаунт """
        self.click_element(self.find(self.locators.LOGIN_LOCATOR))
        element_login_input = self.find(self.locators.INPUT_LOGIN)
        element_login_input.send_keys(login)
        element_password_input = self.find(self.locators.INPUT_PASSWORD)
        element_password_input.send_keys(password)
        element_password_input.send_keys(Keys.ENTER)

        return DashboardPage(driver=self.driver)


class DashboardPage(BasePage):
    locators_create_campaign = basic_locators.CampaignNewLocators()

    def upload_file(self, locator: tuple, file_path: callable, name_file: str):
        upload_file = self.driver.find_element(*locator)
        upload_file.send_keys(file_path(name_file))

    @allure.step("method create new campaign")
    def create_new_campaign(self, name: str):
        create_campaign = self.find(self.locators_create_campaign.CREATE_NEW_CAMPAIGN)
        if create_campaign.is_displayed():
            create_campaign.click()
        else:
            self.find(self.locators_create_campaign.CREATE_NEW_CAMPAIGN_HREF).click()

        product_vk = self.find(self.locators_create_campaign.PRODUCT_VK)
        product_vk.click()

        input_link = self.find(self.locators_create_campaign.INPUT_PLACEHOLDER_LINK)
        input_link.send_keys("https://genius.com")

        tizer_button = self.find(self.locators_create_campaign.TIZER)
        tizer_button.click()

        name_campaign = self.find(self.locators_create_campaign.INPUT_NAME_CAMPAIGN)
        name_campaign.clear()
        name_campaign.send_keys(name)

        header_ad = self.find(self.locators_create_campaign.INPUT_PLACEHOLDER_HEADER)
        header_ad.send_keys(self.random_str())

        text_ad = self.find(self.locators_create_campaign.INPUT_AD)
        text_ad.send_keys(self.random_str())
        self.upload_file(self.locators_create_campaign.LOAD_PICTURES, file_path=file_path, name_file='p.png')

        self.find(self.locators_create_campaign.SAVE_BUTTON_PIC).click()
        self.find(self.locators_create_campaign.SUBMIT_BANNER_BUTTON).click()

        return True
