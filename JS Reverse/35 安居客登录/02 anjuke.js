// 生成一个随机整数，然后转换为16进制字符串
const CryptoJS = require("crypto-js")

function e() {
    let randomHex = (65536 * (1 + Math.random()) | 0).toString(16);

// 从生成的16进制字符串中截取从索引1开始的部分
    let result = randomHex.substring(1);

    return result
}

function get_random_number() {
    return e() + e() + e() + e()
}
data = '{"setLeft":75,"passtime":320,"userresponse":92.53305864932724,"device_id":"","lot_number":"326def76a9ec485da0b1babfe5fb9034","pow_msg":"1|0|md5|2024-12-11T21:20:08.965713+08:00|ffe7f7735b0bc016e927b3241b090995|326def76a9ec485da0b1babfe5fb9034||2e43d45d68851c66","pow_sign":"a2543ee9710ed589a772e62b9581b343","geetest":"captcha","lang":"zh","ep":"123","biht":"1426265548","gee_guard":{"roe":{"aup":"3","sep":"3","egp":"3","auh":"3","rew":"3","snh":"3","res":"3","cdc":"3"}},"rw0k":"cpej","4d98":{"a0b9ec":{"b8ef":"9ec485da"}},"em":{"ph":0,"cp":0,"ek":"11","wd":1,"nt":0,"si":0,"sc":0}}'
key = '206a92ae1694ec71'
iv = "0000000000000000"



// 将WordArray对象转换为字节数组
function wordArrayToByteArray(wordArray) {
    let byteArray = [];
    for (let i = 0; i < wordArray.words.length; i++) {
        let word = wordArray.words[i];
        // 将32位整数拆分为4个字节，并添加到字节数组中
        for (let byte = 0; byte < 4; byte++) {
            byteArray.push((word >>> (byte * 8)) & 0xff);
        }
    }
    return byteArray;
}

// 定义加密函数
function encrypt(text, key, iv) {
    // 使用 CryptoJS 的 AES/CBC 模式进行加密
    const encrypted = CryptoJS.AES.encrypt(text, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });

    // 调用 arrayToHex 函数将数组转换为十六进制字符串
    return encrypted;
}
const encrypted = encrypt(data, key, iv);
const encryptedByteArray = wordArrayToByteArray(encrypted.ciphertext);
console.log("Encrypted byte array:", encryptedByteArray);

