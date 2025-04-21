import hashlib


def getEncryptPwd(password: str) -> str:
    m = hashlib.md5()
    m.update(password.encode("utf8"))
    return m.hexdigest()

if __name__ == '__main__':
    pwd = '18701918314'
    print(getEncryptPwd(pwd))