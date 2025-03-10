var yuan = {
    name: "yuan",
    age: 22
}

var rain = {
    name: "rain",
    age: 32
}


yuan = new Proxy(yuan, {
    get(target, p, receiver) {
        console.log("查询操作")
        console.log("target:", target)
        console.log("p:", p)
        return Reflect.get(target, p)
    },
    set(target, p, value, receiver) {
        console.log("设置操作")
        console.log("target:", target)
        console.log("p:", p)
        console.log("value:", value)

        Reflect.set(target, p, value);
    }
})

rain = new Proxy(rain, {
    get(target, p, receiver) {
        console.log("查询操作")
        console.log("target:", target)
        console.log("p:", p)
        return Reflect.get(target, p)
    },
    set(target, p, value, receiver) {
        console.log("设置操作")
        console.log("target:", target)
        console.log("p:", p)
        console.log("value:", value)

        Reflect.set(target, p, value);
    }
})

// 黑匣子中的逻辑代码
let a = yuan.name
let b = yuan.age
yuan.age = 100
yuan.name = "alvin"
let c = rain.name