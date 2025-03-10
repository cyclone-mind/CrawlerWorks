import requests
import execjs
import time
import random

def u(length=8, chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'):
    return ''.join(random.choice(chars) for _ in range(length))

timer = int(time.time()*1000)

cookies = {
    'dxy_da_cookie-id': '6d54c13aefa517fcce2707b2fa89f3471732343656243',
    'Hm_lvt_5fee00bcc4c092fe5331cc51446d8be2': '1732343657',
    'HMACCOUNT': '862BC833877B77B8',
    '_ga': 'GA1.1.150388227.1732343657',
    'JUTE_SESSION_ID': 'ac4ced11-5c56-4a0a-ba26-b8804545c553',
    '_ga_LTBPLJJK75': 'GS1.1.1732343657.1.1.1732343686.0.0.0',
    'Hm_lpvt_5fee00bcc4c092fe5331cc51446d8be2': '1732343687',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=utf-8',
    # 'cookie': 'dxy_da_cookie-id=6d54c13aefa517fcce2707b2fa89f3471732343656243; Hm_lvt_5fee00bcc4c092fe5331cc51446d8be2=1732343657; HMACCOUNT=862BC833877B77B8; _ga=GA1.1.150388227.1732343657; JUTE_SESSION_ID=ac4ced11-5c56-4a0a-ba26-b8804545c553; _ga_LTBPLJJK75=GS1.1.1732343657.1.1.1732343686.0.0.0; Hm_lpvt_5fee00bcc4c092fe5331cc51446d8be2=1732343687',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.dxy.cn/bbs/newweb/pc/case/search?keyword=%E6%96%B0%E5%86%A0',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '8312a53dbcf74547b98849f99f98a4ea-8da1b147b7acf502-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-kl-ajax-request': 'Ajax_Request',
}

def spider(keyword,page):
    params = {
        'keyword': keyword,
        'sectionCode': '0',
        'pageSize': '20',
        'pageNum': str(page),
        'serverTimestamp': str(timer),
        'timestamp': str(timer+200),
        'noncestr': u(8,),
        # 'sign': 'f8d321b20903d84416c79468b6d0a86949d27f2d',
    }
    data = f'appSignKey=4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&keyword={params['keyword']}&noncestr={params['noncestr']}&pageNum={params['pageNum']}&pageSize={params['pageSize']}&sectionCode=0&serverTimestamp={params['serverTimestamp']}&timestamp={params['timestamp']}'

    sign = execjs.compile(open('./dingxiang.js', 'r', encoding='utf-8').read()).call('s',data)
    # print('sign:::',sign)
    params['sign'] = sign

    #
    response = requests.get('https://www.dxy.cn/bbs/newweb/case-bank/page-post-info', params=params, cookies=cookies, headers=headers)
    # print(response.text)
    return response.text

if __name__ == '__main__':
    keyword = '哮喘'
    page = 1
    print(spider(keyword,page))