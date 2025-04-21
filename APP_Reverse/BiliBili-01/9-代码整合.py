import random
import string
import base64
import time
import re
import json
import requests
import hashlib

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def base64_encrypt(data_string):
    data_bytes = bytearray(data_string.encode('utf-8'))
    data_bytes[0] = data_bytes[0] ^ (len(data_bytes) & 0xFF)
    for i in range(1, len(data_bytes)):
        data_bytes[i] = (data_bytes[i - 1] ^ data_bytes[i]) & 0xFF
    res = base64.encodebytes(bytes(data_bytes))
    return res.strip().strip(b"==").decode('utf-8')


def create_random_mac(sep=":"):
    """ 随机生成mac地址 """
    data_list = []
    for i in range(1, 7):
        part = "".join(random.sample("0123456789ABCDEF", 2))
        data_list.append(part)
    mac = sep.join(data_list)
    return mac


def gen_sn():
    return "".join(random.sample("123456789" + string.ascii_lowercase, 10))


mac_string = create_random_mac(sep="")

did = base64_encrypt(f"{mac_string}|||")

# 获取aid和cid
aid=''
cid=''
def get_video_id_info(exec_url):
    session = requests.Session()
    bvid = exec_url.rsplit('/')[-1]
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
    }
    res = session.get(
        url="https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp".format(bvid),
        headers=header
    )

    cid = res.json()['data'][0]['cid']

    res = session.get(
        url="https://api.bilibili.com/x/web-interface/view?cid={}&bvid={}".format(cid, bvid),
        headers=header
    )
    res_json = res.json()
    aid = res_json['data']['aid']
    view_count = res_json['data']['stat']['view']
    duration = res_json['data']['duration']
    session.close()
    print("aid："+str(aid))
    print("cid："+str(cid))

get_video_id_info("https://www.bilibili.com/video/BV1jUHazxELW")
# 1.明文参数
data_dict = {
    "aid": aid,
    "auto_play": "0",
    "build": "6240300",
    "cid": cid,
    "did": did,
    "epid": "",
    "from_spmid": "main.ugc-video-detail.0.0",
    "ftime": str(int(time.time() - random.randint(100, 5000))),
    "lv": "0",
    "mid": "0",
    "mobi_app": "android",
    "part": "1",
    "sid": "0",
    "spmid": "main.ugc-video-detail.0.0",
    "stime": str(int(time.time())),
    "sub_type": "0",
    "type": "3"
}

# 2.sign签名
v1 = "&".join([f"{key}={data_dict[key]}" for key in sorted(data_dict)])
salt = "9cafa6466a028bfb"
obj = hashlib.sha256()
obj.update(v1.encode('utf-8'))
obj.update(salt.encode('utf-8'))

sign_string = obj.hexdigest()
print(sign_string)

data_string = f"{v1}&sign={sign_string}"

# 3.AES加密

KEY = "fd6b639dbcff0c2a1b03b389ec763c4b"
IV = "77b07a672d57d64c"

aes = AES.new(
    key=KEY.encode('utf-8'),
    mode=AES.MODE_CBC,
    iv=IV.encode('utf-8')
)
bytes_data = pad(data_string.encode('utf-8'), 16)

result = [item for item in bytes_data]
print(result)
