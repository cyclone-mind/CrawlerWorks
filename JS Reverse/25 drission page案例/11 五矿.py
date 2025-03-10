from DrissionPage import ChromiumPage, ChromiumOptions
import time

co = ChromiumOptions()
co.headless(False)
browser = ChromiumPage(co)
tab = browser.new_tab()

tab.listen.start('zbs/by-lx-page',method='POST')
tab.get('https://ec.minmetals.com.cn/open/home/purchase-info?tabIndex=5')

button1 = tab.ele('.sunway-tabs-tab-active sunway-tabs-tab')
button1.click()
button2 = tab.eles('.sunway-btn sunway-btn-icon-only')[1]

for i in range(5):
    time.sleep(1)
    if button2 !="disabled":
        button2.click()
        print(f'点击第{i}次')
    else:
        print("没有更多了")
        break
res = tab.listen.steps()

print(res)
'''
{
  "mc": "成分-江津区先进机电装备和物流产业园项目-公开招标-专业分包-模板脚手架工程二标段",
  "bm": "1497949572636704",
  "xs": "0",
  "lx": "ZBGG",
  "lxmc": "招标公告",
  "rq": "2024-10-18",
  "dwmc": "上海宝冶集团有限公司招标办公室",
  "purchasemode": "01",
  "businessclassification": "010",
  "condDes": "公开招标/工程/上海宝冶集团有限公司招标办公室"
}
'''

for i in res:
    data = i.response.body
    items = data['list']
    for item in items:
        title = item['mc']
        bm = item['bm']
        date = item['rq']
        dwmc = item['dwmc']
        condDes = item['condDes']
        print(title, bm, date, dwmc, condDes)

tab.close()
browser.quit()



