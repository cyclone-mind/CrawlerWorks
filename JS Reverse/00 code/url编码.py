import urllib.parse

# s = 'a'
s = ' 123'
ret = urllib.parse.quote(s)
print(ret) # %20123
s = urllib.parse.unquote(ret)
print(s) #  123

params = {'name': '张三', 'age': 20, 'address': '北京市海淀区'}
query_string = urllib.parse.urlencode(params) # 将字典转换为url字符串
print(query_string) # name=%E5%BC%A0%E4%B8%89&age=20&address=%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA

query_string = 'name=%E5%BC%A0%E4%B8%89&age=20&address=%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA'
params = urllib.parse.parse_qs(query_string) # 将url字符串转换为字典
print(params, type(params)) # {'name': ['张三'], 'age': ['20'], 'address': ['北京市海淀区']} <class 'dict'>