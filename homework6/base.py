import pytest
from client import SqlClient
from models.model import TopRequests, UrlRequests, ServerErrorIp, BadRequests
from utils.builder import MysqlBuilder

from utils.parser_access_log import *


class Base:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client, access_log):
        self.mysql: SqlClient = mysql_client
        self.mysql_builder: MysqlBuilder = MysqlBuilder(self.mysql)
        self.access_log = access_log

    def get_top_requests(self):
        top_requests = count_requests(self.access_log)
        for request in top_requests:
            self.mysql_builder.create_top_requests(name_method=request[0],
                                                   count=request[1])
        self.mysql.session.commit()

        top_requests = self.mysql.session.query(TopRequests)

        return top_requests.all()

    def get_url_requests(self):
        requests = get_url(self.access_log)
        for req in requests:
            self.mysql_builder.create_url_requests(url=req[0], count=req[1])
        self.mysql.session.commit()
        url_requests = self.mysql.session.query(UrlRequests)

        return url_requests.all()

    def get_ip_status_server_error(self):
        requests = get_5xx_status_code(self.access_log)
        for req in requests:
            self.mysql_builder.create_server_error(ip=req[0], size=req[1])
        self.mysql.session.commit()
        result = self.mysql.session.query(ServerErrorIp)

        return result.all()

    def get_bad_requests(self):
        requests = get_4xx_status_code(self.access_log)
        for req in requests:
            self.mysql_builder.create_bad_requests(url=req[0],
                                                   code=req[1],
                                                   size=req[2],
                                                   ip_address=req[3])
        self.mysql.session.commit()
        result = self.mysql.session.query(BadRequests)
        return result.all()
