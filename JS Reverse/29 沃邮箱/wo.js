require('./loader.js')

let i = window.loader(596)
function r(t, e, n) {
    var r = new i;
    return r.setPublic(e, n),
        r.encrypt(t)
}

function encrypt(t, o) {
    return '#!' + r(t, o, '10001')
}

let pwd = "asd123"
let key = 'C4E3F7212602E1E396C0B6623CF11D26204ACE3E7D26685E037AD2507DCE82FC\n' +
    '28F2D5F8A67FC3AFAB89A6D818D1F4C28CFA548418BD9F8E7426789A67E73E41'
console.log(encrypt(pwd, key))