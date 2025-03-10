import requests

# Define the headers to be used in HTTP requests to maintain consistency and proper communication with the server.
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://search.bilibili.com/all?vt=44278689&keyword=mac&from_source=webtop_search&spm_id_from=333.1007&search_source=5&order=pubdate',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

def get_buvid3():
    """
    Sends a GET request to retrieve the `buvid3` cookie from the response.
    This cookie is necessary for subsequent requests for session management.

    Returns:
        str: The value of the `buvid3` cookie.
    """
    params = {
        'spm_id_from': '333.337.search-card.all.click',
    }

    response = requests.get('https://www.bilibili.com/video/BV1YhBZYHEVz/', params=params, headers=headers)
    return response.cookies['buvid3']

buvid3_value = get_buvid3()

# print(buvid3_value)

def get_uuid():
    """
    Uses JavaScript execution to generate a unique identifier (UUID) for the session.

    Returns:
        str: The generated UUID.
    """
    import execjs
    node = execjs.get()
    fp = open('bilibili.js', 'r', encoding='utf-8')
    ctx = node.compile(fp.read())
    uuid = ctx.eval('get__uuid()')
    return uuid

uuid_value = get_uuid()

# print(get_uuid())

def get_b_lsid():
    """
    Uses JavaScript execution to obtain the `b_lsid` cookie value
    which is essential for tracking the user session.

    Returns:
        str: The value of the `b_lsid` cookie.
    """
    import execjs
    node = execjs.get()
    fp = open('bilibili.js', 'r', encoding='utf-8')
    ctx = node.compile(fp.read())
    b_lsid = ctx.eval('get_blsid()')
    return b_lsid

blsid = get_b_lsid()

# print(get_b_lsid())

def get_sid():
    """
    Sends a GET request to obtain the `sid` cookie from the response.

    Returns:
        str: The value of the `sid` cookie.
    """
    response = requests.get(
        'https://api.bilibili.com/x/player/wbi/v2?aid=113557626688987&cid=27066369857&isGaiaAvoided=false&web_location=1315873&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEludGVsLCBJbnRlbChSKSBJcmlzKFIpIFhlIEdyYXBoaWNzICgweDAwMDA0NkE2KSBEaXJlY3QzRDExIHZzXzVfMCBwc181XzAsIEQzRDExKUdvb2dsZSBJbmMuIChJbnRlbC&dm_img_inter=%7B%22ds%22:[],%22wh%22:[3697,2204,81],%22of%22:[49,98,49]%7D&w_rid=6d30c79113f34e7774456946dd777719&wts=1732847047',
        headers=headers,
    )
    sid = response.cookies.get_dict()['sid']
    return sid

sid = get_sid()
# print(get_sid())

# Create a requests session to maintain state across requests and set necessary cookies.
session = requests.session()
session.cookies.set('sid', sid)
session.cookies.set('buvid3', buvid3_value)
session.cookies.set('_uuid', uuid_value)
session.cookies.set('b_lsid', blsid)

# Additional cookies to manage session and state
session.cookies.set('buvid4', 'F28EA838-4FED-9025-0B1B-1BC8A6B1FB6732252-024112901-OVFrWwX7vMS96VbobYV6fQ%3D%3D')
session.cookies.set('b_nut', '1732847129')
session.cookies.set('CURRENT_FNVAL', "4048")
session.cookies.set('buvid_fp', 'a8610d882f9d1b4352253e226c83ac28')
session.cookies.set('bili_ticket', 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9')
session.cookies.set('bili_ticket_expires', '1733106853')
session.cookies.set('rpdid', r"|(m)mkY|RYl0J'u~Jk)R)klR")

# Now requesting to simulate a user interaction
now_url = 'https://api.bilibili.com/x/click-interface/click/now'
ret = session.get(url=now_url, headers=headers).json()
print(ret)

import time, random

# Prepare parameters for the user interaction simulation
ctime = int(time.time())
ftime = str(ctime - random.randint(100, 500)),
stime = str(ctime),
params = {
    'w_aid': '113557626688987',
    'w_part': '1',
    'w_ftime': ftime,
    'w_stime': stime,
    'w_type': '3',
    'web_location': '1315873',
    'w_rid': '142ab5bb9a28e9d6ce8587bf7fdf02bd',
    'wts': '1732848450',
}

# Data required for the POST request
data = {
    'aid': '113557626688987',
    'cid': '27066369857',
    'part': '1',
    'lv': '0',
    'ftime': ftime,
    'stime': stime,
    'type': '3',
    'sub_type': '0',
    'refer_url': 'https://search.bilibili.com/all?vt=44278689&keyword=mac&from_source=webtop_search&spm_id_from=333.1007&search_source=5&order=pubdate',
    'outer': '0',
    'spmid': '333.788.0.0',
    'from_spmid': '333.337.search-card.all.click',
    'session': 'e79d675e2e4398341df79298491f2993',
    'csrf': '',
}

# Send POST request to simulate user interaction
h5_url = 'https://api.bilibili.com/x/click-interface/click/web/h5'
response = session.post(h5_url, params=params, headers=headers, data=data).json()
print(response)