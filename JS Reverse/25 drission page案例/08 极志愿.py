from pprint import pprint
import time
from DrissionPage import ChromiumPage, ChromiumOptions
import pandas as pd
co = ChromiumOptions()
co.headless(False)
page = ChromiumPage(co)
page.listen.start('sch/rank-list')
page.get('https://www.jizhy.com/44/rank/school', retry=1, interval=1, timeout=1.5)
results = {
    'num': [],
    'name': [],
    'score':[]
}
a_list = page.eles('xpath://a[@class="school-item flex flex-tbc"]')
for a in a_list:
    num = a.ele('xpath:./span').text
    name = a.ele('xpath:./div[@class="school-name flex-auto-width"]').text
    score = a.ele('xpath://span[@class = "school-rank--num"]').text
    results['num'].append(num)
    results['name'].append(name)
    results['score'].append(score)
for i in range(10):
    print(i)
    btn = page.ele('xpath://button[@class="btn btn-white"]').click()
    # page.wait.load_start()  # 等待页面进入加载状态
    res = page.listen.wait()
    # print("res:::", res.response.body)
    sch_list = res.response.body['data']['sch_list']
    for sch in sch_list:
        results['num'].append(sch['sch_rank'])
        results['name'].append(sch['sch_name'])
        results['score'].append(sch['sch_rank_score'])
    # print(results)
    time.sleep(1)

df = pd.DataFrame(results)
print(df)
page.quit()
