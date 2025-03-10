function encryptApiKey() {
    var e = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
        , t = e.split("")
        , n = t.splice(0, 8);
    return e = t.concat(n).join("")
}

function encryptTime(e) {
    let c = 1111111111111
    var t = (1 * e + c).toString().split("")
        , n = parseInt(10 * Math.random(), 10)
        , r = parseInt(10 * Math.random(), 10)
        , o = parseInt(10 * Math.random(), 10);
    return t.concat([n, r, o]).join("")
}

function comb(e, t) {
    var n = "".concat(e, "|").concat(t);
    return btoa(n)
}

function get_apikey() {
    var e = (new Date).getTime()
        , t = encryptApiKey();
    return e = encryptTime(e),
        comb(t, e)
}

// console.log(get_apikey())

