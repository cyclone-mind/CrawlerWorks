// debugger
// console.log("hello yuan")
// eval("debugger")
// console.log("hello alex")

// 回顾setInterval和setTimeout
// var ID = setInterval(function (){
//     console.log("hello yuan")
// },1000)
//
//
// clearInterval(ID)


// var ID = setTimeout(function (){
//     console.log("hello yuan")
// },1000)

// clearTimeout(ID)


// 定时器触发debugger
// setInterval(function () {
//         debugger;
//         console.log("hello yuan")
//     }, 1000
// )

// setTimeout(function foo (){
//     debugger;
//     console.log("hello world")
//     setTimeout(foo,1)
// },1)
//


// 通过原型链的方式执行debugger
// Function("debugger").call()
// console.log("111")
// Function("debugger").apply()
// console.log("222")
// Function.constructor("debugger").call("action")
// console.log("333")
// Function.constructor("debugger").apply("action")
// console.log("444");
// (function (){return!![]}["constructor"]("debugger")["call"]("action"))
// console.log("555");
// eval('(function (){return!![]}["constructor"]("debugger")["call"]("action"))')
// console.log("666");


