# https://class.imooc.com/
import requests

cookies = {
    'imooc_uuid': '879e0bb5-d5e9-4951-a9f2-53fea377d056',
    'imooc_isnew': '1',
    'imooc_isnew_ct': '1739626383',
    'sajssdk_2015_cross_new_user': '1',
    'MEIQIA_TRACK_ID': '2t4zyCbtukZ3JiwDPrfapPljJ0Y',
    'MEIQIA_VISIT_ID': '2t4zyBblHnufnj1lkLsv2ym7c5v',
    'PSEID': '2c21c31e3cbcf3f67fd3dc8381316f2a',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2211655718%22%2C%22first_id%22%3A%2219509d00bc8fc4-00117cf1e214a608-26011a51-2073600-19509d00bc9107e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk1MDlkMDBiYzhmYzQtMDAxMTdjZjFlMjE0YTYwOC0yNjAxMWE1MS0yMDczNjAwLTE5NTA5ZDAwYmM5MTA3ZSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjExNjU1NzE4In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2211655718%22%7D%2C%22%24device_id%22%3A%2219509d00bc8fc4-00117cf1e214a608-26011a51-2073600-19509d00bc9107e%22%7D',
    'Hm_lvt_f0cfcccd7b1393990c78efdeebff3968': '1739626566',
    'HMACCOUNT': '34854ED221F6ECA3',
    'Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968': '1739626571',
    'cvde': '67b0978f4095c-12',
    'tgw_l7_route': '1af5f87d28570c08c7ec9d46f7d0ffcc',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.imooc.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.imooc.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'imooc_uuid=879e0bb5-d5e9-4951-a9f2-53fea377d056; imooc_isnew=1; imooc_isnew_ct=1739626383; sajssdk_2015_cross_new_user=1; MEIQIA_TRACK_ID=2t4zyCbtukZ3JiwDPrfapPljJ0Y; MEIQIA_VISIT_ID=2t4zyBblHnufnj1lkLsv2ym7c5v; PSEID=2c21c31e3cbcf3f67fd3dc8381316f2a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211655718%22%2C%22first_id%22%3A%2219509d00bc8fc4-00117cf1e214a608-26011a51-2073600-19509d00bc9107e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk1MDlkMDBiYzhmYzQtMDAxMTdjZjFlMjE0YTYwOC0yNjAxMWE1MS0yMDczNjAwLTE5NTA5ZDAwYmM5MTA3ZSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjExNjU1NzE4In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2211655718%22%7D%2C%22%24device_id%22%3A%2219509d00bc8fc4-00117cf1e214a608-26011a51-2073600-19509d00bc9107e%22%7D; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1739626566; HMACCOUNT=34854ED221F6ECA3; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1739626571; cvde=67b0978f4095c-12; tgw_l7_route=1af5f87d28570c08c7ec9d46f7d0ffcc',
}

data = {
    'username': '18701918314',
    'password': '1tfmYRxtvRKGIoYa/9/20feKudOLioKwh7LweM/4MfmNEs4HG+B/NtMH5nKnXC0PdT0e9NkAykSlTb52HLStVNBmZxz1g5mHXrk3iggmJR0KnVRMETKa9fVDTaA8dAyx7EdY34Wjt+1YC0m/K72ZFLditk8+W0fFjWJo07wxwsc=',
    'verify': '',
    'remember': '1',
    'pwencode': '1',
    'browser_key': 'e65a49fc0bd95fc756b6d9161f738bab',
    'referer': 'https://www.imooc.com',
}

response = requests.post('https://www.imooc.com/passport/user/login', cookies=cookies, headers=headers, data=data)
print(response)
print(response)