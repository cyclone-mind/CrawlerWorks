import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("哔哩哔哩")

scr = """
Java.perform(function () {

    var d = Java.use("tv.danmaku.biliplayerimpl.report.heartbeat.d");
    var ByteString = Java.use("com.android.okhttp.okio.ByteString");
    d.H7.implementation = function(j2,  j4,  i2,  j5,  j6,  i3,  i4,  j7,  str,  i5,  str2,  str3){
        console.log("请求来了");
        var res = this.H7(j2,  j4,  i2,  j5,  j6,  i3,  i4,  j7,  str,  i5,  str2,  str3);

        console.log("字节数组", res);
        console.log("字节数组", JSON.stringify(res));

        console.log(ByteString.of(res).hex()); // 在hook时，直接把抓到的字符数组转成16进制
        console.log(ByteString.of(res).utf8());  //将字节转换成字符串

        return res;
    };

});
"""

script = session.create_script(scr)
def on_message(message, data):
    print(message, data)


script.on("message", on_message)

script.load()
sys.stdin.read()