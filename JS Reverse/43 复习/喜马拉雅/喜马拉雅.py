import requests
import subprocess
import json
import execjs
import time

cookies = {
    '_xmLog': 'h5&3b428353-3e0d-48ce-b173-1ba2a821c535&process.env.sdkVersion',
    'xm-page-viewid': 'ximalaya-web',
    'wfp': 'ACNiODExM2Y3M2ZhM2NhYjc0GjnRRLTEgJh4bXdlYl93d3c',
    'Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070': '1731808675',
    'HMACCOUNT': '083BE51DCD25A78F',
    'Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070': '1731808699',
    'trackType': 'web',
    'x_xmly_traffic': 'utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A',
    'impl': 'passport.ximalaya.com.web',
    's&e': 'bc57db7d4cf06729562d29811a9fad7d',
    's&a': '%1C%0CZX%0A%05@%07N%0C%05STXMZOQY%07XZCRK%0AV%09%0F%07@%07VZXOYXWU@G^ZXSWZOP',
    'fds_otp': '6441412359124443865',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': '_xmLog=h5&3b428353-3e0d-48ce-b173-1ba2a821c535&process.env.sdkVersion; xm-page-viewid=ximalaya-web; wfp=ACNiODExM2Y3M2ZhM2NhYjc0GjnRRLTEgJh4bXdlYl93d3c; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1731808675; HMACCOUNT=083BE51DCD25A78F; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1731808699; trackType=web; x_xmly_traffic=utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A; impl=passport.ximalaya.com.web; s&e=bc57db7d4cf06729562d29811a9fad7d; s&a=%1C%0CZX%0A%05@%07N%0C%05STXMZOQY%07XZCRK%0AV%09%0F%07@%07VZXOYXWU@G^ZXSWZOP; fds_otp=6441412359124443865',
    'Origin': 'https://passport.ximalaya.com',
    'Pragma': 'no-cache',
    'Referer': 'https://passport.ximalaya.com/page/web/login?fromUri=https%3A%2F%2Fstudio.ximalaya.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'X-KL-Ajax-Request': 'Ajax_Request',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'fromUri': 'https%3A%2F%2Fstudio.ximalaya.com',
}


# 第一次请求拿到nonce
def get_nonce():
    t = int(time.time() * 1000)
    url = f'https://passport.ximalaya.com/web/nonce/{t}'
    response = requests.get(url=url, cookies=cookies, headers=headers)
    nonce = response.json().get('nonce')
    return nonce


def get_enc_account(account):
    enc_account = subprocess.check_output(f'node "./account_pwd.js" {account}', shell=True).decode('utf-8').strip()
    return enc_account


def get_enc_password(password):
    enc_password = subprocess.check_output(f'node "./account_pwd.js" {password}', shell=True).decode('utf-8').strip()
    return enc_password


def get_signature(n, i, t):
    enc_account = n
    enc_password = i
    nonce = t
    signature = subprocess.check_output(f'node "./signature.js"  {enc_account} {enc_password} {nonce}',
                                        shell=True).decode('utf-8').strip()
    return signature


def spider_login(encrypted_account, encrypted_pwd, nonce, signature):
    data = {
        'account': encrypted_account,
        'password': encrypted_pwd,
        'nonce': nonce,
        'signature': signature,
        'fromUri': 'https%3A%2F%2Fstudio.ximalaya.com',
        'fdsOtp': '',
    }
    json_data = json.dumps(data, separators=(',', ':'))
    response = requests.post(
        'https://passport.ximalaya.com/web/login/pwd/v2',
        params=params,
        cookies=cookies,
        headers=headers,
        data=json_data,
    )
    print(response.text)


def main(account, password):
    encrypted_account = get_enc_account(account)
    encrypted_pwd = get_enc_password(password)
    print("enc_account:", encrypted_account)
    print("enc_password:", encrypted_pwd)
    nonce = get_nonce()
    # nonce = "0-4BF3DA2F55805f0f5ac7805f87e053a4da1fa5f4d5f4fc60b7041fbda5e891"
    signature = get_signature(encrypted_account, encrypted_pwd, nonce)
    print('signature--->', signature)
    spider_login(encrypted_account, encrypted_pwd, nonce, signature)


if __name__ == '__main__':
    account = '15100326608'
    password = '123456'
    main(account, password)
