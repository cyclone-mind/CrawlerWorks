import requests
import time
import re
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
print(cfp)
print(response.text)
json_str = response.text
match = re.search(r'"challenge"\s*:\s*"([^"]+)"', json_str)

# 如果匹配成功，提取并打印challenge的值
if match:
    challenge_value = match.group(1)
    print("Challenge value:", challenge_value)
else:
    print("Challenge value not found.")
# print(response.json())
