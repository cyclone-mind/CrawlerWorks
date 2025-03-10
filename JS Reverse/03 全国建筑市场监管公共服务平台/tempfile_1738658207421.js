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
