# 需要清空数据
import frida
import sys

rdev = frida.get_remote_device()
pid = rdev.spawn(["tv.danmaku.bili"])
session = rdev.attach(pid)

scr = """
Java.perform(function () {
    var MiscHelperKt = Java.use("com.bilibili.lib.biliid.utils.MiscHelperKt");
    var ByteString = Java.use("com.android.okhttp.okio.ByteString");


    MiscHelperKt.a.implementation = function(bArr){
        console.log('------------------------------');
       console.log("bArr=",JSON.stringify(bArr));
       console.log("bArr=",ByteString.of(bArr).hex());  // 16进制显示  
       var res = this.a(bArr);
       console.log("返回值=",res);
       return res;
    }
});
"""
script = session.create_script(scr)


def on_message(message, data):
    print(message, data)


script.on("message", on_message)
script.load()
rdev.resume(pid)
sys.stdin.read()
