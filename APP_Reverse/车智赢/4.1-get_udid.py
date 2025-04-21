# treeMap.put("udid", AppUtils.getUDID(ContextProvider.getContext()));
# public static String getUDID(Context context) {
#         return SecurityUtil.encode3Des(context, getIMEI(context) + HiAnalyticsConstant.REPORT_VAL_SEPARATOR + (System.currentTimeMillis() / 1000) + ".000000|" + SPUtils.getDeviceId());
#     }
import base64
import time
import string
from Crypto.Cipher import DES3
import uuid

def encode3Des(text:string) -> string:
    BS = 8
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    deskey = "appapiche168comappapiche168comap".encode('utf-8')[:24]
    iv = "appapich".encode('utf-8')

    plaintext = pad(text).encode("utf-8")

    cipher = DES3.new(deskey, DES3.MODE_CBC, iv)
    return base64.b64encode(cipher.encrypt(plaintext)).decode("utf-8")

def get_udid():
    username = "18953675227"
    passwrod = "1234567"

    imei = str(uuid.uuid4()) # 随机uuid
    nano_time =str(time.time())+'.00000|'
    device_id = '449098'  # 可以为空，也可以358908
    return encode3Des(f"{imei}|{nano_time}|{device_id}")

if __name__ == '__main__':
    print("udid:::",get_udid())