cryptoJS = require('crypto-js')
// console.log(cryptoJS.enc.Utf8.parse("1731939342567000"))
data = "your data"
key = "your key"
iv = "your iv"

var i = cryptoJS.enc.Utf8.parse(key)  // enc方法对各种编码的字符串和WordArray.init
    , a = cryptoJS.enc.Utf8.parse(iv)
    , s = cryptoJS.AES.decrypt(data.toString(), i, {
    iv: a
}), c = cryptoJS.enc.Utf8.stringify(s);

console.log(c)