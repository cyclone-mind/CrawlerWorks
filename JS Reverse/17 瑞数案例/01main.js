require('./02env')
require('./03ts')
require('./04auto')

function get_cookie(){
    return document.cookie
}

console.log(get_cookie())