"""
window.PSign.sign中的sign函数内部是一个平坦控制流，不好硬扣，这时改变逻辑，去找window.PSign。搜了window.PSign发现不是webpack而是new
了一个类。不再命名为loader和mod而是命名为source。
补了一些简单的env后不报错，发现h5st直接出来了，但是其实是个假的，因为用py测试了发现拿不到数据。那没辙，上代理监控补环境吧。
第一个点：理论上所有环境都应该补，和浏览器一模一样，只不过不报错，我们先偷懒不补。
第二个点：有时发现h5st结果出来后，那些监控的环境还在打印日志或者hang住了，大概率和我们的h5st没关系了，我们就可以用process.exit()强制程序结束。但是
还有极小概率后面的环境影响前面的h5st，以后遇到了再说。
subprocess.check_output尽量不要用空格。或者使用转义。因为check_output传到终端的命令以空格为分隔符。
subprocess.check_output得到的结果是js文件的所有打印值。需要关掉代理，然后进一步使用re提取h5st
重新补环境，重新打开代理，这里可以在py文件中调用js加密逻辑，打印。即可以运行py文件监控环境。
getElementsByTagName方法返回的是一个数组，注意不是一个对象。
京东的难点就在于document.all环境。它返回的是所有html对象的集合，也就是一个数组。平常我们对于这种情况一般就是补个空对象的数组，结果发现还是不行
，进源文件看见document.all的语句是一个超长的三目运算符。
document.all.__proto__ === HTMLAllCollection.prototype ? void (-0x2681 + -0x1b2 * 0x1 + 0x2833) !== document.all ? null == document.all ? _$tc.bu8 = 0x1b * -0xc3 + 0x2319 + -0x28 * 0x5d : _$tc.bu8 = -0x1 * 0xf5b + 0x85 * -0x31 + 0x28d4 : _$tc.bu8 = -0x269 * 0x6 + -0x1 * 0x4b8 + 0x121 * 0x11 : _$tc.bu8 = 0x228c * -0x1 + -0x1022 + 0x32b0;
不要忘记node环境的关键字删除。
这个接口的风控比较严格，cookie有可能很快就过期了。
京东的这个html接口风控比较严格，可以换返回json数据的那个接口。
打印subprocess的结果时需要使用print(ret.stdout)  # 打印标准输出
"""
# -*- coding: utf-8 -*-
import json
import requests
import subprocess
import re
import time
from hashlib import sha256

timer = int(time.time() * 1000)


def get_h5st(p):
    js_file = './02 京东.js'
    ret = subprocess.run(['node', js_file, json.dumps(p)], capture_output=True, text=True, encoding='utf-8')
    # print(ret.stdout)  # 打印标准输出
    # print(ret.stderr)  # 打印标准错误输出
    return re.search(":::(?P<h5st>.*?):::", ret.stdout).group('h5st')


