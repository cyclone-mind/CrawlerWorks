import requests
import execjs
cookies = {
    'select_city': '110000',
    'lianjia_ssid': '884cbfd6-797e-4240-bdb4-f7a037f0b7a0',
    'lianjia_uuid': 'bd6e896c-d8e2-497e-8cfe-dac8e2acf319',
    'Hm_lvt_b160d5571570fd63c347b9d4ab5ca610': '1732275728',
    'Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610': '1732275728',
    'HMACCOUNT': '564DE01A85DF06AF',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219353aded16e25-0ead288c872fd5-26011851-2073600-19353aded171247%22%2C%22%24device_id%22%3A%2219353aded16e25-0ead288c872fd5-26011851-2073600-19353aded171247%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'select_city=110000; lianjia_ssid=884cbfd6-797e-4240-bdb4-f7a037f0b7a0; lianjia_uuid=bd6e896c-d8e2-497e-8cfe-dac8e2acf319; Hm_lvt_b160d5571570fd63c347b9d4ab5ca610=1732275728; Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610=1732275728; HMACCOUNT=564DE01A85DF06AF; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219353aded16e25-0ead288c872fd5-26011851-2073600-19353aded171247%22%2C%22%24device_id%22%3A%2219353aded16e25-0ead288c872fd5-26011851-2073600-19353aded171247%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
    'Origin': 'https://bj.ke.com',
    'Pragma': 'no-cache',
    'Referer': 'https://bj.ke.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def spider(user,pwd):
    pwd = execjs.compile(open('./beike.js', 'r', encoding='utf-8').read()).call('encrypt', pwd)
    print('pwd:::',pwd)
    json_data = {
        'service': 'https://ajax.api.ke.com/login/login/getuserinfo',
        'mainAuthMethodName': 'username-password',
        'accountSystem': 'customer',
        'credential': {
            'username': str(user),
            'password': str(pwd),
            'encodeVersion': '1',
        },
        'context': {
            'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'clientSource': 'pc',
            'os': 'Windows',
            'osVersion': '10',
            'registerPosLx': 931,
            'registerPosLy': 194.5,
            'registerPosRx': 1211,
            'registerPosRy': 238.5,
            'clickPosX': 1085,
            'clickPosY': 175,
            'screen': '1903_274',
            'dataId': 'eyJ0Ijoie1wiZGF0YVwiOlwiMDAwYWEyYzM2MWE4YjE0YTg2YWJiZWQ2ODA0ODg1ZTcyM2RiZWI5YmEwOTc5YWI1NmMwZTc1ZmI4ZGJiZWE3ZjI4MTRmNGIzZTY0ZjQ5ZDZjMDFiMjIxYzk2NjQ2YzgxZDBjM2Q3ZjRkOWY2ODdjY2ZiZjE0MGE5MTUxZDdjZDQ2NzNhOGM4NmRiMjhiZjFlYTNhMGE2MmMyMGIyZGUyOWQzODVmYzQyMDc1OTlmZGM3NTUyNGRhOTZjMmZiMWI5ZWJmNWIwZGI5YjgwZjYwZGNiMzMwNDU1ZGY0ODVjYzQzMjYxN2E2Yjg4OTIzODZiZTljOTljZjcxNTBjMGNhOVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIzNDNhMjgwMlwifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
        },
        'loginTicketId': 'aGdoWtZ3vNbIiQpWvqhLPsmqIHHx20ed',
        'version': '2.0',
        'srcId': 'eyJ0Ijoie1wiZGF0YVwiOlwiMDAwYWEyYzM2MWE4YjE0YTg2YWJiZWQ2ODA0ODg1ZTcyM2RiZWI5YmEwOTc5YWI1NmMwZTc1ZmI4ZGJiZWE3ZjI4MTRmNGIzZTY0ZjQ5ZDZjMDFiMjIxYzk2NjQ2YzgxZDBjM2Q3ZjRkOWY2ODdjY2ZiZjE0MGE5MTUxZDdjZDQ2NzNhOGM4NmRiMjhiZjFlYTNhMGE2MmMyMGIyZGUyOTdhNDZiYzFjN2U3MTkwMTljY2E5OWM5NzliMTY3ZDVmOGQzZDMyYjI4ZTYyNTJiM2E1YjFkZjYwYjhiZGE0MGE1NjZlYjU2ZmIxNjIwMWFjYWNiMmZmZjEwNDM0NzMyMlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJhYzdhZTcxZlwifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
        'ticketMaxAge': 604800,
    }

    response = requests.post('https://clogin.ke.com/authentication/authenticate', cookies=cookies, headers=headers, json=json_data)
    print(response.text)
    print(response)

spider(13449496636,'addd12345611')
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"service":"https://ajax.api.ke.com/login/login/getuserinfo","mainAuthMethodName":"username-password","accountSystem":"customer","credential":{"username":"13469995957","password":"RVjmL6veL/lRT/T+m9I7NdV7fnLxrgzb0p2DwMYC3vYbxxrUwSHGuqF/yyDH9yLMN1I8tnDonMAWUfpm2DyoMQgFxecvZ5JXWGrBvC35UhJh/GYke8+1OoHnkqYaSZKVqiXKXa5uBBK4oUzTmV53X5zPCRLzCyxA8YjmR+Qtgk0=","encodeVersion":"1"},"context":{"ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","clientSource":"pc","os":"Windows","osVersion":"10","registerPosLx":931,"registerPosLy":163.5,"registerPosRx":1211,"registerPosRy":207.5,"clickPosX":1085,"clickPosY":175,"screen":"1903_274","dataId":"PKz46QL10mdvNUBnelA769FmM59+aZYEuS0DhnV2ltVv0Ywj9iN6ckzyf/UNTzKQ"},"loginTicketId":"DPupPNhCdDNIlE5YDqb2BnovIHFC5Neu","version":"2.0","srcId":"eyJ0Ijoie1wiZGF0YVwiOlwiMDAwYWEyYzM2MWE4YjE0YTg2YWJiZWQ2ODA0ODg1ZTcyM2RiZWI5YmEwOTc5YWI1NmMwZTc1ZmI4ZGJiZWE3ZjI4MTRmNGIzZTY0ZjQ5ZDZjMDFiMjIxYzk2NjQ2YzgxZDBjM2Q3ZjRkOWY2ODdjY2ZiZjE0MGE5MTUxZDdjZDQ2NzNhOGM4NmRiMjhiZjFlYTNhMGE2MmMyMGIyZGUyOTdhNDZiYzFjN2U3MTkwMTljY2E5OWM5NzliMTY3ZDVmOGQzZDMyYjI4ZTYyNTJiM2E1YjFkZjYwYjhiZGE0MGE1NjZlYjU2ZmIxNjIwMWFjYWNiMmZmZjEwNDM0NzMyMlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJhYzdhZTcxZlwifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==","ticketMaxAge":604800}'
#response = requests.post('https://clogin.ke.com/authentication/authenticate', cookies=cookies, headers=headers, data=data)