require('./env.js')
require('./loader.js')
require('./mod 02.js')
require('./mod 01.js')

a = window.loader(20)

function get_account(account) {
    return a.getEncryptPwd(account)
}

let params = process.argv[2];
console.log(get_account(params))
process.exit()



