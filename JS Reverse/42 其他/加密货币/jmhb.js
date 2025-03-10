cryptoJS = require('../../crypto-js')
require('./env.js')
require('./loader.js')
require('./mod1.js')
// t = "ozGVG4G39PqcCyHgGGwJa6bIwF9F4vbQHoVVBaT3NNN/UDUoiTOfkPwwxCNuSzik"
// e = 'Y29pbmdsYXNzL2Fw'
eE = window.loader(27885)
eR = window.loader(81354);

ts = "https://capi.coinglass.com";
var eN = function (t) {
    var e, n = eE.ZP.inflate(new Uint8Array(t.match(/[\da-f]{2}/gi).map(function (t) {
        return parseInt(t, 16)
    }))), r = "", i = 16384;
    for (e = 0; e < n.length / i; e++)
        r += String.fromCharCode.apply(null, n.slice(e * i, (e + 1) * i));
    return decodeURIComponent(escape(r += String.fromCharCode.apply(null, n.slice(e * i))))
}
eB = function (t) {
    var e = t;
    return -1 != t.indexOf("ipa/".split("").reverse().join("")) && (e = -1 == t.indexOf("?") ? t.substring(t.indexOf("ipa/".split("").reverse().join("")), t.length) : t.substring(t.indexOf("ipa/".split("").reverse().join("")), t.indexOf("?"))),
        e
}

eZ = function (t, e) {
    var n = eN(eR.AES.decrypt(t, eR.enc.Utf8.parse(e), {
        mode: eR.mode.ECB,
        padding: eR.pad.Pkcs7
    }).toString(eR.enc.Hex));
    return '"' == n.charAt(0) && (n = n.substring(1, n.length)),
    '"' == n.charAt(n.length - 1) && (n = n.substring(0, n.length - 1)),
        n
}

// console.log(eZ(t, e))


function decrypt(data,user) {
    // var e = eB(t.config.url)
    let t = {
        "data": data,
        "status": 200,
        "statusText": "",
        "headers": {
            "cache-control": "no-cache, no-store, must-revalidate",
            "content-type": "application/json",
            "encryption": "true",
            "user": user
        },
        "config": {
            "transitional": {
                "silentJSONParsing": true,
                "forcedJSONParsing": true,
                "clarifyTimeoutError": false
            },
            "adapter": [
                "xhr",
                "http"
            ],
            "transformRequest": [
                null
            ],
            "transformResponse": [
                null
            ],
            "timeout": 10000,
            "xsrfCookieName": "XSRF-TOKEN",
            "xsrfHeaderName": "X-XSRF-TOKEN",
            "maxContentLength": -1,
            "maxBodyLength": -1,
            "env": {},
            "headers": {
                "Accept": "application/json",
                "language": "zh",
                "encryption": "true",
                "cache-ts": "1732030760401"
            },
            "params": {
                "sort": "",
                "order": "",
                "keyword": "",
                "pageNum": 3,
                "pageSize": 20,
                "ex": "all"
            },
            "method": "get",
            "url": "https://capi.coinglass.com/api/home/v2/coinMarkets",
            "baseURL": "https://capi.coinglass.com"
        },
        "request": {},
        "timeout": 30000
    }
    let e = "/api/home/v2/coinMarkets"
        , n = btoa("coinglass".concat(e, "coinglass"));
    console.log('n:::', n)
    let c = n.substring(0, 16),
        s = eZ(t.headers.user, c);
    console.log('c:::', c)
    console.log('s:::', s)
    return eZ(t.data.data, s)
}

// 接口测试


// console.log(decrypt(t))


