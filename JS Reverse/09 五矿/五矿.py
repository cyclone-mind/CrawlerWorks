# -*- coding: utf-8 -*-
"""五矿难点
(1)入口基于路径搜索，异步操作。控制流，上一个case的返回值是下一个case的sent
(2)loader的一个初始化开关没有关上，导致大量补环境
(3)公钥是一个动态获取的值
"""
import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

# (1)请求得到PublicKey
import requests

cookies = {
    '__jsluid_s': 'afc12e93977012467d867f60f5cff9ae',
    'Hm_lvt_f32803886966beff8fa513f7a33dea1e': '1724663167',
    'SUNWAY-ESCM-COOKIE': 'e0afd46b-bc3e-473d-8b02-3c19cb61ee60',
    'JSESSIONID': '5B1FBB7FAE5B3576DEC961E048EB506F',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': '__jsluid_s=afc12e93977012467d867f60f5cff9ae; Hm_lvt_f32803886966beff8fa513f7a33dea1e=1724663167; SUNWAY-ESCM-COOKIE=e0afd46b-bc3e-473d-8b02-3c19cb61ee60; JSESSIONID=5B1FBB7FAE5B3576DEC961E048EB506F',
    'Origin': 'https://ec.minmetals.com.cn',
    'Referer': 'https://ec.minmetals.com.cn/logonAction.do',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.post('https://ec.minmetals.com.cn/open/homepage/public', cookies=cookies, headers=headers)
print("publickey:::",response.text)
key = response.text
# (2)第二次请求，带着加密的参数。
cookies = {
    '__jsluid_s': 'afc12e93977012467d867f60f5cff9ae',
    'SUNWAY-ESCM-COOKIE': 'f2fb7699-a6ce-412f-88ff-7bac4a4c2f90',
    'JSESSIONID': 'EE3CC05E1561D23956E60469EDC77A39',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': '__jsluid_s=afc12e93977012467d867f60f5cff9ae; SUNWAY-ESCM-COOKIE=f2fb7699-a6ce-412f-88ff-7bac4a4c2f90; JSESSIONID=EE3CC05E1561D23956E60469EDC77A39',
    'Origin': 'https://ec.minmetals.com.cn',
    'Referer': 'https://ec.minmetals.com.cn/open/home/purchase-info?tabIndex=0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
page = 4
enc_params = execjs.compile(open('./五矿.js').read()).call("get_params",page,key)
json_data = {
    'param': enc_params,
}

response = requests.post(
    'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)