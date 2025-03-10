cryptoJS = require("../crypto-js")

function get_sign(t) {
    e = "/youzy.dms.basiclib.api.college.query";
    var r, i = "9SASji5OWnG41iRKiSvTJHlXHmRySRp1", o = "", a = t || {}, s = (e = e || "").split("?");
    if (s.length > 0 && (r = s[1]),
        r) {
        var u = r.split("&")
            , c = "";
        u.forEach((function (e) {
                var t = e.split("=");
                c += "".concat(t[0], "=").concat(encodeURI(t[1]), "&")
            }
        )),
            o = "".concat(_.trimEnd(c, "&"), "&").concat(i)
    } else
        o = Object.keys(a).length > 0 ? "".concat(JSON.stringify(a), "&").concat(i) : "&".concat(i);
    return o = o.toLowerCase(),
        cryptoJS.MD5(o).toString()
}



// 接口测试
/*
var data = {
    "keyword": "",
    "provinceNames": [],
    "natureTypes": [],
    "eduLevel": "",
    "categories": [],
    "features": [],
    "pageIndex": 3,
    "pageSize": 20,
    "sort": 11
}

console.log(get_sign(data)) */
