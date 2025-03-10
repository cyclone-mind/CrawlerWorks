import json
import re
import base64
import execjs
import requests


def cap_union_prehandle():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://cloud.tencent.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'aid': '199999861',
        'protocol': 'https',
        'accver': '1',
        'showtype': 'popup',
        'ua': 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMS4wLjAuMCBTYWZhcmkvNTM3LjM2',
        'noheader': '1',
        'fb': '1',
        'aged': '0',
        'enableAged': '0',
        'enableDarkMode': '0',
        'grayscale': '1',
        'clientype': '2',
        'cap_cd': '',
        'uid': '',
        'lang': 'zh-cn',
        'entry_url': 'https://cloud.tencent.com/product/captcha',
        'elder_captcha': '0',
        'js': '/tcaptcha-frame.7cfc3d42.js',
        'login_appid': '',
        'wb': '2',
        'subsid': '8',
        # 'callback': '_aq_228146',
        'sess': '',
    }

    response = requests.get('https://turing.captcha.qcloud.com/cap_union_prehandle', params=params, headers=headers)

    return response.text


def parse_slide_url(img_url, img_name):
    url = "https://turing.captcha.qcloud.com"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://cloud.tencent.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
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


def get_tdc_js_file(tdc_path_url):
    # tdc_path_url=/tdc.js?app_data=7163914470737158144&t=1652048263
    # https://turing.captcha.qcloud.com/tdc.js?app_data=7163913217567203328&t=295620219
    url = "https://turing.captcha.qcloud.com"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://cloud.tencent.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(url + tdc_path_url, headers=headers)
    with open('03 tdc.js', 'w') as f:
        f.write(response.text)
    return


def get_verify_params():
    with open('./02 Tencent_slider.js', 'r') as f:
        js_code = f.read()
    params = execjs.compile(js_code).call('get_verify_params')
    tlg = len(params['collect'])
    return params['collect'], tlg, params['eks']


def get_pow_params(prefix,md5):
    with open('./04 ans.js', 'r') as f:
        js_code = f.read()
    params = execjs.compile(js_code).call('get_pow_params',prefix,md5)
    return params['ans'],params['duration']

def cap_union_new_verify(collect, tlg, eks, sess, ans, pow_answer, pow_calc_time):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://turing.captcha.gtimg.com",
        "Referer": "https://turing.captcha.gtimg.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://turing.captcha.qcloud.com/cap_union_new_verify"
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
    print("prehandle_reponse:::",prehandle_response)
    prehandle_json = prehandle_json = json.loads(prehandle_response[1:-1])
    prefix = prehandle_json["data"]["comm_captcha_cfg"]["pow_cfg"]["prefix"]
    md5 = prehandle_json["data"]["comm_captcha_cfg"]["pow_cfg"]["md5"]
    print('prefix:::',prefix)
    print('md5:::',md5)
    # print(prehandle_json)

    # 2、滑块分析
    # 2.1、背景图
    img_url = prehandle_json["data"]["dyn_show_info"]["bg_elem_cfg"]["img_url"]
    # img_url = "/cap_union_new_getcapbysig?img_index=1&image=027905000074652b000000098d028dfe2b9a&sess=s0I62lGZVOY0T_TOJOx8Gv1VBiTdBCzG-wxPYeBy8WGYPX9V9KzjdQx2Zm-ei0A6EuoH7a42z25tGQaBuWMEtvI7wqJj6Bo7uWhAvifjjCrvZveoAqrwd-A-j0ESV0lEVAEUrZ2ji-0bcxLMPFEI7nDks4sA3vAxiuGg6MygNngDlJ8dyb7rkL1cY_C980PnsEQNwjRzOZo1TASD5EjFNPzxdSl6qR7qpfeNvsW_vETMT7yp7xAnx8G5H6ahgSMqEFFarhbEGhEZ7mLsNHyHg7ifteWUV0g05y_9XKz3jGbhrDMBHNpNbahZFtWCRHlfzkOnsyZDweeqDza7E7ioZV40Li54fLP27L9FwwucE6S03qByJ64mxob9iSmElkjrcUNRpiUbcGWMQVNm_SNSLeywDBvlQmlzlAYYp98RA8udChFjhrxNRbf0ZOMoZgRQh3"
    sprite_url = prehandle_json["data"]["dyn_show_info"]["sprite_url"]
    parse_slide_url(img_url, 'x1-backgroud_img')
    slide_img = parse_slide_url(sprite_url, 'x2-slide_img')
    print("img_url:::",img_url)
    print("sprite_url:::",sprite_url)


    # 2.2、滑块参数ans
    x = get_slide_x()
    y = prehandle_json["data"]["dyn_show_info"]["fg_elem_list"][1]["init_pos"][1]
    print("x:::",x)
    print("y:::",y)
    ans_json = [{"elem_id": 1, "type": "DynAnswerType_POS", "data": f"{x},{y}"}]
    ans = json.dumps(ans_json, separators=(',', ':'))
    print("ans:::",ans)

    # 3、获取tdc.js文件
    tdc_path_url = prehandle_json["data"]["comm_captcha_cfg"]["tdc_path"]
    get_tdc_js_file(tdc_path_url)

    # 4、cap_union_new_verify滑块接口
    # 4.1、collect/tlg/eks参数
    collect, tlg, eks = get_verify_params()
    print("collect:::",collect)
    print("tlg:::",tlg)
    print("eks:::",eks)
    # 4.2、sess/pow_answer/pow_calc_time参数
    sess = prehandle_json['sess']
    print("sess:::",sess)
    pow_answer, pow_calc_time = get_pow_params(prefix, md5)
    pow_answer = prefix + str(pow_answer)
    print("pow_answer:::",pow_answer)
    print("pow_calc_time:::",pow_calc_time)
    # 4.3、请求cap_union_new_verify接口
    verify_response = cap_union_new_verify(
        collect, tlg, eks, sess, ans, pow_answer, pow_calc_time)
    print(verify_response)
    return
    # collect, tlg, eks = get_verify_params()
    # print(collect, tlg, eks)


if __name__ == '__main__':
    main()
