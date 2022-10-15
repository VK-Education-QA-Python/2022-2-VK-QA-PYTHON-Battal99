import logging
import os
import shutil
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.dashboard_page import LoginPage
from settings import LOGIN, PASSWORD
from _pytest.fixtures import FixtureRequest


def pytest_addoption(parser):
    parser.addoption("--headless", action='store_true')
    parser.addoption('--debug_log', action='store_true')


@pytest.fixture()
def config(request):
    headless = request.config.getoption("--headless")
    debug_log = request.config.getoption('--debug_log')
    return {"headless": headless,
            "debug_log": debug_log}


@pytest.fixture(scope='function')
def driver(config, request, temp_dir):
    options = Options()
    if request.config.option.headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.set_window_size(width=1920, height=1080)
    driver.get("https://target-sandbox.my.com/dashboard")

    yield driver

    driver.quit()


@pytest.fixture(scope='session')
def cookies(request: FixtureRequest):
    driver = request.getfixturevalue('driver')
    login_page = LoginPage(driver)
    login_page.log_in(LOGIN, PASSWORD)
    cookies = driver.get_cookies()
    driver.get("https://target-sandbox.my.com/dashboard")

    return cookies


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def base_temp_dir():
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    return base_dir


@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_temp_dir, request._pyfuncitem.nodeid)
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='function')
def logger(temp_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if not hasattr(config, 'workerunput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.base_temp_dir = base_dir

