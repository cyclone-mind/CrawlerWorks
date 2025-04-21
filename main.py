import requests
import pandas as pd
import time
import json




def run(type, adcode):
    params = {
        "key": KEY,
        "types": type,
        "region": adcode,
        "citylimit": True,
        # "page_size": 25,
        # "page_num": page_num,
        "output": "json"
    }
    res = requests.get(BASEURL, params=params)
    print(f"正在获取 {adcode} 地区 {type} 类型，第  页数据...")
    print(res.json())
    infocode = res.json().get("infocode")

    if infocode != "10000":
        print(f"Error fetching data: {res.json().get('info')}")
        return True  # 出错时结束

    count = int(res.json().get("count"))

    print(f"在当前地区，该类型，记录数: {count}")
    if (count == 0):
        print("No data found.")
        return True  # 无数据时结束
    # is_end = count <= params["page_size"] * page_num

    pois = res.json().get("pois")
    if not pois:
        return True  # 无数据时结束





if __name__ == "__main__":
    KEY = "c5794e46b0d30d126cd19c5f1dd08a25"
    # 上海市行政区划代码
    # 黄浦区 徐汇区 长宁区 静安区 普陀区 虹口区 杨浦区 闵行区 宝山区 嘉定区 浦东新区 金山区 松江区 青浦区 奉贤区 崇明区

    adcode_list = [310101, 310104, 310105, 310106, 310107, 310109, 310110,
                   310112, 310113, 310114, 310115, 310116, 310117, 310118,
                   310120, 310151]
    # 30个教育设施
    types = [140100, 140101, 140102, 140200, 140201, 140300, 140400, 140500, 140600, 140700, 140800, 140900, 141000,
             141100,
             141101, 141102, 141103, 141104, 141105, 141200, 141201, 141202, 141203, 141204, 141205, 141206, 141207,
             141300,
             141400, 141500]

    BASEURL = "https://restapi.amap.com/v3/place/text"
    # 测试单次运行
    run( type="010700", adcode=310101)

    # 全量数据获取
    # for adcode in adcode_list:
    #     for type in types:
    #         time.sleep(1)  # 避免请求过于频繁被封禁
    #         page_num = 1
    #         is_end = False
    #         while not is_end:
    #             is_end = run(page_num, type, adcode)
    #             page_num += 1
    #     print(f"{adcode} 地区数据获取完成。")

