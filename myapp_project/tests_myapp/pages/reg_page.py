import allure

from locators.myapp_locators import RegPageLocator
from pages.base_page import BasePage
from settings import APP_HOST, APP_PORT


class RegPage(BasePage):
    url = f"http://{APP_HOST}:{APP_PORT}/reg"
    reg_locator = RegPageLocator()

    @allure.step("new user creation method")
    def create_user(
            self,
            name,
            surname,
            username,
            email,
            password,
            password_confirm,
            middlename=''):
        """ Создание пользователя
        :str name: имя пользователя
        :str surname: фамилия пользователя
        :str username: никнейм пользователя
        :str email: email
        :str password: пароль
        :str password_confirm: подтверждение пароля
        :str middlename: отчество
        """
        self.find(self.locator.LINK_REG).click()
        name_input = self.find(self.reg_locator.NAME_REG)
        name_input.send_keys(name)
        surname_input = self.find(self.reg_locator.SURNAME_REG)
        surname_input.send_keys(surname)
        middlename_input = self.find(self.reg_locator.Middlename_REG)
        middlename_input.send_keys(middlename)
        username_input = self.find(self.reg_locator.USERNAME_REG)
        username_input.send_keys(username)
        email_input = self.find(self.reg_locator.EMAIL_REG)
        email_input.send_keys(email)
        password_input = self.find(self.reg_locator.PASSWORD_REG)
        password_input.send_keys(password)
        confirm_password_input = self.find(
            self.reg_locator.REPEAT_PASSWORD_REG
        )
        confirm_password_input.send_keys(password_confirm)
        self.find(self.reg_locator.CHECKBOX_REG).click()
        self.find(self.reg_locator.BUTTON_REG).click()
