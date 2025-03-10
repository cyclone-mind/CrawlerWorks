from DrissionPage import Chromium, ChromiumOptions
import time
options = ChromiumOptions()
options.headless(False)
browser = Chromium(options)
tab = browser.new_tab()
tab.listen.start('api.college.query',method='POST')
tab.get(url = 'https://youzy.cn/tzy/search/colleges/collegeList')
for i in range(2):
    tab.ele('#scorllELe').scroll.to_bottom()
    print(f'滑动到底部第{i}次')
    time.sleep(1.5)
res = tab.listen.steps()
# tab.listen.stop()
print(res)

for i in res:

    data = i.response.body
    college_list = data['result']['items']
    for college in college_list:
        cnName = college['cnName']
        cityName = college['cityName']
        provinceName = college['provinceName']
        ranking = college['ranking']
        comScore = college['comScore']
        code = college['code']
        belong = college['belong']
        print(ranking, cnName, comScore, code, provinceName,cityName,  belong)
tab.close()
browser.quit()



