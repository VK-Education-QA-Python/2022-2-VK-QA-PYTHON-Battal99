from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    INPUT_LOGIN = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")

    MAIL_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-rightWrap")]')

    EXIT_BUTTON = (By.XPATH, '//a[contains(@href, "/logout")]')
    ERROR_LOGIN = (By.CLASS_NAME, "formMsg_title")
    INPUT_FIO = (By.CLASS_NAME, "js-form-element")
    BUTTON_SAVE = (By.CLASS_NAME, "button__text")
    ERROR_LOCATOR = (By.CLASS_NAME, "mcBtn")
    PROFILE_LOCATOR = (By.XPATH, "//a[contains(@href, '/profile')]")
    PRO_LOCATOR = (By.XPATH, "//a[contains(@href, '/pro')]")
    STATISTICS_LOCATOR = (By.XPATH, "//a[contains(@href, '/statistics')]")
    BILLING_LOCATOR = (By.XPATH, "//a[contains(@href, '/billing')]")
    SEGMENTS_LOCATOR = (By.XPATH, "//a[contains(@href, '/segments')]")
    TOOLS_LOCATOR = (By.XPATH, "//a[contains(@href, '/tools')]")
    MAIN_CONTENT = (By.XPATH, '//div[contains(@class, "layout-module-pageContentWrap")]')
    BUTTON_PAYMENT_SUBMIT = (By.CLASS_NAME, "js-deposit-payment-submit")
    STATISTICS_LOCATOR_ON_PAGE_INFO = (By.CLASS_NAME, "js-align-info-bubble")
    TOOLS_LOCATOR_ON_PAGE_INSTRUCTION = (By.XPATH,
                                         '//div[contains(@class, "feeds-module-controls")]')
    SEGMENTS_LOCATOR_ON_PAGE_INSTRUCTION = (By.XPATH,
                                            '//span[contains(@class, "left-nav__group__label")]')
