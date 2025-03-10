const crypto = require("crypto")
// let url = "/api/explorer/v1/btc/transactionsNoRestrict?offset=40&limit=20&t=1732173775260"
let fetchConfig = 'get'

url = process.argv[2]


function M(e, t) {
    (null == t || t > e.length) && (t = e.length);
    for (var r = 0, n = new Array(t); r < t; r++)
        n[r] = e[r];
    return n
}

function $(e, t) {
    if (e) {
        if ("string" === typeof e)
            return M(e, t);
        var r = Object.prototype.toString.call(e).slice(8, -1);
        return "Object" === r && e.constructor && (r = e.constructor.name),
            "Map" === r || "Set" === r ? Array.from(e) : "Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r) ? M(e, t) : void 0
    }
}

function G(e) {
    return function (e) {
        if (Array.isArray(e))
            return M(e)
    }(e) || function (e) {
        if ("undefined" !== typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"])
            return Array.from(e)
    }(e) || $(e) || function () {
        throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
    }()
}

function Ke() {
    Ke = function () {
        return r
    }
    ;
    var e, r = {}, n = Object.prototype, o = n.hasOwnProperty, i = Object.defineProperty || function (e, t, r) {
            e[t] = r.value
        }
        , a = "function" == typeof Symbol ? Symbol : {}, c = a.iterator || "@@iterator",
        u = a.asyncIterator || "@@asyncIterator", s = a.toStringTag || "@@toStringTag";

    function l(e, t, r) {
        return Object.defineProperty(e, t, {
            value: r,
            enumerable: !0,
            configurable: !0,
            writable: !0
        }),
            e[t]
    }

    try {
        l({}, "")
    } catch (e) {
        l = function (e, t, r) {
            return e[t] = r
        }
    }

    function f(e, t, r, n) {
        var o = t && t.prototype instanceof y ? t : y
            , a = Object.create(o.prototype)
            , c = new P(n || []);
        return i(a, "_invoke", {
            value: A(e, r, c)
        }),
            a
    }

    function p(e, t, r) {
        try {
            return {
                type: "normal",
                arg: e.call(t, r)
            }
        } catch (e) {
            return {
                type: "throw",
                arg: e
            }
        }
    }

    r.wrap = f;
    var d = "suspendedStart"
        , v = "suspendedYield"
        , g = "executing"
        , h = "completed"
        , b = {};

    function y() {
    }

    function m() {
    }

    function w() {
    }

    var x = {};
    l(x, c, (function () {
            return this
        }
    ));
    var k = Object.getPrototypeOf
        , _ = k && k(k(T([])));
    _ && _ !== n && o.call(_, c) && (x = _);
    var S = w.prototype = y.prototype = Object.create(x);

    function j(e) {
        ["next", "throw", "return"].forEach((function (t) {
                l(e, t, (function (e) {
                        return this._invoke(t, e)
                    }
                ))
            }
        ))
    }

    function E(e, r) {
        function n(i, a, c, u) {
            var s = p(e[i], e, a);
            if ("throw" !== s.type) {
                var l = s.arg
                    , f = l.value;
                return f && "object" == t(f) && o.call(f, "__await") ? r.resolve(f.__await).then((function (e) {
                        n("next", e, c, u)
                    }
                ), (function (e) {
                        n("throw", e, c, u)
                    }
                )) : r.resolve(f).then((function (e) {
                        l.value = e,
                            c(l)
                    }
                ), (function (e) {
                        return n("throw", e, c, u)
                    }
                ))
            }
            u(s.arg)
        }

        var a;
        i(this, "_invoke", {
            value: function (e, t) {
                function o() {
                    return new r((function (r, o) {
                            n(e, t, r, o)
                        }
                    ))
                }

                return a = a ? a.then(o, o) : o()
            }
        })
    }

    function A(t, r, n) {
        var o = d;
        return function (i, a) {
            if (o === g)
                throw new Error("Generator is already running");
            if (o === h) {
                if ("throw" === i)
                    throw a;
                return {
                    value: e,
                    done: !0
                }
            }
            for (n.method = i,
                     n.arg = a; ;) {
                var c = n.delegate;
                if (c) {
                    var u = I(c, n);
                    if (u) {
                        if (u === b)
                            continue;
                        return u
                    }
                }
                if ("next" === n.method)
                    n.sent = n._sent = n.arg;
                else if ("throw" === n.method) {
                    if (o === d)
                        throw o = h,
                            n.arg;
                    n.dispatchException(n.arg)
                } else
                    "return" === n.method && n.abrupt("return", n.arg);
                o = g;
                var s = p(t, r, n);
                if ("normal" === s.type) {
                    if (o = n.done ? h : v,
                    s.arg === b)
                        continue;
                    return {
                        value: s.arg,
                        done: n.done
                    }
                }
                "throw" === s.type && (o = h,
                    n.method = "throw",
                    n.arg = s.arg)
            }
        }
    }

    function I(t, r) {
        var n = r.method
            , o = t.iterator[n];
        if (o === e)
            return r.delegate = null,
            "throw" === n && t.iterator.return && (r.method = "return",
                r.arg = e,
                I(t, r),
            "throw" === r.method) || "return" !== n && (r.method = "throw",
                r.arg = new TypeError("The iterator does not provide a '" + n + "' method")),
                b;
        var i = p(o, t.iterator, r.arg);
        if ("throw" === i.type)
            return r.method = "throw",
                r.arg = i.arg,
                r.delegate = null,
                b;
        var a = i.arg;
        return a ? a.done ? (r[t.resultName] = a.value,
            r.next = t.nextLoc,
        "return" !== r.method && (r.method = "next",
            r.arg = e),
            r.delegate = null,
            b) : a : (r.method = "throw",
            r.arg = new TypeError("iterator result is not an object"),
            r.delegate = null,
            b)
    }

    function O(e) {
        var t = {
            tryLoc: e[0]
        };
        1 in e && (t.catchLoc = e[1]),
        2 in e && (t.finallyLoc = e[2],
            t.afterLoc = e[3]),
            this.tryEntries.push(t)
    }

    function C(e) {
        var t = e.completion || {};
        t.type = "normal",
            delete t.arg,
            e.completion = t
    }

    function P(e) {
        this.tryEntries = [{
            tryLoc: "root"
        }],
            e.forEach(O, this),
            this.reset(!0)
    }

    function T(r) {
        if (r || "" === r) {
            var n = r[c];
            if (n)
                return n.call(r);
            if ("function" == typeof r.next)
                return r;
            if (!isNaN(r.length)) {
                var i = -1
                    , a = function t() {
                    for (; ++i < r.length;)
                        if (o.call(r, i))
                            return t.value = r[i],
                                t.done = !1,
                                t;
                    return t.value = e,
                        t.done = !0,
                        t
                };
                return a.next = a
            }
        }
        throw new TypeError(t(r) + " is not iterable")
    }

    return m.prototype = w,
        i(S, "constructor", {
            value: w,
            configurable: !0
        }),
        i(w, "constructor", {
            value: m,
            configurable: !0
        }),
        m.displayName = l(w, s, "GeneratorFunction"),
        r.isGeneratorFunction = function (e) {
            var t = "function" == typeof e && e.constructor;
            return !!t && (t === m || "GeneratorFunction" === (t.displayName || t.name))
        }
        ,
        r.mark = function (e) {
            return Object.setPrototypeOf ? Object.setPrototypeOf(e, w) : (e.__proto__ = w,
                l(e, s, "GeneratorFunction")),
                e.prototype = Object.create(S),
                e
        }
        ,
        r.awrap = function (e) {
            return {
                __await: e
            }
        }
        ,
        j(E.prototype),
        l(E.prototype, u, (function () {
                return this
            }
        )),
        r.AsyncIterator = E,
        r.async = function (e, t, n, o, i) {
            void 0 === i && (i = Promise);
            var a = new E(f(e, t, n, o), i);
            return r.isGeneratorFunction(t) ? a : a.next().then((function (e) {
                    return e.done ? e.value : a.next()
                }
            ))
        }
        ,
        j(S),
        l(S, s, "Generator"),
        l(S, c, (function () {
                return this
            }
        )),
        l(S, "toString", (function () {
                return "[object Generator]"
            }
        )),
        r.keys = function (e) {
            var t = Object(e)
                , r = [];
            for (var n in t)
                r.push(n);
            return r.reverse(),
                function e() {
                    for (; r.length;) {
                        var n = r.pop();
                        if (n in t)
                            return e.value = n,
                                e.done = !1,
                                e
                    }
                    return e.done = !0,
                        e
                }
        }
        ,
        r.values = T,
        P.prototype = {
            constructor: P,
            reset: function (t) {
                if (this.prev = 0,
                    this.next = 0,
                    this.sent = this._sent = e,
                    this.done = !1,
                    this.delegate = null,
                    this.method = "next",
                    this.arg = e,
                    this.tryEntries.forEach(C),
                    !t)
                    for (var r in this)
                        "t" === r.charAt(0) && o.call(this, r) && !isNaN(+r.slice(1)) && (this[r] = e)
            },
            stop: function () {
                this.done = !0;
                var e = this.tryEntries[0].completion;
                if ("throw" === e.type)
                    throw e.arg;
                return this.rval
            },
            dispatchException: function (t) {
                if (this.done)
                    throw t;
                var r = this;

                function n(n, o) {
                    return c.type = "throw",
                        c.arg = t,
                        r.next = n,
                    o && (r.method = "next",
                        r.arg = e),
                        !!o
                }

                for (var i = this.tryEntries.length - 1; i >= 0; --i) {
                    var a = this.tryEntries[i]
                        , c = a.completion;
                    if ("root" === a.tryLoc)
                        return n("end");
                    if (a.tryLoc <= this.prev) {
                        var u = o.call(a, "catchLoc")
                            , s = o.call(a, "finallyLoc");
                        if (u && s) {
                            if (this.prev < a.catchLoc)
                                return n(a.catchLoc, !0);
                            if (this.prev < a.finallyLoc)
                                return n(a.finallyLoc)
                        } else if (u) {
                            if (this.prev < a.catchLoc)
                                return n(a.catchLoc, !0)
                        } else {
                            if (!s)
                                throw new Error("try statement without catch or finally");
                            if (this.prev < a.finallyLoc)
                                return n(a.finallyLoc)
                        }
                    }
                }
            },
            abrupt: function (e, t) {
                for (var r = this.tryEntries.length - 1; r >= 0; --r) {
                    var n = this.tryEntries[r];
                    if (n.tryLoc <= this.prev && o.call(n, "finallyLoc") && this.prev < n.finallyLoc) {
                        var i = n;
                        break
                    }
                }
                i && ("break" === e || "continue" === e) && i.tryLoc <= t && t <= i.finallyLoc && (i = null);
                var a = i ? i.completion : {};
                return a.type = e,
                    a.arg = t,
                    i ? (this.method = "next",
                        this.next = i.finallyLoc,
                        b) : this.complete(a)
            },
            complete: function (e, t) {
                if ("throw" === e.type)
                    throw e.arg;
                return "break" === e.type || "continue" === e.type ? this.next = e.arg : "return" === e.type ? (this.rval = this.arg = e.arg,
                    this.method = "return",
                    this.next = "end") : "normal" === e.type && t && (this.next = t),
                    b
            },
            finish: function (e) {
                for (var t = this.tryEntries.length - 1; t >= 0; --t) {
                    var r = this.tryEntries[t];
                    if (r.finallyLoc === e)
                        return this.complete(r.completion, r.afterLoc),
                            C(r),
                            b
                }
            },
            catch: function (e) {
                for (var t = this.tryEntries.length - 1; t >= 0; --t) {
                    var r = this.tryEntries[t];
                    if (r.tryLoc === e) {
                        var n = r.completion;
                        if ("throw" === n.type) {
                            var o = n.arg;
                            C(r)
                        }
                        return o
                    }
                }
                throw new Error("illegal catch attempt")
            },
            delegateYield: function (t, r, n) {
                return this.delegate = {
                    iterator: T(t),
                    resultName: r,
                    nextLoc: n
                },
                "next" === this.method && (this.arg = e),
                    b
            }
        },
        r
}

function Ue(e, t, r, n, o, i, a) {
    try {
        var c = e[i](a)
            , u = c.value
    } catch (s) {
        return void r(s)
    }
    c.done ? t(u) : Promise.resolve(u).then(n, o)
}

function Fe(e) {
    return function () {
        var t = this
            , r = arguments;
        return new Promise((function (n, o) {
                var i = e.apply(t, r);

                function a(e) {
                    Ue(i, n, o, a, c, "next", e)
                }

                function c(e) {
                    Ue(i, n, o, a, c, "throw", e)
                }

                a(void 0)
            }
        ))
    }
}

function e(t) {
    var r, n, o, i, a, c, u, s, l, f, p, d;
    return Ke().wrap((function (e) {
            for (; ;)
                switch (e.prev = e.next) {
                    case 0:
                        return r = t.url,
                            n = t.fetchConfig,
                            o = t.timestampForTest,
                            i = t.tokenForTest,
                            a = function () {
                                return crypto.randomUUID ? crypto.randomUUID() : (new Date).getTime()
                            }
                            ,
                            c = function () {
                                var e = Fe(Ke().mark((function e(t) {
                                        var r, n, i, a, c, u, s, l, f, p, d;
                                        return Ke().wrap((function (e) {
                                                for (; ;)
                                                    switch (e.prev = e.next) {
                                                        case 0:
                                                            return r = "",
                                                                e.next = 3,
                                                                crypto.subtle.digest("SHA-256", (new TextEncoder).encode(t));
                                                        case 3:
                                                            for (n = e.sent,
                                                                     i = Array.from(new Uint8Array(n)),
                                                                     a = i.map((function (e) {
                                                                             return e.toString(16).padStart(2, "0")
                                                                         }
                                                                     )).join(""),
                                                                     c = Date.now(),
                                                                     u = o || Math.floor(c / 1e3),
                                                                     s = Math.floor(u / 600 % 32),
                                                                     l = Math.floor(u / 3600 % 32),
                                                                     f = 0; f < 32; f++)
                                                                p = a[(s + (l + f) * f) % 32],
                                                                    r += p;
                                                            return e.next = 13,
                                                                crypto.subtle.importKey("raw", (new TextEncoder).encode(r), {
                                                                    name: "HMAC",
                                                                    hash: "SHA-256"
                                                                }, !1, ["sign"]);
                                                        case 13:
                                                            return d = e.sent,
                                                                e.abrupt("return", {
                                                                    key: d,
                                                                    timestamp: c
                                                                });
                                                        case 15:
                                                        case "end":
                                                            return e.stop()
                                                    }
                                            }
                                        ), e)
                                    }
                                )));
                                return function (t) {
                                    return e.apply(this, arguments)
                                }
                            }(),
                            u = function () {
                                var e = r.replace("?", "");
                                return e
                            }
                            ,
                            s = function () {
                                var e = Fe(Ke().mark((function e(t) {
                                        var r, n, o, i, a, s;
                                        return Ke().wrap((function (e) {
                                                for (; ;)
                                                    switch (e.prev = e.next) {
                                                        case 0:
                                                            return e.next = 2,
                                                                c(t);
                                                        case 2:
                                                            return r = e.sent,
                                                                n = r.key,
                                                                o = r.timestamp,
                                                                i = u(),
                                                                e.next = 8,
                                                                crypto.subtle.sign("HMAC", n, (new TextEncoder).encode(i));
                                                        case 8:
                                                            return a = e.sent,
                                                                s = btoa(String.fromCharCode.apply(String, G(new Uint8Array(a)))),
                                                                e.abrupt("return", {
                                                                    signature: s,
                                                                    timestamp: o
                                                                });
                                                        case 11:
                                                        case "end":
                                                            return e.stop()
                                                    }
                                            }
                                        ), e)
                                    }
                                )));
                                return function (t) {
                                    return e.apply(this, arguments)
                                }
                            }(),
                            l = i || a(),
                            e.next = 8,
                            s(l);
                    case 8:
                        return f = e.sent,
                            p = f.timestamp,
                            d = f.signature,
                            e.abrupt("return", {
                                token: l,
                                timestamp: p,
                                signature: d
                            });
                    case 12:
                    case "end":
                        return e.stop()
                }
        }
    ), e)
}

function getTokenAndSign() {
    var t = this
        , r = arguments;
    return new Promise((function (n, o) {
            var i = e.apply(t, r);

            function a(e) {
                Ue(i, n, o, a, c, "next", e)
            }

            function c(e) {
                Ue(i, n, o, a, c, "throw", e)
            }

            a(void 0)
        }
    ))
}

function get_o(url, fetchConfig) {
    return getTokenAndSign({
        url: url,
        fetchConfig: fetchConfig
    }).then(c => {
        let u = c.token,
            s = c.timestamp,
            l = c.signature;
        return {'Ok-Verify-Token': u, 'Ok-Timestamp': s, 'Ok-Verify-Sign': l};
    });
}


get_o(url, fetchConfig)
    .then(result => console.log(JSON.stringify(result)))
    .catch(error => console.error("Error fetching token and signature:", error));
