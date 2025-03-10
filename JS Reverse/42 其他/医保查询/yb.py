import json
import requests
import execjs

cookies = {
    'amap_local': '310000',
}
page = 2
params = {
    "addr": "",
    "regnCode": "310000",
    "medinsName": "",
    "medinsLvCode": "",
    "medinsTypeCode": "",
    "outMedOpenFlag": "",
    "pageNum": page,
    "pageSize": 10,
    "queryDataSource": "es"
}

enc_data = execjs.compile(open('./signdata.js', 'r', encoding='utf-8').read()).call('get_data', params)

data = json.loads(enc_data)
print(data)
signature = data.get('x-tif-signature')
timestamp = data.get('x-tif-timestamp')
nonce = data.get('x-tif-nonce')
signData = data.get('signData')
headers = {
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'amap_local=310000; yb_header_active=-1',
    'Origin': 'https://fuwu.nhsa.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://fuwu.nhsa.gov.cn/nationalHallSt/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'X-KL-Ajax-Request': 'Ajax_Request',
    'X-Tingyun': 'c=B|4Nl_NnGbjwY;x=a337bd0832c04a75',
    'channel': 'web',
    'contentType': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-tif-nonce': nonce,
    'x-tif-paasid': 'undefined',
    'x-tif-signature': signature,
    'x-tif-timestamp': str(timestamp),
    'x-tingyun': 'c=B|4Nl_NnGbjwY;x=5d7e53eeb1534051'
}

json_data = {
    'data': {
        'data': {
            'encData': '3DFBCA4667B978F639BB23B95DCE4CC7BDF178AF1718B8F5E4BB22A73B5CAC39CCD20943B4DAE96380B41164D761DE9742C84A985FE3BABC31CB352556BB87C9C1495DB24A29AB6BC3A85AB7FCA00F33C56677481A67C67F739EE2C7D589054DC373615B5DDB33C24C5B31E61CB7643E00DDA865C3B75C85735F0744B0227B5CD0B4E7BB97C60BF8E5275CAFCAFD1E13E384C10195003FD638576645B5EF45EA',
        },
        'appCode': 'T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ',
        'version': '1.0.0',
        'encType': 'SM4',
        'signType': 'SM2',
        'timestamp': str(timestamp),
        'signData': signData,
    },
}

response = requests.post(
    'https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.text)
print(response)
