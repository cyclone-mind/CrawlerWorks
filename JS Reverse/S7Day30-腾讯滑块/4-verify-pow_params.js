



function n(t, e) {
    var r = (65535 & t) + (65535 & e);
    return (t >> 16) + (e >> 16) + (r >> 16) << 16 | 65535 & r
}
function i(t, e, r, i, o, a) {
    return n(function (t, e) {
        return t << e | t >>> 32 - e
    }(n(n(e, t), n(i, a)), o), r)
}
function o(t, e, r, n, o, a, s) {
    return i(e & r | ~e & n, t, e, o, a, s)
}
function a(t, e, r, n, o, a, s) {
    return i(e & n | r & ~n, t, e, o, a, s)
}
function s(t, e, r, n, o, a, s) {
    return i(e ^ r ^ n, t, e, o, a, s)
}
function c(t, e, r, n, o, a, s) {
    return i(r ^ (e | ~n), t, e, o, a, s)
}
function u(t, e) {
    var r, i, u, d, l;
    t[e >> 5] |= 128 << e % 32,
        t[14 + (e + 64 >>> 9 << 4)] = e;
    var p = 1732584193
        , f = -271733879
        , h = -1732584194
        , m = 271733878;
    for (r = 0; r < t.length; r += 16)
        i = p,
            u = f,
            d = h,
            l = m,
            f = c(f = c(f = c(f = c(f = s(f = s(f = s(f = s(f = a(f = a(f = a(f = a(f = o(f = o(f = o(f = o(f, h = o(h, m = o(m, p = o(p, f, h, m, t[r], 7, -680876936), f, h, t[r + 1], 12, -389564586), p, f, t[r + 2], 17, 606105819), m, p, t[r + 3], 22, -1044525330), h = o(h, m = o(m, p = o(p, f, h, m, t[r + 4], 7, -176418897), f, h, t[r + 5], 12, 1200080426), p, f, t[r + 6], 17, -1473231341), m, p, t[r + 7], 22, -45705983), h = o(h, m = o(m, p = o(p, f, h, m, t[r + 8], 7, 1770035416), f, h, t[r + 9], 12, -1958414417), p, f, t[r + 10], 17, -42063), m, p, t[r + 11], 22, -1990404162), h = o(h, m = o(m, p = o(p, f, h, m, t[r + 12], 7, 1804603682), f, h, t[r + 13], 12, -40341101), p, f, t[r + 14], 17, -1502002290), m, p, t[r + 15], 22, 1236535329), h = a(h, m = a(m, p = a(p, f, h, m, t[r + 1], 5, -165796510), f, h, t[r + 6], 9, -1069501632), p, f, t[r + 11], 14, 643717713), m, p, t[r], 20, -373897302), h = a(h, m = a(m, p = a(p, f, h, m, t[r + 5], 5, -701558691), f, h, t[r + 10], 9, 38016083), p, f, t[r + 15], 14, -660478335), m, p, t[r + 4], 20, -405537848), h = a(h, m = a(m, p = a(p, f, h, m, t[r + 9], 5, 568446438), f, h, t[r + 14], 9, -1019803690), p, f, t[r + 3], 14, -187363961), m, p, t[r + 8], 20, 1163531501), h = a(h, m = a(m, p = a(p, f, h, m, t[r + 13], 5, -1444681467), f, h, t[r + 2], 9, -51403784), p, f, t[r + 7], 14, 1735328473), m, p, t[r + 12], 20, -1926607734), h = s(h, m = s(m, p = s(p, f, h, m, t[r + 5], 4, -378558), f, h, t[r + 8], 11, -2022574463), p, f, t[r + 11], 16, 1839030562), m, p, t[r + 14], 23, -35309556), h = s(h, m = s(m, p = s(p, f, h, m, t[r + 1], 4, -1530992060), f, h, t[r + 4], 11, 1272893353), p, f, t[r + 7], 16, -155497632), m, p, t[r + 10], 23, -1094730640), h = s(h, m = s(m, p = s(p, f, h, m, t[r + 13], 4, 681279174), f, h, t[r], 11, -358537222), p, f, t[r + 3], 16, -722521979), m, p, t[r + 6], 23, 76029189), h = s(h, m = s(m, p = s(p, f, h, m, t[r + 9], 4, -640364487), f, h, t[r + 12], 11, -421815835), p, f, t[r + 15], 16, 530742520), m, p, t[r + 2], 23, -995338651), h = c(h, m = c(m, p = c(p, f, h, m, t[r], 6, -198630844), f, h, t[r + 7], 10, 1126891415), p, f, t[r + 14], 15, -1416354905), m, p, t[r + 5], 21, -57434055), h = c(h, m = c(m, p = c(p, f, h, m, t[r + 12], 6, 1700485571), f, h, t[r + 3], 10, -1894986606), p, f, t[r + 10], 15, -1051523), m, p, t[r + 1], 21, -2054922799), h = c(h, m = c(m, p = c(p, f, h, m, t[r + 8], 6, 1873313359), f, h, t[r + 15], 10, -30611744), p, f, t[r + 6], 15, -1560198380), m, p, t[r + 13], 21, 1309151649), h = c(h, m = c(m, p = c(p, f, h, m, t[r + 4], 6, -145523070), f, h, t[r + 11], 10, -1120210379), p, f, t[r + 2], 15, 718787259), m, p, t[r + 9], 21, -343485551),
            p = n(p, i),
            f = n(f, u),
            h = n(h, d),
            m = n(m, l);
    return [p, f, h, m]
}
function d(t) {
    var e, r = "";
    for (e = 0; e < 32 * t.length; e += 8)
        r += String.fromCharCode(t[e >> 5] >>> e % 32 & 255);
    return r
}
function l(t) {
    var e, r = [];
    for (r[(t.length >> 2) - 1] = void 0,
        e = 0; e < r.length; e += 1)
        r[e] = 0;
    for (e = 0; e < 8 * t.length; e += 8)
        r[e >> 5] |= (255 & t.charCodeAt(e / 8)) << e % 32;
    return r
}
function p(t) {
    var e, r, n = "0123456789abcdef", i = "";
    for (r = 0; r < t.length; r += 1)
        e = t.charCodeAt(r),
            i += n.charAt(e >>> 4 & 15) + n.charAt(15 & e);
    return i
}
function f(t) {
    return unescape(encodeURIComponent(t))
}
function h(t) {
    return function (t) {
        return d(u(l(t), 8 * t.length))
    }(f(t))
}
function m(t, e) {
    return function (t, e) {
        var r, n, i = l(t), o = [], a = [];
        for (o[15] = a[15] = void 0,
            i.length > 16 && (i = u(i, 8 * t.length)),
            r = 0; r < 16; r += 1)
            o[r] = 909522486 ^ i[r],
                a[r] = 1549556828 ^ i[r];
        return n = u(o.concat(l(e)), 512 + 8 * e.length),
            d(u(a.concat(n), 640))
    }(f(t), f(e))
}
function g(t, e, r) {
    return e ? r ? m(e, t) : function (t, e) {
        return p(m(t, e))
    }(e, t) : r ? h(t) : function (t) {
        return p(h(t))
    }(t)
}


function get_pow_params(prefix, md5) {
    for (var r = prefix, n = md5, i = +new Date, o = 0, a = "number" == typeof e ? e : 3e4; g("".concat(r).concat(o)) !== n && (o += 1,
        !(+new Date - i > a));)
        ;
    return {
        ans: o,
        duration: +new Date - i
    }
}

console.log(get_pow_params("394a5c5f1cc4502b#", "4ea72a53eb719d9746a697870d14fa8a"));
