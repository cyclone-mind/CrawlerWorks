"""
import requests
proxies = {
    "http": "http://your_proxy_ip:port",
    "https": "https://your_proxy_ip:port",
}

response = requests.get("http://www.baidu.com", proxies=proxies) # proxies传入的是一个字典
print(response.text)
"""


""""

import requests  
import random  
import time  

# 假设你有一个代理IP列表，若没有，可以从站大爷的API接口获取
proxy_list = [  
    {
   
   "https": "http://168.168.168.168:80808"},  
    {
   
   "https": "http://178.178.178.178:10008"},  
    # ... 添加更多代理IP  
]  

# 验证代理IP是否有效的函数  
def validate_proxy(proxy):  
    try:  
        # 发送一个简单的请求来测试代理是否有效  
        requests.get("https://www.zdaye.com", proxies=proxy, timeout=5)  
        return True  
    except (requests.exceptions.RequestException, requests.exceptions.ConnectionError):  
        return False  

# 移除无效的代理IP并返回有效代理列表  
def refresh_proxy_list(proxy_list):  
    valid_proxies = [proxy for proxy in proxy_list if validate_proxy(proxy)]  
    return valid_proxies  

# 初始化代理IP池  
proxy_pool = refresh_proxy_list(proxy_list)  

# 网络爬虫函数  
def web_crawler(url):  
    if not proxy_pool:  
        print("No valid proxies available in the pool")  
        return None  

    # 从代理IP池中随机选择一个代理IP  
    proxy = random.choice(proxy_pool)  

    try:  
        # 使用代理IP发送请求  
        response = requests.get(url, proxies=proxy, timeout=10)  
        response.raise_for_status()  # 如果请求失败，抛出异常  
        return response.text  
    except (requests.exceptions.RequestException, requests.exceptions.ConnectionError) as e:  
        print(f"Request failed with proxy {proxy['http']}: {e}")  
        # 移除失效的代理IP并更新代理IP池  
        proxy_pool.remove(proxy)  
        proxy_pool = refresh_proxy_list(proxy_list)  
        return None  

# 示例URL  
target_url = "http://example.com/some-data"  

# 爬虫运行次数  
crawl_count = 10  

# 运行爬虫  
for _ in range(crawl_count):  
    data = web_crawler(target_url)  
    if data:  
        # 处理数据，例如解析、存储等  
        print("Data retrieved successfully")  
        # 这里只是简单地打印数据，实际情况下你会对数据做进一步处理  
        print(data)  
    else:  
        print("Failed to retrieve data")  

    # 暂停一段时间，避免过于频繁的请求  
    time.sleep(5)  

# 更新代理IP池以备下次使用  
proxy_pool = refresh_proxy_list(proxy_list)
"""
