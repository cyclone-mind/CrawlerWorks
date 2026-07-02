// XDF 搜课接口签名 (v3)
// 算法来自线上 chunk：把参数按插入顺序拼成 query，末尾拼接 appKey 后 MD5
// 注意：中文关键字必须先 URL 编码 (与线上 encodeURI 一致) 再传入
const CryptoJS = require("../crypto-js");

var Config = {
  appId: "5052",
  appKey: "2EF9FA45-3317-49D9-B4FB-BABD7C0ACDA5",
};

function getSign(e) {
  var params = Object.assign({}, e, {
    t: new Date().getTime(),
    appId: Config.appId,
  });
  var pairs = [];
  Object.keys(params).forEach(function (key) {
    pairs.push("".concat(key, "=").concat(params[key]));
  });
  var query = pairs.join("&");
  return {
    timestamp: params.t,
    query: query,
    sign: CryptoJS.MD5(query + Config.appKey).toString(),
  };
}
