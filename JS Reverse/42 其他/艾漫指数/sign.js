cryptoJS = require('../../crypto-js')


function get_sign() {
    let movie  = "channel_movielist_iIndex"
    return cryptoJS.MD5(movie).toString()
}
