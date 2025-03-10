# -*- coding: utf-8 -*-
from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions()
co.headless(True)
page = ChromiumPage(co)

url = 'https://www.baidu.com'
page.get(url)
el = page.ele('css:#kw')
print(el)
el.input('IP地址')
page.wait.load_start()
page.ele('css:#su').click()
print(page.html)

page.listen.start('https://qifu-api.baidubce.com/ip/local/geo/v1/district')
res = page.listen.wait()
print(res.response.body)
page.listen.stop()
page.quit()