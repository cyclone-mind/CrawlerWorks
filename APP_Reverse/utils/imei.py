# 第一：简单粗略版
import random
import uuid
def generate_imei_easy():
    return "".join(random.choices('0123456789abcdef', k=15))

# 第二：精准版
def generate_imei_precise():  # 跟useragent类似，要变换一下
    # # 生成随机的TAC（前六位）
    tac = ''.join(random.choices('0123456789abcdef', k=6))

    # 生成随机的FAC（接下来的两位）
    fac = ''.join(random.choices('0123456789abcdef', k=2))

    # 生成随机的SNR（后面的六位）
    snr = ''.join(random.choices('0123456789abcdef', k=6))

    # 计算校验位
    imei_base = tac + fac + snr
    imei_list = [int(digit) for digit in imei_base]
    check_digit = sum(imei_list[::-2] + [sum(divmod(d * 2, 10)) for d in imei_list[-2::-2]]) % 10

    # 生成最终的IMEI
    imei = imei_base + str((10 - check_digit) % 10)

    return imei

if __name__ == '__main__':
    imei = generate_imei_easy()
    print(imei)
    print(str(uuid.uuid4()))
    print(generate_imei_precise())