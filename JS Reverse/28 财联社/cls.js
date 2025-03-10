require('./loader.js')
require('./mod 01.js')
let p = window.loader("W2Yj")


function sign() {
    let r = {
        "os": "web",
        "sv": "8.4.6",
        "app": "CailianpressWeb"
    }
    return p(r)
}

// let sign = p(r)
// console.log(sign)