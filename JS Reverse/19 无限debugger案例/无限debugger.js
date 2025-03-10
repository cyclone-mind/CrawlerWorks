/*

使用该网站：https://artmeta.cn/测试，该网站右键debugger不在此处暂停后会卡死，所以回溯到debugger的位置，发现是构建了一个setTimeOut函数
，所以我们试着直接将setTimeOut函数置空，发现返回了空数据，这应该是影响了其他的逻辑，所以我们再次回溯到最开始的位置，将setTimeOut函数置空，
就可以了。

debugger
console.log("hello yuan")
eval("debugger")
console.log("hello alex")

// 回顾setInterval和setTimeout
const ID = setInterval(function () {
    console.log("hello yuan")
}, 1000);


clearInterval(ID)


var ID = setTimeout(function (){
    console.log("hello yuan")
},1000)

clearTimeout(ID)


// 定时器触发debugger
setInterval(function () {
        debugger;
        console.log("hello yuan")
    }, 1000
)

setTimeout(function foo (){
    debugger;
    console.log("hello world")
    setTimeout(foo,1)
},1)



// 通过原型链的方式执行debugger
Function("debugger").call()
console.log("111")
Function("debugger").apply()
console.log("222")
Function.constructor("debugger").call("action")
console.log("333")
Function.constructor("debugger").apply("action")
console.log("444");
(function (){return!![]}["constructor"]("debugger")["call"]("action"))
console.log("555");
eval('(function (){return!![]}["constructor"]("debugger")["call"]("action"))')
console.log("666");


*/
