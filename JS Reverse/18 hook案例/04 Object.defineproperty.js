var zhangsan = {
    name: 'zhangsan',
    age: 23
}
    // console.log(zhangsan.age)
    // zhangsan,age = 100
    // console.log(zhangsan.age)
    /*版本1
    Object.defineProperty(zhangsan,'age',{
        get:function (){
            return 'yuan'
        },
        set:function (val){
            console.log('设置已完成，值:',val)
        }
    })
    console.log(zhangsan.age)
    zhangsan.age = 100
    */

    (function () {
        var zhangsan = {
            name: 'zhangsan',
            age: 23
        }
        var x = 0
        Object.defineProperty(zhangsan, 'age', {
            get: function () {
                return x
            },
            set: function (val) {
                console.log('设置已完成，值:', val)
                x = val
            }
        })
        console.log(zhangsan.age)
        zhangsan.age = 167
        console.log(zhangsan.age)
    })()

