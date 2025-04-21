import requests
import execjs
import random
import ddddocr


def js_math_random():
    # 生成一个[0,1)之间的随机浮点数，保持与JS的Math.random()相同的精度
    return str(random.uniform(0, 0.9999999999999999))


def get_verifycode(mobile):

    headers = {
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://hotel.bestwehotel.com/NewLogin/',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'HWWAFSESID=c9a5376aa613115268; HWWAFSESTIME=1743239406255; Hm_lvt_b6e767c4467dcad9be907eab9e9c78ac=1743239410; Hm_lpvt_b6e767c4467dcad9be907eab9e9c78ac=1743239410; HMACCOUNT=290D0C677883C1BD; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22195e12a726a14ea-08b94671a326d7-26011d51-2073600-195e12a726b1f57%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk1ZTEyYTcyNmExNGVhLTA4Yjk0NjcxYTMyNmQ3LTI2MDExZDUxLTIwNzM2MDAtMTk1ZTEyYTcyNmIxZjU3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D',
        }

    response = requests.get(
        f'https://hotel.bestwehotel.com/api/safeverify/getImageVerify?mobile={mobile}&verifyImageKey={js_math_random}',
        headers=headers,
    )
    # 获取图片的二进制内容
    image_data = response.content
    
    # 将图片保存到本地
    with open('test.jpg', 'wb') as f:
        f.write(image_data)
    
    
    ocr = ddddocr.DdddOcr()
    img_path = "test.jpg"
    # 读取图片
    with open(img_path, 'rb') as f:
        img_bytes = f.read()
    # 识别验证码
    code = ocr.classification(img_bytes)
    print("code:::",code)
    return code


def spider(mobile,password):
    data = execjs.compile(open("./jj.js","r",encoding="utf-8").read()).call("get_rw_sw",mobile)
    rw = data.get("rw")
    sw = data.get("sw")
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://hotel.bestwehotel.com',
    'Pragma': 'no-cache',
    'Referer': 'https://hotel.bestwehotel.com/NewLogin/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'X-WE-SDK': '1.5.5',
    'rw': rw,
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'HWWAFSESID=c9a5376aa613115268; HWWAFSESTIME=1743239406255; Hm_lvt_b6e767c4467dcad9be907eab9e9c78ac=1743239410; Hm_lpvt_b6e767c4467dcad9be907eab9e9c78ac=1743239410; HMACCOUNT=290D0C677883C1BD; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22195e12a726a14ea-08b94671a326d7-26011d51-2073600-195e12a726b1f57%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk1ZTEyYTcyNmExNGVhLTA4Yjk0NjcxYTMyNmQ3LTI2MDExZDUxLTIwNzM2MDAtMTk1ZTEyYTcyNmIxZjU3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D',
    }
    password = execjs.compile(open("./jj.js","r",encoding="utf-8").read()).call("get_password",password)
    verifyCode = get_verifycode(mobile)
    json_data = {
    'groupTypeId': 2,
    'type': 1,
    'mobile': mobile,
    'password': 'JfYot+NjHbQacTYI6d5KMQ==',
    'rememberMe': False,
    'verifyCode': 'vvqj',
    'TDFingerprint': 'nWPH417432394128RX547mVvR6',
    'blackBoxMd5': 'bba7bb174c8a6ed92cdbf3108c5bb7dc',
    'did': 'b96df3b5231841da141ba03383de0bd8',
    'deviceInfo': {
        'fingerPrintJs': '86f5df16549a213f79f8f415ae76a31c',
        'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'platform': 'Win32',
    },
    'sw': sw,
    'channelCode': 'CA00046',
    }

    response = requests.post('https://hotel.bestwehotel.com/api/member/login', headers=headers, json=json_data)

    print(response)
    print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"groupTypeId":2,"type":1,"mobile":"admin@163.com","password":"JfYot+NjHbQacTYI6d5KMQ==","rememberMe":false,"verifyCode":"vvqj","TDFingerprint":"nWPH417432394128RX547mVvR6","blackBoxMd5":"bba7bb174c8a6ed92cdbf3108c5bb7dc","did":"b96df3b5231841da141ba03383de0bd8","deviceInfo":{"fingerPrintJs":"86f5df16549a213f79f8f415ae76a31c","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36","platform":"Win32"},"sw":"366a9b387a0a45403261d56523f31385","channelCode":"CA00046"}'
#response = requests.post('https://hotel.bestwehotel.com/api/member/login', cookies=cookies, headers=headers, data=data)

if __name__ == "__main__":
    mobile = "admin@163.com"
    password = "123456789"
    spider(mobile,password)