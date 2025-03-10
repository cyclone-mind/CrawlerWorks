import time
import requests
import execjs

timer = int(time.time() * 1000)

cookies = {
    'ASP.NET_SessionId': 'yia0gk1jwug2xfesgxkqoc3u',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=yia0gk1jwug2xfesgxkqoc3u',
    'Origin': 'https://ggzyfw.fj.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ggzyfw.fj.gov.cn/index/new/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = {
    'type': '12',
    'IS_IMPORT': 1,
    'pageSize': 4,
    'ts': timer,
}

# 调用JS的sign值函数
sign = execjs.compile(open("05 fjdzjypt.js").read()).call("d", json_data)
print("sign:::",sign)

headers["portal-sign"] = sign

response = requests.post('https://ggzyfw.fj.gov.cn/FwPortalApi/Article/PageList', cookies=cookies, headers=headers,
                         json=json_data)

print(response.text)
