# -*- coding: utf-8 -*-
import requests
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.endata.com.cn",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}
url = "https://www.endata.com.cn/API/GetData.ashx"
data = {
    "year": "2024",
    "MethodName": "BoxOffice_GetYearInfoData"
}
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)

with open('./02 艺恩.js',encoding='utf-8') as f:
    js_file = f.read()

decrypted_data = execjs.compile(js_file).call('get_data',response.text)
print(decrypted_data)