cookies = {
    'ipLoc-djd': '2-2813-0-0',
    '__jdv': '143920055|direct|-|none|-|1731826741642',
    '3AB9D23F7A4B3CSS': 'jdd03S4PNHN5ETHVTHLH7Y3QN7KXFZ5VCVS2CBEDX572P364PU3HNTLOL5YP2EXNOLUPU224GC4Y7LFRL2JOK2XDN7CQFEYAAAAMTHDVPIHQAAAAAD7U5NQ7GTMA7LYX',
    '__jdu': '17318267416421694805861',
    'shshshfpa': 'f3647ded-212b-9b95-f239-5c0079e42de3-1731826741',
    'shshshfpx': 'f3647ded-212b-9b95-f239-5c0079e42de3-1731826741',
    'areaId': '2',
    'wlfstk_smdl': 'ntu01koqcb6fal7buj9w94uslbak7nqu',
    'TrackID': '1LrIaoLDPpR4fUuPDI2fMnXxX6ffrurfCHpLRxP7oHqTwMX9s2xBaOf6iAnXXlJqy6Y1OG0v9_O0ej4K0TJir9_DnU9UrKzTln6_ncnRKr_I',
    'thor': 'E46492102BBCEFD2CFFC80BA80EC8EF8F52669417E582E8373424D81A1F66115478F816EE85D03B73CA28A21586765DE26C6E11C729E930EC2DCDC7C69F27438C4F2F42F1BF61659986487037557072AAD795D02A6A0EA6C78D8F29E52C5AF734DBC83C52A6CBC9F9D37B68A06E7DDB51A1E750EBE8503E531F4F135FC4A320F69E4B0D5281AF699AB90C5636D8D8AD3F9E3C9707875CE2A05D7E73E6B9338A2',
    'light_key': 'AASBKE7rOxgWQziEhC_QY6yac1wSzqNQMxrPpO23s88NtLVf81lxOExa15ms4kI06N9cet4o',
    'pinId': 'czYWcmDVeEYJbAsbz8NdArV9-x-f3wj7',
    'pin': 'jd_64781993f2ce4',
    'unick': '%E7%BB%99%E6%88%91%E5%B0%8F%E7%AD%96%E7%AD%96',
    'ceshi3.com': '203',
    '_tp': 'C21a8J94duMEufT1Sz3PAshOPlyAuFsV%2BVhg7SuHSb0%3D',
    '_pst': 'jd_64781993f2ce4',
    '__jda': '143920055.17318267416421694805861.1731826742.1731826742.1731826742.1',
    '__jdc': '143920055',
    'shshshfpb': 'BApXSV-jjO_ZAktP902x1IUDwNXfCIpw5BnPDYG5o9xJ1MouvJIG2',
    '3AB9D23F7A4B3C9B': 'S4PNHN5ETHVTHLH7Y3QN7KXFZ5VCVS2CBEDX572P364PU3HNTLOL5YP2EXNOLUPU224GC4Y7LFRL2JOK2XDN7CQFEY',
    'flash': '3_dV-0QDPPUaNOXTskZp-XeQxQ24A2Vt_AXuN6FxNY7qmXNUB7rM84RO8bSOSQ0lIxAVtN7elgHP43_tjVC3XN--Qyq9mZeGvlj5V5tYLBdgVx4cd4M_GxtqcaAdDBHE0rr35OnzzzlqKxBbfQzbBurjWNRaxJpt0X1X3RnOTZ-K2aNW-e1nBBre**',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'cookie': '__jdv=143920055|direct|-|none|-|1725469038503; __jdu=17254690385012015302450; shshshfpa=54074622-fa38-63ff-5f68-e8f15dabe96e-1725469162; shshshfpx=54074622-fa38-63ff-5f68-e8f15dabe96e-1725469162; areaId=7; PCSYCityID=CN_310000_310100_0; ipLoc-djd=7-458-464-37568; mba_muid=17254690385012015302450; jsavif=1; mba_sid=1726119934811684758058003909.1; 3AB9D23F7A4B3CSS=jdd0365EHKN33YV53QJYTUYRWOSKFHJJYJP6CKYYMK634BEESF24X3Y4S4WABYNCMXYC6XTRUXPFAZIQUKMMOLO4ZVPBSXMAAAAMR4TB77LYAAAAACSBGUTC5POVLAIX; _gia_d=1; wlfstk_smdl=nuvdwpijc7ao6vtn1g849c2qg3dx1sjp; TrackID=1MzrsWIfJcNnqy0ZRNFve22iOeLU1QNL1sdcA2N3Jj4v3vjuSWddijEIZjE1i3N1rOvB0KFuAHP-mXMRX0ujWNB29QNDEAcnt_43x7jan9Pg; thor=B1385CA699BE29B12CDB513DE6BBFC6B64C79BD98AFBC69518AE155BC09CDE94A49333B75D94B40B075C576572B0FE0B2C7D2E02A5F5F5FA36E6D9A7F672087B3D9906005BE3986AEB74F8B7B5E1D20975F0AE75842F207FF923CA2096FFEC67FF7EFE9054A3D46F6C28B9DEACDE99D8A563B1E58FCF1B7F3954A92F99A585EF; light_key=AASBKE7rOxgWQziEhC_QY6yahkBxQwE9XNOswKLk61AE6SLn9cJinqygdmK3ctLbVE1vp47Z; pinId=leteGGkBL5U; pin=vz437h; unick=8488ht9kyvzjvb; ceshi3.com=000; _tp=M82tgnVBwuIXRL%2B4F1dywQ%3D%3D; _pst=vz437h; __jda=143920055.17254690385012015302450.1725469039.1726117511.1726119934.6; __jdb=143920055.3.17254690385012015302450|6.1726119934; __jdc=143920055; flash=3_XTjcPUqPMT7ixPF5D37spKp3A-hLVeEk9Ctfwl5YVbW2E3Q3joPEz4wTqez30k6tH5Q8SAamCd-LimDLF7zrEuztlT6seisv_Ey6Siq2AqJU0q8yMqbcIamq7cztZIU-VPxeYPamTl_fjFS8OIn2_GDLo5_ifwS0wBzSLCwJ; shshshfpb=BApXSy2bM5_RA8egyCH-NS-2hgYbmbVi0BmcHlk1q9xJ1MleqxYC2; 3AB9D23F7A4B3C9B=65EHKN33YV53QJYTUYRWOSKFHJJYJP6CKYYMK634BEESF24X3Y4S4WABYNCMXYC6XTRUXPFAZIQUKMMOLO4ZVPBSXM',
    'origin': 'https://search.jd.com',
    'priority': 'u=1, i',
    'referer': 'https://search.jd.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-referer-page': 'https://search.jd.com/Search',
    'x-rp-client': 'h5_1.0.0',
}

