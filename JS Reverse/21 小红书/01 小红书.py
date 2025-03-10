# -*- coding: utf-8 -*-
import json

import requests
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

cookies = {
    'abRequestId': '6a3da154-9f4e-5395-85a2-8635e05b8984',
    'xsecappid': 'xhs-pc-web',
    'a1': '191ea69341dhgsp3cc1tdstoju9ys4z4a9vqp5bbn50000265309',
    'webId': 'd492a6bdb3d1f5d09716938476992aa4',
    'web_session': '030037a1d0a58e09c934b6b79b214a073c4bc8',
    'gid': 'yjyd0Kjqjd0qyjyd0Kjq4j2DyfxkMUqSSy9fhDIM9lV7jA28vM4u4U888JK2q8j88D28KdYS',
    'webBuild': '4.34.0',
    'acw_tc': '7035b9ea39a7d14000df5c7c3d54f973c23f0d51e4e8b18c05756ae2ff6443f1',
    'websectiga': 'cffd9dcea65962b05ab048ac76962acee933d26157113bb213105a116241fa6c',
    'sec_poison_id': '91017a2f-cb26-4f7c-9b49-53fe46eec91f',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'abRequestId=6a3da154-9f4e-5395-85a2-8635e05b8984; xsecappid=xhs-pc-web; a1=191ea69341dhgsp3cc1tdstoju9ys4z4a9vqp5bbn50000265309; webId=d492a6bdb3d1f5d09716938476992aa4; web_session=030037a1d0a58e09c934b6b79b214a073c4bc8; gid=yjyd0Kjqjd0qyjyd0Kjq4j2DyfxkMUqSSy9fhDIM9lV7jA28vM4u4U888JK2q8j88D28KdYS; webBuild=4.34.0; acw_tc=7035b9ea39a7d14000df5c7c3d54f973c23f0d51e4e8b18c05756ae2ff6443f1; websectiga=cffd9dcea65962b05ab048ac76962acee933d26157113bb213105a116241fa6c; sec_poison_id=91017a2f-cb26-4f7c-9b49-53fe46eec91f',
    'origin': 'https://www.xiaohongshu.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-b3-traceid': 'd232a364607e2143',
    'x-s': 'XYW_eyJzaWduU3ZuIjoiNTUiLCJzaWduVHlwZSI6IngyIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6ImVmYTNiYWM2MTQxMmQ5OTYyMTU0ZmIyNzc0NzY0MDNlNzMwZTA3ZDllZjQ0MzRlZGY1MTMwYTg4YTg0NmZjMmY0Mzc5ZjI1YWVhOGE0OTI4YTJjZDA2MmNmZDgyMGIyOTRlZDU2M2FlZTgwN2FlODE5NDUyYjBjMzc0NDM5ZGExMDEwOTYyMjgzNzc2NjBkYzRkOTNlYjUyNGM4ZGM3ZTdmYzgxMTUzYzViMDM5MGZjOTY1NmVlOGVhZDliZTBkNGU2ZGI2YjBkOTNhOGRlYWM4ZWM0MWVmMDZmNmUwNTFiNGY3MzUzM2JiZGU4NTE0YTJmMjYwNDg0MjY5OWUzYmVjN2I3ODhlMDhiODI0NmMyNjVkMDE0MzQ2NDYzYzFjYzg2NzA1MWY5ZGNlNWM0Nzg2YTU0OTYwMzQyMjVhNTRkMDlhNGQxMGM1YmZiZjYzY2VlMTE3Mzc2Yzg4MzBkMjJkMzEzMTYyOGI0ODRhNWU5MTQ4YTNmNTgxOGVjNGY2MzBmZWJlODkzMmFlZGIyZjY4ZTBhOGE5NDdlNmUzOTc1In0=',
    'x-s-common': '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',
    'x-t': '1726556705856',
}

json_data = {
    'cursor_score': '',
    'num': 31,
    'refresh_type': 1,
    'note_index': 20,
    'unread_begin_note_id': '',
    'unread_end_note_id': '',
    'unread_note_count': 0,
    'category': 'homefeed.food_v3',
    'search_key': '',
    'need_num': 6,
    'image_formats': [
        'jpg',
        'webp',
        'avif',
    ],
    'need_filter_image': False,
}
with open('./02 小红书.js') as f:
    js_file = f.read()
Xs = execjs.compile(js_file).call('get_headers', json_data)
headers['x-s'] = Xs['X-s']
headers['x-t'] = str(Xs['X-t'])
data = json.dumps(json_data, separators=(',', ':'))
response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', cookies=cookies, headers=headers,
                         data=data)
print(response.text)
print(response)

