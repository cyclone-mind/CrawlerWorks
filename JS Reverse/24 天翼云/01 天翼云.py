# -*- coding: utf-8 -*-
import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "csm": "d103b53abd2922aa7ff4c44b80a32337c5436efaa969afd870bf87db0c5e6c1e",
    "cst": "1726585424596",
    "origin": "https://www.ctyun.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.ctyun.cn/h5/auth/login",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-ctyun-accesstoken": "null",
    "x-riskdevicesign": "b6a6a45cbb6ee258aba384112d89df9f"
}
cookies = {
    "ct_tgc": "1e814f31-db42-468e-9440-4e826247a0f3",
    "ct_m_search_from": "bing",
    "ct_m_sid1": "1726585309578-nuSWWK8qqW",
    "ct_m_sid2": "1726585309578-nuSWWK8qqW",
    "ct_m_dvc_id": "b6a6a45cbb6ee258aba384112d89df9f",
    "vid": "3gQ20Oq2YGW18keAcnnCvFTMFNWBDTXjq1yqyK9HhHQunF1YVTKbeDVs37vz9kWQ",
    "Hm_lvt_4b4ce93f1c92033213556e55cb65769f": "1726585313",
    "HMACCOUNT": "29F50534414B0FBE",
    "Hm_lpvt_4b4ce93f1c92033213556e55cb65769f": "1726585330",
    "ct_m_pvid": "5",
    "JSESSIONID": "1bdfddrq51cz1tmx5jewgn7bv",
    "ct_m_cat2_time": "1726585424585",
    "ct_m_cat2_id": "10001.0.3",
    "ct_m_label_id": "10"
}
url = "https://www.ctyun.cn/gw/auth/Login"
account_1 = "295448@qq.com"
account_2 = account_1.replace('@','%40')
pwd = '13215154'
data = {
    "id": account_1,
    "loginFree": "false",
    "loginType": "password",
    "newMode": "true",
    # "other": "29518%40qq.com",
    # "password": "Zhnby1L1t2xU3evf/d9A/A=="
}
with open('./02 天翼云.js') as f:
    js_file = f.read()
enc_pwd = execjs.compile(js_file).call('get_pwd',account_2,pwd)
data['other'] = account_2
data['password'] = enc_pwd
# print(data)
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)