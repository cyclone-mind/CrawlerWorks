# -*- coding: utf-8 -*-
import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

cookies = {
    'Hm_lvt_cadcf695428f7859d9d5e5d7bd270572': '1724489950,1725200690',
    'HMACCOUNT': 'BA51EFD0C63D01A7',
    'SHOW_ACTIVITY_PANEL': 'false',
    'Hm_lpvt_cadcf695428f7859d9d5e5d7bd270572': '1725202147',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'cookie': 'Hm_lvt_cadcf695428f7859d9d5e5d7bd270572=1724489950,1725200690; HMACCOUNT=BA51EFD0C63D01A7; SHOW_ACTIVITY_PANEL=false; Hm_lpvt_cadcf695428f7859d9d5e5d7bd270572=1725202147',
    'priority': 'u=1, i',
    'referer': 'https://www.fnscore.cn/score-basketball.html',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

enc_params = execjs.compile(open('./蜂鸟竞技.js').read()).call("get_params")
timestamp = enc_params['timestamp']
sign = enc_params['sign']
print("timestamp:::",timestamp)
print("sign",sign)
params = {
    'gameType': '5',
    'date': '2024-08-20',
    'hot': 'false',
    'onlyAnchor': 'false',
    'token': '',
    'timestamp': timestamp,
    'sign': sign,
}

response = requests.get('https://www.fnscore.cn/api/score/getListByDate', params=params, cookies=cookies, headers=headers)
print(response.text)