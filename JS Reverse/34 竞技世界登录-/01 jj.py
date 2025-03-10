import requests
import time
import re
import ddddocr
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://login.jj.cn/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}


def parse_config():
    timer = str(int(time.time() * 1000))
    params = [
        ('business_id', 'b8beba75fedf7b18611359fe84afb8b8'),
        ('appid', '501'),
        ('hd', 'false'),
        ('ts', timer),
        ('blid', '1'),
        ('plid', '1'),
        ('cfp', 'b3a49292'),
        ('ts', timer),
        ('callback', '__jjsecurity_0'),
    ]

    response = requests.get('https://captcha.srv.jjmatch.cn/v3/config', params=params, headers=headers)
    cfp = response.cookies.get_dict()['Session_b8beba75fedf7b18611359fe84afb8b8']
    json_str = response.text
    match = re.search(r'"challenge"\s*:\s*"([^"]+)"', json_str)
    challenge = match.group(1)
    return cfp, challenge


def parse_get_business_id(cfp, challenge):
    timer = str(int(time.time() * 1000))
    params = {
        'business_id': 'b8beba75fedf7b18611359fe84afb8b8',
        'appid': '501',
        'challenge': challenge,
        'blid': '1',
        'plid': '1',
        'cfp': cfp,
        'ts': timer,
        'hd': 'false',
        'callback': '__jjsecurity_1',
    }
    response = requests.get('https://captcha.srv.jj.cn/v3/get', params=params, headers=headers)
    json_str = response.text
    match = re.search(r'"coverimg"\s*:\s*"([^"]+)"', json_str)
    front_url = match.group(1)
    match = re.search(r'"img"\s*:\s*"([^"]+)"', json_str)
    bg_url = match.group(1)
    return front_url, bg_url


def parse_slide(bg_url, fg_url):
    bg_url = f'https://jj-sec-captcha.cache.jj.cn/{bg_url}'
    fg_url = f'https://jj-sec-captcha.cache.jj.cn/{fg_url}'
    with open('./x1-bg.jpg', 'wb') as f:
        f.write(requests.get(bg_url).content)
    with open('./x2-fg.jpg', 'wb') as f:
        f.write(requests.get(fg_url).content)
    with open('./x1-bg.jpg', 'rb') as f:
        bg_bytes = f.read()
    with open('./x2-fg.jpg', 'rb') as f:
        front_bytes = f.read()
    ocr = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    result = ocr.slide_match(target_bytes=front_bytes,
                             background_bytes=bg_bytes, simple_target=True)
    slide_distance = result['target'][0]
    return int(slide_distance)


# def parse_traceData(slide_distance, pointY):
#     traceData = []
#     x = 0
#     y = pointY
#     t = int(time.time()*1000)


def main(username, password):
    cfp, challenge = parse_config()
    print("cfp:::", cfp)
    print("challenge:::", challenge)
    front_url, bg_url = parse_get_business_id(cfp, challenge)
    print("front_url:::", front_url)
    print("bg_url:::", bg_url)
    slide_distance = parse_slide(bg_url,front_url)
    print(slide_distance)
    # parse_traceData()



if __name__ == '__main__':
    username = "admin"
    password = 'asd123'
    main(username, password)
    pass
