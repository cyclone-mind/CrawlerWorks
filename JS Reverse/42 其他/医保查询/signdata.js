cryptoJS = require('../../crypto-js')
require('./env.js')
require('./loader.js')

sm2 = window.loader("68b2").sm2
e_ = window.loader('b639').Buffer
sm4 = window.loader("68b2").sm4


function p(e) {
    var t = new Array
        , n = 0;
    for (var i in e)
        t[n] = i,
            n++;
    var r = [].concat(t).sort()
        , o = {};
    for (var a in r)
        o[r[a]] = e[r[a]];
    return o
}

function m(e) {
    var t = {}
        , n = ["signData", "encData", "extra"];
    for (var i in e)
        e.hasOwnProperty(i) && !n.includes(i) && null != e[i] && (t[i] = e[i]);
    return t
}

function v(e) {
    var t = [];
    for (var n in e)
        if (e.hasOwnProperty(n) && (e[n] || "".concat(e[n])))
            if ("data" === n) {
                var i = Object.assign({}, e[n]);
                for (var r in i) {
                    if ("number" != typeof i[r] && "boolean" != typeof i[r] || (i[r] = "" + i[r]),
                    Array.isArray(i[r]) && !i[r].length && delete i[r],
                    Array.isArray(i[r]) && i[r].length > 0)
                        for (var o = 0; o < i[r].length; o++)
                            i[r][o] = p(i[r][o]);
                    null != i[r] && i[r] || delete i[r]
                }
                var a = p(i);
                t.push("".concat(n, "=").concat(JSON.stringify(a)))
            } else
                t.push("".concat(n, "=").concat(e[n]));
    return t.push("key=".concat(u)),
        t.join("&")
}

function A(e) {
    var t, n, i = new Array;
    t = e.length;
    for (var r = 0; r < t; r++)
        (n = e.charCodeAt(r)) >= 65536 && n <= 1114111 ? (i.push(n >> 18 & 7 | 240),
            i.push(n >> 12 & 63 | 128),
            i.push(n >> 6 & 63 | 128),
            i.push(63 & n | 128)) : n >= 2048 && n <= 65535 ? (i.push(n >> 12 & 15 | 224),
            i.push(n >> 6 & 63 | 128),
            i.push(63 & n | 128)) : n >= 128 && n <= 2047 ? (i.push(n >> 6 & 31 | 192),
            i.push(63 & n | 128)) : i.push(255 & n);
    return i
}

function y(e, t) {
    return A(b(A(e.substr(0, 16)), A(t)).toUpperCase().substr(0, 16))
}

function b(t, n) {
    var i = 16 - parseInt(n.length % 16);
    n = n.concat(new Array(i).fill(i));
    var r = sm4.encrypt(n, t);
    return e_.from(r).toString("hex")
}

function f(e) {
    if (e >= a())
        throw new RangeError("Attempt to allocate Buffer larger than maximum size: 0x" + a().toString(16) + " bytes");
    return 0 | e
}


var l = {
    appCode: "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
    version: "1.0.0",
    appSecret: "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P",
    publicKey: "BEKaw3Qtc31LG/hTPHFPlriKuAn/nzTWl8LiRxLw4iQiSUIyuglptFxNkdCiNXcXvkqTH79Rh/A2sEFU6hjeK3k=",
    privateKey: "AJxKNdmspMaPGj+onJNoQ0cgWk2E3CYFWKBJhpcJrAtC",
    publicKeyType: "base64",
    privateKeyType: "base64"
}
var c = l.appCode
    , u = l.appSecret
    , h = l.publicKey
    , d = l.privateKey;

params = {
    "addr": "",
    "regnCode": "310000",
    "medinsName": "",
    "medinsLvCode": "",
    "medinsTypeCode": "",
    "outMedOpenFlag": "",
    "pageNum": 2,
    "pageSize": 10,
    "queryDataSource": "es"
}

