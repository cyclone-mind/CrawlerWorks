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
};

window = global;
delete global;
delete Buffer;

navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    languages: ['zh-CN', 'zh'],
    cookieEnabled: true,
    platform: "MacIntel",
    vendor: "Google Inc.",
    webdriver: false,
    hardwareConcurrency: 8
}
window.addEventListener = function () {
}
window.RTCPeerConnection = function (params) {
    // console.log('window.RTCPeerConnection--->', params);
};
window.webkitRTCPeerConnection = function (params) {
    // console.log('window.webkitRTCPeerConnection--->', params);
};
window.screen = {
    availHeight: 1080,
    availLeft: 0,
    availTop: 0,
    availWidth: 1920,
    colorDepth: 24,
    height: 1080,
    isExtended: false,
    onchange: null,
    orientation: {
        angle: 0,
        onchange: null,
        type: "landscape-primary"
    },
    pixelDepth: 24,
    width: 1920,
}
window.TCaptchaReferrer = 'https://cloud.tencent.com/product/captcha'
window.localStorage = {
    "TDC_itoken": "559026644:1735113852"
}
window.sessionStorage = {
    "TDC_itoken": "559026644:1735113852"
}

CanvasRenderingContext2D = {
    textBaseline:'alphabetic',
    font:'10px sans-serif',
    fillRect:function (){},
    // fillStyle:'#000000'
}

canvas1 = {
    getContext: function (params) {
        // console.log('canvas.getContext--->', params);
        if (params === '2d') {
            return CanvasRenderingContext2D;
        }
    },
}
div1 = {
    style: {},
    appendChild: function (params) {
        // console.log('div.appendChild--->', params);
    },
    clone: function () {
    },
}
p1 = {}
_body = {}
_documentElement = {}
document = {
    characterSet: 'UTF-8',
    charset: 'UTF-8',
    createElement: function (params) {
        // console.log('document.createElement:', params)
        if (params === 'canvas') {
            return canvas1;
        } else if (params === 'div') {
            return div1;
        } else if (params === "p") {
            return p1;
        }
    },
    getElementById: function (params) {
        // console.log("document.getElementById:", params)
        if (params === 'tCaptchaDyContent') {
            return '';
        }
    },
    addEventListener: function () {
    },
    location: {
        "ancestorOrigins": {
            "0": "https://cloud.tencent.com"
        },
        "href": "https://turing.captcha.gtimg.com/1/template/drag_ele.html",
        "origin": "https://turing.captcha.gtimg.com",
        "protocol": "https:",
        "host": "turing.captcha.gtimg.com",
        "hostname": "turing.captcha.gtimg.com",
        "port": "",
        "pathname": "/1/template/drag_ele.html",
        "search": "",
        "hash": ""
    },
    URL: 'https://turing.captcha.gtimg.com/1/template/drag_ele.html',
    cookie: '',
    body: _body,
    documentElement: _documentElement
}

// setProxyArr(["document", 'navigator', "canvas1", "div1", "p1","CanvasRenderingContext2D"])

require('./03 tdc.js')


function a(t) {
    window.TDC && "function" == typeof window.TDC.setData && window.TDC.setData(t)
}

getTdcData = function () {
    return a({"ft": "qf_7Pf__H"}),
        window.TDC && "function" == typeof window.TDC.getData ? window.TDC.getData(!0) || "---" : "------"
}

function c() {
    return window.TDC && "function" == typeof window.TDC.getInfo && window.TDC.getInfo() || {}
}

getKeyInfo = function () {
    return (c() || {}).info || ""
}

function get_verify_params() {
    let a = decodeURIComponent((0, getTdcData)())
    let s = (0, getKeyInfo)()
    return {
        'collect': a,
        'eks': s
    }
}

console.log(get_verify_params())