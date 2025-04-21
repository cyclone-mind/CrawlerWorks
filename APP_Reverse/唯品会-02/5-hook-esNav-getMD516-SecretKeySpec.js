/**
 * Java层Hook函数
 * 主要Hook KeyInfo.esNav方法和SecretKeySpec构造函数
 */
function java_hook() {
    Java.perform(function () {
        // Hook KeyInfo.esNav 方法
        var KeyInfo = Java.use("com.vip.vcsp.KeyInfo");
        KeyInfo.esNav.implementation = function (ctx, str, str2, str3, i10) {
            console.log("=================================================");
            console.log("[Java] Hook KeyInfo.esNav");
            console.log("-------------------------------------------------");
            console.log("输入参数 str:", str);
            var res = this.esNav(ctx, str, str2, str3, i10);
            // esNav方法内部会调用getMD516，进而调用new SecretKeySpec
            console.log("返回结果:", res);
            console.log("=================================================\n");
            return res;
        };

        // Hook SecretKeySpec 构造函数
        var SecretKeySpec = Java.use("javax.crypto.spec.SecretKeySpec");
        var ByteString = Java.use("com.android.okhttp.okio.ByteString");
        SecretKeySpec.$init.overload('[B', 'java.lang.String').implementation = function (key, name) {
            if (name === 'AES') {
                console.log("=================================================");
                console.log("[Java] Hook SecretKeySpec.$init");
                console.log("-------------------------------------------------");
                //console.log("key bytes =", JSON.stringify(key));
                console.log("AES密钥(hex):", ByteString.of(key).hex());
                //console.log("key(string)", ByteString.of(key).utf8());
                console.log("=================================================\n");
            }
            var res = this.$init(key, name);
            return res;
        };
    });
}

/**
 * 延迟Hook函数
 * 等待指定so库加载完成后再执行Hook操作
 * @param {string} so_name - 需要监听加载的so库名称
 * @param {function} hook_func - Hook执行函数
 */
function delay_hook(so_name, hook_func) {
    var dlopen = Module.findExportByName(null, "dlopen");
    var android_dlopen_ext = Module.findExportByName(null, "android_dlopen_ext");

    // Hook dlopen 函数
    Interceptor.attach(dlopen, {
        onEnter: function (args) {
            var path_ptr = args[0];
            var path = ptr(path_ptr).readCString();
            // console.log("[dlopen] 加载:", path);
            this.path = path;
        }, 
        onLeave: function (retval) {
            if (this.path && this.path.indexOf(so_name) !== -1) {
                console.log("[dlopen] 加载完成:", this.path);
                hook_func();
            }
        }
    });

    // Hook android_dlopen_ext 函数
    Interceptor.attach(android_dlopen_ext, {
        onEnter: function (args) {
            var path_ptr = args[0];
            var path = ptr(path_ptr).readCString();
            this.path = path;
        },
        onLeave: function (retval) {
            if (this.path && this.path.indexOf(so_name) !== -1) {
                console.log("\n[android_dlopen_ext] 加载完成:", this.path);
                hook_func();
            }
        }
    });
}

/**
 * Native层Hook函数
 * Hook libkeyinfo.so库中的getMD516函数
 */
function so_hook() {
    var getMD516 = Module.findExportByName("libkeyinfo.so", "getMD516");
    console.log('[Native] getMD516 函数地址:', getMD516);

    if (getMD516) {
        Interceptor.attach(getMD516, {
            onEnter: function (args) {
                console.log("=================================================");
                console.log("[Native] Hook getMD516");
                console.log("-------------------------------------------------");
                console.log("输入参数(hex):\n" + hexdump(args[1], {length: args[2].toInt32()}));
                // console.log('输入参数2(hex):\n' + hexdump(args[1]));
                console.log("=================================================\n");
            },
            onLeave: function (retval) {
                // console.log('返回值(hex):\n' + hexdump(retval));
                console.log("=================================================");
                console.log("[Native] getMD516 返回值");
                console.log("-------------------------------------------------");
                console.log("返回结果(hex):\n" + hexdump(retval, {length: 16}));
                console.log("=================================================\n");
            }
        });
    }
}

// 等待libkeyinfo.so加载到内存后再开始hook
console.log("正在等待 libkeyinfo.so 加载...");
delay_hook("libkeyinfo.so", so_hook);
java_hook();

// 使用命令: frida -U -f com.achievo.vipshop -l 5-hook-esNav-getMD516-SecretKeySpec.js

