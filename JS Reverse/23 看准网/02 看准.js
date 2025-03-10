require('./04 env')
require('./03 loader')
require('./05 mod1')


// n = '{"query":"python","cityCode":"101210100","salaryId":"","experienceId":"","pageNum":1,"limit":15}'
// function get_kiv() {
//     return kiv
// }
//
// function get_b(n) {
//     return k.mA(n, {
//         iv: kiv
//     })
// }


function get_data(n) {
    let k = window.loader(12210)
    let kiv = k._A()
    let b = k.mA(n, {
        iv: kiv
    }).replace(/\//g, "_").replace(/\+/g, "-").replace(/=/g, "~")
    return [b, kiv]
}

function get_res(res,kiv) {
    let k = window.loader(12210)
    let decrypted_data = k.gy(res, {
        iv: kiv
    })
    return decrypted_data
}

// console.log(get_data(n))
