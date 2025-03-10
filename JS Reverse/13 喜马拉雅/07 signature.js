require('./04 env')
require('./05 mod01')
require('./06 mod02')
require('./03 loader')

a = window.loader(20)

// 接口测试
// encrypted_account = a.getEncryptPwd('19856613841')
// encrypted_password = a.getEncryptPwd('123456')
// nonce = '0-A33FFC80A67Bddb1872f4eff2225f5a9900ec4473f82fd68b5fa82beffaf72'

var n = process.argv[2]
var i = process.argv[3]
var t = process.argv[4]
function get_sign(n, i, t) {
    return a.getSignature({
        account: n,
        password: i,
        nonce: t
    })
}

// console.log(process.argv)
console.log(get_sign(n, i, t))
process.exit()

