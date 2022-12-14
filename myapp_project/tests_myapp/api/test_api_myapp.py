import json
from random import choice
from string import ascii_letters

import pytest
import allure

from client_api import ApiClient
from orm.client_orm import MySqlClient

from settings import APP_PORT, USERNAME, PASSWORD, APP_HOST_API

from utils import FakeUser, mysql_client


class TestApiMyApp:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.api_client = ApiClient(
            host=APP_HOST_API,
            port=APP_PORT,
            login=USERNAME,
            password=PASSWORD
        )
        self.fake_user = FakeUser()

        self.api_client.post_login()

    @pytest.fixture(scope='function', autouse=True)
    def setup_mysql_client(self):
        self.client: MySqlClient = mysql_client()

        yield self.client

        self.client.connection.close()

    @allure.step('Check status app')
    @allure.issue("API test")
    @allure.description("Test to check 'ok' status ")
    @pytest.mark.API
    def test_get_status_app(self):
        """ Проверка статуса приложения"""
        result = self.api_client.get_status_app()

        assert result.status_code == 200

        assert json.loads(result.text)['status'] == 'ok'

    @allure.step('Check login api')
    @allure.issue("API test")
    @allure.description("Test to login in app")
    @pytest.mark.API
    def test_post_login(self):
        """ Провера авторизации """
        res = self.api_client.post_login()
        assert res.status_code == 302  # 302

    @allure.step('Check login api')
    @allure.issue("API test")
    @allure.description("Test to login in app")
    @pytest.mark.API
    def test_post_create_user(self):
        """ Создание пользователя """
        user = self.fake_user
        res = self.api_client.post_create_user(user)
        res_json = json.loads(res.text)
        person = self.client.find_person(user.username)

        assert person
        assert res_json['detail'] == 'User was added'
        assert res_json['status'] == 'success'
        assert res.status_code == 201  # 210

    @allure.step('Check login api')
    @allure.issue("API test")
    @allure.description("Test to login in app")
    @pytest.mark.API
    @pytest.mark.parametrize("username, email", [
        ('', 'email@.com'),
        ('battal48328248', '')
    ])
    def test_post_negative_create_user(self, username, email):
        """ Создание пользователя с пустым username или email """
        user = self.fake_user
        user.username = username
        user.email = email
        res = self.api_client.post_create_user(user)
        person = self.client.find_person(user.username)

        assert res.status_code == 400
        assert person is False

        self.api_client.delete_user(user.username)

    @allure.step('delete user')
    @allure.issue("API test")
    @allure.description("Test to delete user")
    @pytest.mark.API
    def test_delete_user(self):
        """ Удаление пользователя """
        user = self.fake_user
        self.api_client.post_create_user(user)
        res = self.api_client.delete_user(user.username)

        assert res  # 210 - а нужно 204

    @allure.step('change password')
    @allure.issue("API test")
    @allure.description("Test to change password user")
    @pytest.mark.API
    def test_put_change_password(self):
        """ Смена пароля пользователя
         1. Создаем fake user
         2. Меняем пароль
         3. Авторизируемся под новым паролем
         4. Удаляем пользователя
         """
        user = self.fake_user
        new_password = ''.join(choice(ascii_letters) for _ in range(10))
        self.api_client.post_create_user(user)

        assert self.api_client.put_change_password(user.username, new_password)

        res = self.api_client.post_login(user.username, new_password)

        assert res.status_code == 302  # 302

        self.api_client.delete_user(user.username)

    @allure.step('block user')
    @allure.issue("API test")
    @allure.description("Test to block user")
    @pytest.mark.API
    def test_post_block_user(self):
        """ Блокировка пользователя
         1. Создаем fake user
         2. Блокируем пользователя
         3. Проверяем статус код
         4. В случае успеха пользователю проставляется access = 0 в БД.
         5. удаляем fake user
         """
        user = self.fake_user
        self.api_client.post_create_user(user)

        res = self.api_client.post_block_user(user.username)

        assert res.status_code == 200
        assert self.client.get_access_user(user) == 0

        self.api_client.delete_user(user.username)

    @allure.step('accept user')
    @allure.issue("API test")
    @allure.description("Test to accept user")
    @pytest.mark.API
    def test_accept_user(self):
        """ Разблокировка пользователя
         1. Создаем fake user
         2. Блокируем пользователя
         3. Разблокируем
         4. В случае успеха пользователю проставляется access = 1 в БД.
         5. удаляем fake user
        """
        user = self.fake_user
        self.api_client.post_create_user(user)
        self.api_client.post_block_user(user.username)

        res = self.api_client.post_accept_user(user.username)

        assert res.status_code == 200
        assert self.client.get_access_user(user) == 1

        self.api_client.delete_user(user.username)

    @allure.step('create existing email user')
    @allure.issue("API test")
    @allure.description("Negative test to create new user")
    @pytest.mark.API
    def test_create_existing_email_user(self):
        """ Проверка на создание пользователя с одинаковым email"""
        user = self.fake_user
        self.api_client.post_create_user(user)
        user.username = 'Newuser'
        count_user_before_add = self.client.count_user()
        result = self.api_client.post_create_user(user)

        assert count_user_before_add == self.client.count_user()

        assert result.status_code == 304

    @allure.step('create existing login user')
    @allure.issue("API test")
    @allure.description(
        "Negative test to create new user"
        " 1. Создаем фейкового пользователя"
        " 2. Меняем email"
        " 3. Создаем еще раз пользователя"
        " 4. Пользователь не должен создаться, код ответа должен быть 304"
    )
    @pytest.mark.API
    def test_create_existing_username(self):
        """ Проверка на создание пользователя с одинаковым username
        1. Создаем фейкового пользователя
        2. Меняем email
        3. Создаем еще раз пользователя
        4. Пользователь не должен создаться, код ответа должен быть 304
        """
        user = self.fake_user
        self.api_client.post_create_user(user)
        user.email = 'test_email@mail.ru'
        count_user_before_add = self.client.count_user()
        result = self.api_client.post_create_user(user)

        assert count_user_before_add == self.client.count_user()

        assert result.status_code == 304

    @allure.step('block non-existent user')
    @allure.issue("API test")
    @allure.description("Negative test to block  user")
    @pytest.mark.API
    def test_negative_block_user(self):
        """
        Негативный тест на блокировку несуществующего пользователя
        """
        user = self.fake_user
        res = self.api_client.post_block_user(user.username)

        assert res.status_code == 404

    @allure.step('accept non-existent user')
    @allure.issue("API test")
    @allure.description("Negative test to accept  user")
    @pytest.mark.API
    def test_negative_accept_user(self):
        """
        Негативный тест на разблокировку несуществующего пользователя
        """
        user = self.fake_user
        res = self.api_client.post_accept_user(user.username)

        assert res.status_code == 404

    @allure.step('block user twice')
    @allure.issue("API test")
    @allure.description("test to block  user")
    @pytest.mark.API
    def test_block_user_twice(self):
        """ Тест на повторную блокировку """
        user = self.fake_user
        self.api_client.post_create_user(user)
        self.api_client.post_block_user(user.username)
        res = self.api_client.post_block_user(user.username)

        assert res.status_code == 304  # не изменилось

    @allure.step('accept user twice')
    @allure.issue("API test")
    @allure.description("test to accept user")
    @pytest.mark.API
    def test_accept_user_twice(self):
        """ Тест на повторную разблокировку """
        user = self.fake_user
        self.api_client.post_create_user(user)
        self.api_client.post_accept_user(user.username)
        res = self.api_client.post_accept_user(user.username)

        assert res.status_code == 304  # не изменилось

    @allure.step('check active user')
    @allure.issue("API test")
    @allure.description("test to check activity")
    @pytest.mark.API
    def test_check_active_user(self):
        """ Тест на проверку активности пользователя"""
        user = self.fake_user
        self.api_client.post_create_user(user)
        self.api_client.post_login(user.username, user.password)

        active = self.client.check_active_user(user.username)

        assert active == 1

        self.api_client.delete_user(user.username)
