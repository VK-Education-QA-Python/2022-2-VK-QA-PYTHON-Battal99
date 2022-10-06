from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    INPUT_LOGIN = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")

    MAIL_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-rightButton-3e-duF right-module-mail")]')

    EXIT_BUTTON = (By.XPATH, '//li[2]/a[contains(@class, "rightMenu-module-rightMenuLink")]')
    ERROR_LOGIN = (By.CLASS_NAME, "formMsg_title")
    INPUT_FIO = (By.CLASS_NAME, "js-form-element")
    BUTTON_SAVE = (By.CLASS_NAME, "button__text")
    ERROR_LOCATOR = (By.CLASS_NAME, "mcBtn")
    PROFILE_LOCATOR = (By.XPATH, "//li[6]/a[contains(@class, 'center-module-profile')]")
    PRO_LOCATOR = (By.XPATH, "//li[5]/a[contains(@class, 'center-module-pro')]")
    STATISTICS_LOCATOR = (By.XPATH, "//li[4]/a[contains(@class, 'center-module-statistics')]")
    BILLING_LOCATOR = (By.XPATH, "//li[3]/a[contains(@class, 'center-module-billing')]")
    SEGMENTS_LOCATOR = (By.XPATH, "//li[2]/a[contains(@class, 'center-module-segments')]")
    TOOLS_LOCATOR = (By.XPATH, "//li[7]/a[contains(@class, 'center-module-tools')]")

    BUTTON_PAYMENT_SUBMIT = (By.CLASS_NAME, "js-deposit-payment-submit")
    STATISTICS_LOCATOR_ON_PAGE_INFO = (By.CLASS_NAME, "js-align-info-bubble")
    TOOLS_LOCATOR_ON_PAGE_INSTRUCTION = (By.XPATH, '//div[contains(@class, "feeds-module-controls")]')
    SEGMENTS_LOCATOR_ON_PAGE_INSTRUCTION = (By.XPATH, '//span[contains(@class, "left-nav__group__label")]')
    PROMO_MAIN_PAGE = (By.XPATH, '//div[contains(@class, "mainPage-module-promo-2gzeMf")]')
