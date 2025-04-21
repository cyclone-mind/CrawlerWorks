import requests

res = requests.get(
    url="https://vcsp-api.vip.com/token/getTokenByFP?vcspKey=4d9e524ad536c03ff203787cf0dfcd29",
    headers={
        "vcspauthorization": "vcspSign=05a68135d2bfd322e3a22f95bbc25a24c777f387"
    }
)

print(res.text)
# {"code":1,"data":{"expireTime":"1766319949","vcspToken":"NGQ5ZTUyNGFkNTM2YzAzZmYyMDM3ODdjZjBkZmNkMjl8fHwxNzY2MzE5OTQ5fHx8.3236811a9e0c3aa9b593558829741242"},"msg":"ok"}