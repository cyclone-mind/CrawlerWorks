import requests

cookies = {
    '_evga_8292': 'ffec7837c9482d5b.',
    'dk_sft_ses': 'c79c2f5b-b829-4dd9-a408-61c4c79caa33',
    'digikey_theme': 'dklt',
    'TS01afc56e': '01c72bed21029d1b11c2a2d501a04024021b9db057c7f04fddc253cdc6b58c4f5ef684f72741051a4e5d4bcb4a81060bb48b8e7a5f',
    'dk_tagxi': 'undefined.0.undefined',
    '__ssid': 'f983cbde3b94686027a61320237c79c',
    'OptanonAlertBoxClosed': '2025-02-05T12:02:09.565Z',
    '_ga': 'GA1.1.432972856.1738756920',
    'search': '%7B%22id%22%3A%22cc9966ca-7905-4eba-b525-ffd4af79800b%22%2C%22usage%22%3A%7B%22dailyCount%22%3A1%2C%22lastRequest%22%3A%222025-02-05T12%3A02%3A13.102Z%22%7D%2C%22version%22%3A1.1%7D',
    '_cs_c': '0',
    '_pxhd': 'dffdf229bbc0522439ceb124046c7ea7fe28d5d28d5bb33ca22b722b9c3307f0:1544bb80-e3b9-11ef-bbbb-5bbec33c4aa6',
    'TSf44f2996027': '08a1509f8aab200083125b41f716fa78c1983b6a52f02db0ff9589c51d13778e120c384eeda461110809e0bff3113000edf8c32f1e226f5b636b720d7a614700d23be74ee1162ca7a35957d4617c08c1644896a78f61ffa830f3bff683eaabc8',
    'pxcts': '2361b427-e3b9-11ef-8924-d1935e651e93',
    '_pxvid': '1544bb80-e3b9-11ef-bbbb-5bbec33c4aa6',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Feb+05+2025+20%3A03%3A15+GMT%2B0800+(%E9%A6%99%E6%B8%AF%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202407.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=3d793a6d-ad47-447f-a33b-4f0539529fce&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&intType=1&geolocation=CN%3BHA&AwaitingReconsent=false',
    'ping-accept-language': 'en-US',
    '_uetsid': '0a42c3e0e3b911efaf6be7f450c52919',
    '_uetvid': '0a42f100e3b911ef819d4715400cd916',
    'EG-U-ID': 'C3fde62005-f731-4a16-a837-72df08a979f3',
    'EG-S-ID': 'E35c2f85fa-ad7d-4c0d-9b47-3d363874483a',
    'QSI_HistorySession': '',
    'TSf2b291e0027': '085f3c8666ab2000345d3408f6e6339cf0e27876797740bfa66f90938dd525ae870e5e18b2e5f04f08363e10c0113000977a8275716463ce5485a7230d896334d227dbc18d6df362cd7ab88b4008e39f019ed92d4f3c4f5105977e3068f0a550',
    'TS01173021': '01ec0843e3fe7ddae93cb27466f24f70f0b8c825f563b89cb83051f46e650752e079d6c2e5e3abc79bfc2106b379c01a65253d0305',
    'dk_ref_click_data': 'ref_click_element=a.tss-css-4ab7bf-root-categoryanchor|li.tss-css-1ymwirl-categorylistitem|ul.tss-css-1b2e6rp-categorylist|div.tss-css-nk42lr-dynamiccontent|div.muigrid-root muigrid-item tss-css-txpgxm-categorysidecar mui-css-1wxaqej|div.tss-css-1msxwy2-contentwrapper-paperwithchildren|section.print-hide tss-css-1co3nbu-stickycontainer|div.muigrid-root muigrid-item muigrid-grid-md-3 tss-css-hharvs-item mui-css-1kwm6s6|div.muigrid-root muigrid-container muigrid-spacing-xs-4 mui-css-1tz8m30|div.muicontainer-root muicontainer-maxwidthxl tss-css-1j9l6vw-container mui-css-1cm4zze|div.tss-css-1h4jlar-headingcontainer|main|div.muiscopedcssbaseline-root mui-css-7hk5do|div#__next',
    'TScb802422027': '089265d43dab2000ca6e53b22ea560263f0ce674ce7fce93faf856590a9295ba17c30d1d7da7b0c2089d3bf85e11300042c49f2f5889c7d16d2ead7eef72dece7922ed918b538d558490cc8d2db59913315bf4c067b5b9bf205d71adfd36b1ea',
    'dk_item_data': 'vil=ps-fam_475',
    'dk_ref_data_x': 'ref_page_type=PS&ref_page_sub_type=FAM&ref_page_id=475&ref_page_url=https://www.digikey.cn/en/products/filter/coaxial-cables-rf/475&ref_content_search_keywords=undefined',
    '_ga_276R9HWFF5': 'GS1.1.1738756919.1.1.1738757189.49.0.0',
    '_cs_cvars': '%7B%221%22%3A%5B%22Page%20Title%22%2C%22Part%20Search%20-%20Family%20Page%22%5D%2C%222%22%3A%5B%22Page%20Site%22%2C%22CN%22%5D%2C%223%22%3A%5B%22Page%20Type%22%2C%22PS%22%5D%2C%224%22%3A%5B%22Page%20Sub%20Type%22%2C%22FAM%22%5D%2C%225%22%3A%5B%22Page%20Content%20Group%22%2C%22Part%20Search%22%5D%2C%226%22%3A%5B%22PageContentSubGroup%22%2C%22Category%20Page%22%5D%2C%227%22%3A%5B%22Page%20ID%22%2C%22475%22%5D%2C%2210%22%3A%5B%22Customer%20Dimension%22%2C%22%7B%5C%22%5C%5C%5C%22PLS%5C%5C%5C%22%5C%22%3A%5C%22Scrolling%5C%22%7D%22%5D%2C%2215%22%3A%5B%22Page%20State%22%2C%22Sort%20Order%20Test%20-%20Default%22%5D%2C%2216%22%3A%5B%22L1%20cat%22%2C%22Cables%2C%20Wires%22%5D%7D',
    '_cs_id': '21b5dea6-f296-a4de-d182-1e6f282ac162.1738756937.1.1738757189.1738756937.1730827023.1772920937304.1',
    'dkc_tracker': '3670569572465',
    '_cs_s': '10.5.0.9.1738759226439',
    '_dd_s': 'rum=0&expire=1738758355464',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': 'Bearer',
    'cache-control': 'no-cache',
    # 'cookie': '_evga_8292=ffec7837c9482d5b.; dk_sft_ses=c79c2f5b-b829-4dd9-a408-61c4c79caa33; digikey_theme=dklt; TS01afc56e=01c72bed21029d1b11c2a2d501a04024021b9db057c7f04fddc253cdc6b58c4f5ef684f72741051a4e5d4bcb4a81060bb48b8e7a5f; dk_tagxi=undefined.0.undefined; __ssid=f983cbde3b94686027a61320237c79c; OptanonAlertBoxClosed=2025-02-05T12:02:09.565Z; _ga=GA1.1.432972856.1738756920; search=%7B%22id%22%3A%22cc9966ca-7905-4eba-b525-ffd4af79800b%22%2C%22usage%22%3A%7B%22dailyCount%22%3A1%2C%22lastRequest%22%3A%222025-02-05T12%3A02%3A13.102Z%22%7D%2C%22version%22%3A1.1%7D; _cs_c=0; _pxhd=dffdf229bbc0522439ceb124046c7ea7fe28d5d28d5bb33ca22b722b9c3307f0:1544bb80-e3b9-11ef-bbbb-5bbec33c4aa6; TSf44f2996027=08a1509f8aab200083125b41f716fa78c1983b6a52f02db0ff9589c51d13778e120c384eeda461110809e0bff3113000edf8c32f1e226f5b636b720d7a614700d23be74ee1162ca7a35957d4617c08c1644896a78f61ffa830f3bff683eaabc8; pxcts=2361b427-e3b9-11ef-8924-d1935e651e93; _pxvid=1544bb80-e3b9-11ef-bbbb-5bbec33c4aa6; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Feb+05+2025+20%3A03%3A15+GMT%2B0800+(%E9%A6%99%E6%B8%AF%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202407.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=3d793a6d-ad47-447f-a33b-4f0539529fce&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&intType=1&geolocation=CN%3BHA&AwaitingReconsent=false; ping-accept-language=en-US; _uetsid=0a42c3e0e3b911efaf6be7f450c52919; _uetvid=0a42f100e3b911ef819d4715400cd916; EG-U-ID=C3fde62005-f731-4a16-a837-72df08a979f3; EG-S-ID=E35c2f85fa-ad7d-4c0d-9b47-3d363874483a; QSI_HistorySession=; TSf2b291e0027=085f3c8666ab2000345d3408f6e6339cf0e27876797740bfa66f90938dd525ae870e5e18b2e5f04f08363e10c0113000977a8275716463ce5485a7230d896334d227dbc18d6df362cd7ab88b4008e39f019ed92d4f3c4f5105977e3068f0a550; TS01173021=01ec0843e3fe7ddae93cb27466f24f70f0b8c825f563b89cb83051f46e650752e079d6c2e5e3abc79bfc2106b379c01a65253d0305; dk_ref_click_data=ref_click_element=a.tss-css-4ab7bf-root-categoryanchor|li.tss-css-1ymwirl-categorylistitem|ul.tss-css-1b2e6rp-categorylist|div.tss-css-nk42lr-dynamiccontent|div.muigrid-root muigrid-item tss-css-txpgxm-categorysidecar mui-css-1wxaqej|div.tss-css-1msxwy2-contentwrapper-paperwithchildren|section.print-hide tss-css-1co3nbu-stickycontainer|div.muigrid-root muigrid-item muigrid-grid-md-3 tss-css-hharvs-item mui-css-1kwm6s6|div.muigrid-root muigrid-container muigrid-spacing-xs-4 mui-css-1tz8m30|div.muicontainer-root muicontainer-maxwidthxl tss-css-1j9l6vw-container mui-css-1cm4zze|div.tss-css-1h4jlar-headingcontainer|main|div.muiscopedcssbaseline-root mui-css-7hk5do|div#__next; TScb802422027=089265d43dab2000ca6e53b22ea560263f0ce674ce7fce93faf856590a9295ba17c30d1d7da7b0c2089d3bf85e11300042c49f2f5889c7d16d2ead7eef72dece7922ed918b538d558490cc8d2db59913315bf4c067b5b9bf205d71adfd36b1ea; dk_item_data=vil=ps-fam_475; dk_ref_data_x=ref_page_type=PS&ref_page_sub_type=FAM&ref_page_id=475&ref_page_url=https://www.digikey.cn/en/products/filter/coaxial-cables-rf/475&ref_content_search_keywords=undefined; _ga_276R9HWFF5=GS1.1.1738756919.1.1.1738757189.49.0.0; _cs_cvars=%7B%221%22%3A%5B%22Page%20Title%22%2C%22Part%20Search%20-%20Family%20Page%22%5D%2C%222%22%3A%5B%22Page%20Site%22%2C%22CN%22%5D%2C%223%22%3A%5B%22Page%20Type%22%2C%22PS%22%5D%2C%224%22%3A%5B%22Page%20Sub%20Type%22%2C%22FAM%22%5D%2C%225%22%3A%5B%22Page%20Content%20Group%22%2C%22Part%20Search%22%5D%2C%226%22%3A%5B%22PageContentSubGroup%22%2C%22Category%20Page%22%5D%2C%227%22%3A%5B%22Page%20ID%22%2C%22475%22%5D%2C%2210%22%3A%5B%22Customer%20Dimension%22%2C%22%7B%5C%22%5C%5C%5C%22PLS%5C%5C%5C%22%5C%22%3A%5C%22Scrolling%5C%22%7D%22%5D%2C%2215%22%3A%5B%22Page%20State%22%2C%22Sort%20Order%20Test%20-%20Default%22%5D%2C%2216%22%3A%5B%22L1%20cat%22%2C%22Cables%2C%20Wires%22%5D%7D; _cs_id=21b5dea6-f296-a4de-d182-1e6f282ac162.1738756937.1.1738757189.1738756937.1730827023.1772920937304.1; dkc_tracker=3670569572465; _cs_s=10.5.0.9.1738759226439; _dd_s=rum=0&expire=1738758355464',
    'lang': 'en',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.digikey.cn/en/products/filter/coaxial-cables-rf/475',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'site': 'cn',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'x-currency': 'CNY',
    'x-kl-ajax-request': 'Ajax_Request',
    'x-request-id': '72a4e501-ba95-40e7-a362-d4526d897aee',
}

params = {
    's': 'N4IgrCBcoA5QTAGhDOl5gL6aA',
}

response = requests.get('https://www.digikey.cn/products/api/v5/filter-page/475', params=params, cookies=cookies, headers=headers)
print(response)
print(response.text)