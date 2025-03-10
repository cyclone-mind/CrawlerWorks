import json
from urllib.parse import quote
import requests
import execjs


cookies = {
    '_c_WBKFRo': 'LnoLtsjXvuJhVWI6m48OCunlKTKkv0mRFLn9BH4V',
    'Hm_lvt_b966fe201514832da03dcf6cbf25b8a2': '1740038230,1740060699',
    'HMACCOUNT': '862BC833877B77B8',
    'acw_tc': '2760825917400649457936300e7d29f55d8f798799aed86593afdc68af4e99',
    'Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2': '1740065085',
    'ssxmod_itna': 'eqh=D5iI4GxUxQq0Le0PF=o5tD=QI4G87teT4ESIKDBkiW4iNDnD8x7YDvmjMt7ihr4b+ec+edDgGSaoKX74aoeY6bnEa0xbDCPGnDBKe=q3YxiiSDCeDIDWeDiDG4Gm4qGtDpxG=Djey1M2yCDYPDEeYDRZPDuO7+DGpz26I+DeKD0ruHDQFwn2DDBx4Y1WD8PmYDeZp+Scozij3x2xG1=40H+mdq2pEUlRDGLtdx59R8DlIRDCKsWzHvaivGZ1A3Hchexp0xbCnDiQ0x3ZxePjZD31+YzWaQoYUY5n0qkr2KCqDWq0DHei4tiDD===',
    'ssxmod_itna2': 'eqh=D5iI4GxUxQq0Le0PF=o5tD=QI4G87teT4ESGD8wpeY5D/K4hxFrnhgI7A7GQD6GS9Uki7QCDmk00xo2iCSifWYe5ZG9O7+eye34ghh8o+WnR2AhD2M7zoHzBIly4LNDO0lYr+yDwaDsza5HzxKWH2n=1GWxqZrNGppm=cYeZ=03gi7WRDxhoAPvCiT4=omqs/F=MoKWbamiqWgkde9NFoT17aYNtm8NvWI7jrDbtQmYBlYefoW5MavkbFyvZcxhayPr=agaShmym85XbuwCrHDhR6QrGoHmbyqmqceNsjmZTuVzP0kMO1BMCX+sSM=+YGS3KZADoAqtDzokQiud7fo+RdpST+MroDr5MhPfF6u3D8Y5iNir=CDQc4QsOezDahgD8CKcbe=xKs4+93bmYQ1RbsEhEmiV8wvrw1Erd=Y10H6bK1DOl+D8rTEWeNu+Q4YyAt4Ld+G=1Abfre08HiAdnfbdu1t3Yyh5mRxfxTyrKe3TfxQk1XWSzlAKEhs6Wb5IaZ7pu7D/+LknH93pf8QEaK0CNHm5cRrpON9RLtrXQq+gAor0pQ7AMmNzabT=QoiRZYd4QdSRuQbihgTbrQG9uWWEzKNv2uZEtZaYigziyrmkYsfmV=p+gKa8BOHTI2zkWYncshFsVGPD7jX0DH65bAXoxqEGBtj6CWeelz5hVT0q70aBh4Y4Ce98jmQ8DG30L+n7GSkDg6+o5BoPlK3DoQxYLG0/f=xo+SxKBoFImg/nwTBr4i8G5nxCB5t4FgftxdjPsAwB9bDD7=DiQp0LYiWhqwNL3Y+AYTieD',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://ctbpsp.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'X-KL-Ajax-Request': 'Ajax_Request',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': '_c_WBKFRo=LnoLtsjXvuJhVWI6m48OCunlKTKkv0mRFLn9BH4V; Hm_lvt_b966fe201514832da03dcf6cbf25b8a2=1740038230,1740060699; HMACCOUNT=862BC833877B77B8; acw_tc=2760825917400649457936300e7d29f55d8f798799aed86593afdc68af4e99; Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2=1740065085; ssxmod_itna=eqh=D5iI4GxUxQq0Le0PF=o5tD=QI4G87teT4ESIKDBkiW4iNDnD8x7YDvmjMt7ihr4b+ec+edDgGSaoKX74aoeY6bnEa0xbDCPGnDBKe=q3YxiiSDCeDIDWeDiDG4Gm4qGtDpxG=Djey1M2yCDYPDEeYDRZPDuO7+DGpz26I+DeKD0ruHDQFwn2DDBx4Y1WD8PmYDeZp+Scozij3x2xG1=40H+mdq2pEUlRDGLtdx59R8DlIRDCKsWzHvaivGZ1A3Hchexp0xbCnDiQ0x3ZxePjZD31+YzWaQoYUY5n0qkr2KCqDWq0DHei4tiDD===; ssxmod_itna2=eqh=D5iI4GxUxQq0Le0PF=o5tD=QI4G87teT4ESGD8wpeY5D/K4hxFrnhgI7A7GQD6GS9Uki7QCDmk00xo2iCSifWYe5ZG9O7+eye34ghh8o+WnR2AhD2M7zoHzBIly4LNDO0lYr+yDwaDsza5HzxKWH2n=1GWxqZrNGppm=cYeZ=03gi7WRDxhoAPvCiT4=omqs/F=MoKWbamiqWgkde9NFoT17aYNtm8NvWI7jrDbtQmYBlYefoW5MavkbFyvZcxhayPr=agaShmym85XbuwCrHDhR6QrGoHmbyqmqceNsjmZTuVzP0kMO1BMCX+sSM=+YGS3KZADoAqtDzokQiud7fo+RdpST+MroDr5MhPfF6u3D8Y5iNir=CDQc4QsOezDahgD8CKcbe=xKs4+93bmYQ1RbsEhEmiV8wvrw1Erd=Y10H6bK1DOl+D8rTEWeNu+Q4YyAt4Ld+G=1Abfre08HiAdnfbdu1t3Yyh5mRxfxTyrKe3TfxQk1XWSzlAKEhs6Wb5IaZ7pu7D/+LknH93pf8QEaK0CNHm5cRrpON9RLtrXQq+gAor0pQ7AMmNzabT=QoiRZYd4QdSRuQbihgTbrQG9uWWEzKNv2uZEtZaYigziyrmkYsfmV=p+gKa8BOHTI2zkWYncshFsVGPD7jX0DH65bAXoxqEGBtj6CWeelz5hVT0q70aBh4Y4Ce98jmQ8DG30L+n7GSkDg6+o5BoPlK3DoQxYLG0/f=xo+SxKBoFImg/nwTBr4i8G5nxCB5t4FgftxdjPsAwB9bDD7=DiQp0LYiWhqwNL3Y+AYTieD',
}






def main(province, industry,currentpage,type1):
    province1 = quote(province)
    industry1 = quote(industry)
    type1 = str(type1)
    currentpage1 = str(currentpage)
    params0 = f"https://ctbpsp.com/cutominfoapi/recommand/type/{type1}/pagesize/10/currentpage/{currentpage1}?province={province1}&industry={industry1}"
    print(params0)
    # "https://ctbpsp.com/cutominfoapi/recommand/type/0/pagesize/10/currentpage/3?province=%E5%8C%97%E4%BA%AC&industry=%E5%85%AC%E8%B7%AF"
    type__1017 = execjs.compile(open('./type_1017.js', 'r', encoding='utf-8').read()).call('get_type',params0)
    print(type__1017)

    url = params0+f'&type__1017={type__1017}'
    # print(url)
    response = requests.get(
        url = url,
        cookies=cookies,
        headers=headers,
    )
    # print(response)
    print(response.text)

    data = execjs.compile(open('./招标.js', 'r', encoding='utf-8').read()).call('Y',response.text.strip('"'))
    print(data)

if __name__ == '__main__':
    main('北京', '公路', 3, 5)
