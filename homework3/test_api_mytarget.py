import pytest

from base import ApiBase


class TestApi(ApiBase):

    # @pytest.mark.API
    # def test_create_campaign(self, target_object_names):
    #     campaign_id = self.create_campaign(target_object_names.campaign_name)
    #
    #     assert self.api_client.get_campaign(campaign_id, 200) == target_object_names.campaign_name
    #
    #     self.delete_campaign(campaign_id)

    @pytest.mark.API
    def test_create_segment(self, target_object_names):
        segment_id = self.create_segment(target_object_names.segment_name)

        assert self.api_client.get_segment(segment_id, 200) == target_object_names.segment_name

        assert self.delete_segment(segment_id)

    @pytest.mark.API
    def test_delete_segment(self, target_object_names):
        segment_id = self.create_segment(target_object_names.segment_name)

        assert self.delete_segment(segment_id)

        assert not self.api_client.get_segment(segment_id, 404)

    @pytest.mark.API
    def test_create_vk_group_segment(self, target_object_names):
        segment_id = self.create_segment(target_object_names.segment_name, 'vk_group')

        assert self.api_client.get_segment(segment_id, 200) == target_object_names.segment_name

        assert self.delete_segment(segment_id)

        assert not self.api_client.get_segment(segment_id, 404)
