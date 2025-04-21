import re
import requests
import execjs

cookies = {
    'btoken': '69LFW2ZF3DJ8WUUYXE3O2PC0NJOB682B',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1732092615',
    'hy_data_2020_id': '19348c4006a2716-000227a4cc90fe-26011851-2073600-19348c4006b2b1f',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2219348c4006a2716-000227a4cc90fe-26011851-2073600-19348c4006b2b1f%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2219348c4006a2716-000227a4cc90fe-26011851-2073600-19348c4006b2b1f%22%7D',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.xiniudata.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-kl-ajax-request': 'Ajax_Request',
    # 'cookie': 'btoken=69LFW2ZF3DJ8WUUYXE3O2PC0NJOB682B; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1732092615; hy_data_2020_id=19348c4006a2716-000227a4cc90fe-26011851-2073600-19348c4006b2b1f; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2219348c4006a2716-000227a4cc90fe-26011851-2073600-19348c4006b2b1f%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2219348c4006a2716-000227a4cc90fe-26011851-2073600-19348c4006b2b1f%22%7D',
}




params = {
    'sort': 1,
    'start': 60,
    'limit': 20,
}
with open('xiniu.js', 'r') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
data = ctx.call('get_sig_payload', params)
print(data)
json_data = {
    'payload': data.get('payload'),
    'sig': data.get('sig'),
    'v': 1,
}
response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.status_code)
# print(response.text)

res_data = response.json()
# print(res_data)

decry_data = ctx.call('get_decryptodata', res_data.get("d"))
print(decry_data)

