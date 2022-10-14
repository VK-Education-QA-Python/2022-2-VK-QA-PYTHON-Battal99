import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from settings import LOGIN, PASSWORD


def pytest_addoption(parser):
    parser.addoption("--headless", action='store_true')

@pytest.fixture()
def config(request):
    headless = request.config.getoption("--headless")
    return headless


@pytest.fixture(scope='function')
def driver(config, request):
    options = Options()
    if request.config.option.headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.set_window_size(width=1920, height=1080)
    driver.get("https://target-sandbox.my.com/dashboard")

    yield driver

    driver.quit()


# @pytest.fixture(scope='session')
# def cookies(config):
#     driver.get(config['url'])
#     login_page = LoginPage(driver)
#     login_page.log_in(LOGIN, PASSWORD)
#
#     cookies = driver.get_cookies()
#     driver.quit()
#     return cookies
