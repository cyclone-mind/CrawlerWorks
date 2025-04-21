cryptoJs = require("../crypto-js")
var m = {
    "words": [
        808530483,
        875902519,
        943276354,
        1128547654
    ],
    "sigBytes": 16
}
var f = {
    "words": [
        1148467306,
        964118391,
        624314466,
        2019968622
    ],
    "sigBytes": 16
}


function b(t) {
    var e = cryptoJs.enc.Hex.parse(t)
        , n = cryptoJs.enc.Base64.stringify(e)
        , a = cryptoJs.AES.decrypt(n, f, {
        iv: m,
        mode: cryptoJs.mode.CBC,
        padding: cryptoJs.pad.Pkcs7
    })
        , r = a.toString(cryptoJs.enc.Utf8);
    return r.toString()
}


// var e = JSON.parse(b(data))
// console.log(b(data))