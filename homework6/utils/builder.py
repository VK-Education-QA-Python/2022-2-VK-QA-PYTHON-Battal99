from models.model import (
    TopRequests,
    UrlRequests,
    BadRequests,
    ServerErrorIp,
)


class MysqlBuilder:

    def __init__(self, client):
        self.client = client

    def create_top_requests(self, name_method, count):
        top_requests = TopRequests(
            name_method=name_method,
            count=count
        )
        self.client.session.add(top_requests)
        self.client.session.commit()
        return top_requests

    def create_url_requests(self, url, count):
        url_requests = UrlRequests(
            url=url,
            count=count
        )
        self.client.session.add(url_requests)
        self.client.session.commit()
        return url_requests

    def create_bad_requests(self, url, code, size, ip_address):
        client_errors = BadRequests(
            url=url,
            status_code=code,
            count=size,
            ip_address=ip_address
        )
        self.client.session.add(client_errors)
        self.client.session.commit()
        return client_errors

    def create_server_error(self, ip, size):
        server_errors = ServerErrorIp(
            ip_address=ip,
            count=size
        )
        self.client.session.add(server_errors)
        self.client.session.commit()
        return server_errors
