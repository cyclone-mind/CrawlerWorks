require('./env.js')
require('./loader.js')
cryptoJS = require('../../crypto-js')



// console.log(d)
function v(A, e) {
    var t = Object.keys(A);
    if (Object.getOwnPropertySymbols) {
        var n = Object.getOwnPropertySymbols(A);
        e && (n = n.filter((function (e) {
                return Object.getOwnPropertyDescriptor(A, e).enumerable
            }
        ))),
            t.push.apply(t, n)
    }
    return t
}

function m(A) {
    for (var e = 1; e < arguments.length; e++) {
        var t = null != arguments[e] ? arguments[e] : {};
        e % 2 ? v(Object(t), !0).forEach((function (e) {
                b(A, e, t[e])
            }
        )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(A, Object.getOwnPropertyDescriptors(t)) : v(Object(t)).forEach((function (e) {
                Object.defineProperty(A, e, Object.getOwnPropertyDescriptor(t, e))
            }
        ))
    }
    return A
}

function b(A, e, t) {
    return e in A ? Object.defineProperty(A, e, {
        value: t,
        enumerable: !0,
        configurable: !0,
        writable: !0
    }) : A[e] = t,
        A
}

function p(A, e, t, n, r, a, s) {
    try {
        var i = A[a](s)
            , o = i.value
    } catch (g) {
        return void t(g)
    }
    i.done ? e(o) : Promise.resolve(o).then(n, r)
}

function h(A) {
    return function () {
        var e = this
            , t = arguments;
        return new Promise((function (n, r) {
                var a = A.apply(e, t);

                function s(A) {
                    p(a, n, r, s, i, "next", A)
                }

                function i(A) {
                    p(a, n, r, s, i, "throw", A)
                }

                s(void 0)
            }
        ))
    }
}

function w(A) {
    var e, t, n = "", r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", a = "=";
    for (e = 0; e + 3 <= A.length; e += 3)
        t = parseInt(A.substring(e, e + 3), 16),
            n += r.charAt(t >> 6) + r.charAt(63 & t);
    e + 1 == A.length ? (t = parseInt(A.substring(e, e + 1), 16),
        n += r.charAt(t << 2)) : e + 2 == A.length && (t = parseInt(A.substring(e, e + 2), 16),
        n += r.charAt(t >> 2) + r.charAt((3 & t) << 4));
    while ((3 & n.length) > 0)
        n += a;
    return n
}


function enc_param(page, publickey) {
    d = window.loader("9816")
    t = new d["a"]
    t.encryptLong = function(A) {
            var e = this.getKey()
              , t = (e.n.bitLength() + 7 >> 3) - 11;
            try {
                var n = ""
                  , r = "";
                if (A.length > t)
                    return n = A.match(/.{1,50}/g),
                    n.forEach((function(A) {
                        var t = e.encrypt(A);
                        r += t
                    }
                    )),
                    w(r);
                var a = e.encrypt(A)
                  , s = w(a);
                return s
            } catch (i) {
                return i
            }
        }
    let e = {
        "inviteMethod": "",
        "businessClassfication": "",
        "mc": "",
        "lx": "ZBGG",
        "dwmc": "",
        "pageIndex": page
    }
    t.setPublicKey(publickey)
    a = m(m({}, e), {}, {
        sign: cryptoJS.MD5(JSON.stringify(e)).toString(),
        timeStamp: +new Date
    })
    let s = t.encryptLong(JSON.stringify(a))
    return s
}

console.log(enc_param(1, "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCELE7y04pAe0g/kQn9X2uUkMYvdX+oyjpwtkVyZ/Vhmc8bVIUVojxIbSSPlGoQ7GxUhtUafdZTFcBgR+c4Y8oiYP9rINiDkK6gvOq7TJ8VqpYv4raUCWI5ErBjRUHgLHQvEdu396V5/qO9fFor4JvWIYmDoMsOQmp8DdQvPfaDFQIDAQAB"))

