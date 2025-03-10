import requests
import json
import execjs
from PIL import Image
from io import BytesIO
import base64


class DeTaYun:
    def __init__(self, key, verify_idf_id, img_path):
        self.key = key
        self.img_path = img_path
        self.verify_idf_id = verify_idf_id

    # PIL图片保存为base64编码
    def PIL_base64(self, img, coding='utf-8'):
        img_format = img.format
        if img_format == None:
            img_format = 'JPEG'
        format_str = 'JPEG'
        if 'png' == img_format.lower():
            format_str = 'PNG'
        if 'gif' == img_format.lower():
            format_str = 'gif'
        if img.mode == "P":
            img = img.convert('RGB')
        if img.mode == "RGBA":
            format_str = 'PNG'
            img_format = 'PNG'
        output_buffer = BytesIO()
        img.save(output_buffer, quality=100, format=format_str)
        byte_data = output_buffer.getvalue()
        base64_str = 'data:image/' + img_format.lower() + ';base64,' + \
                     base64.b64encode(byte_data).decode(coding)
        return base64_str

    # 验证码识别接口
    def parse_verify(self):
        url = "http://www.detayun.cn/openapi/verify_code_identify/"
        header = {"Content-Type": "application/json"}
        data = {
            # 用户的key
            "key": self.key,
            # 验证码类型
            "verify_idf_id": self.verify_idf_id,
            # 样例图片
            "img_base64": self.PIL_base64(Image.open(self.img_path)),
        }
        # 发送请求调用接口
        response = requests.post(url=url, json=data, headers=header)
        # 获取响应数据，识别结果
        return response.text


def cap_union_prehandle():
    url = "https://turing.captcha.qcloud.com/cap_union_prehandle"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://secure.elong.com/",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    params = {
        "aid": "199680628",  # 192499621,199680628
        "protocol": "https",
        "accver": "1",
        "showtype": "popup",
        "ua": "TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMS4wLjAuMCBTYWZhcmkvNTM3LjM2",
        "noheader": "1",
        "fb": "1",
        "aged": "0",
        "enableAged": "0",
        "enableDarkMode": "0",
        "grayscale": "1",
        "clientype": "2",
        "cap_cd": "",
        "uid": "",
        "lang": "zh-cn",
        "entry_url": "https://secure.elong.com/passport/login_cn.html#",
        "elder_captcha": "0",
        "js": "/tcaptcha-frame.22125576.js",
        "login_appid": "",
        "wb": "1",
        "subsid": "9",
        # "callback": "_aq_177803",
        "sess": ""
    }
    response = requests.get(url, headers=headers, params=params)
    return response.text


def parse_slide_url(img_url, img_name):
    url = "https://turing.captcha.qcloud.com"
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://turing.captcha.gtimg.com/",
        "Sec-Fetch-Dest": "image",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    response = requests.get(url + img_url, headers=headers)
    with open(f'{img_name}.jpg', 'wb') as f:
        # print(f'{img_name}下载成功')
        f.write(response.content)
    return

def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""


def get_slide_x():
    img_path = "./x1-backgroud_img.jpg"
    distance = base64_api(uname='cece', pwd='Aa12345678', img=img_path, typeid=34)
    return int(distance) - 18

# def get_slide_x():
#     key = "MlSIf6jxBTGQ48oImXGj"
#     verify_idf_id = '6'
#     img_path = './x1-backgroud_img.jpg'
#     detayun = DeTaYun(key, verify_idf_id, img_path)
#     distance = json.loads(detayun.parse_verify())['data']['distance']
#     return distance - 20


def get_tdc_js_file(tdc_path_url):
    # tdc_path_url=/tdc.js?app_data=7163914470737158144&t=1652048263
    # https://turing.captcha.qcloud.com/tdc.js?app_data=7163913217567203328&t=295620219
    url = "https://turing.captcha.qcloud.com"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://turing.captcha.gtimg.com/",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    response = requests.get(url + tdc_path_url, headers=headers)
    with open('2-tdc.js', 'w') as f:
        f.write(response.text)
    return


def get_verify_params():
    with open('./3-windowTDC.js', 'r') as f:
        js_file = f.read()
    js_code = execjs.compile(js_file)
    verify_params = js_code.call('get_verify_params')
    collect = verify_params['collect']
    tlg = len(collect)
    eks = verify_params['eks']
    return collect, tlg, eks


