import frida
import sys
# 连接手机设备
rdev = frida.get_remote_device()

# 包名：com.che168.autotradercloud
# 车智赢+
session = rdev.attach("车智赢+")
scr = """
Java.perform(function () {

    var AHAPIHelper = Java.use("com.autohome.ahkit.AHAPIHelper");

    //替换类中的方法
    AHAPIHelper.getDesKey.implementation = function(contxt){
        var res = this.getDesKey(context);
        console.log("res:::",res);
        return res;
    }
});
"""

script = session.create_script(scr)

def on_message(message, data):
    print(message, data)

script.on("message", on_message)
script.load()
sys.stdin.read()

'''
固定值：appapiche168comappapiche168comap
'''