import requests
# import subprocess
# from functools import partial
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

cookies = {
    'SUNWAY-ESCM-COOKIE': 'ce0e0b80-eddd-4ff6-ace9-85f10614a188',
    '__jsluid_s': '5f1b67bf6d0e45240c62a85f29e205e8',
    'JSESSIONID': '71765FE01D32323CC7144585531BE975',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': 'SUNWAY-ESCM-COOKIE=ce0e0b80-eddd-4ff6-ace9-85f10614a188; __jsluid_s=5f1b67bf6d0e45240c62a85f29e205e8; JSESSIONID=71765FE01D32323CC7144585531BE975',
    'Origin': 'https://ec.minmetals.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ec.minmetals.com.cn/open/home/purchase-info',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'X-KL-Ajax-Request': 'Ajax_Request',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
# 第一次请求拿到publickey
response = requests.post('https://ec.minmetals.com.cn/open/homepage/public', cookies=cookies, headers=headers)
# print(response.text)

publickey = response.text
page = 2

# 第二次请求完成参数加密并返回数据
enc_param = execjs.compile(open('五矿.js', 'r', encoding='utf-8').read()).call('enc_param', page, publickey)

# print(enc_param)
json_data = {
    'param': enc_param
}

response = requests.post(
    'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.text)
