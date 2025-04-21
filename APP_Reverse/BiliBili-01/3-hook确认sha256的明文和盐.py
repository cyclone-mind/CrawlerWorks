import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("哔哩哔哩")
scr = """
Java.perform(function () {
    var a = Java.use("com.bilibili.commons.m.a");
    var ByteString = Java.use("com.android.okhttp.okio.ByteString");
    a.g.implementation = function(bytes, bytes2){
        console.log("请求来了");
        console.log("明文：bytes=",ByteString.of(bytes).utf8());
        console.log("盐：bytes2=",ByteString.of(bytes2).utf8());

        var res = this.g(bytes, bytes2);
        console.log("签名后结果：sign=",res);

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