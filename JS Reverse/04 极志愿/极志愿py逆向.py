# -*- coding: utf-8 -*-
import requests
from hashlib import md5
import urllib.parse
import time

ts = round(time.time() * 1000)
# print(ts)
cookies = {
    'PI': '44',
    'Hm_lvt_2610e5c202b60841b30a62960fbef0ad': '1722954442,1722994638,1723448670',
    'Hm_lpvt_2610e5c202b60841b30a62960fbef0ad': '1723448670',
    'HMACCOUNT': 'BA51EFD0C63D01A7',
}
params = {
    'page': '3',
    'page_len': '20',
    'diploma_id': '7',
    'wenli': '0',
    'app_id': '98357f659cf8fb6001cff80f7c6b85f2',
    'ts': ts,
    'platform': 'desktop',
    'v': '210',
}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'cookie': 'PI=44; Hm_lvt_2610e5c202b60841b30a62960fbef0ad=1722954442,1722994638,1723448670; Hm_lpvt_2610e5c202b60841b30a62960fbef0ad=1723448670; HMACCOUNT=BA51EFD0C63D01A7',
    'priority': 'u=1, i',
    'referer': 'https://www.jizhy.com/44/rank/school',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}


def sort_params(params):
    l = sorted(params.items(), key=lambda i: i[0])
    d = dict(l)
    # print(d)

    s = urllib.parse.urlencode(d)
    s = "{" + s + "}" + "&key=146fd1e66513611ac7af69f21f1d7725"
    return s


def get_sign(s):
    # 创建摘要对象
    obj = md5()
    # 对摘要进行加密
    obj.update(s.encode('utf-8'))
    # 返回加密数据
    return obj.hexdigest().upper()


s = sort_params(params)
sign = get_sign(s)
print("sign::", sign)
params['sign'] = sign

response = requests.get('https://www.jizhy.com/open/sch/rank-list', params=params, cookies=cookies, headers=headers)
print(response.text)