params = {
    'appid': 'search-pc-java',
    'functionId': 'pc_search_s_new',
    'client': 'pc',
    'clientVersion': '1.0.0',
    't': str(timer),
    'body': '{"keyword":"手机","pvid":"d1d01d957303422e9ad99c677fd6f34c","isList":0,"page":"7","s":"176","click":"0","log_id":"1726120002045.4883","show_items":""}',
    'loginType': '3',
    'uuid': '143920055.17254690385012015302450.1725469039.1726117511.1726119934.6',
    'area': '7_458_464_37568',
    'h5st': '20240912134648731;yy9mz56nitgmyg96;f06cc;tk03wba721c1618ncRwwyNa7o8kZJcBjtb8CKWjbJusVSj40HFto1IuRIU6mGsT8usg-90Y4k-3sgJCV6uoNc0KpQj9y;404361000b48f0bcaea63a0af54a1a46;4.7;1726120008731;TKmWueWMdg5KB6xNnBpHvK0R0rsLTHSSbdSiFNUzVQA3gqk29xrabrbDHwlxBBs_Avne2Qsg2347P6RO2pnmGt38z0C1C480yGc-Ehzc64_uT1rYvfAdXrnc-4ufy2rN6VoW_znyQO_cgt7fm5aRQuGLxfEW3wAey-TCE77dOeaymjy6NoULN8G8dFTyFkr5XsinswtKcWuW5ZESsiS2rXRCNgjyEnKtcxmiJd-5v8MRt-ZTL27dz3JjTix4NtWF7CECTc2otOGFlOElkzUas15cwIrjGIJrnSTYgjLteNHqFkVybyfa3qGBQQjyCs9thY-SSvVccze2hgZD1u_eUIB9dZbFy82JnRK96Wzf3PTrjz4ntsdoJnA8ZIz_glsQr66_TGRgZT74HLAWTFgEX7QopDOw3x2qF4EQIJlwh3VivUrvifZwI7KcG4Hb_MWgOUMSTct4Glbcl9ETcr9EoSlO-ZBzZUindepKIIsEoLRn0vy6T6OU4IJEiwkvWUobblkCdine926J0EDkvnRlB5wI6utedXghCkPCXV-GsyO104dQuCtLpRmkFDuC6VykF1OWggE7nDk8PeheJO0dl8zjLad9Prk3hGJ0DQIeqffFGvzEemLTD52YgeDqWQHLXbk3;80f4424cd64828e51e23f92e8d7464e1',
    'x-api-eid-token': 'jdd0365EHKN33YV53QJYTUYRWOSKFHJJYJP6CKYYMK634BEESF24X3Y4S4WABYNCMXYC6XTRUXPFAZIQUKMMOLO4ZVPBSXMAAAAMR4TB77LYAAAAACSBGUTC5POVLAIX',
}
s = sha256()
s.update(params['body'].encode())

body = s.hexdigest()

params2 = {
    "appid": "search-pc-java",
    "functionId": "pc_search_s_new",
    "client": "pc",
    "clientVersion": "1.0.0",
    "t": timer,
    "body": body
}
h5st = get_h5st(params2)
print("h5st:::", h5st)
params['h5st'] = h5st

response = requests.get('https://api.m.jd.com/', params=params, cookies=cookies, headers=headers)
print(response.text)
print(response)
