from DrissionPage import ChromiumPage, ChromiumOptions
import time
co = ChromiumOptions()
page = ChromiumPage(co)
page.get("https://jzsc.mohurd.gov.cn/data/company")
data = []
for i in range(5):
    time.sleep(1)
    trs = page.eles('xpath://tr[@class="el-table__row"]')
    for tr in trs:
        number = tr.ele('xpath:.//td[1]').text
        code = tr.ele('xpath:.//td[2]').text
        company_ame = tr.ele('xpath:.//td[3]').text
        boos = tr.ele('xpath:.//td[4]').text
        city = tr.ele('xpath:.//td[5]').text
        print(number, code, company_ame, boos, city)
        data.append([number, code, company_ame, boos, city])
    btn = page.ele('xpath://button[@class="btn-next"]')
    btn.click()

page.quit()

