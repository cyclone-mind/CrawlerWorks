const sm = require('sm-crypto');

let l = sm.sm4;
function d(e) {
    var t = l.encrypt(e, "30062AFC48C0E7B5B0918851C0445A37");
    return t
}

i = {
    "applyType": 1,
    "year": 2025,
    "buyerName": "",
    "code": "",
    "areaCode": "",
    "status": "",
    "distributor": "",
    "enterpriseId": "",
    "factoryNumber": "",
    "machineCode": "",
    "purchaseDateStart": "",
    "purchaseDateEnd": "",
    "pageNum": 3,
    "pageSize": 15
}

console.log(d(JSON.stringify(i)))