function get_h() {
    var e, t, n, i = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", r = "0123456789";
    return e = o(6, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"),
        t = o(1, i),
        n = o(1, r),
    t + n + e;

    function o(e, t) {
        e = e || 32;
        for (var n = "", i = 0; i < e; i++)
            n += t.charAt(Math.ceil(1e3 * Math.random()) % t.length);
        return n
    }
}

let s = Math.ceil((new Date).getTime() / 1e3)

// console.log(get_h())
function get_signature() {
    let headers = {}
    let r = cryptoJS.SHA256
        , h = get_h()
        , f = s + h + s;
    headers["x-tif-signature"] = r(f).toString()
    headers["x-tif-timestamp"] = s
    headers["x-tif-nonce"] = h
    return headers
}

function get_signData(data) {
    //获取加密请求参数
    var t = {"data": data}
    t.data = {
        data: t.data || {}
    },
        t.data.appCode = l.appCode,
        t.data.version = l.version,
        t.data.encType = "SM4",
        t.data.signType = "SM2",
        t.data.timestamp = s,
        t.data.signData = function (t) {
            try {
                var n = m(t.data)
                    , i = p(n);
                i.data = p(i.data);
                var r = v(i)
                // , a = o.doSignature(r, d, {
                d = "009c4a35d9aca4c68f1a3fa89c93684347205a4d84dc260558a049869709ac0b42"
                    , a = sm2.doSignature(r, d, {
                    hash: !0
                });
                return e_.from(a, "hex").toString("base64")
            } catch (e) {
                console.log(e)
            }
        }(t)
    // t.data.data = {
    //     encData: function (e, t) {
    //         switch (e.toUpperCase()) {
    //             case "SM2":
    //                 return function (e) {
    //                     try {
    //                         var t = o.generateKeyPairHex()
    //                             , n = t.publicKey
    //                             , i = e;
    //                         o.doEncrypt(i, n, 1)
    //                     } catch (e) {
    //                         console.log(e)
    //                     }
    //                 }(t);
    //             case "SM3":
    //                 return function (e) {
    //                     try {
    //                         var t = a(e);
    //                         return t
    //                     } catch (e) {
    //                         console.log(e)
    //                     }
    //                 }(t);
    //             case "SM4":
    //                 return function (e) {
    //                     try {
    //                         var t = e.data.data && JSON.stringify(e.data.data)
    //                             , n = A(t);
    //                         e.data.appCode && e.data.appCode !== c && (c = e.data.appCode);
    //                         var i = b(c, u)
    //                             , r = y(i, n);
    //                         return r.toUpperCase()
    //                     } catch (e) {
    //                         console.log(e)
    //                     }
    //                 }(t)
    //         }
    //     }("SM4", t)
    // }
    return t.data
}

function g(t, n) {
    switch (t.toUpperCase()) {
        case "SM4":
            return function (t) {
                if (!t)
                    return null;
                var n = e.from(t.data.data.encData, "hex")
                    , i = function (t, n) {
                    var i = s.decrypt(n, t)
                        , r = i[i.length - 1];
                    return i = i.slice(0, i.length - r),
                        e_.from(i).toString("utf-8")
                }(y(u, c), n);
                return JSON.parse(i)
            }(n);
        case "SM2":
            return function (e) {
                try {
                    var t = o.generateKeyPairHex()
                        , n = t.privateKey;
                    o.doDecrypt(encryptData, n, 1)
                } catch (e) {
                }
            }()
    }
}

function get_data(p) {
    let headers = get_signature(), sign = get_signData(p)
    return JSON.stringify({
        'x-tif-signature': headers['x-tif-signature'],
        'x-tif-timestamp': headers['x-tif-timestamp'],
        'x-tif-nonce': headers['x-tif-nonce'],
        'signData': sign['signData']
    })
}

console.log(get_data(params))
// console.log(get_signature())
// console.log(get_signData(params).signData)