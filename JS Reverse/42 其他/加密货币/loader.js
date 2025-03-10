!function() {
    "use strict";
    var e, t, c, n, r, a, f, s, u, i, o, d, b = {}, l = {};
    function h(e) {
        var t = l[e];
        if (void 0 !== t)
            return t.exports;
        var c = l[e] = {
            id: e,
            loaded: !1,
            exports: {}
        }
          , n = !0;
        try {
            console.log('e:::',e)
            b[e].call(c.exports, c, c.exports, h),
            n = !1
        } finally {
            n && delete l[e]
        }
        return c.loaded = !0,
        c.exports
    }
    window.loader = h
    h.m = b,
    e = [],
    h.O = function(t, c, n, r) {
        if (c) {
            r = r || 0;
            for (var a = e.length; a > 0 && e[a - 1][2] > r; a--)
                e[a] = e[a - 1];
            e[a] = [c, n, r];
            return
        }
        for (var f = 1 / 0, a = 0; a < e.length; a++) {
            for (var c = e[a][0], n = e[a][1], r = e[a][2], s = !0, u = 0; u < c.length; u++)
                f >= r && Object.keys(h.O).every(function(e) {
                    return h.O[e](c[u])
                }) ? c.splice(u--, 1) : (s = !1,
                r < f && (f = r));
            if (s) {
                e.splice(a--, 1);
                var i = n();
                void 0 !== i && (t = i)
            }
        }
        return t
    }
    ,
    h.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return h.d(t, {
            a: t
        }),
        t
    }
    ,
    c = Object.getPrototypeOf ? function(e) {
        return Object.getPrototypeOf(e)
    }
    : function(e) {
        return e.__proto__
    }
    ,
    h.t = function(e, n) {
        if (1 & n && (e = this(e)),
        8 & n || "object" == typeof e && e && (4 & n && e.__esModule || 16 & n && "function" == typeof e.then))
            return e;
        var r = Object.create(null);
        h.r(r);
        var a = {};
        t = t || [null, c({}), c([]), c(c)];
        for (var f = 2 & n && e; "object" == typeof f && !~t.indexOf(f); f = c(f))
            Object.getOwnPropertyNames(f).forEach(function(t) {
                a[t] = function() {
                    return e[t]
                }
            });
        return a.default = function() {
            return e
        }
        ,
        h.d(r, a),
        r
    }
    ,
    h.d = function(e, t) {
        for (var c in t)
            h.o(t, c) && !h.o(e, c) && Object.defineProperty(e, c, {
                enumerable: !0,
                get: t[c]
            })
    }
    ,
    h.f = {},
    h.e = function(e) {
        return Promise.all(Object.keys(h.f).reduce(function(t, c) {
            return h.f[c](e, t),
            t
        }, []))
    }
    ,
    h.u = function(e) {
        return 5437 === e ? "static/chunks/5437-55e57eaf00a7e95f.js" : 5772 === e ? "static/chunks/5772-ed454b7693a6ae61.js" : 5551 === e ? "static/chunks/5551-910cb6204fbd54e4.js" : 568 === e ? "static/chunks/568-a0e2750f38c596a2.js" : 1864 === e ? "static/chunks/1864-9a19e143d3205769.js" : 3638 === e ? "static/chunks/3638-d92558b4c3f4b4b1.js" : 4267 === e ? "static/chunks/4267-e9d8c92221e45b32.js" : 4749 === e ? "static/chunks/4749-8d38b1b8572ce1df.js" : 2068 === e ? "static/chunks/2068-08611942b5ad5ef9.js" : 1116 === e ? "static/chunks/1116-0e9b687aecb88e8f.js" : 2307 === e ? "static/chunks/2307-d3fc4170a2ef5f7f.js" : 1216 === e ? "static/chunks/1216-8c32767922748cac.js" : 9714 === e ? "static/chunks/9714-7c5b510fe455d317.js" : 6268 === e ? "static/chunks/6268-194215404b228dd8.js" : 5633 === e ? "static/chunks/5633-64c3fc748825d8ca.js" : 7204 === e ? "static/chunks/7204-68e6f9b497d18679.js" : 2062 === e ? "static/chunks/2062-728cef005675f516.js" : 5798 === e ? "static/chunks/5798-8b19f13e482b20a8.js" : 5584 === e ? "static/chunks/5584-9c8768e686b26d6e.js" : 1314 === e ? "static/chunks/1314-9148f32034131b1a.js" : 5607 === e ? "static/chunks/5607-b2420250688b9147.js" : 6337 === e ? "static/chunks/6337-64e1963f66f54e9f.js" : 758 === e ? "static/chunks/758-68e45fd3a63b16da.js" : 3219 === e ? "static/chunks/3219-0b6f75bdcd7d9d15.js" : 5867 === e ? "static/chunks/5867-6d83c063c81c4e7a.js" : 793 === e ? "static/chunks/793-dacd22814c3dbd51.js" : 7284 === e ? "static/chunks/7284-dbb2f72e348fff94.js" : 6782 === e ? "static/chunks/6782-09b197bc42c0b3e4.js" : 5455 === e ? "static/chunks/5455-ff854fad4d8cda9d.js" : 8213 === e ? "static/chunks/8213-a7821451840fc0b0.js" : 3662 === e ? "static/chunks/29107295-1453a3860b50f70e.js" : "static/chunks/" + (({
            5520: "260fb190",
            6898: "4b358913"
        })[e] || e) + "." + ({
            1: "a8afebe73658108f",
            1517: "a6a7ba18013de15f",
            1538: "2727a45a0d17f5ba",
            1758: "e2b716cd297f9b15",
            1765: "3847c4a632aab975",
            1819: "e4eaa38346df2238",
            2513: "e0e5994923eb027c",
            3052: "e1504a690f8abcf3",
            3092: "4c1d67ba993cf8c3",
            3644: "4d98812d641b542e",
            3678: "8875cc991275133e",
            4093: "969e3f6516e9e7e9",
            4118: "116ce273d782b990",
            4140: "85dda52e54e24b38",
            4857: "7000d395ebdeda27",
            5520: "2945413288ddb018",
            5545: "dad2d0a78fe1cf44",
            5662: "e611a2aa27fa80f8",
            5708: "bf87e5e9b42daa7c",
            5725: "4652820fb730da29",
            5734: "90009a88386700c3",
            5813: "aa6b35754cae9533",
            6394: "e885c309d00562e7",
            6898: "dd13094e24aa9896",
            7190: "d1a658c02ac68d43",
            7269: "8717500b80b1a0c9",
            7287: "fc0055284b6966fa",
            7427: "49c16f42f01fadf9",
            7493: "632525754483f5f1",
            8292: "a4eb1f2a5dd2e621",
            8468: "dbc07f1b01c60661",
            8625: "3801b87f42462d4a",
            8670: "9e66ec43d1684412",
            8805: "c36866ce2d1777a5",
            8970: "79b9cdb0b0ec72f4",
            8977: "0e4bd1a7f2d51016",
            9162: "6a5604404f1e5c1e",
            9398: "5a8b175ec0968863",
            9420: "8f045b9775417bce"
        })[e] + ".js"
    }
    ,
    h.miniCssF = function(e) {
        return "static/css/" + ({
            1: "32861b2ca577bab6",
            237: "32861b2ca577bab6",
            1754: "32861b2ca577bab6",
            2690: "32861b2ca577bab6",
            2699: "32861b2ca577bab6",
            2888: "ef394eecd5b53e26",
            3497: "32861b2ca577bab6",
            3937: "32861b2ca577bab6",
            4393: "32861b2ca577bab6",
            4814: "32861b2ca577bab6",
            5215: "32861b2ca577bab6",
            5405: "32861b2ca577bab6",
            5844: "8af6571b0a68de1a",
            6368: "dd18791d836e2bc9",
            7113: "32861b2ca577bab6",
            7226: "32861b2ca577bab6",
            7386: "32861b2ca577bab6",
            8585: "cc8d90aa8c156e0f",
            8957: "cc8d90aa8c156e0f"
        })[e] + ".css"
    }
    ,
    h.g = function() {
        if ("object" == typeof globalThis)
            return globalThis;
        try {
            return this || Function("return this")()
        } catch (e) {
            if ("object" == typeof window)
                return window
        }
    }(),
    h.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    n = {},
    r = "_N_E:",
    h.l = function(e, t, c, a) {
        if (n[e]) {
            n[e].push(t);
            return
        }
        if (void 0 !== c)
            for (var f, s, u = document.getElementsByTagName("script"), i = 0; i < u.length; i++) {
                var o = u[i];
                if (o.getAttribute("src") == e || o.getAttribute("data-webpack") == r + c) {
                    f = o;
                    break
                }
            }
        f || (s = !0,
        (f = document.createElement("script")).charset = "utf-8",
        f.timeout = 120,
        h.nc && f.setAttribute("nonce", h.nc),
        f.setAttribute("data-webpack", r + c),
        f.src = h.tu(e)),
        n[e] = [t];
        var d = function(t, c) {
            f.onerror = f.onload = null,
            clearTimeout(b);
            var r = n[e];
            if (delete n[e],
            f.parentNode && f.parentNode.removeChild(f),
            r && r.forEach(function(e) {
                return e(c)
            }),
            t)
                return t(c)
        }
          , b = setTimeout(d.bind(null, void 0, {
            type: "timeout",
            target: f
        }), 12e4);
        f.onerror = d.bind(null, f.onerror),
        f.onload = d.bind(null, f.onload),
        s && document.head.appendChild(f)
    }
    ,
    h.r = function(e) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    h.nmd = function(e) {
        return e.paths = [],
        e.children || (e.children = []),
        e
    }
    ,
    h.tt = function() {
        return void 0 === a && (a = {
            createScriptURL: function(e) {
                return e
            }
        },
        "undefined" != typeof trustedTypes && trustedTypes.createPolicy && (a = trustedTypes.createPolicy("nextjs#bundler", a))),
        a
    }
    ,
    h.tu = function(e) {
        return h.tt().createScriptURL(e)
    }
    ,
    h.p = "https://aws-s3.coinglasscdn.com/cg_v3/_next/",
    f = function(e, t, c, n) {
        var r = document.createElement("link");
        r.rel = "stylesheet",
        r.type = "text/css";
        var a = function(a) {
            if (r.onerror = r.onload = null,
            "load" === a.type)
                c();
            else {
                var f = a && ("load" === a.type ? "missing" : a.type)
                  , s = a && a.target && a.target.href || t
                  , u = Error("Loading CSS chunk " + e + " failed.\n(" + s + ")");
                u.code = "CSS_CHUNK_LOAD_FAILED",
                u.type = f,
                u.request = s,
                r.parentNode.removeChild(r),
                n(u)
            }
        };
        return r.onerror = r.onload = a,
        r.href = t,
        document.head.appendChild(r),
        r
    }
    ,
    s = function(e, t) {
        for (var c = document.getElementsByTagName("link"), n = 0; n < c.length; n++) {
            var r = c[n]
              , a = r.getAttribute("data-href") || r.getAttribute("href");
            if ("stylesheet" === r.rel && (a === e || a === t))
                return r
        }
        for (var f = document.getElementsByTagName("style"), n = 0; n < f.length; n++) {
            var r = f[n]
              , a = r.getAttribute("data-href");
            if (a === e || a === t)
                return r
        }
    }
    ,
    u = {
        2272: 0
    },
    h.f.miniCss = function(e, t) {
        u[e] ? t.push(u[e]) : 0 !== u[e] && ({
            1: 1
        })[e] && t.push(u[e] = new Promise(function(t, c) {
            var n = h.miniCssF(e)
              , r = h.p + n;
            if (s(n, r))
                return t();
            f(e, r, t, c)
        }
        ).then(function() {
            u[e] = 0
        }, function(t) {
            throw delete u[e],
            t
        }))
    }
    ,
    i = {
        2272: 0,
        5844: 0
    },
    h.f.j = function(e, t) {
        var c = h.o(i, e) ? i[e] : void 0;
        if (0 !== c) {
            if (c)
                t.push(c[2]);
            else if (/^(2272|5844)$/.test(e))
                i[e] = 0;
            else {
                var n = new Promise(function(t, n) {
                    c = i[e] = [t, n]
                }
                );
                t.push(c[2] = n);
                var r = h.p + h.u(e)
                  , a = Error()
                  , f = function(t) {
                    if (h.o(i, e) && (0 !== (c = i[e]) && (i[e] = void 0),
                    c)) {
                        var n = t && ("load" === t.type ? "missing" : t.type)
                          , r = t && t.target && t.target.src;
                        a.message = "Loading chunk " + e + " failed.\n(" + n + ": " + r + ")",
                        a.name = "ChunkLoadError",
                        a.type = n,
                        a.request = r,
                        c[1](a)
                    }
                };
                h.l(r, f, "chunk-" + e, e)
            }
        }
    }
    ,
    h.O.j = function(e) {
        return 0 === i[e]
    }
    ,
    o = function(e, t) {
        var c, n, r = t[0], a = t[1], f = t[2], s = 0;
        if (r.some(function(e) {
            return 0 !== i[e]
        })) {
            for (c in a)
                h.o(a, c) && (h.m[c] = a[c]);
            if (f)
                var u = f(h)
        }
        for (e && e(t); s < r.length; s++)
            n = r[s],
            h.o(i, n) && i[n] && i[n][0](),
            i[n] = 0;
        return h.O(u)
    }
    ,
    (d = self.webpackChunk_N_E = self.webpackChunk_N_E || []).forEach(o.bind(null, 0)),
    d.push = o.bind(null, d.push.bind(d)),
    h.nc = void 0
}();
