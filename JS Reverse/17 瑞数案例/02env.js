content = "dzRZUw_8_bcYrgDaKfUlpKki15nwevTA"

window = top = self = global;
window.addEventListener = function () {
}
window.attachEvent = function () {
}
div = {
    getElementsByTagName() {
        return []
    }
}
head = {
    removeChild() {
    }
}
script = {
    getAttribute: function (ele) {
        console.log('script getAttribute', ele)
        if (ele === 'r') {
            return 'm'
        }
    },
    parentElement: head
}
meta = {
    content: "pjNK_csuLYP41l4KpIS.nl5TC5YRTr7QzhmLNYj5mQEpfVx8Vd.Q.PucNB.BKZj.",
    r: 'm',
    id: 'K5MK4FPPNWrv',
    getAttribute: function (ele) {
        console.log('meta  getAttribute', ele)
        if (ele === 'r') {
            return 'm'
        }
    },
    parentNode: head
}
base = {
    getAttribute: function (ele) {
        console.log('base  getAttribute', ele)
    }
}

document = {
    createElement: function (ele) {
        console.log('document createElement ', ele)
        if (ele === 'div') {
            return div
        }
        if (ele === "form") {
            return {}
        }
        if (ele === "a") {
            return {}
        }

    },
    getElementsByTagName: function (ele) {
        console.log('document getElementsByTagName ', ele)
        if (ele === 'script') {
            return [script, script]
        }
        if (ele === 'base') {
            return [base, base]
        }
    },
    getElementById: function (id) {
        console.log('document getElementById ', id)
        if (id === 'K5MK4FPPNWrv') {
            return meta
        }
    },
    addEventListener: function () {
    },
    attachEvent: function () {
    }

};
location = {
    "ancestorOrigins": {},
    "href": "http://epub.cnipa.gov.cn/",
    "origin": "http://epub.cnipa.gov.cn",
    "protocol": "http:",
    "host": "epub.cnipa.gov.cn",
    "hostname": "epub.cnipa.gov.cn",
    "port": "",
    "pathname": "/",
    "search": "",
    "hash": ""
}
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    cookieEnabled: true,
    platform: "Win32"
}

setInterval = function () {
}
setTimeout = function () {
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

setProxyArr(['window', 'navigator', 'document', 'location', 'div', 'script', 'head', 'meta', 'base'])


'ts_js';
'auto_js';

function get_cookie() {
    return document.cookie
}