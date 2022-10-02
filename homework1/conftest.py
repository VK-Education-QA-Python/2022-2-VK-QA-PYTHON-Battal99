import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--headless", action='store_true')


@pytest.fixture()
def config(request):
    headless = request.config.getoption("--headless")
    return headless


@pytest.fixture(scope='function')
def driver(config, request):
    options = Options()
    site: str = "https://target-sandbox.my.com/"
    if request.config.option.headless:
        options.add_argument('--headless')
        options.add_argument('disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.get(site)
    driver.maximize_window()
    yield driver
    driver.quit()
