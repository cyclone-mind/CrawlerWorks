import base64
import random
import time
import execjs
import requests
import execjs
import json
from PIL import Image
from io import BytesIO


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


def parse_auth():
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-cn",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://jiagu.360.cn",
        "Referer": "https://jiagu.360.cn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://captcha.jiagu.360.cn/api/v3/auth"
    data = execjs.compile(open('./02 天御.js', 'r', encoding='utf-8').read()).call('parse_auth')
    response = requests.post(url, headers=headers, data=data)
    # print(response.json())
    k = response.json()['data']['k']
    captchaId = response.json()['data']['captchaId']
    token = response.json()['data']['token']
    front = response.json()['data']['front'][0]
    bg = response.json()['data']['bg'][0]
    return k, captchaId, token, front, bg


def parse_slice_list(bg):
    bg_id = bg.split('/')[-1].split('.')[0]
    with open('./02 天御.js', 'r') as f:
        js_file = f.read()
    ctx = execjs.compile(js_file)
    slice_list = ctx.call('captcha_list', bg_id)
    return slice_list


def download_img(front, bg):
    with open('./x1-front.png', 'wb') as f:
        f.write(requests.get(front).content)
    with open('./x2-bg.png', 'wb') as f:
        f.write(requests.get(bg).content)
    return


def recover_bg(slice_list):
    bg_img = Image.open('./x2-bg.png')
    recover_img = Image.new('RGBA', (544, 284), 'white')
    for index, item in enumerate(slice_list):
        x = index * 17
        y = 0
        l = bg_img.crop((x, y, x + 17, y + 284))
        recover_img.paste(l, (item * 17, 0))
    recover_img.save('./x2-recover-bg.png')
    return


def parse_slide():
    img_path = "./x2-recover-bg.png"
    slide_distance = base64_api(uname='cece', pwd='Aa12345678', img=img_path, typeid=33)
    slide_distance = int(slide_distance)
    return int(slide_distance * 300 / 544)


def parse_traceData(slide_distance):
    traceData = {}
    x = 0
    t = int(time.time() * 1000)
    y = random.randint(210, 220)
    traceData[str(x)] = {'t': t, 'y': y}
    while x < slide_distance:
        x += random.randint(1, 5)
        t += random.randint(10, 20)
        if x >= slide_distance:
            x = slide_distance
            traceData[str(x)] = {'t': t, 'y': y + random.randint(-1, 1)}
            break
        traceData[str(x)] = {'t': t, 'y': y + random.randint(-1, 1)}
    return [traceData]


def parse_check_data(k, captchaId, token, traceData):
    with open('./02 天御.js', 'r') as f:
        js_file = f.read()
    ctx = execjs.compile(js_file)
    traceData = json.dumps(traceData)
    report = ctx.call('parse_check', traceData, k, captchaId, token)
    return report


def login(captchaId,token,report):
    url = "https://captcha.jiagu.360.cn/api/v3/check"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-cn",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://jiagu.360.cn",
        "Referer": "https://jiagu.360.cn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    data = {
        "captchaId": captchaId,
        "token": token,
        "length": "218",
        "version": "2.0.0",
        "width": "300",
        "report": report,
        "tracking": "[object Object]"
    }
    return requests.post(url, headers=headers, data=data)



def main():
    k, captchaId, token, front, bg = parse_auth()
    # print(k, captchaId, token, front, bg)

    slice_list = parse_slice_list(bg)
    # print(slice_list)

    download_img(front, bg)
    recover_bg(slice_list)

    slide_distance = parse_slide()
    # print(slide_distance)

    trace = parse_traceData(slide_distance)
    # print(trace)

    report = parse_check_data(k, captchaId, token, trace)
    # print(report)

    response = login(captchaId,token,report)
    print(response.text )

if __name__ == '__main__':
    main()
