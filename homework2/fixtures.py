# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
#
# from pages.base_page import BasePage
# from pages.dashboard_page import DashboardPage
# from pages.login_page import LoginPage
# from settings import LOGIN, PASSWORD


# @pytest.fixture(scope='function')
# def driver(config, request):
#     options = Options()
#     if request.config.option.headless:
#         options.add_argument('--headless')
#     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
#     driver.set_window_size(width=1920, height=1080)
#     # driver.get("https://target-sandbox.my.com/")
#
#     yield driver
#
#     driver.quit()



