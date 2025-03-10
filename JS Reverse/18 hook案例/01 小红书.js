(function() {
    var stringify = JSON.stringify;
    JSON.stringify = function(params) {
        if (params['payload']){
            debugger;
        }
        return stringify(params);
    }
})();