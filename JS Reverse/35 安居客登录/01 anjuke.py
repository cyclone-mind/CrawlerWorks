import requests
import uuid
import time
import re
import ddddocr

timer = str(int(time.time() * 1000))
# 生成一个随机的UUID
generated_uuid = uuid.uuid4()

# print(generated_uuid)
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://api.anjuke.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def parse_load():
    params = {
        'captcha_id': 'ffe7f7735b0bc016e927b3241b090995',
        'challenge': generated_uuid,
        'client_type': 'web',
        'lang': 'zho',
        'callback': f'geetest_{timer}',
    }
    response = requests.get('https://gcaptcha4.geetest.com/load', params=params, headers=headers)
    json_str = response.text
    match = re.search(r'"payload"\s*:\s*"([^"]+)"', json_str)
    payload = match.group(1)
    match = re.search(r'"process_token"\s*:\s*"([^"]+)"', json_str)
    process_token = match.group(1)
    match = re.search(r'"slice"\s*:\s*"([^"]+)"', json_str)
    front_url = match.group(1)
    match = re.search(r'"bg"\s*:\s*"([^"]+)"', json_str)
    bg_url = match.group(1)
    match = re.search(r'"lot_number"\s*:\s*"([^"]+)"', json_str)
    lot_number = match.group(1)
    return payload, process_token, front_url, bg_url, lot_number
    # print(response.text)
    # print(response)
def parse_slide(bg_url, fg_url):
    bg_url = f'https://static.geetest.com/{bg_url}'
    fg_url = f'https://static.geetest.com/{fg_url}'
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

def main():
    payload, process_token, front_url, bg_url, lot_number = parse_load()
    print("payload:::", payload)
    print("process_token:::", process_token)
    print("front_url:::", front_url)
    print("bg_url:::", bg_url)
    slide_distance = parse_slide(bg_url, front_url)
    print("slide_distance:::", slide_distance)


if __name__ == '__main__':
    main()
    pass
