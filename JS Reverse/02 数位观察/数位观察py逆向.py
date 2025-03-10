# -*- coding: utf-8 -*-
import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://www.swguancha.com',
    'Referer': 'https://www.swguancha.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'deviceType': '1',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'size': 6,
    'current': 4,
    'propertyCode': [
        'DISTRICT_PROP_GJ025_RJDQSCZZ',
        'DISTRICT_PROP_GJ117_NMSYGGQDCYYCLS',
        'DISTRICT_PROP_GJ001_NMHJRK',
    ],
    'dimensionTime': '2019',
    'levelType': 2,
}

response = requests.post('https://app.swguancha.com/client/v1/cPublic/consumer/baseInfo', headers=headers, json=json_data)

# print(response.text)

# 设置key
key = 'QV1f3nHn2qm7i3xrj3Y9K9imDdGTjTu9'.encode()

# 构建算法对象
aes = AES.new(key, AES.MODE_ECB)
# 定义需要解密的数据
base64_encrypt_data = response.text
# 先将字符串转为字节，再进行base64的转码
encrypt_data = base64.b64decode(base64_encrypt_data.encode())
# 对转码后的字节进行解密
data = aes.decrypt(encrypt_data).decode()
# 对解密后的字节数据进行填充
# data = unpad(data).decode()
print(data)