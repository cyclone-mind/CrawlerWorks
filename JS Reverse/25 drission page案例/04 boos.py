from DrissionPage import ChromiumPage, ChromiumOptions
import pandas as pd
import time
cp = ChromiumPage()
cp.listen.start("/wapi/zpgeek/search/joblist.json")
cp.get("https://www.zhipin.com/web/geek/job?query=python&city=101020100", retry=3, interval=2, timeout=15)

res = cp.listen.wait()
# print("res:::", res.response.body)

jobs = res.response.body["zpData"]["jobList"]
for i in range(3):
    time.sleep(1)
    btn = cp.ele('.ui-icon-arrow-right')
    btn_a = btn.parent().attr('class')
    if btn_a !="disabled":
        btn.click()
        res = cp.listen.wait()
        jobs += res.response.body["zpData"]["jobList"]
    else:
        print("没有更多了")
        break

# 写入到excel中
# df = pd.DataFrame(jobs)
# df.to_excel('boss直聘.xlsx', index=False)
cp.quit()




