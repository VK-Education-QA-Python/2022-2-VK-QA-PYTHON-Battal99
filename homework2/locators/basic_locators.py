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


class DashboardLocators:
    # CREATE_NEW_CAMPAIGN = (By.XPATH, "//a[contains(@href, '/campaign/new')]")
    CREATE_NEW_CAMPAIGN = (By.XPATH, "//div[contains(@class, 'button-module-textWrapper')]")
    PROFILE_LOCATOR = (By.XPATH, "//a[contains(@href, '/profile')]")
    PRO_LOCATOR = (By.XPATH, "//a[contains(@href, '/pro')]")
    STATISTICS_LOCATOR = (By.XPATH, "//a[contains(@href, '/statistics')]")
    BILLING_LOCATOR = (By.XPATH, "//a[contains(@href, '/billing')]")
    SEGMENTS_LOCATOR = (By.XPATH, "//a[contains(@href, '/segments')]")
    TOOLS_LOCATOR = (By.XPATH, "//a[contains(@href, '/tools')]")
    MAIN_CONTENT = (By.XPATH, '//div[contains(@class, "layout-module-pageContentWrap")]')


class CampaignNewLocators(DashboardLocators):
    AUDIO_ADV = (By.XPATH, "//div[contains(@class, '_audiolistening')]")
    PRODUCT_VK = (By.XPATH, "//div[contains(@class, '_general_ttm')]")
    TIZER = (By.XPATH, "//div[contains(@class, 'pac-id-451')]")
    INPUT_PLACEHOLDER_LINK = (By.XPATH, "//input[contains(@class, 'suggester-module-searchInput')]")  # https://genius.com
    INPUT_PLACEHOLDER_HEADER = (By.XPATH, "//input[contains(@data-name, 'title_25')]")
    # INPUT_PLACEHOLDER_HEADER = (By.NAME, "title_25")
    INPUT_AD = (By.XPATH, "//textarea[@data-name='text_90']")
    LOAD_PICTURES = (By.XPATH, "//div/input[@type='file' and @data-test='image_90x75']")  # @data-test='button' and
    LOAD_PICTURES2 = (By.XPATH, "//input[@type='button' and @pseudo='file-selector-button']")
    SAVE_BUTTON_PIC = (By.XPATH, "//input[contains(@class,'image-cropper__save')]")
    SUBMIT_BANNER_BUTTON = (By.XPATH, "//button[@cid='view642']")
    INPUT_NAME_CAMPAIGN = (By.XPATH, "//input[contains(@class, 'input__inp')]")
    # UPLOAD_AUDIO_FILE = (By.XPATH, "//div[contains(@class, 'roles-module-uploadButton')]")
    # UPLOAD_PICTURES = (By.XPATH, "//div[contains(@class, 'upload-module-dropArea'")
    BUTTON_CREATE_CAMPAIGN = (By.XPATH, "//div[contains(@class , 'button__text' ")
    NAME_CAMPAIGN = (By.XPATH, "//a[contains(@class,'nameCell-module-campaignNameLink')]")


class SegmentsLocator(DashboardLocators):

    button_create_segment = (By.XPATH, "//button[@data-class-name='Submit']")
    APP_GAMES = (By.XPATH, "//div[@class='adding-segments-item']")
    CHECK_BOX = (By.XPATH, "//input[contains(@class,'adding-segments-source__checkbox')]")
    ADD_SEGMENT = (By.XPATH, "//div[contains(@class, 'adding-segments-modal__btn-wrap')]")
    BUTTON_CREATE_NEW_SEGMENT = (By.XPATH, "//button[contains(@class,'button_submit')]")
    TITLE_SEGMENT = (By.XPATH, "//div[@data-row-id='central-0']")
    NAME_SEGMENT = (By.XPATH, "//input[@data-translated-attr='placeholder' and @maxlength='60']")

    DATA_SOURCE_GROUP_VK = (By.XPATH, "//a[contains(@href,'/segments/groups_list')]")
    INPUT_GROUP_VK = (By.XPATH, "//input[contains(@class,'multiSelectSuggester-module-searchInput')]")
    SHOW_GROUP_VK = (By.XPATH, "//div[@data-test='show']")
    VK_EDUCATION = (By.XPATH, "//span[contains(@class, 'optionsList-module-text')]")
    BUTTON_SUBMIT_GROUP = (By.XPATH, "//div[@data-test='add_selected_items_button']")
    CHECK_ADD_VK_GROUP = (By.XPATH, "//span[@title='VK Образование'")

    ADD_SEGMENT_VK = (By.XPATH, "//div[1]/div[10][@class='adding-segments-item']")

    SEARCH_SEGMENT = (By.XPATH, "//input[contains(@class,'suggester-module-searchInput')]")

    DELETE_SEGMENT = (By.XPATH, "//li[@data-id='remove']")

    BUTTON_ACTION = (By.XPATH, "//span[contains(@class, 'select-module-itemInner')]")
    REMOVE_SOURCE = (By.XPATH, "//div[contains(@class, 'remove-source-wrap')]")

    BUTTON_REMOVE_SOURCE = (By.XPATH, "//button[contains(@class, 'button_confirm-remove')]")
