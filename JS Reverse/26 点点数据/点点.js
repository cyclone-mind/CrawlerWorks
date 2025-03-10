const Crypto = require('crypto')
function isObject(value) {
    return value !== null && typeof value === 'object' && !Array.isArray(value);
}
const t = Buffer;

function aes_encrypt(e, n, o) {
    var d = "";
    n = t.from(n, "utf8"),
        o = t.from(o, "utf8");
    var c = Object(Crypto.createDecipheriv)("aes-128-cbc", n, o);
    return d += c.update(e, "hex", "utf8"),
        d += c.final("utf8")
}

function h(e, path, n, r) {
    var s = n.s
        , d = n.k
        , f = n.l
        , v = n.d
        , h = n.sort
        , k = n.num
        , y = function (content, t, e) {
        for (var a = Array.from(content), n = Array.from(t), r = a.length, o = n.length, d = String.fromCodePoint, i = 0; i < r; i++)
            a[i] = d(a[i].codePointAt(0) ^ n[(i + e) % o].codePointAt(0));
        return a.join("")
    }(function (s, t, path, e) {
        return [s, t, e, path].join("(&&)")
    }(function (t, e) {
        // var n = c()(t);
        var n = t;
        if (true) {
            var r = [];
            for (var d in n)
                Array.isArray(n[d]) && "get" === e && (n[d] = n[d].join("")),
                "post" === e && (Array.isArray(n[d]) || isObject(n[d])) && (n[d] = JSON.stringify(n[d])),
                    r.push(n[d]);
            return r.sort(),
                r.join("")
        }
    }(e, r), parseInt((new Date).getTime() / 1e3) - 655876800 - v, path, h), aes_encrypt(s, d, f), k);
    return btoa(y)
}

// 接口测试
function test(e,d) {

    let path = "/v1/user/favorite/app"
    let n = {
        "s": d.s,
        "k": d.k,
        "l": d.l,
        "d": -1,
        "sort": "dd",
        "num": 10
    }
    let r = 'get'
    return h(e, path, n, r)
}
// let e = {
//         "app_id": "y21ulux1r7mwra1",
//         "country_id": 75,
//         "market_id": 1,
//         "device_id": 1,
//         "start_time": 1731945600,
//         "end_time": 1732032000
//     }
// test()

