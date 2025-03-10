function get_proxy(obj, obj_name) {
    obj = new Proxy(obj, {
        get: function (target, property1) {
            if (property1 === 'entry') {
                return Reflect.get(target, property1)
            }
            console.log('方法：get  对象-->', obj_name, '属性-->', property1, '属性类型-->', typeof (property1), '值-->', target[property1])
            //debugger
            return Reflect.get(target, property1)
        },
        set: function (target, property1, value) {
            console.log('方法：set  对象-->', obj_name, '属性-->', property1, '属性类型-->', typeof (property1), '值-->', target[property1])
            // debugger
            return Reflect.set(target, property1, value)
        }
    })
    return obj;
};

window = global;
delete global;
delete Buffer;
window.addEventListener = function (params) {
    // console.log('window.addEventListener--->', params);
};
window.RTCPeerConnection = function (params) {
    // console.log('window.RTCPeerConnection--->', params);
};
window.webkitRTCPeerConnection = function (params) {
    // console.log('window.webkitRTCPeerConnection--->', params);
};
window.TCaptchaReferrer = 'https://cloud.tencent.com/product/captcha';
window.innerWidth = 1366;
window.innerHeight = 768;

CanvasRenderingContext2D = {
    textBaseline: 'alphabetic',
    font: '10px sans-serif',
    fillStyle: '#000000',
    fillRect: function (params) {
        // console.log("CanvasRenderingContext2D.fillRect --->", params);
    },
    fillText: function (params) {
        // console.log("CanvasRenderingContext2D.fillText --->", params);
    },
    // drawImage: function (params) {
    //     // console.log("CanvasRenderingContext2D.drawImage --->", params);
    // },
};
canvas = {
    getContext: function (params) {
        // console.log('canvas.getContext--->', params);
        if (params === '2d') {
            return CanvasRenderingContext2D;
        }
    },
};
div = {
    style: {},
    appendChild: function (params) {
        // console.log('div.appendChild--->', params);
    },
};
span = {
    setAttribute: function (params) {
        // console.log('span.setAttribute--->', params);
    },
    removeAttribute: function (params) {
        // console.log('span.removeAttribute--->', params);
    },
};
iframe = {
    style: {},
};
_documentElement = {};
_body = {};
document = {
    characterSet: "UTF-8",
    charset: "UTF-8",
    cookie: '',
    URL: 'https://turing.captcha.gtimg.com/1/template/drag_ele.html',
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
    // documentMode: undefined,
    createElement: function (params) {
        // console.log('document.createElement--->', params);
        if (params === 'canvas') {
            return canvas;
        } else if (params === 'div') {
            return div;
        } else if (params === 'span') {
            return span;
        } else if (params === 'iframe') {
            return iframe;
        }
    },
    addEventListener: function (params) {
        // console.log('document.addEventListener--->', params);
    },
    getElementById: function (params) {
        // console.log('document.getElementById--->', params);
        if (params === 'tCaptchaDyContent') {
            return '';
        }
    },
    documentElement: _documentElement,
    body: _body,
};

navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    languages: ['zh-CN', 'zh'],
    cookieEnabled: true,
    platform: "MacIntel",
    vendor: "Google Inc.",
    webdriver: false,
    hardwareConcurrency: 8
};

location = {
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
};

screen = {
    availHeight: 875,
    availLeft: 0,
    availTop: 25,
    availWidth: 1440,
    colorDepth: 30,
    height: 900,
    isExtended: false,
    pixelDepth: 30,
    width: 1440
};

localStorage = {
    getItem: function (params) {
        // console.log('localStorage.getItem--->', params);
    },
    setItem: function (params) {
        // console.log('localStorage.setItem--->', params);
    },
};

sessionStorage = {};

history = {};

// window = get_proxy(window, 'window');
// document = get_proxy(document, 'document');
// navigator = get_proxy(navigator, 'navigator');
// location = get_proxy(location, 'location');
// screen = get_proxy(screen, 'screen');
// localStorage = get_proxy(localStorage, 'localStorage');
// sessionStorage = get_proxy(sessionStorage, 'sessionStorage');
// history = get_proxy(history, 'history');
// canvas = get_proxy(canvas, 'canvas');
// div = get_proxy(div, 'div');
// span = get_proxy(span, 'span');
// iframe = get_proxy(iframe, 'iframe');
// _documentElement = get_proxy(_documentElement, '_documentElement');
// _body = get_proxy(_body, '_body');
// CanvasRenderingContext2D = get_proxy(CanvasRenderingContext2D, 'CanvasRenderingContext2D');


require('./2-tdc.js')

function a(t) {
    window.TDC && "function" == typeof window.TDC.setData && window.TDC.setData(t)
}
getTdcData = function () {
    return a({ "ft": "qf_7Pf__H" }),
        window.TDC && "function" == typeof window.TDC.getData ? window.TDC.getData(!0) || "---" : "------"
}
function c() {
    return window.TDC && "function" == typeof window.TDC.getInfo && window.TDC.getInfo() || {}
}
getKeyInfo = function () {
    return (c() || {}).info || ""
}
function get_verify_params() {
    var collect = decodeURIComponent((0, getTdcData)())
    var eks = (0, getKeyInfo)();
    return { collect: collect, eks: eks }
}
console.log('verify_params--->', get_verify_params());
