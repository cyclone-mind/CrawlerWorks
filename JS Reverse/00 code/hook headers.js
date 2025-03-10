(function () {
    let originalSetRequestHeader = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
        console.log("Hook set header %s => %s", key, value);
        if (key === "X-Dgi-Req-Signature") {
            debugger;
        }
        return originalSetRequestHeader.apply(this, arguments);
    };
})();
(function () {
    let originalEventSource = window.EventSource;
    window.EventSource = function (...args) {
        console.log("Hook EventSource request:", args);
        // 在这里可以添加自定义逻辑
        return new originalEventSource(...args);
    };
})();
(function ($) {
    let originalAjax = $.ajax;
    $.ajax = function (options) {
        console.log("Hook jQuery ajax request:", options);
        // 在这里可以添加自定义逻辑，比如检查请求头等
        return originalAjax.apply(this, arguments);
    };
})(jQuery);
if (window.axios) {
    axios.interceptors.request.use(function (config) {
        console.log("Hook axios request:", config);
        // 在这里可以添加自定义逻辑，比如检查请求头等
        return config;
    }, function (error) {
        return Promise.reject(error);
    });
}
(function () {
    let originalFetch = window.fetch;
    window.fetch = function (...args) {
        console.log("Hook fetch request:", args);
        // 在这里可以添加自定义逻辑，比如检查请求头等
        return originalFetch.apply(this, args);
    };
})();

