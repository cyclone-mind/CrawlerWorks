"""

"""
import requests
import execjs

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/octet-stream",
    "Origin": "https://www.spolicy.com",
    "Pragma": "no-cache",
    "Referer": "https://www.spolicy.com/typePolicy?id=4&name=%E6%94%BF%E7%AD%96%E6%96%87%E4%BB%B6",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "X-KL-Ajax-Request": "Ajax_Request",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://www.spolicy.com/info_api/policyType/showPolicyType"
with open('02 zc.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

data = execjs.compile(js_code).call("get_data",1,4)

# print(bytes(data.get('data')))
data = bytes(data.get('data'))

# data = '\\n\\u00014\\u0012\\u0000\\u001a\\u0000"\\u0000*\\u00002\\u00008\\u0000@\\u0002H\\n'.encode('unicode_escape')
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)