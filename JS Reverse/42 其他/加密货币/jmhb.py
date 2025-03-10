"""
稍微注意一下，发现解密用到两个参数：解密数据和headers.user。后者是响应头里面的user，可通过response.headers取出，不用管是如何加密的。
"""
import requests
import execjs
import time
timer = str(int(time.time()))
headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'cache-ts': timer,
    'encryption': 'true',
    'language': 'zh',
    'origin': 'https://www.coinglass.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.coinglass.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

def spider(page):
    global decrypted_data
    params = {
        'sort': '',
        'order': '',
        'keyword': '',
        'pageNum': str(page),
        'pageSize': '20',
        'ex': 'all',
    }

    response = requests.get('https://capi.coinglass.com/api/home/v2/coinMarkets', params=params, headers=headers)
    # print(response.text)
    # print(response.headers.get('user'))

    enc_data = response.json()
    user = response.headers.get('user')
    #
    with open('./jmhb.js', 'r', encoding='utf-8') as f:
        js_code = f.read()

    # Compile JS and prepare decrypt function
    ctx = execjs.compile(js_code)

    # Pass the response data and params to decrypt
    response_text = response.text
    try:
        decrypted_data = ctx.call('decrypt', enc_data,user)
        print("Decrypted Data:", decrypted_data)
    except Exception as e:
        print("Error during decryption:", e)

    return decrypted_data

if __name__ == '__main__':
    spider(2)

