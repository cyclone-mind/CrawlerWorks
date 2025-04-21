import frida
import sys
# 连接手机设备
rdev = frida.get_remote_device()

# 包名：com.che168.autotradercloud
# 车智赢+
session = rdev.attach("车智赢+")
scr = """
Java.perform(function () {

    var LaunchModel = Java.use("com.che168.autotradercloud.launch.model");

    //替换类中的方法
    LaunchModel.lambda$initRequestCommonParams$0.implementation = function(i, treeMap){
        console.log("i:::",str);
        console.log("treeMap:::",treeMap.toString());
        var res = this.lambda$initRequestCommonParams$0(i,treeMap);
        console.log("res:::",restoString());
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
执行了，参数： {pwd=fcea920f7412b5da7be0cf42b8c93759, signkey=, type=, username=18523654211}
执行了，参数： {
 _appid=atc.android, 

 appversion=3.77.1,
 channelid=csy, 
 pwd=fcea920f7412b5da7be0cf42b8c93759,
 signkey=, 
 type=, 
 udid=TqQL7FHOY40ZuoW+03VGhQ+TP8TxLur7/pTOUbwRUxTQMCNdkQ5Sslyfcosq I9XDlv5mKQyv7/8X8fXMjSLxMw==, 
 username=18523654211}
'''