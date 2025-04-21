import frida
import sys

rdev = frida.get_remote_device()
pid = rdev.spawn(["tv.danmaku.bili"])
session = rdev.attach(pid)

scr = """
Java.perform(function () {
    var a = Java.use("com.bilibili.okretro.f.a");

    a.e.implementation = function(aVar){   
       console.log("aVar=",aVar);
       console.log("aVar=",JSON.stringify(aVar));
       this.e(aVar);
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

# 确定 e走了---》找到的buvid的位置是正确的