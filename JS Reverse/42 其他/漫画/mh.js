const fs = require("fs").promises;
const { Blob } = require("buffer");

class iL {
  async readAsArrayBuffer(e) {
    try {
      if (e instanceof Blob) {
        return await e.arrayBuffer();
      } else {
        const buffer = await fs.readFile(e);
        return buffer.buffer;
      }
    } catch (error) {
      throw new Error("Failed to read data.");
    }
  }
}
class i$ {
  static xor(e, t) {
    let n = new Uint8Array(e),
      { length: r } = n,
      { length: i } = t,
      s = new Uint8Array(r);
    for (let e = 0; e < r; e += 1) s[e] = n[e] ^ t[e % i];
    return s;
  }
  static generateKey(e) {
    let t = e.slice(0, 16).match(/[\da-f]{2}/gi);
    return new Uint8Array(t.map((e) => parseInt(e, 16)));
  }
  static decodeHashToArr(e) {
    let t = Buffer.from(e, "base64"),
      n = [];
    for (let e = 0; e < t.length; e += 1) n[e] = t[e];
    return n;
  }
  static async decodeURLToBlob(e, t) {
    let n = await I(e).then((e) => e.blob()),
      r = await new iL().readAsArrayBuffer(n);
    return new Blob([this.xor(r, this.generateKey(t))], {
      type: "image/jpeg",
    });
  }
}

let $ = fetch,
  D = (e) => {
    if (!e.ok)
      throw new L(e,"Network response was not ok.");
    return e;
  },
  I = async (...e) => $(...e).then(D);

iI = async (e) => {
  if (null != e.meta.drm_hash) {
    let t = await i$.decodeURLToBlob(e.meta.source_url, e.meta.drm_hash);
    // 将 Blob 转换为 Buffer 并保存到文件
    const buffer = Buffer.from(await t.arrayBuffer());
    const filename = `decrypted_${e.id}.jpg`;
    await fs.writeFile(filename, buffer);
    return filename;
  }
};

let data = {
  id: 10285844,
  meta: {
    resource: {
      bgm: null,
      se: null,
    },
    duration: 1,
    width: 650,
    height: 889,
    is_spread: false,
    source_url:
      "https://drm.cdn.nicomanga.jp/image/4b048448d946e0afc205b73dd76e2365d52ceeea_10089/16483464p.webp?1743145040",
    drm_hash: "4b048448d946e0afc205b73dd76e2365d52ceeea_10089",
    link_url: null,
  },
};

iI(data).then((e) => console.log(e));
