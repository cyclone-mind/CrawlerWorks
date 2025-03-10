# -*- coding: utf-8 -*-
import requests
import json
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://pv4y-pc.youzy.cn',
    'Referer': 'https://pv4y-pc.youzy.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'u-token': '',
}

json_data = {
    'keyword': '',
    'provinceNames': [],
    'natureTypes': [],
    'eduLevel': '',
    'categories': [],
    'features': [],
    'pageIndex': 5,
    'pageSize': 20,
    'sort': 11,
}

sign = execjs.compile(open("优志愿.js").read()).call("get_sign",json_data)

json_data = json.dumps(json_data, separators=(",", ":"))

print("sign:::", sign)

headers["u-sign"] = sign

response = requests.post(
    'https://uwf7de983aad7a717eb.youzy.cn/youzy.dms.basiclib.api.college.query',
    headers=headers,
    data=json_data,
)
print(response.json())
