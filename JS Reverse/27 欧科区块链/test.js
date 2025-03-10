const crypto = require('crypto');

// 定义密钥（字符串形式）
const secretKey = "your-secret-key";

// 数据待签名
const data = "data-to-sign";

// 生成 HMAC 签名
const hmac = crypto.createHmac("sha256", secretKey);
hmac.update(data);
const signature = hmac.digest();
d = Buffer.from(signature).toString("base64");
console.log("Node.js Signature:", d);