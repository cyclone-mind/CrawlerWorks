# url : https://webapi.cninfo.com.cn/#/marketDataDate
import requests
import execjs



def spider(tdate):
    with open('szx.js', 'r') as f:
        js_code = f.read()
    ctx = execjs.compile(js_code)
    Accept_EncKey = ctx.call('getResCode')
    headers = {
    'Accept': '*/*',
    'Accept-EncKey': Accept_EncKey,
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://webapi.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://webapi.cninfo.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'X-KL-Ajax-Request': 'Ajax_Request',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1742973791; MALLSSID=6E7945505731644E484953775564633161596372626264344E4833674C45787A77714865374A4C697267674E466178763967657348327859356441774C377158; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1742974809',
}

    data = {
        'tdate': tdate,
        'market': 'SZE',
    }
    response = requests.post('https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007', headers=headers, data=data)
    print(response.text)

def main(tdate):
    spider(tdate)

if __name__ == '__main__':
    res = main('2025-03-20')
    print(res)
