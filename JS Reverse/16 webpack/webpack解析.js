// 基于对象的模式
//  webpack的流程：
// (1) 找调度器loader并本地存储
// (2) 在调度器中找到调度函数,全局化
// (3) 在调度器函数写入调用模块的日志
// (4) 全局查找依赖的模块，导入执行文件中

window = global
!function (e) {
    var t = {};

    function n(r) {
        if (t[r])
            return t[r].exports;
        var o = t[r] = {
            i: r,
            l: !1,
            exports: {}
        };

        console.log("r:::", r)
        e[r].call(o.exports, o, o.exports, n);
        return o.exports.exports; // 返回 o.exports.exports，而不是整个 o.exports 对象
    }

    window.loader = n

    console.log(n("1003"));
}(
    {
        "1001": function () {
            console.log("foo");
            this.exports = 100; // 直接修改 exports 变量
        },
        "1002": function () {
            console.log("bar");
            window.loader("1001")
            this.exports = 200;
        },
        "1003": function () {
            console.log("atr");
            console.log(document.cookie)
            console.log(screen.width)

            this.exports = 300;
        }
    });

window.loader("1002")

