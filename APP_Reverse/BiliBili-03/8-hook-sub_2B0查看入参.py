import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("哔哩哔哩")
scr = """
Java.perform(function () {

    var libbili = Module.findBaseAddress("libbili.so");
	// hook sub_22B0函数，通过偏移量找到 偏移量 22B0
	var s_func = libbili.add(0x22b0 + 1); // 32位的so文件都要 +1
    console.log(s_func);

    Interceptor.attach(s_func, {
        onEnter: function (args) {
            // args[0]
            // args[1]，明文字符串
            // args[2]，明文字符串长度

            console.log("执行update，长度是：",args[2], args[2].toInt32());

            // console.log( hexdump(args[1], {length: args[2].toInt32()})  );
            console.log(args[1].readUtf8String())
        },
        onLeave: function (args) {
            console.log("=======================结束===================");
        }
    });
});
"""
script = session.create_script(scr)
script.load()
sys.stdin.read()

'''

# 根据抓包的 aid--》定位到请求体参数是如下
access_key=&appkey=1d8b6e7d45233436&build=6240300&buvid=XX7F4F27A7D2A9F42FAAF7EDC024AB65C980E&c_locale=zh_CN&channel=xxl_gdt_wm_253&device=android&from_spmid=tm.recommend.0.0&install_apps=&mobi_app=android&oid=115328327621553&platform=android&s_locale=zh_CN&share_id=main.ugc-video-detail.0.0.pv&share_origin=vinfo_share&sid=32884919960&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.24.0%22%2C%22abtest%22%3A%22%22%7D&ts=1763129580
=======================结束===================
执行update，长度是： 0x8 8
560c52cc
=======================结束===================
执行update，长度是： 0x8 8
d288fed0
=======================结束===================
执行update，长度是： 0x8 8
45859ed1
=======================结束===================
执行update，长度是： 0x8 8
8bffd973


'''