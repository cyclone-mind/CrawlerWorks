// 引入内置的 crypto 模块
const crypto = require('crypto');

/**
 * 生成 HMAC (SHA-256) 签名
 * @param {string} secretKey - 密钥
 * @param {string} data - 待签名数据
 * @returns {string} - Base64 编码的签名
 */
function generateHmacSHA256(secretKey, data) {
    const hmac = crypto.createHmac('sha256', secretKey);
    hmac.update(data);
    const signature = hmac.digest('base64');
    return signature;
}

// 示例用法
const secretKey = "your-secret-key";
const data = "/api/explorer/v1/btc/transactionsNoRestrict?offset=40&limit=20&t=1732173775260";

const signature = generateHmacSHA256(secretKey, data);
console.log("Node.js HMAC SHA-256 Signature:", signature);
/*
    示例输出:
    Node.js HMAC SHA-256 Signature: QvEc4ghsL0qOqH249yLG7v+wLCSMgyhsVA6U6nVQi2I=
*/
