cryptoJs = require("../crypto-js")

// console.log(cryptoJs.MD5("123456").toString())


function l(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}

function u(t) {
    for (var e = Object.keys(t).sort(l), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]] instanceof Object || t[e[a]] instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}

function d(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = "B3978D054A72A7002063637CCDF6B2E5" + u(t);
    return cryptoJs.MD5(n).toString().toLocaleLowerCase()
}

// 测试

/*t = {
    "ts": 1722759738105,
    "type": "12",
    "IS_IMPORT": 1,
    "pageSize": 3
}

console.log(d(t))*/


function b(t) {
    var e = cryptoJs.enc.Utf8.parse("EB444973714E4A40876CE66BE45D5930")
        , n = cryptoJs.enc.Utf8.parse("B5A8904209931867")
        , a = cryptoJs.AES.decrypt(t, e, {
        iv: n,
        mode: cryptoJs.mode.CBC,
        padding: cryptoJs.pad.Pkcs7
    });
    return a.toString(cryptoJs.enc.Utf8)
}


//接口测试
t = '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'

console.log(b(t))