def get_pow_params(prehandle_json):
    prefix = prehandle_json["data"]["comm_captcha_cfg"]["pow_cfg"]["prefix"]
    md5 = prehandle_json["data"]["comm_captcha_cfg"]["pow_cfg"]["md5"]
    with open('./4-verify-pow_params.js', 'r') as f:
        js_file = f.read()
    js_code = execjs.compile(js_file)
    pow_params = js_code.call('get_pow_params', prefix, md5)
    pow_answer = prefix + str(pow_params['ans'])
    pow_calc_time = pow_params['duration']
    return pow_answer, pow_calc_time


def cap_union_new_verify(collect, tlg, eks, sess, ans, pow_answer, pow_calc_time):
    url = "https://turing.captcha.qcloud.com/cap_union_new_verify"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://turing.captcha.gtimg.com",
        "Pragma": "no-cache",
        "Referer": "https://turing.captcha.gtimg.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    data = {
        "collect": collect,
        "tlg": tlg,
        "eks": eks,
        "sess": sess,
        "ans": ans,
        "pow_answer": pow_answer,
        "pow_calc_time": pow_calc_time
    }
    response = requests.post(url, headers=headers, data=data)
    return response.text


def main():
    # 1、cap_union_prehandle前置请求接口
    prehandle_response = cap_union_prehandle()
    prehandle_json = json.loads(prehandle_response[1:-1])

    # 2、滑块分析
    # 2.1、背景图
    img_url = prehandle_json["data"]["dyn_show_info"]["bg_elem_cfg"]["img_url"]
    # img_url = "/cap_union_new_getcapbysig?img_index=1&image=02790500005c321000000015022f59763720&sess=s0ZvsyscT3qCfiIAOkHMEq0dxATSwh5SiKTBWA54xIg_smHLojvMLa-SfeFLySxifQWzQ1i-6rq3n0fg-6M2qb4wsLoW4-aXGXtDZ3O7bQH37KDY8vqwV3LifYNaynx1IBpoOT_JBs7WZv3cPkQgg3eE1NCbK7d32bIcn0sSo-G15Gm48gLTDojEQcgodQsdv-u4dJs1lQ96HojaGnH0Mx8RFljyakuB2HqLnY8vUR4I88mEv6HnKRFwUALopQYaoQTcZX3JY1XUJmGXeK7fgv55L_fnKPGvp-5tarN3T1uREn4duLY1cPpznrxo4dyYOPH8RQefe-6oGrb55B9GYxK0hpdiYTgqfxQtxCT8ztHYSP5g_uWahoNgQSSAPQqF8YmXavgaBQ6uJGB113h2Z28lQQF_W9FSQzd7XScHjZsj8*"
    # sprite_url = prehandle_json["data"]["dyn_show_info"]["sprite_url"]
    parse_slide_url(img_url, 'x1-backgroud_img')
    # slide_img = parse_slide_url(sprite_url, 'x2-slide_img')
    # 2.2、滑块参数ans
    x = get_slide_x()
    y = prehandle_json["data"]["dyn_show_info"]["fg_elem_list"][1]["init_pos"][1]
    ans_json = [{"elem_id": 1, "type": "DynAnswerType_POS", "data": f"{x},{y}"}]
    ans = json.dumps(ans_json, separators=(',', ':'))
    # print(ans)

    # 3、获取tdc.js文件
    tdc_path_url = prehandle_json["data"]["comm_captcha_cfg"]["tdc_path"]
    get_tdc_js_file(tdc_path_url)

    # 4、cap_union_new_verify滑块接口
    # 4.1、collect/tlg/eks参数
    collect, tlg, eks = get_verify_params()
    # 4.2、sess/pow_answer/pow_calc_time参数
    sess = prehandle_json['sess']
    pow_answer, pow_calc_time = get_pow_params(prehandle_json)
    # 4.3、请求cap_union_new_verify接口
    verify_response = cap_union_new_verify(
        collect, tlg, eks, sess, ans, pow_answer, pow_calc_time)
    print(verify_response)
    return


if __name__ == '__main__':
    main()
# https://cloud.tencent.com/product/captcha
