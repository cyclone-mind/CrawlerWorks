import json
import re
from hashlib import sha256
from curl_cffi import requests
import subprocess
import execjs
import time
timer = int(time.time() * 1000)

cookies = {
    'ipLoc-djd': '2-2813-0-0',
    '__jdv': '143920055|direct|-|none|-|1731826741642',
    '3AB9D23F7A4B3CSS': 'jdd03S4PNHN5ETHVTHLH7Y3QN7KXFZ5VCVS2CBEDX572P364PU3HNTLOL5YP2EXNOLUPU224GC4Y7LFRL2JOK2XDN7CQFEYAAAAMTHDVPIHQAAAAAD7U5NQ7GTMA7LYX',
    '__jdu': '17318267416421694805861',
    'shshshfpa': 'f3647ded-212b-9b95-f239-5c0079e42de3-1731826741',
    'shshshfpx': 'f3647ded-212b-9b95-f239-5c0079e42de3-1731826741',
    'areaId': '2',
    'wlfstk_smdl': 'ntu01koqcb6fal7buj9w94uslbak7nqu',
    'TrackID': '1LrIaoLDPpR4fUuPDI2fMnXxX6ffrurfCHpLRxP7oHqTwMX9s2xBaOf6iAnXXlJqy6Y1OG0v9_O0ej4K0TJir9_DnU9UrKzTln6_ncnRKr_I',
    'thor': 'E46492102BBCEFD2CFFC80BA80EC8EF8F52669417E582E8373424D81A1F66115478F816EE85D03B73CA28A21586765DE26C6E11C729E930EC2DCDC7C69F27438C4F2F42F1BF61659986487037557072AAD795D02A6A0EA6C78D8F29E52C5AF734DBC83C52A6CBC9F9D37B68A06E7DDB51A1E750EBE8503E531F4F135FC4A320F69E4B0D5281AF699AB90C5636D8D8AD3F9E3C9707875CE2A05D7E73E6B9338A2',
    'light_key': 'AASBKE7rOxgWQziEhC_QY6yac1wSzqNQMxrPpO23s88NtLVf81lxOExa15ms4kI06N9cet4o',
    'pinId': 'czYWcmDVeEYJbAsbz8NdArV9-x-f3wj7',
    'pin': 'jd_64781993f2ce4',
    'unick': '%E7%BB%99%E6%88%91%E5%B0%8F%E7%AD%96%E7%AD%96',
    'ceshi3.com': '203',
    '_tp': 'C21a8J94duMEufT1Sz3PAshOPlyAuFsV%2BVhg7SuHSb0%3D',
    '_pst': 'jd_64781993f2ce4',
    '__jda': '143920055.17318267416421694805861.1731826742.1731826742.1731826742.1',
    '__jdc': '143920055',
    'shshshfpb': 'BApXSV-jjO_ZAktP902x1IUDwNXfCIpw5BnPDYG5o9xJ1MouvJIG2',
    '3AB9D23F7A4B3C9B': 'S4PNHN5ETHVTHLH7Y3QN7KXFZ5VCVS2CBEDX572P364PU3HNTLOL5YP2EXNOLUPU224GC4Y7LFRL2JOK2XDN7CQFEY',
    'flash': '3_dV-0QDPPUaNOXTskZp-XeQxQ24A2Vt_AXuN6FxNY7qmXNUB7rM84RO8bSOSQ0lIxAVtN7elgHP43_tjVC3XN--Qyq9mZeGvlj5V5tYLBdgVx4cd4M_GxtqcaAdDBHE0rr35OnzzzlqKxBbfQzbBurjWNRaxJpt0X1X3RnOTZ-K2aNW-e1nBBre**',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'ipLoc-djd=2-2813-0-0; __jdv=143920055|direct|-|none|-|1731826741642; 3AB9D23F7A4B3CSS=jdd03S4PNHN5ETHVTHLH7Y3QN7KXFZ5VCVS2CBEDX572P364PU3HNTLOL5YP2EXNOLUPU224GC4Y7LFRL2JOK2XDN7CQFEYAAAAMTHDVPIHQAAAAAD7U5NQ7GTMA7LYX; __jdu=17318267416421694805861; shshshfpa=f3647ded-212b-9b95-f239-5c0079e42de3-1731826741; shshshfpx=f3647ded-212b-9b95-f239-5c0079e42de3-1731826741; areaId=2; wlfstk_smdl=ntu01koqcb6fal7buj9w94uslbak7nqu; TrackID=1LrIaoLDPpR4fUuPDI2fMnXxX6ffrurfCHpLRxP7oHqTwMX9s2xBaOf6iAnXXlJqy6Y1OG0v9_O0ej4K0TJir9_DnU9UrKzTln6_ncnRKr_I; thor=E46492102BBCEFD2CFFC80BA80EC8EF8F52669417E582E8373424D81A1F66115478F816EE85D03B73CA28A21586765DE26C6E11C729E930EC2DCDC7C69F27438C4F2F42F1BF61659986487037557072AAD795D02A6A0EA6C78D8F29E52C5AF734DBC83C52A6CBC9F9D37B68A06E7DDB51A1E750EBE8503E531F4F135FC4A320F69E4B0D5281AF699AB90C5636D8D8AD3F9E3C9707875CE2A05D7E73E6B9338A2; light_key=AASBKE7rOxgWQziEhC_QY6yac1wSzqNQMxrPpO23s88NtLVf81lxOExa15ms4kI06N9cet4o; pinId=czYWcmDVeEYJbAsbz8NdArV9-x-f3wj7; pin=jd_64781993f2ce4; unick=%E7%BB%99%E6%88%91%E5%B0%8F%E7%AD%96%E7%AD%96; ceshi3.com=203; _tp=C21a8J94duMEufT1Sz3PAshOPlyAuFsV%2BVhg7SuHSb0%3D; _pst=jd_64781993f2ce4; __jda=143920055.17318267416421694805861.1731826742.1731826742.1731826742.1; __jdc=143920055; shshshfpb=BApXSV-jjO_ZAktP902x1IUDwNXfCIpw5BnPDYG5o9xJ1MouvJIG2; 3AB9D23F7A4B3C9B=S4PNHN5ETHVTHLH7Y3QN7KXFZ5VCVS2CBEDX572P364PU3HNTLOL5YP2EXNOLUPU224GC4Y7LFRL2JOK2XDN7CQFEY; flash=3_AoAQXJHgtMZt60k4vLTDrzmfRlwR-o7BT0nhq8WpRyBOrMw8vjlUscNyPfNINo4FliULOX2j-B6FZDMcJ0AQ39KeTQtSwvF13e4xdGIuMEwGofH1RmhIqF6f93tPocKayCZHTeujUyxWz5-H0O5L5zwcDmwu6sKbiRT3J4trMZHRrSvip8Cwee**',
    'origin': 'https://search.jd.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://search.jd.com/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-referer-page': 'https://search.jd.com/Search',
    'x-rp-client': 'h5_1.0.0',
}

