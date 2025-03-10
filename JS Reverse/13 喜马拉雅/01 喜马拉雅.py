"""
喜马拉雅关键要点：
1. 加密入口通过关键字或者XHR回溯定位。模块所在的文件使用的是数组，a=r[20]中的20不是键而是数组的索引。
2. 加载器模块初始化的动作注释不掉，所以只能补a__award_library__变量，mod 01使用到了a__award_library__变量。
3. 全局搜__award_library__，将__award_library__所在的文件也作为一个模块，但是导入的顺序是需要先导入mod02，再导入mod01。
4. 发现__award_library__所在的mod02文件中，去掉__award_library__的var声明，变为全局变量，这样require之后r[20]所在的mod01就可以
使用__award_library__了。
5. 第一个难点，设置creatElement方法时，应当根据传进来的参数创建不同的element对象
6. 第二个难点，当最后一个监控的对象被调用的属性或方法设置了以后仍旧绕不过去，所有的对象也都监控了，日志还是看不出来，还是绕不过去。那就是有可
能是之前监控的对象（那些没有补的但是没报错的属性或方法）在后面用到了。一种方法：根据报错位置，在源文件中查看其逻辑。另一种方法：回头把偷懒没补
的属性或方法补上。
7. a.getSignature函数中的n,i,t是加密参数，必须将断点断在a.getSignature函数是，鼠标悬浮显示的才是真正的加密所需要的参数。原因是n，i，t
在加密signature前完成了重新加密赋值。
8. js代码会hang住，使用process强制结束，但是execjs无法调用，所以只能用subprocess.check_output()运行终端，在终端运行js代码。并且拿到
js代码的打印结果。
"""
# -*- coding: utf-8 -*-
import requests
import subprocess
# from functools import partial
import json
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import time

cookies = {
    '_xmLog': 'h5&0a7fb2fd-ee95-480c-a827-7d50a14df224&process.env.sdkVersion',
    'xm-page-viewid': 'ximalaya-mobile',
    'wfp': 'ACMyMzBmMjQ2YTBjNDk4ZGQ1wnF2a9nNXqp4bXdlYl9t',
    'Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070': '1725894472',
    'Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070': '1725894472',
    'HMACCOUNT': 'BA51EFD0C63D01A7',
    'trackType': 'web',
    'x_xmly_traffic': 'utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A',
    'impl': 'passport.ximalaya.com.web',
    's&e': 'd9d739335f8c013cad121e5e40c28e15',
    's&a': '%1ER%0BXYZLTO%01W%04^RL%04%1B%0F^U_%06N%06N[%08UV%06JVVZYOYVWT@G^XUZWW@R',
    'fds_otp': '5372227307329413477',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': '_xmLog=h5&0a7fb2fd-ee95-480c-a827-7d50a14df224&process.env.sdkVersion; xm-page-viewid=ximalaya-mobile; wfp=ACMyMzBmMjQ2YTBjNDk4ZGQ1wnF2a9nNXqp4bXdlYl9t; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1725894472; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1725894472; HMACCOUNT=BA51EFD0C63D01A7; trackType=web; x_xmly_traffic=utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A; impl=passport.ximalaya.com.web; s&e=d9d739335f8c013cad121e5e40c28e15; s&a=%1ER%0BXYZLTO%01W%04^RL%04%1B%0F^U_%06N%06N[%08UV%06JVVZYOYVWT@G^XUZWW@R; fds_otp=5372227307329413477',
    'Origin': 'https://passport.ximalaya.com',
    'Referer': 'https://passport.ximalaya.com/page/web/login?fromUri=https%3A%2F%2Fstudio.ximalaya.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_encrypted_pwd(account):
    encrypted_account = subprocess.check_output(f'node "./02 account_pwd.js" {account}', shell=True).decode('utf-8').strip()
    return encrypted_account



def get_nonce():
    t = int(time.time() * 1000)
    url = f'https://passport.ximalaya.com/web/nonce/{t}'
    response = requests.get(url=url, cookies=cookies, headers=headers)
    nonce = response.json().get('nonce')
    return nonce


def get_signature(account, password, nonce):
    signature = subprocess.check_output(f'node "./07 signature.js" {account} {password} {nonce}', shell=True).decode('utf-8').strip()
    return signature


def spider_login(encrypted_account, encrypted_pwd, nonce, signature):
    params = {
        'fromUri': 'https%3A%2F%2Fstudio.ximalaya.com',
    }
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
    encrypted_account = get_encrypted_pwd(account)
    encrypted_pwd = get_encrypted_pwd(password)
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
