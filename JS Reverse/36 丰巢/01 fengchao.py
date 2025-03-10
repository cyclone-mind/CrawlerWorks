import random
import time
import ddddocr
import requests
import uuid
import execjs

# The headers to be used in requests to the server
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.fcbox.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.fcbox.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def parse_querySlideImage_url(uuid):
    """
    Sends a POST request to retrieve slide image details based on the provided UUID.

    Parameters:
        uuid (str): The unique identifier for the captcha.

    Returns:
        tuple: A tuple containing checkId, clientIp, key, pointY, shadeImageUrl, and slideImageUrl.
    """
    url = f"https://acs.fcbox.com/captcha/querySlideImage/{uuid}"
    response = requests.post(url, headers=headers)
    checkId = response.json()['data']['checkId']
    clientIp = response.json()['data']['clientIp']
    key = response.json()['data']['key']
    pointY = response.json()['data']['pointY']
    shadeImageUrl = response.json()['data']['shadeImageUrl']
    slideImageUrl = response.json()['data']['slideImageUrl']
    return checkId, clientIp, key, pointY, shadeImageUrl, slideImageUrl

def parse_slide(bg_url, fg_url):
    """
    Downloads background and foreground images, then performs a sliding verification match.

    Parameters:
        bg_url (str): URL of the background image.
        fg_url (str): URL of the foreground image.

    Returns:
        int: The calculated slide distance.
    """
    with open('./x1-bg.jpg', 'wb') as f:
        f.write(requests.get(bg_url).content)
    with open('./x2-fg.jpg', 'wb') as f:
        f.write(requests.get(fg_url).content)
    with open('./x1-bg.jpg', 'rb') as f:
        bg_bytes = f.read()
    with open('./x2-fg.jpg', 'rb') as f:
        front_bytes = f.read()
    ocr = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    result = ocr.slide_match(target_bytes=front_bytes,
                             background_bytes=bg_bytes, simple_target=True)
    slide_distance = result['target'][0]
    return int(slide_distance) - 1

def parse_traceData(slide_distance, pointY):
    """
    Generates a trace data list simulating movement based on slide distance and fixed Y position.

    Parameters:
        slide_distance (int): The distance the slide should cover.
        pointY (int): The fixed Y coordinate for the trace.

    Returns:
        list: A list of dictionaries containing x, y, and time values for each trace point.
    """
    traceData = []
    x = 0
    y = pointY
    t = int(time.time() * 1000)
    while x < slide_distance:
        trace = {"x": x, "y": y, "time": t}
        traceData.append(trace)
        x += random.randint(0, 5)
        y = pointY
        t += random.randint(1, 20)
        if x >= slide_distance:
            x = slide_distance
            trace = {"x": x, "y": y, "time": t}
            traceData.append(trace)
            break
    return traceData

def fetch_data(clientIp, checkId, captcha_uuid, traceData, key):
    """
    Encrypts the parameters needed for captcha verification using JavaScript.

    Parameters:
        clientIp (str): Client IP address.
        checkId (str): Check ID obtained from the captcha image.
        captcha_uuid (str): UUID of the captcha.
        traceData (list): List of generated trace data.
        key (str): Key obtained from the captcha image.

    Returns:
        str: The encrypted parameters for the captcha verification.
    """
    url = f"https://acs.fcbox.com/captcha/checkCode/{captcha_uuid}"
    with open('./04 decrypt.js', 'r') as f:
        js_code = f.read()
    enc_param = execjs.compile(js_code).call('decrypt', clientIp, checkId, captcha_uuid, traceData, key)
    return enc_param

def parse_checkCode_url(captcha_uuid, data):
    """
    Sends a POST request to check the code and retrieves a token.

    Parameters:
        captcha_uuid (str): UUID of the captcha.
        data (str): The encrypted data needed for verification.

    Returns:
        str: The token received from the server.
    """
    url = f"https://acs.fcbox.com/captcha/checkCode/{captcha_uuid}"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://www.fcbox.com",
        "Pragma": "no-cache",
        "Referer": "https://www.fcbox.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    data = data.encode('unicode_escape')
    response = requests.post(url, headers=headers, data=data)
    token = response.json()['data']['token']
    return token

def get_public_key():
    """
    Retrieves the public key needed for password decryption from the server.

    Returns:
        dict: The public key data retrieved from the server.
    """
    cookies = {
        'Hm_lvt_bf8738513d38a2418063f7b873084c15': '1734765429',
        'Hm_lpvt_bf8738513d38a2418063f7b873084c15': '1734765429',
        'HMACCOUNT': '9BFBEC200A822004',
        'Hm_lvt_753eeeff229f4510294f196bd27291b5': '1734765429',
        'Hm_lpvt_753eeeff229f4510294f196bd27291b5': '1734765429',
        '_2a12e': 'http://172.29.107.23:8080',
    }
    response = requests.post('https://www.fcbox.com/noshiro/getPublicKey', cookies=cookies, headers=headers)
    return response.json()['data']

def parse_login(username, password, token):
    """
    Sends the login request with the provided username, password, and token.

    Parameters:
        username (str): The username for login.
        password (str): The password for login.
        token (str): The verification token received from the captcha.

    Returns:
        Response: The HTTP response object from the login request.
    """
    key = get_public_key()
    with open('./05 decrypt_pwd.js', 'r') as f:
        js_code = f.read()
    pwd = execjs.compile(js_code).call('get_pwd', password, key)
    params = {
        'username': username,
        'password': pwd,
        'verifyCode': token,
        '_': int(time.time() * 1000),
    }
    response = requests.get('https://www.fcbox.com/passport/login', params=params, headers=headers)
    return response

def main(username, password):
    """
    Main function that orchestrates the captcha solving and login process.

    Parameters:
        username (str): The username for login.
        password (str): The password for login.
    """
    captcha_uuid = str(uuid.uuid4())

    checkId, clientIp, key, pointY, shadeImageUrl, slideImageUrl = parse_querySlideImage_url(captcha_uuid)

    slide_distance = parse_slide(shadeImageUrl, slideImageUrl)

    traceData = parse_traceData(slide_distance, pointY)

    data = fetch_data(clientIp, checkId, captcha_uuid, traceData, key)

    token = parse_checkCode_url(captcha_uuid, data)
    print(token)

    response = parse_login(username, password, token)
    print(response.text)

if __name__ == '__main__':
    username = 'qwe123456'
    password = 'qwe123'
    main(username, password)