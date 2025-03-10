function arrayBufferToBase64(buffer) {
    let binary = '';
    const bytes = new Uint8Array(buffer);
    const len = bytes.byteLength;
    for (let i = 0; i < len; i++) {
        binary += String.fromCharCode(bytes[i]);
    }
    return window.btoa(binary);
}

// 示例 ArrayBuffer
const buffer = new ArrayBuffer(8);

const base64Data = arrayBufferToBase64(buffer);
console.log(base64Data); // 复制此输出
