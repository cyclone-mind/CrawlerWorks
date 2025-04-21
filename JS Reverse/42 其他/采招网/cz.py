import requests
import urllib.parse
from Crypto.Cipher import AES
import base64
from Crypto.Util.Padding import pad, unpad

headers = {
    'accept': 'text/plain, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://search.bidcenter.com.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://search.bidcenter.com.cn/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
}


def spider(keywords, page):

    data = {
        'from': '6137',
        'guid': '0c779afe-8382-463d-bfba-196bfc94fd74',
        'location': '6138',
        'token': '',
        'next_token': '',
        'keywords': urllib.parse.quote(keywords),
        'mod': '0',
        'page': str(page),
    }

    response = requests.post('https://interface.bidcenter.com.cn/search/GetSearchProHandler.ashx', headers=headers, data=data)
    # print(response)
    # print(response.text)

        # 一、 base64的解码

    encrypt_data = base64.b64decode(response.text.encode())
    # print("encrypt_data:", encrypt_data)

    # 二、解密数据
    # (1) 确认key和iv必须保证是16或者24，或者32
    key = '3zKzyf6eEfuDjAG3'.encode()
    iv = 'fyUANZ0qSNZhhNCV'.encode()
    # (2) 构建一个aes对象
    aes = AES.new(key, AES.MODE_CBC, iv)

    # (3) 对数据解密
    data = aes.decrypt(encrypt_data).decode()



    return data

def main(keywords, page):
    return spider(keywords, page)

if __name__ =="__main__":
    keywords = "无人机"
    page = 5
    res = main(keywords,page)
    print(res)
