# -*- coding: utf-8 -*-
import requests
from lxml import etree
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

url = 'http://epub.cnipa.gov.cn/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'NOh8RTWx6K2dS=60HC.Mv3PuYqzv7Uumvub2CEZzPLp0oKni9oJ3elAKyET.TKU2.O4prpQzdkR_mXcuxlyCFqsvOUhOB3fSvHco8q; NOh8RTWx6K2dT=0WI7dQkzjvHZN5YRDkTzqiaZZrgZytIYYFWKMQnlqkKjzqcdyKhyzk.gYV4y1Cx84ThblfjHNmO3i34GV5PwKzGS1DxFVunzgiViHiiPf__GpTAoCremg5ag8sAbJ49rCbOs1t4dmtKns4vK6VWHKMiehUOePOYlg5Jh1eV17nDG46z6Ii0mL8CyOT8hS1ntsK0v6sSEfbZFgz3g7XRnjn.manxRvDCBvi2YpWd7YI0SHKG_OAojOibr6s3kCWYAG',
    'Pragma': 'no-cache',
    'Referer': 'http://epub.cnipa.gov.cn/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}
session = requests.session()
response = session.get(url, headers=headers, verify=False)
response.encoding = 'utf-8'
print(response)
# print('cookies值：：：', session.cookies.get_dict())

html = etree.HTML(response.text)
content_str = html.xpath('//meta/@content')[-1]
ts_js = html.xpath('//script/text()')[0]
auto_url = "http://epub.cnipa.gov.cn" + html.xpath('//script[2]/@src')[0]
auto_js = session.get(auto_url).text
# print('content_str:::',content_str)
# print('ts_js:::',ts_js)
# print('auto_js:::',auto_url)


with open('02env.js', 'r', encoding='utf-8') as js_file:
    js_code = js_file.read()
js_code = js_code.replace('metaContent', content_str).replace("'auto_js'", auto_js).replace("'ts_js'", ts_js)

js_compile = execjs.compile(js_code)
cookie_t = js_compile.call('get_cookie').split(';')[0].split('=')
print(cookie_t)

session.cookies.update({cookie_t[0]: cookie_t[1]})

# print(session.cookies.get_dict())

response = session.get(url, headers=headers, verify=False)
print(response)


