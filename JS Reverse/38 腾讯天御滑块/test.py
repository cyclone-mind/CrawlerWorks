import requests
import base64
import json

def parse_slide_url(img_url, img_name):
    url = "https://turing.captcha.qcloud.com"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://cloud.tencent.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(url + img_url, headers=headers)
    with open(f'{img_name}.jpg', 'wb') as f:
        # print(f'{img_name}下载成功')
        f.write(response.content)
    return

def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""


def get_slide_x():
    img_path = "./x1-backgroud_img.jpg"
    distance = base64_api(uname='cece', pwd='Aa12345678', img=img_path, typeid=34)
    return int(distance) - 18


img_url = "/cap_union_new_getcapbysig?img_index=1&image=02790500008adf3a0000000bb9ea824430bf&sess=s0jTVyToIJO393ewo1B1SI4ntF5I4K6JdU3bxuKiakG9kNS0NIKQBTZ6_i8CSfdkVHA79fPlSlZ2BZJBvJmLZ6Q-tr2H24qJWVbvESmXkJYAIuy4Qycp8V3YOn2EGKWVQ7rOVqwipJqKnvjbozGQi-tix-SkkeLUePWRwqkI73qhHz-1iCH54y2vPXFaqNi_qfENaIb0HQILUu83reDG8WdwREe9ArCflgRChkCiUl6AJOa-TTO57deuTKCP5BZ5ePSlhWA_CggtX1swHdiDu6sY7Se8G3m4V7T0dGG7nOvuD13q7r9uhsGw0fuOb8TaPeQO7v2E-qBqbCd9kprqgjOhMeDglz3rAhuIJY96NdnWYP4SuM-2KHfeV5G6oqJlDrRsf8CwTRI0is4kV8b0LPxWK0UGXp3IbYPQTsj9qRcD0TLAQif1YVDWnkpB9JP7VW"

parse_slide_url(img_url, 'x1-backgroud_img')

x = get_slide_x()
print("x:::",x)
