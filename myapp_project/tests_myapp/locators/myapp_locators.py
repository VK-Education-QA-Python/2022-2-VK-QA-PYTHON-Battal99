from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_USERNAME = (By.ID, 'username')
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN = (By.ID, 'submit')
    LINK_REG = (By.XPATH, "//a[contains(@href, '/reg')]")
    login_success_locator = (By.ID, 'login-name')
    INVALID_USER = (By.ID, 'flash')


class RegPageLocator(LoginPageLocators):
    NAME_REG = (By.ID, 'user_name')
    SURNAME_REG = (By.ID, 'user_surname')
    Middlename_REG = (By.ID, 'user_middle_name')
    USERNAME_REG = (By.ID, 'username')
    PASSWORD_REG = (By.ID, 'password')
    REPEAT_PASSWORD_REG = (By.ID, 'confirm')
    CHECKBOX_REG = (By.ID, 'term')
    BUTTON_REG = (By.ID, 'submit')
    EMAIL_REG = (By.ID, 'email')
    FLASH = (By.ID, 'flash')


class MainPageLocators(LoginPageLocators):
    LOGOUT = (By.XPATH, "//a[contains(@href, '/logout')]")
    LINUX = (By.XPATH, '//a[contains(text(), "Linux")]')
    LINUX_REF = (By.XPATH, "//a[contains(text(), 'Download Centos7')]")

    PYTHON = (By.XPATH, '//a[contains(text(), "Python")]')
    LINK_PYHTON_HIS = (By.XPATH, '//a[contains(text(), "Python history")]')
    LINK_FLASK = (By.XPATH, '//a[contains(text(), "About Flask")]')

    NETWORK = (By.XPATH, '//a[contains(text(), "Network")]')
    LINK_WIRESHARK_NEWS = (By.XPATH, '//a[contains(text(), "News")]')
    LINK_WIRESHARK_DOWNLOAD = (By.CSS_SELECTOR, 'a[href="https://www.wireshark.org/#download"]')
    LINK_TCP_EXAMPLES = (By.XPATH, '//a[contains(text(), "Examples")]')

    ICON_API = (By.CSS_SELECTOR, 'img[src="/static/images/laptop.png"]')
    ICON_FUTURE = (By.CSS_SELECTOR, 'img[src="/static/images/loupe.png"]')
    ICON_SMTP = (By.CSS_SELECTOR, 'img[src="/static/images/analytics.png"]')