params = {
    "functionId": "pc_search_adv_Search",
    "appid": "search-pc-java",
    "client": "pc",
    "clientVersion": "1.0.0",
    "uuid": "143920055.17318267416421694805861.1731826742.1731826742.1731826742.1",
    "loginType": "3",
    "t": "1731832892419",
    "body": "{\"area\":\"2\",\"enc\":\"utf-8\",\"adType\":7,\"page\":\"5\",\"ad_ids\":\"291:19\",\"xtest\":\"new_search\"}",
    # "h5st": "20241117164132424;80hqyfe5ruzu4ze1;f06cc;tk03w91db1c8118nz4fmC7UQhfL5L_WTrQR9Zs41XG8XFs6MVgZ_oCp6J1_8LT9fqzL3ZNFSqPzfosoqtcmrUMYhOvBr;a6a73649fb12b37e95f9fd02824a032a65db1dfa84e9d0ae2706c12969ed4c8a;4.9;1731832892424;q3EpJnYSxaYOxWEP2XFSymkR7LIjLDIj7SFjLrJp-TYfLDIj9e1TJrpjh7JjzTIS1bFf1HoS4X4e5PYf7f1TGSofFO4TFWleKWVTHeFjLDIj7SnQEiVS0ipjLDrgJTFT0nIe2n1f4foS7jFfJOYfJSITJmIfGGYf6T1eJSlfJrJdJfUT1yVTIipjLDrgJfIgyzpe1uWS-GFSMWoRJrJdJTEjLrJp-jZVF2HYaKYVoaUZ2KIjLDIj_ulS9mFPJrpjh7Jj5fIQCOGjLDIjFqEjLrJp-3kjLDrfLDIjzXETJrpjLrJp-jJjLDIj0XETJrpjLrJp-f4fLDIj1XETJrpjLrJp-rojxjZe2iFjLrpjLDrg7rJdJbYOJipjLrpjh7Jf3rJdJfYOJipjLrpjh7Jf_rJdJjYOJipjLrpjh7Jj1zZf9rIjLDIj6XETJrpjLrJp-rojxj5R0ipjLrpjh7JfLDIj46FjLrpjLDrg7rJdJ7FjLrpjLDrg7rJdJb1OJrpjLrJpwqJdJbFQGakNGipjLDrguqpjhjpeGeFfFeYdynod0bIeMaFRJrJdJjoPJrpjLrJpwqJdJrkPJrpjh7Jj3ToNL-oe1zVRUq5d7zpf6rpWdq5P0ulS9G1WJrJdJnVO4ipjLD7N;3bf6c1e5497a4e66d6c3309755e145b1ea9c8cb69632430c2ce2e0554c99f2fc",
    "x-api-eid-token": "jdd03S4PNHN5ETHVTHLH7Y3QN7KXFZ5VCVS2CBEDX572P364PU3HNTLOL5YP2EXNOLUPU224GC4Y7LFRL2JOK2XDN7CQFEYAAAAMTHDVPIHQAAAAAD7U5NQ7GTMA7LYX",
    "keyword": "xiaomi"
}


obj = sha256()
obj.update(params['body'].encode('utf-8'))
enc_body = obj.hexdigest()
# print(enc_body)
params2 = {
    "appid": "search-pc-java",
    "functionId": "pc_search_s_new",
    "client": "pc",
    "clientVersion": "1.0.0",
    "t": str(timer),
    "body": enc_body
}

# print(params2)
def get_h5st(p):
    res = subprocess.run(['node', './jd.js', json.dumps(p)], capture_output=True, text=True, encoding='utf-8')
    print(res.stdout)  # 打印标准输出
    return re.search('::: (?P<h5st>.*?) :::', res.stdout).group('h5st')
    # print(res.stderr)  # 打印标准错误输出
    # print(res)

params['h5st'] = get_h5st(params2)
print(params['h5st'])

response = requests.get('https://api.m.jd.com/', params=params, cookies=cookies, headers=headers)

print(response.text)
print(response)
