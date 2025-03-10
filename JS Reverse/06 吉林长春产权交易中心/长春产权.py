# -*- coding: utf-8 -*-
# 这个使用encrypt关键字定位加密入口。把相关的js代码全扣下来，缺什么补什么。注意对加密参数对象进行了两次JSON.stringfy处理

import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'text/xml;charset=UTF-8',
    'Origin': 'https://www.ccprec.com',
    'Referer': 'https://www.ccprec.com/navCqzr/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
page = 2
enrcypt_params = execjs.compile(open('长春产权.js', 'r', encoding='utf-8').read()).call('enc_page',page)

response = requests.post('https://www.ccprec.com/honsanCloudAct', headers=headers, data=enrcypt_params)
decrypt_data = execjs.compile(open('长春产权.js', 'r', encoding='utf-8').read()).call('decryptCode',response.text)
print(decrypt_data)