const cryptoJS = require('crypto-js')
require('./env.js')
require('./loader.js')
let r = window.loader(6),
    a = window.loader.n(r)

function encrypt(password) {
    let o = this;
    this.ec = new a.a
    return o.ec.encrypt(password)
}
// 接口测试
console.log(encrypt("add12345677"))
