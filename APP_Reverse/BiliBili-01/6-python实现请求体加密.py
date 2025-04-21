from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

KEY = "fd6b639dbcff0c2a1b03b389ec763c4b"
IV = "77b07a672d57d64c"

def aes_encrypt(data_string):
    aes = AES.new(
        key=KEY.encode('utf-8'),
        mode=AES.MODE_CBC,
        iv=IV.encode('utf-8')
    )
    raw = pad(data_string.encode('utf-8'), 16)
    return aes.encrypt(raw)


data = "aid=115112790728380&auto_play=0&build=6240300&cid=32034588013&did=LUl8HyZCchYuHHlPKk97Tw9fNk4rR3UtYQ&epid=&from_spmid=tm.recommend.0.0&ftime=1762441147&lv=0&mid=0&mobi_app=android&part=1&sid=0&spmid=main.ugc-video-detail.0.0&stime=1762520941&sub_type=0&type=3&sign=20bf5be3b469b916240d524e8707c14ae60e6cb21ae4ff693cf76fa06ed3fada"

# 字节类型
bytes_data = aes_encrypt(data)

result = [item for item in bytes_data]
print(result)
res = [hex(item)[2:] for item in result]
print(''.join(res))

'''
执行结果：fc4e6c659d49f96125a98c4c58a4bb986f853eeaf7bf2416b3c901341565b2f64532d29d35c3d112ee3967a1a23feed0a62741a37281f23410ae649af37a44ff8ba62571118ac6070dd618326b2b72e7d86747bf36ef5881f9411c95a84c3c180d7b0144d68b0a49a84e5f38243fd354e2595aeda3af3f16be8474acfe596a022a84f32477e283df471308e127cafad8dbf297d3df394a848a884e07f318ad4c8875c1ff36067399c8b2c64a312873a5916d5f332d2c9fa38a638adfb679aaa3a499ee8937cfd26b8b4e8cae735d2df3f52f55a47743616accaec5069a1cf81cd522ff070b9f0378997d3b09f8d59aa9033c6facef889fb7b1961a110a996c2c98c46a3be68cda18623c5eda980dabc32d64b83cba3a9679d74907e4dfc54874251d8378b6749bdd920b9f79e18eae461b17d54562fecd0a7c9477171c613d56545e3c5
抓包：一致

'''