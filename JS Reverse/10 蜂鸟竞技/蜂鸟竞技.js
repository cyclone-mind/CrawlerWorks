require("./env")
require("./loader")
require("./mod1")


r = window.loader(390)
a = window.loader(391)

function get_params() {
    var p = "KHVheWluZ18zZWNyZXRfYXBB"
    var e = (new Date).getTime()
        , n = "timestamp=".concat(e, "&secret=").concat(p)

    var s = r(n);
    sign = encodeURIComponent(a.stringify(s))
    timestamp = e
    var part_params = {
        'timestamp':timestamp,
        'sign':sign
    }
    return part_params
}
