window = global;
window.addEventListener = function (){}
window.requestAnimationFrame = function (){}
window.cancelAnimationFrame = function (){}
canvas = {
    toDataURL: function () {
        return ''
    }
}
div = {
    style: {},
    setAttribute:function (){
    }
}
_body = {
    style:{
        fontSize: ''
    }
}
document = {
    createElement: function (res) {
        // console.log('创建标签名:::', res)
        if (res === 'canvas') {
            return canvas
        } else if (res === 'div') {
            return div
        }

    },
    addEventListener:function (){
    },
    documentElement:{
        clientWidth:1779,
        style:{
            fontSize:''
        }
    },
    getElementById:function (res){
        // console.log("创建标签:::",res)
    },
    body:_body

};
navigator = {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}
location = {
    "ancestorOrigins": {},
    "href": "https://passport.ximalaya.com/page/web/login?fromUri=https%3A%2F%2Fstudio.ximalaya.com",
    "origin": "https://passport.ximalaya.com",
    "protocol": "https:",
    "host": "passport.ximalaya.com",
    "hostname": "passport.ximalaya.com",
    "port": "",
    "pathname": "/page/web/login",
    "search": "?fromUri=https%3A%2F%2Fstudio.ximalaya.com",
    "hash": ""
}

function setProxyArr(proxyObjArr) {
    for (let i = 0; i < proxyObjArr.length; i++) {
        const handler = `{
      get: function(target, property, receiver) {
        console.log("方法:", "get  ", "对象:", "${proxyObjArr[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property], ", 属性值类型：", typeof target[property]);
        return target[property];
      },
      set: function(target, property, value, receiver) {
        console.log("方法:", "set  ", "对象:", "${proxyObjArr[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
        return Reflect.set(...arguments);
      }
    }`;
        eval(`try {
            ${proxyObjArr[i]};
            ${proxyObjArr[i]} = new Proxy(${proxyObjArr[i]}, ${handler});
        } catch (e) {
            ${proxyObjArr[i]} = {};
            ${proxyObjArr[i]} = new Proxy(${proxyObjArr[i]}, ${handler});
        }`);
    }
}

// setProxyArr(['window', 'navigator', 'document', 'location', 'canvas', 'div','_body'])