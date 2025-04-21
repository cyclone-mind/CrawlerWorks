import hashlib
import string


def encodeMD5(password: str) -> str:
    m = hashlib.md5()
    m.update(password.encode("utf8"))
    return m.hexdigest()


def get_sign(paramMap: dict) -> string:
    str = "W@oC!AH_6Ew1f6%8"
    result = "".join(["{}{}".format(key, paramMap[key]) for key in sorted(paramMap.keys())])
    sign = encodeMD5(f"{str}{result}{str}").upper()
    return sign


if __name__ == '__main__':
    data = {
        "_appid": "atc.android",
        "appversion": "3.77.1",
        "channelid": "csy",
        "pwd": encodeMD5("123456"),
        "udid": 'TqQL7FHOY40ZuoW+03VGhQ+TP8TxLur7/pTOUbwRUxTQMCNdkQ5Sslyfcosq I9XDlv5mKQyv7/8X8fXMjSLxMw==',
        "username": '18523654211',
        'signkey' : None,
        'type' : None,
    }
    print("_sign:::", get_sign(data))

# def initRequestCommonParams(i:int) -> data:
#     treeMap = {
#         "_appid": "atc.android",
#         "appversion": "3.77.1",
#         "channelid": "csy",
#         "pwd": encodeMD5(passwrod),
#         "udid": udid,
#         "username": username
#     }
#     treeMap.update("_sign": get_sign(treeMap))
#     return treeMap
