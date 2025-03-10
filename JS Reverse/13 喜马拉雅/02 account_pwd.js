require('./04 env')
require('./05 mod01')
require('./06 mod02')
require('./03 loader')

a = window.loader(20)
// enc_data = a.getEncryptPwd('123456')
// console.log(enc_data)
// process.exit()

var params = process.argv[2];
var encrypted_params = a.getEncryptPwd(params)
console.log(encrypted_params)
process.exit()
