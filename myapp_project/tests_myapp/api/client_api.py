import json
from urllib.parse import urljoin

import requests
import allure


class ApiClient:
    def __init__(self, host, port, login, password):
        self.base_url = f"http://{host}:{port}/"
        self.session = requests.Session()
        self.user = login
        self.password = password

    def _request(self, method,
                 location,
                 headers=None,
                 data=None,
                 params=None,
                 files=None,
                 allow_redirects=False,
                 join_url=True,
                 jsonify=False,
                 **kwargs):

        if join_url:
            url = urljoin(self.base_url, location)
        else:
            url = location
        res = self.session.request(
            method=method,
            url=url,
            headers=headers,
            data=data,
            params=params,
            files=files,
            allow_redirects=allow_redirects,
            **kwargs
        )
        if jsonify:
            json_response = res.json()
            return json_response

        return res

    def get_status_app(self) -> requests.Response:
        """ Статус приложения """
        location = 'status'
        res = self._request('GET', location)

        return res

    @allure.step("POST method login user")
    def post_login(self, user=None, password=None) -> requests.Response:
        location = 'login'
        headers = {
            'Referer': self.base_url,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        if user is None or password is None:
            body_payload = f'username={self.user}&password={self.password}&submit=Login"'
        else:
            body_payload = f'username={user}&password={password}&submit=Login"'
        res = self._request(
            'POST',
            location=location,
            headers=headers,
            data=body_payload,
            allow_redirects=False
        )

        return res

    def get_main_page(self):
        location = 'welcome/'
        res = self._request('GET', location=location)

        return res

    @allure.step("POST method create user")
    def post_create_user(self, user) -> requests.Response:
        """  Создание пользователя """
        location = 'api/user'
        headers = {
            'Content-Type': "application/json",
        }

        data = json.dumps(dict(
            username=user.username,
            name=user.name,
            password=user.password,
            email=user.email,
            surname=user.surname)
        )
        res = self._request('POST', location, headers=headers, data=data)

        return res

    @allure.step("DELETE method delete user")
    def delete_user(self, user_name: str):
        location = f"/api/user/{user_name}"
        res = self._request('DELETE', location)

        return res  # 210 - а нужно 204

    @allure.step("PUT method change password")
    def put_change_password(self, user_name: str, new_password: str):
        """ Смена пароля пользователя.
        В случае успеха у пользователя меняется пароль;
        Новый пароль не может совпадать с паролем из БД.
        """
        location = f"api/user/{user_name}/change-password"
        headers = {
            'Content-Type': "application/json",
        }

        data = json.dumps({"password": new_password})

        res = self._request('PUT', location, headers=headers, data=data)

        return res

    @allure.step("POST method block user")
    def post_block_user(self, user_name: str):
        """ Блокировка пользователя.
        В случае успеха пользователю
        проставляется access = 0 в БД.
        """
        location = f'api/user/{user_name}/block'
        res = self._request('POST', location)

        return res

    @allure.step("POST method accept user")
    def post_accept_user(self, user_name: str):
        """ Разблокировка пользователя
        В случае успеха пользователю проставляется access = 1 в БД.
        """
        location = f'api/user/{user_name}/accept'
        res = self._request('POST', location)

        return res
