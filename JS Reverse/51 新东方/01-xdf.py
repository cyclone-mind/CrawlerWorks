import os
import requests
import execjs
from urllib.parse import quote

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 加密借助 01-xdf.js 里的 getSign（CryptoJS.MD5），不在 Python 里算签名
with open('01-xdf.js') as f:
    ctx = execjs.compile(f.read())

keyword = input('请输入关键词: ')

# 关键字必须先 URL 编码一次（与线上 JS 的 encodeURI 一致）再传入 getSign，
# 否则签名串里是中文原文，而 URL 里会被编码成 %EX..，两者不一致 -> sign验证失败
params = {
    'cityCode': '310100',
    'pageIndex': 1,
    'pageSize': 12,
    'keyword': quote(keyword),
    'order': '0',
}

result = ctx.call('getSign', params)

headers = {
    'accept': '*/*',
    'content-type': 'application/json',
    'origin': 'https://m.souke.xdf.cn',
    'referer': 'https://m.souke.xdf.cn/search?cityCode=310100&categoryCode=124',
    'sign': result['sign'],
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
}

# 【坑】不能用 requests.get(url, params=...)！
# params 里 keyword 已经是 %E9%9F%A9... 形式，requests 会把 % 再次编码成 %25，
# 实际发出的 URL 变成 keyword=%25E9%259F...，和签名串里的 keyword=%E9... 对不上，
# 服务端重算 MD5 不匹配 -> "sign验证失败"。
# 正确做法（与线上 JS 一致）：把签名时拼好的 query 串直接拼到 URL 后面，
# 整条 URL 传给 requests.get，不再让 requests 二次编码。
url = 'https://dsapi.xdf.cn/product/v3/class/search?' + result['query']
response = requests.get(url, headers=headers)
print(response.text)
