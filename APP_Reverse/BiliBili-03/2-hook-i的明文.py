import frida
import sys
from frida.core import Device
rdev = frida.get_remote_device()
session = rdev.attach("哔哩哔哩")

scr = """
Java.perform(function () {
    var a = Java.use("com.bilibili.commons.m.a");

    a.i.implementation = function(str){   
       console.log("参数=",str); //
       var res = this.i(str);
       console.log("返回值=",res);// 抓包抓到的session
       return res;
    }

});
"""
script = session.create_script(scr)

script.load()
sys.stdin.read()