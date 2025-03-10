# -*- coding: utf-8 -*-
import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

with open('./02 同花顺.js',encoding='utf-8') as f:
    js_file = f.read()
enc_cookies = execjs.compile(js_file).call('get_cookie')

headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://q.10jqka.com.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "hexin-v": enc_cookies,
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

cookies = {
    "v": enc_cookies
}
url = "https://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/2/ajax/1/"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)