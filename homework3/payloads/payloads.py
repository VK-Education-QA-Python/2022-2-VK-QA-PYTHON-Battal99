import json


def campaign_data(name: str, image_id: int, url_id: int):
    return json.dumps({
        'name': name,
        'max_price': '0',
        'mixing': 'fastest',
        'autobidding_mode': 'second_price_mean',
        'objective': 'general_ttm',
        'package_id': 451,
        'read_only': False,
        'enable_utm': True,
        'banners': [{
            'urls': {
                'primary': {'id': url_id}
            },
            'textblocks': {'title_25': {'text': 'Bfrvfbbtb'},
                           'text_90': {'text': 'Bebtabae'}},
            'content': {
                'image_90x75': {
                    'id': image_id
                }
            },
            'name': ''
        }]

    })


def segment_data_vk_group(name, vk_group_id=None):
    data = {
        "name": name,
        "logicType": "or",
        "pass_condition": 1,
        "relations": [{
            "object_type": "remarketing_vk_group",
            "params": {
                'source_id': vk_group_id,
                "type": "positive"
            }
        }]
    }

    return data


def segment_data_games(name):
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
