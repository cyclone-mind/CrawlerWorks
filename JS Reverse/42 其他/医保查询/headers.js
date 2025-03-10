cryptoJS = require('../../crypto-js')

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


// console.log(get_h())
function get_signature() {
    let headers = {}
    let r = cryptoJS.SHA256
        , s = Math.ceil((new Date).getTime() / 1e3)
        , h = get_h()
        , f = s + h + s;
    headers["x-tif-signature"] = r(f).toString()
    headers["x-tif-timestamp"] = s
    headers["x-tif-nonce"] = h
    return headers
}


// console.log(get_signature())

