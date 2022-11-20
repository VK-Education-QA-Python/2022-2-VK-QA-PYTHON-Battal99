import json
from urllib.parse import urljoin

import requests

from api.custom_exception import (
    ResponseStatusCodeException,
    ApiClientException,
)
from api.location import (
    CONTINUE_LOCATION,
    LOGIN_REF,
    CREATE_SEGMENT,
    REF_CREATE_SEGMENT,
    CREATE_CAMPAIGN,
    REF_CREATE_CAMPAIGN,
    LOAD_FILE,
    DELETE_CAMPAIGN,
    REF_DELETE_CAMPAIGN,
    GET_CAMPAIGN,
    REF_GET_CAMPAIGN,
    REF_DELETE_SEGMENT,
    DELETE_SEGMENT,
    GET_URL,
    REF_GET_URL,
    CSRF_LOCATION,
    GET_SEGMENT,
    REF_GET_SEGMENT,
    GET_VK_GROUP,
    GET_GROUP_LIST, FAILURE_LOGIN,
)
# from payloads.payloads import Payloads
from payloads.payloads import campaign_data, segment_data_vk_group, segment_data_games
from settings import VK_GROUP, URL_GENIUS


class ApiClient:

    def __init__(self, base_url: str, login: str, password: str):
        self.base_url = base_url

        self.login = login
        self.password = password
        self.csrftoken = None
        self.session = requests.Session()

    def headers(self, location):
        return {
            'Referer': urljoin(self.base_url, location),
            'X-CSRFToken': self.csrftoken
        }

    def get_csrftoken(self):
        headers = {
            'Referer': urljoin(self.base_url, 'dashboard')
        }

        response = self._request('GET',
                                 CSRF_LOCATION,
                                 headers=headers,
                                 allow_redirects=True)
        self.csrftoken = response.cookies.get('csrftoken')

    def post_login(self):

        headers = {
            'Referer': self.base_url
        }
        data = {
            'email': self.login,
            'password': self.password,
            'continue': urljoin(self.base_url, CONTINUE_LOCATION),
            'failure': FAILURE_LOGIN
        }
        resp = self._request('POST', LOGIN_REF,
                             headers=headers,
                             data=data,
                             allow_redirects=True,
                             join_url=False)

        self.get_csrftoken()

        return resp

    def _request(self, method,
                 location,
                 headers=None,
                 data=None,
                 params=None,
                 files=None,
                 allow_redirects=False,
                 expected_status=200,
                 join_url=True,
                 jsonify=False,
                 **kwargs):

        if join_url:
            url = urljoin(self.base_url, location)
        else:
            url = location
        print(headers)
        print(data)
        res = self.session.request(method, url,
                                   headers=headers,
                                   data=data,
                                   params=params,
                                   files=files,
                                   allow_redirects=allow_redirects,
                                   **kwargs)
        print(res.text)
        if res.status_code != expected_status:
            raise ResponseStatusCodeException(
                f'Got {res.status_code} {res.request} {res.headers} :"{url}"'
            )

        if jsonify:
            json_response = res.json()
            return json_response

        return res

    def post_create_segment(self, segment_name, object_type):
        vk_group = self.get_vk_group(VK_GROUP)
        if object_type == 'vk_group':
            data = json.dumps(
                segment_data_vk_group(segment_name, vk_group)
            )
        elif object_type == 'games':
            data = json.dumps(segment_data_games(segment_name))
        else:
            raise ApiClientException("Wrong object_type")
        response = self._request('POST', CREATE_SEGMENT,
                                 headers=self.headers(REF_CREATE_SEGMENT),
                                 data=data,
                                 jsonify=True)

        return response.get('id')

    def get_url_id(self):
        params = {
            'url': URL_GENIUS
        }
        response = self._request('GET', GET_URL,
                                 headers=self.headers(REF_GET_URL),
                                 params=params,
                                 jsonify=True)

        return response.get('id')

    def post_upload_file(self, file_path: callable):
        file = {
            'file': open(file_path('test_pic.jpg'), 'rb'),
        }

        response = self._request('POST', LOAD_FILE,
                                 headers=self.headers(REF_CREATE_CAMPAIGN),
                                 files=file,
                                 jsonify=True
                                 )

        return response.get('id')

    def post_create_campaign(self, campaign_name, file_path: callable) -> dict:
        image_id: int = self.post_upload_file(file_path)
        url_id: int = self.get_url_id()

        data = campaign_data(campaign_name, image_id, url_id)
        response = self._request('POST',
                                 CREATE_CAMPAIGN,
                                 headers=self.headers(REF_CREATE_CAMPAIGN),
                                 data=data, jsonify=True)

        return response

    def post_delete_campaign(self, campaign_id):
        data = json.dumps([{
            'id': campaign_id,
            'status': 'deleted'
        }])

        response = self._request('POST', DELETE_CAMPAIGN,
                                 headers=self.headers(REF_DELETE_CAMPAIGN),
                                 data=data,
                                 expected_status=204)

        return response

    def get_campaign(self, campaign_id, expected_status=200):
        response = self._request('GET',
                                 GET_CAMPAIGN.format(campaign_id),
                                 headers=self.headers(
                                     REF_GET_CAMPAIGN.format(campaign_id)),
                                 expected_status=expected_status,
                                 jsonify=True)

        return response.get('name')

    def get_segment(self, segment_id, expected_status=200):
        response = self._request('GET',
                                 GET_SEGMENT.format(segment_id),
                                 headers=self.headers(
                                     REF_GET_SEGMENT.format(segment_id)),
                                 expected_status=expected_status,
                                 jsonify=True)

        return response.get('name')

    def get_vk_group(self, vk_group):
        param = {
            '_q': vk_group
        }
        response = self._request('GET',
                                 GET_VK_GROUP,
                                 headers=self.headers(GET_GROUP_LIST),
                                 params=param,
                                 jsonify=True)

        return response.get('items')[0]['id']

    def _delete_segment(self, segment_id):
        response = self._request('DELETE', DELETE_SEGMENT.format(segment_id),
                                 headers=self.headers(REF_DELETE_SEGMENT),
                                 expected_status=204)

        return response
