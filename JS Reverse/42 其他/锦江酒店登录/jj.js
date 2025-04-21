const CryptoJS = require("crypto-js")
const getRandom = function() {
    for (var e = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", n = 6, a = "", t = 0; t < n; t++) {
        var o = Math.floor(Math.random() * e.length);
        a += e.charAt(o)
    }
    return a
}

// console.log(getRandom());

const hex_md5 = CryptoJS.MD5

function get_rw_sw(mobile){
    let a = {
        mobile:mobile,
        deviceInfo:{
            fingerPrintJs:"86f5df16549a213f79f8f415ae76a31c"
        }
    }
    let rw = getRandom()
    let sw = hex_md5(rw + a.mobile + a.deviceInfo.fingerPrintJs).toString()
    return {
        rw:rw,
        sw:sw
    }

}
// console.log("sw:::",sw);

let password = "123456789"
function l(e) {
    var n = CryptoJS.enc.Latin1.parse("h5LoginKey123456")
      , a = CryptoJS.enc.Latin1.parse("h5LoginIv1234567")
      , t = e
      , o = CryptoJS.AES.encrypt(t, n, {
        iv: a,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    });
    return o.toString()
}

function get_password(password){
    return l(password)
}

console.log("enc_password:::",l(password));

