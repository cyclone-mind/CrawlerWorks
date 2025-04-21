import hashlib
# 时间戳+0--100w之间的数字
arg0 = "1763124305081257773"

hash_object = hashlib.sha1()
hash_object.update(arg0.encode('utf-8'))
arg7 = hash_object.hexdigest()
print(arg7)
# 运行得到：32eafdfe550b874506427c18fd4bbb2944931d2c
# hook得到：32eafdfe550b874506427c18fd4bbb2944931d2c