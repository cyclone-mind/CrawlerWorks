# -*- coding: utf-8 -*-
import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import json

cookies = {
    '__c': '1726574421',
    'wd_guid': '9ba0fac0-80b1-4b34-a731-d7f8bee11e58',
    '__g': '-',
    'historyState': 'state',
    'Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e': '1726574423',
    'HMACCOUNT': '29F50534414B0FBE',
    '__l': 'r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fapi_to%2Fhome%2Frec.json%3Fb%3DqYt5JDhL0CyTFEiKHZ0rMw~~%26kiv%3D45nMwBdsHP1fwZzo',
    '__a': '33410151.1726574421..1726574421.4.1.4.4',
    'Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e': '1726574504',
    'wbrwsid': '45774860',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    # 'cookie': '__c=1726574421; wd_guid=9ba0fac0-80b1-4b34-a731-d7f8bee11e58; __g=-; historyState=state; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1726574423; HMACCOUNT=29F50534414B0FBE; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fapi_to%2Fhome%2Frec.json%3Fb%3DqYt5JDhL0CyTFEiKHZ0rMw~~%26kiv%3D45nMwBdsHP1fwZzo; __a=33410151.1726574421..1726574421.4.1.4.4; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1726574504; wbrwsid=45774860',
    'href': 'https://www.kanzhun.com/search?cityCode=101020100&experienceId=&pageNum=1&query=python&salaryId=&type=5',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kanzhun.com/search?cityCode=101020100&experienceId=&pageNum=1&query=python&salaryId=&type=5',
    'reqsource': 'fe',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceid': 'F-dfbb2eahZttl4j12',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

n = {"query":"python",
          "cityCode":"101210100",
          "salaryId":"",
          "experienceId":"",
          "pageNum":1,
          "limit":15
}
n_str = json.dumps(n)
with open('./02 看准.js',encoding='utf-8') as f:
    js_file = f.read()
list = execjs.compile(js_file).call('get_data',n_str)
b = list[0]
kiv = list[1]
print(b)
print(kiv)


params = {
    'b': b,
    'kiv': kiv,
}

response = requests.get('https://www.kanzhun.com/api_to/search/job.json', params=params, cookies=cookies, headers=headers)
# print(response.text)
print(response)
res_data = execjs.compile(js_file).call('get_res',response.text,kiv)
print(res_data)
