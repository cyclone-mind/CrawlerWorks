import time
import re
import requests
import execjs

# 第一次请求
import requests

cookies = {
    'i18n_redirected': 'zh',
    'deviceid': '7b680ba2abfc163dd376f8f2693a6bb',
    '_ga': 'GA1.1.1359786416.1731943083',
    'token': 'fcb2fdd7187ab9f4e059687f512bea71e1ac14bec6ef149859cef25dbd0c1463288ab11cbde176b783ca385c010d32c0a56fc446c4d091b38bc889ff8b4cc3e1d0125edbed03b84d381fac09f190683c',
    'Hm_lvt_4b46d92b8c2be1622e347873de8ada00': '1732026659,1732069305',
    'Hm_lpvt_4b46d92b8c2be1622e347873de8ada00': '1732069305',
    'HMACCOUNT': '862BC833877B77B8',
    'Hm_lvt_c420cc498e4250baa6114afe2947045e': '1732026659,1732069305',
    'Hm_lpvt_c420cc498e4250baa6114afe2947045e': '1732069305',
    'Hm_lvt_e1382854e68f4d69f837bb54a6d1e22f': '1732026659,1732069306',
    'Hm_lpvt_e1382854e68f4d69f837bb54a6d1e22f': '1732069306',
    'activityTime': '1732118399999',
    'Hm_lvt_d185b2974609101d8f9340b5f861ca70': '1731943082,1732026752,1732069323',
    'Hm_lvt_8a5bd6e095cd118016489cab0443c2d7': '1731943082,1732026752,1732069323',
    'Hm_lvt_beac6fc75c36ba113cbffa9a59b1b18d': '1731943082,1732026753,1732069323',
    'Qs_lvt_404253': '1731943081%2C1731944473%2C1731944484%2C1732026752%2C1732069323',
    'showMajorDialog': 'true',
    '_ga_GVCWL6PNZ2': 'GS1.1.1732086569.6.1.1732086656.0.0.0',
    'Hm_lpvt_d185b2974609101d8f9340b5f861ca70': '1732086698',
    'Hm_lpvt_8a5bd6e095cd118016489cab0443c2d7': '1732086698',
    'Hm_lpvt_beac6fc75c36ba113cbffa9a59b1b18d': '1732086698',
    'Qs_pv_404253': '3664863510711997400%2C4033237115294589000%2C1342671318725410600%2C986299796234955500%2C4412131441979813000',
    '_uetsid': '4deb0500a5c011ef970c0dcf34a94356',
    '_uetvid': '4deb2a80a5c011ef9971e1420778623d',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'i18n_redirected=zh; deviceid=7b680ba2abfc163dd376f8f2693a6bb; _ga=GA1.1.1359786416.1731943083; token=fcb2fdd7187ab9f4e059687f512bea71e1ac14bec6ef149859cef25dbd0c1463288ab11cbde176b783ca385c010d32c0a56fc446c4d091b38bc889ff8b4cc3e1d0125edbed03b84d381fac09f190683c; Hm_lvt_4b46d92b8c2be1622e347873de8ada00=1732026659,1732069305; Hm_lpvt_4b46d92b8c2be1622e347873de8ada00=1732069305; HMACCOUNT=862BC833877B77B8; Hm_lvt_c420cc498e4250baa6114afe2947045e=1732026659,1732069305; Hm_lpvt_c420cc498e4250baa6114afe2947045e=1732069305; Hm_lvt_e1382854e68f4d69f837bb54a6d1e22f=1732026659,1732069306; Hm_lpvt_e1382854e68f4d69f837bb54a6d1e22f=1732069306; activityTime=1732118399999; Hm_lvt_d185b2974609101d8f9340b5f861ca70=1731943082,1732026752,1732069323; Hm_lvt_8a5bd6e095cd118016489cab0443c2d7=1731943082,1732026752,1732069323; Hm_lvt_beac6fc75c36ba113cbffa9a59b1b18d=1731943082,1732026753,1732069323; Qs_lvt_404253=1731943081%2C1731944473%2C1731944484%2C1732026752%2C1732069323; showMajorDialog=true; _ga_GVCWL6PNZ2=GS1.1.1732086569.6.1.1732086656.0.0.0; Hm_lpvt_d185b2974609101d8f9340b5f861ca70=1732086698; Hm_lpvt_8a5bd6e095cd118016489cab0443c2d7=1732086698; Hm_lpvt_beac6fc75c36ba113cbffa9a59b1b18d=1732086698; Qs_pv_404253=3664863510711997400%2C4033237115294589000%2C1342671318725410600%2C986299796234955500%2C4412131441979813000; _uetsid=4deb0500a5c011ef970c0dcf34a94356; _uetvid=4deb2a80a5c011ef9971e1420778623d',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://app.diandian.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

response = requests.get('https://app.diandian.com/', cookies=cookies, headers=headers)
# print(response.text)

def extract_skls(text):
    """
    从给定的字符串中提取s、k、l的值，并返回一个字典。

    :param text: 输入的字符串
    :return: 包含s、k、l键的字典
    """
    # 使用正则表达式找到u:{...}部分
    u_section_match = re.search(r'u:\{([^}]*)\}', text)

    if not u_section_match:
        print("未找到u:{...}部分")
        return {}

    u_content = u_section_match.group(1)

    # 使用findall提取所有键值对，格式为 key:"value"
    key_value_pairs = re.findall(r'(\w+):"([^"]+)"', u_content)

    # 过滤出s、k、l键，并构建字典
    result = {key: value for key, value in key_value_pairs if key in ('s', 'k', 'l')}

    return result

# 调用函数并打印结果
extracted_dict = extract_skls(response.text)
print(extracted_dict)

cookies = {
    'deviceid': '7b680ba2abfc163dd376f8f2693a6bb',
    '_ga': 'GA1.1.1359786416.1731943083',
    'token': 'fcb2fdd7187ab9f4e059687f512bea71e1ac14bec6ef149859cef25dbd0c1463288ab11cbde176b783ca385c010d32c0a56fc446c4d091b38bc889ff8b4cc3e1d0125edbed03b84d381fac09f190683c',
    'Hm_lvt_4b46d92b8c2be1622e347873de8ada00': '1732026659,1732069305',
    'Hm_lpvt_4b46d92b8c2be1622e347873de8ada00': '1732069305',
    'HMACCOUNT': '862BC833877B77B8',
    'Hm_lvt_c420cc498e4250baa6114afe2947045e': '1732026659,1732069305',
    'Hm_lpvt_c420cc498e4250baa6114afe2947045e': '1732069305',
    'Hm_lvt_e1382854e68f4d69f837bb54a6d1e22f': '1732026659,1732069306',
    'Hm_lpvt_e1382854e68f4d69f837bb54a6d1e22f': '1732069306',
    'activityTime': '1732118399999',
    'Qs_lvt_404253': '1731943081%2C1731944473%2C1731944484%2C1732026752%2C1732069323',
    'Qs_pv_404253': '1342671318725410600%2C986299796234955500%2C4412131441979813000%2C840241747558512900%2C1513341325292802000',
    '_ga_GVCWL6PNZ2': 'GS1.1.1732086569.6.1.1732086760.0.0.0',
    '_uetsid': '4deb0500a5c011ef970c0dcf34a94356',
    '_uetvid': '4deb2a80a5c011ef9971e1420778623d',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'deviceid=7b680ba2abfc163dd376f8f2693a6bb; _ga=GA1.1.1359786416.1731943083; token=fcb2fdd7187ab9f4e059687f512bea71e1ac14bec6ef149859cef25dbd0c1463288ab11cbde176b783ca385c010d32c0a56fc446c4d091b38bc889ff8b4cc3e1d0125edbed03b84d381fac09f190683c; Hm_lvt_4b46d92b8c2be1622e347873de8ada00=1732026659,1732069305; Hm_lpvt_4b46d92b8c2be1622e347873de8ada00=1732069305; HMACCOUNT=862BC833877B77B8; Hm_lvt_c420cc498e4250baa6114afe2947045e=1732026659,1732069305; Hm_lpvt_c420cc498e4250baa6114afe2947045e=1732069305; Hm_lvt_e1382854e68f4d69f837bb54a6d1e22f=1732026659,1732069306; Hm_lpvt_e1382854e68f4d69f837bb54a6d1e22f=1732069306; activityTime=1732118399999; Qs_lvt_404253=1731943081%2C1731944473%2C1731944484%2C1732026752%2C1732069323; Qs_pv_404253=1342671318725410600%2C986299796234955500%2C4412131441979813000%2C840241747558512900%2C1513341325292802000; _ga_GVCWL6PNZ2=GS1.1.1732086569.6.1.1732086760.0.0.0; _uetsid=4deb0500a5c011ef970c0dcf34a94356; _uetvid=4deb2a80a5c011ef9971e1420778623d',
    'Origin': 'https://app.diandian.com',
    'Pragma': 'no-cache',
    'Referer': 'https://app.diandian.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'language': 'zh',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'app_id': 'y21ulux1r7mwra1',
    'country_id': '76',
    'market_id': '1',
    'device_id': '1',
    'start_time': str(int(time.time())),
    'end_time': str(int(time.time()) + 4000),
    # 'k': 'VAAHH0tBGAFUdlUBBx9LQhEGU3BVAQEdAUIQQA01HQBEHxUHU1RQaEMXHxlIRxcHUXlcBwIAXlYIUQVoQxcfBw5BDkASJRceUEkOH1NcFSVKUEZY',
}
k = execjs.compile(open('./点点.js', 'r', encoding='utf-8').read()).call('test', params,extracted_dict)
print('k:::', k)
params['k'] = k

response = requests.get('https://api.diandian.com/pc/app/v1/user/favorite/app', params=params, cookies=cookies,
                        headers=headers)
print(response)
print(response.text)
