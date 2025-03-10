// 创建js执行文件，引入加载器、环境
require('./env')
require('./loader')
console.log(window.loader(141))

function p(e) {
    return e && e.__esModule ? e : {
        default: e
    }
}

console.log()

function get_s(user, pwd){
    c = p(window.loader(141))
    s = `/WebApi/Users/Login?username=${user}&password=${pwd}DUE$DEHFYE(YRUEHD*&`
    return c.default(s)
}

// console.log(get_s('assd','ss12'))
