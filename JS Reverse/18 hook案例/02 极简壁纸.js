(function() {
    var parse = JSON.parse;
    JSON.parse = function(params) {
        console.log("Hook JSON.parse::: ", params);
        debugger;
        return parse(params);
    }
})();