"""
1. 这个案例初期做的很不严谨，虽然cookie中的ok-ses-id变化，但其实不要cookie也能请求成功。
2. 所以无论如何应该使用文本比对工具比对两次请求中变化的参数。x-apikey是关键参数，但其实前几位和后几位一样，
只是简单的比对了，没有发现该参数是变化的。最终发现headers中的x-apikey和ok-verify-sign是解密参数。
首先应明确关键参数是在哪个js文件中生成的，可以通过堆栈回溯。
搜apikey出不来。因为在headers中，所以使用了headers关键字搜索，前提是在正确的JS文件中。
3. 在堆栈回溯时，可以直接打断点断在发送请求的JS文件的第一步，以确定参数是在这个JS文件中产生的。
4. `i.o.mathRandom() `其实生成一个随机数，对应着 `Math.random()` 。
5. `a.A.btoa(n)` 其实是一个 base64 的转码，对应着`btoa`。
6. 在控制流开始的地方，switch (e.prev = e.next ){...} 添加日志点：“这个是控制流执行顺序：”，e.next 。
如果case中没有写 e.next = 某个数字的话
"""

import requests
import urllib.parse
import execjs
import time
import subprocess
import json
import sys

timer = int(time.time() * 1000)

headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "app-type": "web",
    "cache-control": "no-cache",
    "devid": "1a8c82bb-69ef-4aef-a06d-f7326d485b5e",
    # "ok-timestamp": "1732178954146",
    # "ok-verify-sign": "msGQobUNPW+aTIy1B/EcXpz6n4P8B2Hw+EmvBX9uCWY=",
    # "ok-verify-token": "235c1703-3b29-4c2d-9d48-8241ba739f3f",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.oklink.com/zh-hans/btc/tx-list/page/2",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    # "x-apikey": "LWIzMWUtNDU0Ny05Mjk5LWI2ZDA3Yjc2MzFhYmEyYzkwM2NjfDI4NDMyOTAwNjUyNTExNTM=",
    "x-cdn": "https://static.oklink.com",
    "x-id-group": "2020121688352890002-c-23",
    "x-kl-ajax-request": "Ajax_Request",
    "x-locale": "zh_CN",
    "x-site-info": "9FjOikHdpRnblJCLiskTJx0SPJiOiUGZvNmIsIiTDJiOi42bpdWZyJye",
    "x-utc": "8",
    "x-zkdex-env": "0"
}
cookies = {
    "devId": "1a8c82bb-69ef-4aef-a06d-f7326d485b5e",
    "ok_site_info": "9FjOikHdpRnblJCLiskTJx0SPJiOiUGZvNmIsIiTDJiOi42bpdWZyJye",
    "locale": "zh_CN",
    "ok-exp-time": str(timer),
    "first_ref": "https%3A%2F%2Fwww.bing.com%2F",
    "okg.currentMedia": "xl",
    "aliyungf_tc": "f3bfee56bdac128f9ff07d423f5c111815e47d963b3a8dd243991425bb48ef7c",
    "traceId": "2020121688352890002",
    "oklink.unaccept_cookie": "1",
    "_monitor_extras": "{\"deviceId\":\"GRp2JWzRLnFZ2of3WV9mbV\",\"eventId\":55,\"sequenceNumber\":55}",
    "amp_d77757": "1a8c82bb-69ef-4aef-a06d-f7326d485b5e...1id6ktp5l.1id6ktrv3.1n.a.21",
    "ok-ses-id": "fbBQO6BLt/PIb5/DJ2uwbVqU3hpCYlHwclgBh+Mt1v93YH3uBnC1E29W0d0Ysm3Quy+Kb4gK8OZglOmoNfkV9XxEZssu7trKzV7P7dj1J8TTp/s1vlicD4Zyud5iiNPR"
}



def get_js_result(url):
    try:
        # 调用 Node.js 脚本，并传递参数
        result = subprocess.run(
            ['node', './bit.js', url],
            capture_output=True,
            text=True,
            check=True
        )
        # 解析 JSON 输出
        output = json.loads(result.stdout)
        return output
    except subprocess.CalledProcessError as e:
        print("Error calling JS script:", e.stderr, file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e, file=sys.stderr)
        return None
def get_apikey():
    return execjs.compile(open('./apikey.js').read()).call('get_apikey')

    print(response)
    print(response.text)

def spider(p):

    # 将字典转换为URL参数字符串
    query_string = urllib.parse.urlencode(p)

    # 基础URL
    base_url = "/api/explorer/v1/btc/transactionsNoRestrict"

    # 将基础URL和参数字符串组合成完整的URL
    full_url = f"{base_url}?{query_string}"
    # print(full_url)
    enc_data = get_js_result(full_url)
    apikey = get_apikey()
    # print(enc_data)
    # print(apikey)

    headers['ok-timestamp'] = str(enc_data.get('Ok-Timestamp'))
    headers['ok-verify-sign'] = enc_data.get('Ok-Verify-Sign')
    headers['ok-verify-token'] = enc_data.get('Ok-Verify-Token')
    headers['x-apikey'] = apikey
    # print(headers)
    response = requests.get(
        'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response

if __name__ == '__main__':
    params = {
        'offset': '20',
        'limit': '20',
        't': str(timer),
    }
    response = spider(params)
    print(response.text)


