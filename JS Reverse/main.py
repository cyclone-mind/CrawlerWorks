import requests
import json


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.xiaohongshu.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.xiaohongshu.com/",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "x-b3-traceid": "f75ef827d47f646f",
    "x-mns": "awgzKh+e6J6Dpxjj1wMdBj6jawzm891WHE1bv7XQlhSGPdah2bNDZhchtu28nehcgGIxF6hhtuGhP7tFaKax+98f00jLD6Io7FlknGX4f3gkekcOWH+8Dbd4CBB4uHP79nxkgJSaRLgONfQzd2uEN/ci5Z+DEcoHFMBG2FgpjkFQafB4pltnG4Q3dhMC5EMloBginRxek6jwB2GPp/FiP/gbe+1tTZX+gOzv1k9L44+lPn2EoSYmmk9+eLi4Ho99J3aZhfYQdvuw9m5WmTQtiR/hxNOdbNc7068dcQktXODcL93E5hjyy7p9wN05/NOnjQwdiyfIdCkk4HLOpL1vd7KvhJz5/nttzG0lmevZuL5R0G9GcIPXa03ITROmCv8MOJh6PS76dZ8vZpHSL+aQeeeaSh6MaY0EI+hh5H3knvagkR2J4g5LzyvT3OTjFamug58Ccf3En9MoYCvfxCma9xDWDww+H+Y5vHOmDcOXRgFlahHTou+LZ03QyRhj",
    "x-s": "XYW_eyJzaWduU3ZuIjoiNTYiLCJzaWduVHlwZSI6IngyIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6IjM0Y2U1N2M3OTMyMDgxY2VjNzU3YjA5ZjBjN2EyZWE3OWZkOTU0OGJmNDg2YjQyMWZhZGE4MzUyMDVkMmZkN2UyMDBjMWZjMmQwMjM5MTEwMmRkODc3NWZlOGRmMjhkNDNhOTVjOGJkYzFmMjU3ZDM2MmU2ZjZjNGNiMTg0ZDQzMGUyNzZkZmE4ZTQwNTZlZjVkNTE2YjM5MzRmNDc1ZGU2ZTdiY2E0Yzc5NTRkZWEzODg5OTg0ZDljMDk1YmZlMTMyMzc4ZDE3ZDUwYjI1YmRjNDYxMGZjYmI5NTExYmJlODQzNTMyMmYzZmU1NTAxMmJlNmM5YTFmY2U4ZGE5YzNjMmJmZmEzNmM5OWM5YTUzYzQyOWZmOGFlYTUzZDM1MzVmYWFlYzI0NmU4ZjFhZDE4ZjYyNjI5OTNiMDU0YjEwMjg2ZjM2YzBjY2IwM2U5OTA4MWVmNTE2NzBmY2NmNmZlZTI4MzZlOWI4NjUwNTlmNGVhNzA0OWJhYThiM2M2MzJmNjJhNjlmZDhmMjIxNmJiZjMxZGYyNjhlNjI0Yjk2In0=",
    "x-s-common": "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",
    "x-t": "1743693605708",
    "x-xray-traceid": "cafe1e75a08e6939da7acd0b01a95b31"
}
cookies = {
    "abRequestId": "40ea7692-60c3-50f4-b079-0789b27ef18d",
    "xsecappid": "xhs-pc-web",
    "a1": "1957a97779b392w0ka8ovhdsb6pvvue284as9x16w50000299002",
    "webId": "922bfe1e45d61851325d37d61291b756",
    "gid": "yj2W0jWYd8Yiyj2W0jWWW4CyjDqjJE8T0Ylh0KExfMDKUM28hh7dJj888Jjj88J8DDf4qWYd",
    "web_session": "040069b1990c4f56e80facbad8354bfa40e7d4",
    "webBuild": "4.62.1",
    "unread": "{%22ub%22:%2267d7e92e000000000900e898%22%2C%22ue%22:%2267eaaa4d000000000b02f661%22%2C%22uc%22:25}",
    "loadts": "1743691679625",
    "acw_tc": "0a4ada7717436923840692218ebbb79beb9694a6e96e223f34a44378a515a1",
    "websectiga": "cffd9dcea65962b05ab048ac76962acee933d26157113bb213105a116241fa6c",
    "sec_poison_id": "f95dd0b8-17a1-40cb-988d-d3ac84daa6e1"
}
url = "https://edith.xiaohongshu.com/api/sns/web/v1/search/notes"
data = {
    "keyword": "甲亢哥重庆",
    "page": 99,
    "page_size": 20,
    "search_id": "2emhiey00hsxww4wlp8dg",
    "sort": "general",
    "note_type": 0,
    "ext_flags": [],
    "filters": [
        {
            "tags": [
                "general"
            ],
            "type": "sort_type"
        },
        {
            "tags": [
                "不限"
            ],
            "type": "filter_note_type"
        },
        {
            "tags": [
                "不限"
            ],
            "type": "filter_note_time"
        },
        {
            "tags": [
                "不限"
            ],
            "type": "filter_note_range"
        },
        {
            "tags": [
                "不限"
            ],
            "type": "filter_pos_distance"
        }
    ],
    "geo": "",
    "image_formats": [
        "jpg",
        "webp",
        "avif"
    ]
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)