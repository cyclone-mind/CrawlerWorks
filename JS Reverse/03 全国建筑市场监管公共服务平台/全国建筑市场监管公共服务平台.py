# -*- coding: utf-8 -*-
import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import json

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1722957003,1722998757',
    'HMACCOUNT': 'BA51EFD0C63D01A7',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1722999632',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1722957003,1722998757; HMACCOUNT=BA51EFD0C63D01A7; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1722999632',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'accessToken': '',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timeout': '30000',
    'v': '231012',
}

params = {
    'pg': '2',
    'pgsz': '15',
    'total': '0',
}

response = requests.get(
    'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list',
    params=params,
    cookies=cookies,
    headers=headers,
)
encrypted_data = response.text
# print(encrypted_data)

data = execjs.compile(open('./jzjg.js', encoding='utf-8').read()).call('b', encrypted_data)
data = json.loads(data)
print(type(data))
# print(data.get('data').get('list'))

for i in data.get('data').get('list'):
    print(i)