import frida
import sys
# 连接手机设备
rdev = frida.get_remote_device()

# 包名：com.che168.autotradercloud
# 车智赢+
session = rdev.attach("车智赢+")
scr = """
Java.perform(function () {
    // 找到类：根据包和类名
    var AHAPIHelper = Java.use("com.autohome.ahkit.AHAPIHelper");
    // Hook，替换
    AHAPIHelper.toSign.implementation = function(ctx,map1){
        // 执行原来的方法
        console.log("传入的参数为：",map1);
        var res = this.toSign(ctx,map1);
        console.log("返回值为：",res);
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