import json

import pytest

from client_api import ApiClient
from settings import APP_HOST, APP_PORT, USERNAME, PASSWORD
from utils import FakeUser


class TestApiMyApp:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.api_client = ApiClient(
            host=APP_HOST,
            port=APP_PORT,
            login=USERNAME,
            password=PASSWORD)

        self.fake_user = FakeUser()

        self.api_client.post_login()

    def test_get_status_app(self):
        """ Проверка статуса приложения"""
        result = self.api_client.get_status_app()

        assert result.status_code == 200

        assert json.loads(result.text)['status'] == 'ok'

    def test_post_login(self):
        res = self.api_client.post_login()
        assert res.status_code == 200  # 302

    def test_post_create_user(self):
        """ Создание пользователя """
        res = self.api_client.post_create_user(self.fake_user)
        res_json = json.loads(res.text)

        assert res_json['status'] == 'success'  # 210



    def test_delete_user(self):
        # self.api_client.post_create_user()
        # res = self.api_client.delete_user()
        pass
    