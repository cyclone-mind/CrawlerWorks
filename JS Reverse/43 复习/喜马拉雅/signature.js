require('./env.js')
require('./loader.js')
require('./mod 02.js')
require('./mod 01.js')

a = window.loader(20)
let n = process.argv[2]
let i = process.argv[3]
let t = process.argv[4]

function get_signature(n, i, t) {
    return a.getSignature({
        account: n,
        password: i,
        nonce: t
    })
}


console.log(get_signature(n, i, t))
process.exit()




