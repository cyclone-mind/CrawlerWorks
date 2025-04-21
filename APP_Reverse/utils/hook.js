// 代码 hook.js
/*
* attach 方式，先启动app，然后再在已经激活的 python 环境 终端执行：
*           frida -UF -l hook.js
* spawn 方式，脚本自动重启APP并进行Hook，终端执行
*           frida -U -f com.che168.autotradercloud -l hook.js
*           注意：输入q + 再点击回车则退出
* */

// --------------------------------------------一、基础的 hook   --------------------------------------------------------
Java.perform(function () {
    // 包.类
    var SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");
    SecurityUtil.encodeMD5.implementation = function(str){
        console.log("明文：",str);
        var res = this.encodeMD5(str);
        console.log("md5加密结果=",res);
        return "305eb636-eb15-4e24-a29d-9fd60fbc91bf";
    }
});

// -------------------------------------------- 二、Hook OkHttp --------------------------------------------
Java.perform(function () {
    console.log("[*] Starting script to hook OkHttp.enqueue...");

    try {
        // 目标类：okhttp3.Call
        var Call = Java.use("okhttp3.Call");

        // 获取 Call 的实现类 RealCall
        var RealCall = Java.use("okhttp3.RealCall");

        // Hook RealCall 的 enqueue 方法
        RealCall.enqueue.overload('okhttp3.Callback').implementation = function (callback) {
            console.log("\n[+] OkHttp.enqueue() called!");

            // --- 打印请求信息 ---
            var request = this.request();
            console.log("    - URL: " + request.url().toString());
            console.log("    - Method: " + request.method());

            // 检查是否是我们关心的 URL
            if (request.url().toString().includes("/x/report/heartbeat/mobile")) {
                console.log("    [!] Found target request: /x/report/heartbeat/mobile");

                // --- 打印 Form 表单内容 ---
                var requestBody = request.body();
                if (requestBody) {
                    // 尝试转换为 FormBody 来打印字段
                    var FormBody = Java.use("okhttp3.FormBody");
                    if (requestBody instanceof FormBody) {
                        console.log("    - Form Body:");
                        var formBody = Java.cast(requestBody, FormBody);
                        for (var i = 0; i < formBody.size(); i++) {
                            console.log("      * " + formBody.encodedName(i) + " = " + formBody.encodedValue(i));
                        }
                    }
                }

                // --- 打印调用栈 ---
                console.log("    --- Java Stack Trace ---");
                // 使用 Android 的 Log 工具类获取格式化的调用栈
                var Log = Java.use("android.util.Log");
                var stackTrace = Log.getStackTraceString(Java.use("java.lang.Exception").$new());
                console.log(stackTrace);
                console.log("    --- End of Stack Trace ---");
            }

            // 调用原始方法，让请求继续执行
            return this.enqueue(callback);
        };

        console.log("[*] Hooking okhttp3.RealCall.enqueue() successful.");

    } catch (error) {
        console.error("[-] Error setting up hook: " + error);
    }
});

// -------------------------------------------- 三、hook NewStringUTF --------------------------------------------
// hooks NewStringUTF 这个 so文件中 方法   想hook--》c返回给java字符串--》都可以使用
// 执行命令 frida -UF  -l  5-通用hook-NewStringUTF脚本.js -o v1.txt，在v1.txt中查看
//1 加载安卓手机底层包，系统自带的库，我们hook的 NewStringUTF 在这个包中
var symbols = Module.enumerateSymbolsSync("libart.so");
//2 定义一个变量，用来接收一会找到的NewStringUTF的地址
var addrNewStringUTF = null;
//3 循环找出libart.so中所有成员，匹配是NewStringUTF的函数，取出地址，赋值给上面的变量
for (var i = 0; i < symbols.length; i++) {
    //3.1 取出libart.so的一个个方法对象
    var symbol = symbols[i];
    //3.2 判断方法对象的名字是不是包含 NewStringUTF和CheckJNI---》因为在真正底层，函数名不叫NewStringUTF，前后有别的字符串
    // 实际它真正的名字：asdfa_NewStringUTF_dadsfasfd
    if (symbol.name.indexOf("NewStringUTF") >= 0 && symbol.name.indexOf("CheckJNI") < 0) {
        // 3.3 找到后，把地址赋值个上面的变量
        addrNewStringUTF = symbol.address;
        // 3.4 控制台打印一下
        console.log("NewStringUTF is at ", symbol.address, symbol.name);
        // 0xecb57cb5 _ZN3art3JNIILb0EE12NewStringUTFEP7_JNIEnvPKc
        // 可能会找到多个--》一般用找到的第一个就可以，如果你们代码不可以，把break去掉，使用最后一个
        break
    }
}
// 4 如果不为空，我们开始hook它(通过地址hook，有onEnter和onExit，所有的参数都给了args，通过位置取到每个参数)
if (addrNewStringUTF != null) {
    Interceptor.attach(addrNewStringUTF, {
        onEnter: function (args) {
            // 4.1 取出NewStringUTF传入的第一个参数,是字符串
            // return (*env)->NewStringUTF(env,info);
            var c_string = args[1];
            // 4.2 第一个参数是c的字符串，我们把它转一下，变成真正的字符串
            var dataString = c_string.readCString();
            // 4.3 改字符串不为空，且长度为32，我们输出一下，并且打印出它的调用栈
            if (dataString) {
                if (dataString.length === 32) {
                    console.log(dataString);
                    // 4.4 读取当前在执行那个so文件,及so文件中的地址
                    console.log(Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\n') + '\n');
                    // 4.5 打印调用栈
                    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
                }
            }

        }
    });
}


// -------------------------------------------- 三、延迟 hook  --------------------------------------------
// 实时打印 正在加载的 so 文件，待加载到目标 so 文件后，开始 hook
function do_hook() {
	setTimeout(function(){
        var addr = Module.findExportByName("libkeyinfo.so", "getByteHash");
        Interceptor.attach(addr, {
            onEnter: function (args) {
                this.x1 = args[2];
            },
            onLeave: function (retval) {
                console.log("-------参数和返回值-------------")
                console.log(Memory.readCString(this.x1));
                console.log(Memory.readCString(retval));
            }
        })
     },10);

}

function load_so_and_hook() {
    var dlopen = Module.findExportByName(null, "dlopen");
    var android_dlopen_ext = Module.findExportByName(null, "android_dlopen_ext");

    Interceptor.attach(dlopen, {
        onEnter: function (args) {
            var path_ptr = args[0];
            var path = ptr(path_ptr).readCString();
            // console.log("[dlopen:]", path);
            this.path = path;
        }, onLeave: function (retval) {
            if (this.path.indexOf("libkeyinfo.so") !== -1) {
                console.log("[dlopen:]", this.path);
                do_hook();

            }
        }
    });

    Interceptor.attach(android_dlopen_ext, {
        onEnter: function (args) {
            var path_ptr = args[0];
            var path = ptr(path_ptr).readCString();

            this.path = path;
        }, onLeave: function (retval) {
            if (this.path.indexOf("libkeyinfo.so") !== -1) {
                console.log("\nandroid_dlopen_ext加载：", this.path);
                do_hook();

            }
        }
    });
}

load_so_and_hook();

// spawn方案：frida -U -f com.achievo.vipshop -l 6-延迟hook-getByteHash-参数和返回值.js
// spawn-->应用重启---》一个个加载so--》当加载到libkeyinfo.so的时候，[延迟10毫秒]执行hook-getByteHash


