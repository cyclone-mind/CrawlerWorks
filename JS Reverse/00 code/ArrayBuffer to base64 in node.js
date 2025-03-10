// 法一：通过String.fromCharCode方法
// 示例二进制数据（可以是任意二进制数据）
/*
const a = [72, 101, 108, 108, 111]; // 对应字符串 "Hello"

// 步骤 1：创建 Uint8Array
const uint8Array = new Uint8Array(a);

// 步骤 2：将 Uint8Array 转换为字符串
funtion unit8Array_to_char(p){
	let str = '';
	for (let i = 0; i < p.length; i++) {
	    str += String.fromCharCode(p[i]);
	}
	return str
}

str = unit8Array_to_char(uint8Array)

// 步骤 3：使用 btoa 方法将字符串转换为 Base64 编码
const base64String = btoa(str);

console.log(base64String); // 输出: "SWZtbXA="

// 法二：借助Bufffer类

// 示例大数组
const a = new Array(100000).fill(65); // 100,000 个 'A'

// 创建 Uint8Array
const uint8Array = new Uint8Array(a);

// 转换为 Buffer
const buffer = Buffer.from(uint8Array);

// 转换为 Base64
const s = buffer.toString('base64');

console.log(s.slice(0, 100) + '...'); // 输出前100个字符


*/
