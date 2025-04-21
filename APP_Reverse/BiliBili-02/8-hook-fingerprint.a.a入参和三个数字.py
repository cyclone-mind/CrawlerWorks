import frida
import sys
from frida.core import Device

rdev = frida.get_remote_device()
session = rdev.attach("哔哩哔哩")

scr = """
Java.perform(function () {
    var a = Java.use("com.bilibili.lib.biliid.internal.fingerprint.a.a");
    a.b.implementation = function(str){   
       console.log("参数=",str);
       var res = this.b(str);
       console.log("结果=",res);
       return res;
    }

    var q = Java.use("kotlin.g0.q");
    q.S0.implementation = function(iVar,i ){   
       var res = this.S0(iVar,i);
       console.log('g=',res.g());
       console.log('h=',res.h());
       console.log('i=',res.i());
       return res;
    }

});
"""
script = session.create_script(scr)

script.load()
sys.stdin.read()

# g=0
# h=60
# i=2

'''之前hook到的
参数= a2d2ceff7d22f8fe4167e9cf389e88ed2023032317424507d8304083431dd8
g= 0
h= 60
i= 2
结果= 92

'''