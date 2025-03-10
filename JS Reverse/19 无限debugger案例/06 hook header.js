(function (){
   let set_header  = window.XMLHttpRequest.prototype.setRequestHeader
    window.XMLHttpRequest.prototype.setRequestHeader = function (header,val){
       if (header.toUpperCase()=== "hexin-v".toUpperCase()){
           debugger
       }
       return set_header.apply(this,arguments)
    }

})()