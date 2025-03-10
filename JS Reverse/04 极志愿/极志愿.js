cryptoIS = require("../crypto-js")
require('./env.js')
require('./loader.js')
require('./mod 01.js')
require('./mod 02.js')

// 接口测试
let params = '{app_id=98357f659cf8fb6001cff80f7c6b85f2&diploma_id=7&page=3&page_len=20&platform=desktop&ts=1731728579193&v=210&wenli=0}&key=146fd1e66513611ac7af69f21f1d7725'

console.log(Qt(params))