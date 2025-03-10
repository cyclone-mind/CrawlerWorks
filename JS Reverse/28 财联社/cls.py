import requests
import execjs
cookies = {
    'HWWAFSESID': '51c541ed78197fdb959',
    'HWWAFSESTIME': '1732339979860',
    'Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e': '1732339985',
    'HMACCOUNT': '862BC833877B77B8',
    'hasTelegraphRemind': 'on',
    'hasTelegraphSound': 'on',
    'vipNotificationState': 'on',
    'hasTelegraphNotification': 'off',
    'Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e': '1732340022',
    'tfstk': 'faXmt6ZzasRX9chkq7Jb_6Ztv0N8km96aNH9WdLaaU8SkqHAbFqGbUBv6K8tIlbdRhEXBOnfNwIEHtFXBAvXCdzLJJedDi96QdYRDuLf4gtZtHYZyisXC0ss2zCRcVXOkx_2QNJyUnK2QA-w7umyxUk2bx-ZzuYWbd-20ASy4H-w0nkV7grkfU8ZZcHw-OW5UrB8JRnNVvfymIYiBUDiJlKDieS2ryzFE-OD8i8oQy9P_KYMP9z8Zg_dgZK5SJ4kL6_lIBJgn2tcaMvykpymceWvjMCGxy09Vs7cUCX8fSslIEAF3QmEBLJWbNRGNyDpmKCkttfbf4SVJEfehGn3kgAhZBtyacc2H6IdCBW4n2TJOhbk9s4nnwSPMbleqgM6tr1n1fO2V3YKGvObAS3aZiEuqXNXg3tYJuqo1fO2V3YLqucQGI-WDyC..',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=utf-8',
    # 'Cookie': 'HWWAFSESID=51c541ed78197fdb959; HWWAFSESTIME=1732339979860; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1732339985; HMACCOUNT=862BC833877B77B8; hasTelegraphRemind=on; hasTelegraphSound=on; vipNotificationState=on; hasTelegraphNotification=off; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1732340022; tfstk=faXmt6ZzasRX9chkq7Jb_6Ztv0N8km96aNH9WdLaaU8SkqHAbFqGbUBv6K8tIlbdRhEXBOnfNwIEHtFXBAvXCdzLJJedDi96QdYRDuLf4gtZtHYZyisXC0ss2zCRcVXOkx_2QNJyUnK2QA-w7umyxUk2bx-ZzuYWbd-20ASy4H-w0nkV7grkfU8ZZcHw-OW5UrB8JRnNVvfymIYiBUDiJlKDieS2ryzFE-OD8i8oQy9P_KYMP9z8Zg_dgZK5SJ4kL6_lIBJgn2tcaMvykpymceWvjMCGxy09Vs7cUCX8fSslIEAF3QmEBLJWbNRGNyDpmKCkttfbf4SVJEfehGn3kgAhZBtyacc2H6IdCBW4n2TJOhbk9s4nnwSPMbleqgM6tr1n1fO2V3YKGvObAS3aZiEuqXNXg3tYJuqo1fO2V3YLqucQGI-WDyC..',
    'Pragma': 'no-cache',
    'Referer': 'https://www.cls.cn/telegraph',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'X-KL-Ajax-Request': 'Ajax_Request',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

sign = execjs.compile(open('./cls.js', 'r', encoding='utf-8').read()).call('sign')
params = {
    'app': 'CailianpressWeb',
    'lastTime': '1732339786',
    'os': 'web',
    'sv': '8.4.6',
    'sign': sign,
}


response = requests.get('https://www.cls.cn/nodeapi/refreshTelegraphList', params=params, cookies=cookies, headers=headers)
print(response)
print(response.text)