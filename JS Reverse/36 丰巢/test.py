import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'https://www.fcbox.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.fcbox.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

cookies = {
    'Hm_lvt_bf8738513d38a2418063f7b873084c15': '1734765429',
    'Hm_lpvt_bf8738513d38a2418063f7b873084c15': '1734765429',
    'HMACCOUNT': '9BFBEC200A822004',
    'Hm_lvt_753eeeff229f4510294f196bd27291b5': '1734765429',
    'Hm_lpvt_753eeeff229f4510294f196bd27291b5': '1734765429',
    '_2a12e': 'http://172.29.107.23:8080',
}


def get_public_key():
    cookies = {
        'Hm_lvt_bf8738513d38a2418063f7b873084c15': '1734765429',
        'Hm_lpvt_bf8738513d38a2418063f7b873084c15': '1734765429',
        'HMACCOUNT': '9BFBEC200A822004',
        'Hm_lvt_753eeeff229f4510294f196bd27291b5': '1734765429',
        'Hm_lpvt_753eeeff229f4510294f196bd27291b5': '1734765429',
        '_2a12e': 'http://172.29.107.23:8080',
    }
    response = requests.post('https://www.fcbox.com/noshiro/getPublicKey', cookies=cookies, headers=headers)
    return response.json()['data']


print(get_public_key())
