from base import Base
from utils.parser_access_log import (
    count_requests,
    get_url,
    get_4xx_status_code,
    get_5xx_status_code,
)


class TestSql(Base):

    def test_top_requests(self):
        top_requests = self.get_top_requests()
        top_requests_pars = count_requests(self.access_log)

        assert len(top_requests) == len(top_requests_pars)

    def test_url_requests(self):
        url_requests = self.get_url_requests()

        assert len(url_requests) == len(get_url(self.access_log))

    def test_bad_requests(self):
        bad_requests = self.get_bad_requests()

        assert len(bad_requests) == len(get_4xx_status_code(self.access_log))

    def test_server_error_ip(self):

        server_error_ip = self.get_ip_status_server_error()

        assert len(server_error_ip) == len(get_5xx_status_code(self.access_log))
