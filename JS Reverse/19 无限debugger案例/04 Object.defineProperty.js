// var zhangsan = {
//     name: "张三",
//     age: 18
// }
//
// console.log(zhangsan.age)
// zhangsan.age = 10000
// console.log(zhangsan.age)
// 版本1
/*
Object.defineProperty(zhangsan, "age", {
    get: function () {
        return "yuan"
    },
    set: function (val) {
        console.log("设置已经完成,值：",val)
    }
})

console.log(zhangsan.age)
zhangsan.age = 1000
console.log(zhangsan.age)
*/

(function () {
    var zhangsan = {
        name: "张三",
        age: 18
    }
    var x = 0
    Object.defineProperty(zhangsan, "age", {
        get: function () {
            return x
        },
        set: function (val) {
            if (val > 100) {
                console.log("Error：设置的年龄过大！")
            } else {
                console.log("设置已经完成,值：", val)
                x = val
            }

        }
    })

    console.log(zhangsan.age)
    zhangsan.age = 167
    console.log(zhangsan.age)

})()
