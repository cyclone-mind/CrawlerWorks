import requests
from lxml import etree
import pandas as pd

def main(page):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'https://sh.lianjia.com/ershoufang/pg2/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    page = str(page)
    response = requests.get(f'https://sh.lianjia.com/ershoufang/pg{page}/',headers=headers)
    # print(response)
    # print(response.text)
    tree=etree.HTML(response.text)
    items = tree.xpath('//div[@class="info clear"]')
    data = []
    for item in items:
        title = item.xpath('.//div[@class="title"]/a/text()')[0].strip()
        position1 = item.xpath('./div[@class="flood"]/div[@class="positionInfo"]/a[1]/text()')[0].strip()
        position2 = item.xpath('./div[@class="flood"]/div[@class="positionInfo"]/a[2]/text()')[0].strip()
        houseInfo = item.xpath('./div[@class="address"]/div[@class="houseInfo"]/text()')[0].strip()
        followInfo = item.xpath('./div[@class="followInfo"]/text()')[0].strip()
        spans = item.xpath('./div[@class="tag"]/span/text()')
        totalPrice = item.xpath('./div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/span/text()')[0].strip()
        unitPrice = item.xpath('./div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()')[0].strip()
        print(title, position1, position2, followInfo, spans, totalPrice, unitPrice)
        # 将数据存储为字典
        data.append({
            'Title': title,
            'Position1': position1,
            'Position2': position2,
            'HouseInfo': houseInfo,
            'FollowInfo': followInfo,
            'Tags': ', '.join(spans),
            'TotalPrice': totalPrice,
            'UnitPrice': unitPrice
        })

    # 创建 DataFrame
    df = pd.DataFrame(data)

    # 将 DataFrame 写入 Excel 文件
    df.to_excel(f'lianjia_page_{page}.xlsx', index=False)

if __name__ == '__main__':
    main(1)

