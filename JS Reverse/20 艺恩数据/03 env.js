window = global;
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows)",
    buildID: "20181001000000",
    cookieEnabled: true,
    globalPrivacyControl: false,
    hardwareConcurrency: 16,
    language: "zh-CN",
    maxTouchPoints: 20,
    oscpu: "Windows NT 10.0; Win64; x64",
    pdfViewerEnabled: true,
    platform: "Win32",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    vendorSub: "",
    webdriver: false
}
document = {}

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

setProxyArr(['window', 'navigator', 'document'])