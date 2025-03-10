// 将复制的 Base64 字符串粘贴到此处
const base64Data = 'AQIDBAUGBwg=';

// 将 Base64 字符串转换回 Buffer
const buffer = Buffer.from(base64Data, 'base64');
console.log('Buffer:', buffer);

// 如果需要转换回 ArrayBuffer
const arrayBuffer = buffer.buffer.slice(buffer.byteOffset, buffer.byteOffset + buffer.byteLength);
console.log('ArrayBuffer:', arrayBuffer);
