window = global
window.toString = function (){
    return '[object Window]'
}
delete global
__process = process
delete process
function enc2() {

    if (window.setTimeout && window.toString() === '[object Window]') {

        // 再次校验
        try {
            // global
            process
            return "yyy"
        } catch (obj) {
            // 浏览器环境执行process应该报错
            return "asdfg"
        }

    } else {
        return "xxx"
    }

}


console.log(enc2())
console.log(window.toString())
__process.exit(1)
console.log('...')


