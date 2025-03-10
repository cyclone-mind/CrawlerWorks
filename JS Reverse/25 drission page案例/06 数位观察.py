from DrissionPage import ChromiumPage, ChromiumOptions
import pandas as pd
import time

page = ChromiumPage()
# page.listen.start("/v1/cPublic/consumer/baseInfo")
page.get("https://www.swguancha.com/home/city")
data = []
for i in range(5):
    time.sleep(1)
    city_list = page.eles("css:.city-name")
    city_item_list = page.eles("css:.city-item-bottom")
    for city, city_item in zip(city_list, city_item_list):
        city_name = city.text
        GDP = city_item.child(0).ele("css:.count").text
        bus = city_item.child(1).ele("css:.count").text
        population = city_item.child(2).ele("css:.count").text
        print(city_name, GDP, bus, population)
        data.append([city_name, GDP, bus, population])
    btn_i = page.ele("css:.query-city-data > div:nth-child(3) > div:nth-child(1) > button:nth-child(3)")
    btn_i.click()

page.quit()
# 将列表转换为DataFrame对象
df = pd.DataFrame(data, columns=['City', 'GDP', 'Bus', 'Population'])
# 将DataFrame写入Excel文件
df.to_excel('city_data_数位观察.xlsx', index=False)
