# treeMap.put("udid", AppUtils.getUDID(ContextProvider.getContext()));
# public static String getUDID(Context context) {
#         return SecurityUtil.encode3Des(context, getIMEI(context) + HiAnalyticsConstant.REPORT_VAL_SEPARATOR + (System.currentTimeMillis() / 1000) + ".000000|" + SPUtils.getDeviceId());
#     }
import base64
import hashlib
import string
import time
import uuid

import requests
from Crypto.Cipher import DES3


def encode3Des(text: string) -> string:
    BS = 8
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    deskey = "appapiche168comappapiche168comap".encode('utf-8')[:24]
    iv = "appapich".encode('utf-8')

    plaintext = pad(text).encode("utf-8")

    cipher = DES3.new(deskey, DES3.MODE_CBC, iv)
    return base64.b64encode(cipher.encrypt(plaintext)).decode("utf-8")


def get_udid():
    imei = str(uuid.uuid4())  # 随机uuid
    nano_time = str(time.time()) + '.00000|'
    device_id = '449098'  # 可以为空，也可以358908
    return encode3Des(f"{imei}|{nano_time}|{device_id}")


def encodeMD5(password: str) -> str:
    m = hashlib.md5()
    m.update(password.encode("utf8"))
    return m.hexdigest()


def get_sign(paramMap: dict) -> string:
    str = "W@oC!AH_6Ew1f6%8"
    result = "".join(["{}{}".format(key, paramMap[key]) for key in sorted(paramMap.keys())])
    sign = encodeMD5(f"{str}{result}{str}").upper()
    return sign


def run():
    username = "18701918314"
    password = "123456"

    data = {
        "_appid": "atc.android",
        "appversion": "3.77.1",
        "channelid": "csy",
        "pwd": encodeMD5(password),
        "signkey":"", # 这两个字段要么没有、要么空字符串，不能是None，因为None会出现在字符串中，生成的sign不对
        "type":"",
        "udid": get_udid(),
        "username": username,
    }

    sign = get_sign(data)
    data.update({'_sign': sign})

    res = requests.post(
        url="https://dealercloudapi.che168.com/tradercloud/sealed/login/login.ashx",
        data=data
    )

    print(res.text)


if __name__ == '__main__':
    run()
