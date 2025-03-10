// 该案例是一个多文件的webpack示例
// 01 定位加密入口，关键字----password > password: > captchaVerification> captchaVerification:
// 02 定位入口以后不要进入加密函数，找到谁用了加密函数，发现是  password: Object(g.b)(t) t是参数，那么g.b
// 则是加密函数，往上瞅一眼：g = n("MuMZ")，发现是webpack打包的模块进行了加密，那简单，进入调度器 n ，滑到最后
// 发现是一个空数组，则模块函数写在了其他文件。因为"MuMZ"是一个键，因此，全局搜索：“MuMZ:”即可找到该模块。

require('./env')
require('./loader')
require('./mod1')
require('./mod2')

g = window.loader('MuMZ')
console.log(g.b('123'))