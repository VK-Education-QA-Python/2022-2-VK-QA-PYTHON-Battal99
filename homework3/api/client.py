import json
from urllib.parse import urljoin

import requests

from api.ref import CONTINUE_LOCATION, LOGIN_REF, CREATE_SEGMENT, REF_CREATE_SEGMENT, CREATE_CAMPAIGN, \
    REF_CREATE_CAMPAIGN, LOAD_FILE, REF_LOAD_FILE, DELETE_CAMPAIGN, REF_DELETE_CAMPAIGN, GET_CAMPAIGN, REF_GET_CAMPAIGN, \
    REF_DELETE_SEGMENT, DELETE_SEGMENT, GET_URL, REF_GET_URL, CSRF, GET_SEGMENT, REF_GET_SEGMENT


# from utils import file_path


class ApiClientException(Exception):
    ...


class ResponseStatusCodeException(Exception):
    ...


class RespondErrorException(Exception):
    ...


class ApiClient:

    def __init__(self, base_url: str, login: str, password: str):
        self.base_url = base_url

        self.login = login
        self.password = password
        self.mc = None
        self.sdc = None
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

        response = self._request('GET', CSRF, headers=headers, allow_redirects=True)
        self.csrftoken = response.cookies.get('csrftoken')

    # def get_mc(self):
    #     headers = {
    #         'Referer': urljoin(self.base_url, 'dashboard')
    #     }
    #
    #     response = self._request('GET', urljoin(self.base_url, 'dashboard'), headers=headers)
    #     print(response.cookies)
    #     self.csrftoken = response.cookies.get('mc')

    def post_login(self):

        headers = {
            'Referer': self.base_url
        }
        data = {
            'email': self.login,
            'password': self.password,
            'continue': urljoin(self.base_url, CONTINUE_LOCATION),
            # 'continue': 'https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1%23email',
            'failure': 'https://account.my.com/login/'
        }
        resp = self._request('POST', LOGIN_REF, headers=headers, data=data, allow_redirects=True, join_url=False)

        self.get_csrftoken()

        return resp

    def _request(self, method, location, headers=None, data=None, params=None, files=None, allow_redirects=False,
                 expected_status=200, join_url=True, jsonify=False):

        if join_url:
            url = urljoin(self.base_url, location)
        else:
            url = location

        res = self.session.request(method, url, headers=headers, data=data, params=params, files=files,
                                   allow_redirects=allow_redirects)

        if res.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {res.status_code} {res.request} :"{url}"')

        if jsonify:
            json_response = res.json()
            return json_response

        return res

    def post_create_segment(self, segment_name):
        data = json.dumps(self.segment_data(segment_name))

        response = self._request('POST', CREATE_SEGMENT,
                                 headers=self.headers(REF_CREATE_SEGMENT), data=data, jsonify=True)
        return response.get('id')

    @staticmethod
    def segment_data(name):
        data = {
            "name": name,
            "logicType": "or",
            "pass_condition": 1,
            "relations": [{
                "object_type": "remarketing_player",
                "params": {
                    "left": 365,
                    "right": 0,
                    "type": "positive"
                }
            }]
        }

        return data

    @staticmethod
    def campaign_structure(name, image_id: int, url_id: int):
        # return {"name": name, "read_only": False, "price": "1.55", "package_id": "451", "banners": [
        #     {"urls": {"primary": {"id": url_id}},
        #      "textblocks": {"title_25": {"text": "Vrvvfwrwrwrbe"}, "text_90": {"text": "Bebtbte"}},
        #                     'banners': [{"content": {"image_90x75": {"id": image_id}},
        #      "name": ""}]}
        return {
            'name': name,
            'objective': 'general_ttm',
            'package_id': 451,
            'price': '1.64',
            'banners': [{
                'urls': {
                    'primary': {'id': url_id}
                },
                'textblocks': {'title_25': {'text': 'Bvfbbtb'}, 'text_90': {'text': 'Bebtabaabbte'},
                               'cta_sites_full': {'text': 'visitSite'}},
                'content': {
                    'image_90x75': {
                        'id': image_id
                    }
                },
                'name': '',
            }]

        }

    def get_url(self):
        params = {
            'url': 'https://genius.com/'
        }
        response = self._request('GET', GET_URL, headers=self.headers(REF_GET_URL), params=params, jsonify=True)

        return response.get('id')

    def post_upload_file(self, file_path: callable):
        file = {
            'file': open(file_path('p.png'), 'rb'),
            'data': '{"width": 0, "height": 0}'
        }

        response = self._request('POST', LOAD_FILE, headers=self.headers(REF_LOAD_FILE),
                                 files=file, jsonify=True)
        return response.get('id')

    def post_create_campaign(self, campaign_name, file_path: callable):
        image_id = self.post_upload_file(file_path)
        url_id = self.get_url()
        data = json.dumps(self.campaign_structure(campaign_name, image_id, url_id))

        response = self._request('POST', CREATE_CAMPAIGN, headers=self.headers(REF_CREATE_CAMPAIGN), data=data, jsonify=True)
        return response.get('id')

    def post_delete_campaign(self, campaign_id):
        data = json.dumps([{
            'id': campaign_id,
            'status': 'deleted'
        }])

        response = self._request('POST', DELETE_CAMPAIGN,
                                 headers=self.headers(REF_DELETE_CAMPAIGN), data=data,
                                 expected_status=204)
        return response

    def get_campaign(self, campaign_id, expected_status):
        response = self._request('GET', GET_CAMPAIGN.format(campaign_id),
                                 headers=self.headers(REF_GET_CAMPAIGN.format(campaign_id)),
                                 expected_status=expected_status, jsonify=True)

        return response.get('name')

    def get_segment(self, segment_id, expected_status):
        response = self._request('GET', GET_SEGMENT.format(segment_id),
                                 headers=self.headers(REF_GET_SEGMENT.format(segment_id)),
                                 expected_status=expected_status, jsonify=True)

        return response.get('name')

    def _delete_segment(self, segment_id):
        response = self._request('DELETE', DELETE_SEGMENT.format(segment_id),
                                 headers=self.headers(REF_DELETE_SEGMENT), expected_status=204)

        return response


# c = ApiClient("https://target-sandbox.my.com/", "batal990@mail.ru", "9Gq*686vJcYRtK")
# # c.get_token()
# c.post_login()
#
# print(c.csrftoken)
