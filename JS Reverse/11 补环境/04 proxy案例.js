window = global
delete process
delete Buffer
delete global

window.addEventListener = function () {
}
var kw = {
    getAttribute: function () {
    }
}
ctx = {
    fillRect:function (){}
}
canvas = {
    getContext:function (ele) {
        console.log("canvas getContext::", ele)
        return ctx
    }
}
document = {
    getElementById: function (ele) {
        console.log("document getElementById::", ele)
        return kw
    },
    createElement: function (ele) {
        console.log("document createElement::", ele)
        return canvas
    }
}
navigator = {
    toString: function () {
        return '[object Navigator]'
    }
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

setProxyArr(['navigator', 'window', 'document', 'kw','canvas','ctx'])

function enc3() {

    // 校验
    try {
        if (navigator.toString() === '[object Navigator]') {

            window.addEventListener()
            // 搜索框
            let kw = document.getElementById("kw")
            let val = kw.getAttribute("class")
            // 创建画布
            let canvas = document.createElement("canvas")
            var ctx = canvas.getContext("2d");
            ctx.fillStyle = "green";
            ctx.fillRect(10, 10, 100, 100);

            console.log(val)
            return "asdfg"
        } else {
            return "YYY"
        }


    } catch (obj) {
        console.log(obj)

        return "XXX"
    }


}

console.log(enc3())
