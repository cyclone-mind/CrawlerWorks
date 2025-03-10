// 首先获得_uuid
var get__uuid = function () {
    var e = o(8)
        , t = o(4)
        , r = o(4)
        , n = o(4)
        , a = o(12)
        , s = (new Date).getTime();
    return e + "-" + t + "-" + r + "-" + n + "-" + a + i((s % 1e5).toString(), 5) + "infoc"
}
    , o = function (e) {
    for (var t = "", r = 0; r < e; r++)
        t += a(16 * Math.random());
    return i(t, e)
}
    , i = function (e, t) {
    var r = "";
    if (e.length < t)
        for (var n = 0; n < t - e.length; n++)
            r += "0";
    return r + e
}
    , a = function (e) {
    return Math.ceil(e).toString(16).toUpperCase()
}

// console.log(get__uuid())
function get_splitDate(e) {
    var t = new Date(e || Date.now())
        , r = t.getDate()
        , n = t.getHours()
        , o = t.getMinutes()
        , i = t.getTime();
    return {
        day: r,
        hour: n,
        minute: o,
        second: Math.floor(i / 1e3),
        millisecond: i
    }
}

function get_blsid() {
    let e = get_splitDate()
        , t = a(e.millisecond);
    return "".concat(o(8), "_").concat(t)
}

console.log(get_blsid())