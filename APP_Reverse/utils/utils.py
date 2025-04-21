import random
def query_to_dict(s):
    return {item.split('=')[0]:item.split('=')[1]for item in s.split('&')}

def header_str_to_dict(header_str):
    res = [item for item in
           header_str.split('\n')]
    res = res[1:len(res) - 1]
    d = {item.split('\t')[0]: item.split('\t')[1] for item in res}
    return d


# 获取随机imei-->简单版
def generate_imei():
    return "".join(random.choices('0123456789abcdef', k=15))


# def generate_imei():  # 跟useragent类似，要变换一下
#     # # 生成随机的TAC（前六位）
#     tac = ''.join(random.choices('0123456789', k=6))
#     # 生成随机的FAC（接下来的两位）
#     fac = ''.join(random.choices('0123456789', k=2))
#     # 生成随机的SNR（后面的六位）
#     snr = ''.join(random.choices('0123456789', k=6))
#     # 计算校验位
#     imei_base = tac + fac + snr
#     imei_list = [int(digit) for digit in imei_base]
#     check_digit = sum(imei_list[::-2] + [sum(divmod(d * 2, 10)) for d in imei_list[-2::-2]]) % 10
#     # 生成最终的IMEI
#     imei = imei_base + str((10 - check_digit) % 10)
#     return imei


# aes 加密
###aes的加密
# aes加密方法  pip3 install pycryptodome
from Crypto.Cipher import AES
import base64
def pad_data(data):
    # 计算需要填充的字节数
    pad_len = AES.block_size - (len(data) % AES.block_size)
    # 使用填充字节进行填充
    padding = bytes([pad_len] * pad_len)
    padded_data = data + padding
    return padded_data
def encrypt_data(password):
    # 创建 AES 密码对象
    # cipher = AES.new(key, AES.MODE_CBC, iv)
    # 密钥（16 字节）
    key = b'6d6656a37cdb7977c10f6d83cab168e9'
    # 初始化向量（16 字节）
    iv = b'0000000000000000'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 填充数据
    padded_data = pad_data(password.encode('utf-8'))
    print(padded_data)
    # 加密数据
    encrypted_data = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted_data).decode('utf-8')

# 将 字节流数据/二进制数据 解释为文本的工具
def java_arr_to_python_str(v1, decode = "utf-8"):
    num_list = bytearray()
    for i in v1:
        if i < 0:
            i = i + 256
        num_list.append(i)
    return num_list.decode(decode)

# 以 16 进制的形式展现 java 字节数组
def java_arr_to_python_16(v1):
    py_bytes = bytes([b % 256 for b in v1])
    return py_bytes.hex()

import random


def generate_random_hex_list(length: int = 10) -> str:
    """
    生成指定长度的随机字节，并通过列表收集其十六进制表示后连接返回。

    参数:
        length (int): 随机字节的长度，默认为10。

    返回:
        str: 由十六进制字符组成的字符串，长度为给定字节长度的两倍。
    """
    data = random.randbytes(length)
    ele_list = []
    for item in data:
        ele = hex(item)[2:]  # 将字节转换为不带'0x'前缀的十六进制字符串
        ele_list.append(ele)
    return ''.join(ele_list)


def generate_random_hex_comprehension(length: int = 10) -> str:
    """
    生成指定长度的随机字节，并使用列表推导式将其快速转换为十六进制字符串。

    参数:
        length (int): 随机字节的长度，默认为10。

    返回:
        str: 由十六进制字符组成的字符串，长度为给定字节长度的两倍。
    """
    return ''.join([hex(item)[2:] for item in random.randbytes(length)])






if __name__ == '__main__':
    frida_byte_array = [115, 106, -90, 86, 114, -84, 20, 113, 126, -102, -37, 126, 4, 97, 5, 45]
    print(java_arr_to_python_16(frida_byte_array))