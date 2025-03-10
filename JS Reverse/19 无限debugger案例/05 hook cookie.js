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