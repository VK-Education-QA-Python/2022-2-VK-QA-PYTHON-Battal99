import os.path

import pytest
from client import SqlClient


def pytest_configure(config):
    mysql_client = SqlClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_tables()

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> SqlClient:
    client = request.config.mysql_client

    yield client

    client.connection.close()


@pytest.fixture(scope='session')
def access_log():

    return os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        'access.txt'))
