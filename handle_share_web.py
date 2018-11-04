import requests
import re
from lxml import etree
from scrapy.selector import Selector
from db.handle_db import handle_get_task, insert_to_db
from splash.server import crawl

def handle_decode(input_data):
    regex_list = [
        {'unicode':['\ue60d', '\ue603', '\ue616'], 'value':'0'},
        {'unicode':['\ue602', '\ue60e', '\ue618'], 'value':'1'},
        {'unicode':['\ue605', '\ue610', '\ue617'], 'value':'2'},
        {'unicode':['\ue604', '\ue611', '\ue61a'], 'value':'3'},
        {'unicode':['\ue606', '\ue60c', '\ue619'], 'value':'4'},
        {'unicode':['\ue607', '\ue60f', '\ue61b'], 'value':'5'},
        {'unicode':['\ue608', '\ue612', '\ue61f'], 'value':'6'},
        {'unicode':['\ue60a', '\ue613', '\ue61c'], 'value':'7'},
        {'unicode':['\ue60b', '\ue614', '\ue61d'], 'value':'8'},
        {'unicode':['\ue609', '\ue615', '\ue61e'], 'value':'9'},
        ]
    for num_map in regex_list:
        for uni in num_map['unicode']:
            input_data = re.sub(uni, num_map['value'], input_data)
    return input_data

def handle_douyin_web_share(task):
    url = 'https://www.iesdouyin.com/share/user/%s'%task['share_id']
    response = crawl(url)
    decode_page = handle_decode(response.text)
    html = etree.HTML(decode_page)

    user = {}

    user['shareid'] = task['share_id']
    user['nickname'] = str(html.xpath('//*[@id="pagelet-user-info"]/div[2]/div[1]/p[1]/text()')[0])
    user['shortid'] = "".join(html.xpath('//*[@id="pagelet-user-info"]/div[2]/div[1]/p[2]')[0].xpath('string(.)').split()[1:])
    user['info'] = str(html.xpath('//*[@id="pagelet-user-info"]/div[2]/div[2]/p[1]/text()')[0])
    try:
        user['verify'] = ",".join(html.xpath('//*[@id="pagelet-user-info"]/div[2]/div[2]/div')[0].xpath('string(.)').split())
    except:
        pass
    user['location'] = str(html.xpath('//*[@id="pagelet-user-info"]/div[2]/div[2]/p[2]/span[1]/text()')[0])
    user['constellation'] = str(html.xpath('//*[@id="pagelet-user-info"]/div[2]/div[2]/p[2]/span[2]/text()')[0])
    user['focus'] = "".join(html.xpath('//*[@id="pagelet-user-info"]/div[2]/div[2]/p[3]/span[1]/span[1]')[0].xpath('string(.)').split())
    user['follower'] = "".join(html.xpath('//*[@id="pagelet-user-info"]/div[2]/div[2]/p[3]/span[2]/span[1]')[0].xpath('string(.)').split())
    user['liked'] = "".join(html.xpath('//*[@id="pagelet-user-info"]/div[2]/div[2]/p[3]/span[3]/span[1]')[0].xpath('string(.)').split())
    user['video'] = "".join(html.xpath('//*[@id="pagelet-user-info"]/div[3]/div/div[1]/span')[0].xpath('string(.)').split())
    user['like'] = "".join(html.xpath('//*[@id="pagelet-user-info"]/div[3]/div/div[2]/span')[0].xpath('string(.)').split())

    print(user)
    return user

if __name__ == '__main__':
    while True:
        task = handle_get_task()
        user = handle_douyin_web_share(task)
        insert_to_db(user)