import json
from urllib.parse import urljoin

import requests


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

    def post_login(self) -> requests.Response:
        location = 'login'
        headers = {
            'Referer': self.base_url,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body_payload =\
            f'username={self.user}&password={self.password}&submit=Login"'
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
            surname=user.surname))
        # data = json.dumps(dict(
        #     username='battall1',
        #     name='nsdfwrvewg',
        #     password='wewfwe',
        #     email='email@mail.ru',
        #     surname='wfrvwrfw'))
        res = self._request('POST', location, headers=headers, data=data)
        print(res)
        return res

    def delete_user(self, user_name: str):
        location = f"/api/user/{user_name}"
        res = self._request('DELETE', location)

        return res  # 210 - а нужно 204


# a = ApiClient('127.0.0.1', '83', 'battal99', 'hanika73')
# print(a.get_status_app())
# print(a.post_login())
# print(a.get_main_page())
# # print(a.post_create_user())
# print(a.delete_user('battall1'))
