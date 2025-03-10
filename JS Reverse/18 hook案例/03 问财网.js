/*钩cookie
(function(){
   'use strict'
    var _cookie = "";
    Object.defineProperty(document, 'cookie', {
        set: function(val) {
            console.log(val);
            debugger
            _cookie = val;
            return val;
        },
        get: function() {
            return _cookie;
        },
});
})()
*/

/*
 钩header中的hexin-v
(function () {
    let set_header = window.XMLHttpRequest.prototype.setRequestHeader()
    window.XMLHttpRequest.prototype.setRequestHeader = function (header, value) {
        if (header.toUpperCase() === 'hexin-v'.toUpperCase()) {
            debugger
        }
        return set_header.apply(this, arguments)
    }
})()
*/
