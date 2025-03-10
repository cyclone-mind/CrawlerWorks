import requests
import time
import execjs

timer = int(time.time() * 1000)

sign = execjs.compile(open('./sign.js', 'r', encoding='utf-8').read()).call('get_sign')
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.chinaindex.net/ranklist/4",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "UUID": "7666dd24-4912-545f-a703-76f15464ca17",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "X-KL-Ajax-Request": "Ajax_Request",
    "funcID": "undefined",
    "incognitoMode": "0",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "mobile_iindex_uuid": "7666dd24-4912-545f-a703-76f15464ca17",
    "Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f": "1731934251",
    "Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f": "1731934251",
    "HMACCOUNT": "862BC833877B77B8"
}
url = "https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank"
params = {
    "channel": "movielist",
    "sign": sign
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
print(response)
print(response.json())
text = response.json()

dec_data = execjs.compile(open('./decrypt.js', 'r', encoding='utf-8').read()).call('decrypt', text)
print(dec_data)

