import frida
import sys

rdev = frida.get_remote_device()
pid = rdev.spawn(["tv.danmaku.bili"])
session = rdev.attach(pid)

scr = """
Java.perform(function () {
    var a = Java.use("com.bilibili.api.a");

    a.o.implementation = function(arg0){   
       console.log("obj=",arg0);
       console.log("obj=",JSON.stringify(arg0));
       this.o(arg0);
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

'''
obj= [object Object]
obj= "<instance: com.bilibili.api.a$b, $className: tv.danmaku.bili.utils.p$a>"
0 & 表示类内部的接口或类
1 com.bilibili.api.a$b  对象的类型---》对象是个接口类型
2 tv.danmaku.bili.utils.p$a 真正的类是 a这个类
3 找到a类：tv.danmaku.bili.utils.p.a  搜索
public final class p {
    public static final class a implements a.b {
       public String getSessionId() {
            return com.bilibili.lib.foundation.e.b().getSessionId();
        }

 }
}
'''