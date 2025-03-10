import requests
import base64
import json
import time
from Crypto.Util.Padding import pad, unpad

from Crypto.Cipher import AES

import requests

cookies = {
    'ASP.NET_SessionId': 'yia0gk1jwug2xfesgxkqoc3u',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=yia0gk1jwug2xfesgxkqoc3u',
    'Origin': 'https://ggzyfw.fj.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ggzyfw.fj.gov.cn/index/new/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'portal-sign': '48197d57e016b17190a66082bb9e009b',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = {
    'pageSize': 8,
    'type': '12',
    'ts': int(time.time() * 1000),
}

response = requests.post('https://ggzyfw.fj.gov.cn/FwPortalApi/Article/PageList', cookies=cookies, headers=headers,
                         json=json_data)

print(response.text)

#base64_encrypt_data = response.json().get("Data")

# # 一、 base64的解码
#
# encrypt_data = base64.b64decode(base64_encrypt_data)
# print("encrypt_data:", encrypt_data)
#
# # 二、解密数据
# # (1) 确认key和iv必须保证是16或者24，或者32
# key = 'EB444973714E4A40876CE66BE45D5930'.encode()
# iv = 'B5A8904209931867'.encode()
# # (2) 构建一个aes对象
# aes = AES.new(key, AES.MODE_CBC, iv)
#
# # (3) 对数据解密
# data = aes.decrypt(encrypt_data)
# data = unpad(data, 16).decode()
# data = json.loads(data).get("Table")
# # print(data)
# for i in data:
#     print(i)
