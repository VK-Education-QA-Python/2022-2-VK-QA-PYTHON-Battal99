import pytest

from builder import Builder
from utils import file_path


class ApiBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        self.builder = Builder()

        self.api_client.post_login()

    @pytest.fixture()
    def target_object_names(self):
        target_name = self.builder.target_names()

        yield target_name

    def create_segment(self, segment_name):
        segment_id = self.api_client.post_create_segment(segment_name)

        return segment_id

    def create_campaign(self, campaign_name):
        campaign_id = self.api_client.post_create_campaign(campaign_name, file_path)

        return campaign_id

    def delete_campaign(self, campaign_id):

        return self.api_client.post_delete_campaign(campaign_id)

    def delete_segment(self, segment_id):

        return self.api_client._delete_segment(segment_id)

    # def check_campaign(self, campaign_id, campaign_name):
    #     return self.api_client.get_campaign(campaign_id, 200) == campaign_name
    #
    # def check_segment(self, segment_id, segment_name):
    #     return self.api_client.get_segment(segment_id, 200) == segment_name
