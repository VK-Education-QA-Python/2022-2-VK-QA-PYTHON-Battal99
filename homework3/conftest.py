import os

import pytest

import settings
from api.client import ApiClient


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def api_client():
    return ApiClient(base_url=settings.URL, login=settings.LOGIN, password=settings.PASSWORD)
