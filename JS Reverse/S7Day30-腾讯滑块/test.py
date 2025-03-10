import execjs


def get_verify_params():
    with open('./3-windowTDC.js', 'r') as f:
        js_file = f.read()
    js_code = execjs.compile(js_file)
    verify_params = js_code.call('get_verify_params')
    collect = verify_params['collect']
    tlg = len(collect)
    eks = verify_params['eks']
    return collect, tlg, eks

print(get_verify_params())