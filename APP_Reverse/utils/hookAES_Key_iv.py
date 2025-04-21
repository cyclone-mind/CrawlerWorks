
import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("哔哩哔哩")

scr = """
Java.perform(function () {
    var ByteString = Java.use("com.android.okhttp.okio.ByteString");

    var SecretKeySpec = Java.use("javax.crypto.spec.SecretKeySpec");
    SecretKeySpec.$init.overload('[B', 'java.lang.String').implementation = function(key,name){
        console.log("AES::");
        console.log("key===",ByteString.of(key).utf8());
        console.log("name===",name);

        var res = this.$init(key,name);
        return res;
    };

    var IvParameterSpec = Java.use("javax.crypto.spec.IvParameterSpec");
    IvParameterSpec.$init.overload('[B').implementation = function(iv){
        console.log("iv===",ByteString.of(iv).utf8());
        var res = this.$init(iv);
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