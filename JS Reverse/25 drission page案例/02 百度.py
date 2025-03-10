from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions().auto_port()
cp = ChromiumPage(co)
cp.get('https://www.baidu.com/')
cp.ele("#kw").input("IP地址")  # 定位到搜索框并填充数据
cp.wait.load_start()  # 等待页面加载完成
cp.ele("#su").click()  # 找到搜索按钮并点击搜索

# 监听接口：qifu-api.baidubce.com/ip/local/geo/v1/district
cp.listen.start("qifu-api.baidubce.com/ip/local/geo/v1/district")
# 等待监听
res = cp.listen.wait()
print(res.response.body)