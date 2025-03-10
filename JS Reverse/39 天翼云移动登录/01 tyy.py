import requests
import execjs

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Csm": "4af1a9a40b45b63a2d15854c282413633ab5bc2717b07d5c8cb3485d7178ad9f",
    "Cst": "1739020965044",
    "Origin": "https://m.ctyun.cn",
    "Pragma": "no-cache",
    "Referer": "https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "X-KL-Ajax-Request": "Ajax_Request",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    # "x-riskdevicesign": "e262af849891c00bb81e55ff0602f133"
}
cookies = {
    "Hm_lvt_4b4ce93f1c92033213556e55cb65769f": "1739020908",
    "Hm_lpvt_4b4ce93f1c92033213556e55cb65769f": "1739020908",
    "HMACCOUNT": "B336C50914760A9A",
    "sid1": "1739020908952-A2951EF274BD4D9DD64987E42838E8D4",
    "sid2": "1739020908952-A2951EF274BD4D9DD64987E42838E8D4",
    "pvid": "1"
}


def main(username, password):
    url = "https://m.ctyun.cn/account/login"
    with open("./02 tyy.js") as f:
        js_code = f.read()
    password = execjs.compile(js_code).call('get_password', username, password)
    params = execjs.compile(js_code).call('get_params')
    data = {
        "userName": username,
        "password": password
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

    print(response.text)
    print(response)

userName = "admin@163.com"
password = "123456"

if __name__ == '__main__':
    main(userName, password)