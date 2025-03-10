CryptoJS = require('crypto-js');

let b = {
    c: function (e) {
        let p = {
            a: CryptoJS
        };
        let n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : ""
            , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {}
            , r = t.enc
            , a = void 0 === r ? "Utf8" : r
            , o = t.mode
            , i = void 0 === o ? "ECB" : o
            , c = t.padding
            , u = void 0 === c ? "Pkcs7" : c
            , d = p.a.enc[a].parse(n)
            , s = {
            mode: p.a.mode[i],
            padding: p.a.pad[u]
        }
            , l = p.a.TripleDES.encrypt(e, d, s);
        return l.toString()
    },
    f: function (e) {
        let n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {};
        if (e && "string" === typeof e) {
            let t = n.text || "0"
                , r = n.length || 24;
            if (e.length < r)
                for (let a = e.length; a < r; a++)
                    e += t;
            else
                e = e.substring(0, r);
            return e
        }
    },
    g: function () {
        let e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "";
        return e.replace(/\s+/g, "")
    }
}


function get_password(userName, password) {
    return encodeURI(Object(b["c"])(password, Object(b["f"])(Object(b["g"])(userName))))

}

// 测试代码

let userName = "admin@163.com";
let password = "123456";

// console.log(get_password(userName, password))

let u = {
    k: function () {
        var e, n, t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 32,
            r = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 16,
            a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split(""), o = [];
        if (r = r || a.length,
            t)
            for (e = 0; e < t; e++)
                o[e] = a[0 | Math.random() * r];
        else
            for (o[8] = o[13] = o[18] = o[23] = "-",
                     o[14] = "4",
                     e = 0; e < 36; e++)
                o[e] || (n = 0 | 16 * Math.random(),
                    o[e] = a[19 === e ? 3 & n | 8 : n]);
        return o.join("")
    }
}

function get_params() {
    function c(){
        return CryptoJS.MD5
    }
    let n = (new Date).getTime() - "116"
        , t = "s54zv9bm1vd5czfujy6nnuxj1l4g2ny6"
        , r = Object(u["k"])()
        , a = c()(n + r + c()(r + t + n).toString()).toString();
    return {
        "referrer": "wap",
        mainVersion: "300031500",
        comParam_curTime: n,
        comParam_seqCode: r,
        comParam_signature: a,
        isCheck: !0,
        locale: "zh-cn"
    }
}

// console.log(get_params())