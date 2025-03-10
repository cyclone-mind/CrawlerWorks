function e(e, t, n) {
    return t in e ? Object.defineProperty(e, t, {
        value: n,
        enumerable: !0,
        configurable: !0,
        writable: !0
    }) : e[t] = n,
        e
}

function n(e, t) {
    return t = {
        exports: {}
    },
        e(t, t.exports),
        t.exports
}

var o = n((function (e) {
        (function () {
                var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
                    , n = {
                    rotl: function (e, t) {
                        return e << t | e >>> 32 - t
                    },
                    rotr: function (e, t) {
                        return e << 32 - t | e >>> t
                    },
                    endian: function (e) {
                        if (e.constructor == Number)
                            return 16711935 & n.rotl(e, 8) | 4278255360 & n.rotl(e, 24);
                        for (var t = 0; t < e.length; t++)
                            e[t] = n.endian(e[t]);
                        return e
                    },
                    randomBytes: function (e) {
                        for (var t = []; e > 0; e--)
                            t.push(Math.floor(256 * Math.random()));
                        return t
                    },
                    bytesToWords: function (e) {
                        for (var t = [], n = 0, r = 0; n < e.length; n++,
                            r += 8)
                            t[r >>> 5] |= e[n] << 24 - r % 32;
                        return t
                    },
                    wordsToBytes: function (e) {
                        for (var t = [], n = 0; n < 32 * e.length; n += 8)
                            t.push(e[n >>> 5] >>> 24 - n % 32 & 255);
                        return t
                    },
                    bytesToHex: function (e) {
                        for (var t = [], n = 0; n < e.length; n++)
                            t.push((e[n] >>> 4).toString(16)),
                                t.push((15 & e[n]).toString(16));
                        return t.join("")
                    },
                    hexToBytes: function (e) {
                        for (var t = [], n = 0; n < e.length; n += 2)
                            t.push(parseInt(e.substr(n, 2), 16));
                        return t
                    },
                    bytesToBase64: function (e) {
                        for (var n = [], r = 0; r < e.length; r += 3)
                            for (var o = e[r] << 16 | e[r + 1] << 8 | e[r + 2], i = 0; i < 4; i++)
                                8 * r + 6 * i <= 8 * e.length ? n.push(t.charAt(o >>> 6 * (3 - i) & 63)) : n.push("=");
                        return n.join("")
                    },
                    base64ToBytes: function (e) {
                        e = e.replace(/[^A-Z0-9+\/]/gi, "");
                        for (var n = [], r = 0, o = 0; r < e.length; o = ++r % 4)
                            0 != o && n.push((t.indexOf(e.charAt(r - 1)) & Math.pow(2, -2 * o + 8) - 1) << 2 * o | t.indexOf(e.charAt(r)) >>> 6 - 2 * o);
                        return n
                    }
                };
                e.exports = n
            }
        )()
    }
))
    , i = {
    utf8: {
        stringToBytes: function (e) {
            return i.bin.stringToBytes(unescape(encodeURIComponent(e)))
        },
        bytesToString: function (e) {
            return decodeURIComponent(escape(i.bin.bytesToString(e)))
        }
    },
    bin: {
        stringToBytes: function (e) {
            for (var t = [], n = 0; n < e.length; n++)
                t.push(255 & e.charCodeAt(n));
            return t
        },
        bytesToString: function (e) {
            for (var t = [], n = 0; n < e.length; n++)
                t.push(String.fromCharCode(e[n]));
            return t.join("")
        }
    }
}
    , a = i
    , s = n((function (e) {
        (function () {
                var t = o
                    , n = a.utf8
                    , i = a.bin
                    , s = function (e) {
                    e.constructor == String ? e = n.stringToBytes(e) : "undefined" !== typeof r && "function" == typeof r.isBuffer && r.isBuffer(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || (e = e.toString());
                    var o = t.bytesToWords(e)
                        , i = 8 * e.length
                        , a = []
                        , s = 1732584193
                        , u = -271733879
                        , c = -1732584194
                        , l = 271733878
                        , f = -1009589776;
                    o[i >> 5] |= 128 << 24 - i % 32,
                        o[15 + (i + 64 >>> 9 << 4)] = i;
                    for (var d = 0; d < o.length; d += 16) {
                        for (var p = s, h = u, v = c, y = l, g = f, m = 0; m < 80; m++) {
                            if (m < 16)
                                a[m] = o[d + m];
                            else {
                                var b = a[m - 3] ^ a[m - 8] ^ a[m - 14] ^ a[m - 16];
                                a[m] = b << 1 | b >>> 31
                            }
                            var _ = (s << 5 | s >>> 27) + f + (a[m] >>> 0) + (m < 20 ? 1518500249 + (u & c | ~u & l) : m < 40 ? 1859775393 + (u ^ c ^ l) : m < 60 ? (u & c | u & l | c & l) - 1894007588 : (u ^ c ^ l) - 899497514);
                            f = l,
                                l = c,
                                c = u << 30 | u >>> 2,
                                u = s,
                                s = _
                        }
                        s += p,
                            u += h,
                            c += v,
                            l += y,
                            f += g
                    }
                    return [s, u, c, l, f]
                }
                    , u = function (e, n) {
                    var r = t.wordsToBytes(s(e));
                    return n && n.asBytes ? r : n && n.asString ? i.bytesToString(r) : t.bytesToHex(r)
                };
                u._blocksize = 16,
                    u._digestsize = 20,
                    e.exports = u
            }
        )()
    }
))

// 接口测试
// let data = 'appSignKey=4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&keyword=新冠&noncestr=74243375&pageNum=2&pageSize=20&sectionCode=0&serverTimestamp=1732343691463&timestamp=1732346804811'
// console.log(s(data))