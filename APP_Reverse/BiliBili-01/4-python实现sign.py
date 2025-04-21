import hashlib

data = "aid=115112790728380&auto_play=0&build=6240300&cid=32034588013&did=LUl8HyZCchYuHHlPKk97Tw9fNk4rR3UtYQ&epid=&from_spmid=tm.recommend.0.0&ftime=1762441147&lv=0&mid=0&mobi_app=android&part=1&sid=0&spmid=main.ugc-video-detail.0.0&stime=1762519902&sub_type=0&type=3"
salt = "9cafa6466a028bfb"
obj = hashlib.sha256()
obj.update(data.encode('utf-8'))
obj.update(salt.encode('utf-8'))

res = obj.hexdigest()
print(res)
# hook到的：   3f57c6a5a1a69342ff9a1a11dc4d21ac7b2541ee565b7133c3435af615216f09
# 我们运算得到  3f57c6a5a1a69342ff9a1a11dc4d21ac7b2541ee565b7133c3435af615216f09