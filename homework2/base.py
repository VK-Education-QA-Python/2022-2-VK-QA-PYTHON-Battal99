import pytest
from _pytest.fixtures import FixtureRequest

from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage, LoginPage


# from ui.pages.main_page import MainPage
from pages.segments_page import SegmentPage


class BaseCase:
    driver = None
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = BasePage(driver=driver)
        self.dashboard_page: DashboardPage = DashboardPage(driver=driver)
        self.segment_page: SegmentPage = SegmentPage(driver=driver)

        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()

