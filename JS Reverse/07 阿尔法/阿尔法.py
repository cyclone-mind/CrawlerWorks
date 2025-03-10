# -*- coding: utf-8 -*-
# 使用update更新字典data.update(val)

import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

cookies = {
    'gitblock-session-id': 'lraah3fquqplillw1555enbd',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://aerfaying.com',
    'Connection': 'keep-alive',
    'Referer': 'https://aerfaying.com/',
    # 'Cookie': 'gitblock-session-id=lraah3fquqplillw1555enbd',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=0',
}

data = {
    'username': 'asdas22',
    'password': '1231456',
    # 't': '1727280247180',
    # 's': '0a364dd10397bbcc7e3c6c742da382974962c548',
}

val = execjs.compile(open('阿爾法.js', 'r', encoding='utf-8').read()).call('get_s', data['username'], data['password'])
# print(val)
data.update(val)
print(data)
response = requests.post('https://aerfaying.com/WebApi/Users/Login', cookies=cookies, headers=headers, data=data)
print(response.text)