import requests
import execjs

account = '13498556932',
password = 'kuis'


enc_account = execjs.compile(open('./account_pwd.js', encoding='utf-8').read()).call('get_account', account)
print(enc_account)