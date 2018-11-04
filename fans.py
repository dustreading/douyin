import json

from db.handle_db import fans_save


def response(flow):
    if 'aweme/v1/user/follower/list' in flow.request.url:
        for follower in json.loads(flow.response.text)['followers']:
            fans = dict()
            fans['short_id'] = follower['short_id']
            fans['uid'] = follower['uid']
            fans['nickname'] = follower['nickname']
            fans_save(fans)
