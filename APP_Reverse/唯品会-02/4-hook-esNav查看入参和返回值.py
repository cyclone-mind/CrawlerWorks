# 清除数据，重新运行--如果清除数据运行--》hook不到--》重装app
# 不要忘了删除so文件--》frida检测的so文件
import frida
import sys

rdev = frida.get_remote_device()

session = rdev.attach("唯品会")

scr = """
Java.perform(function () {
    var KeyInfo = Java.use("com.vip.vcsp.KeyInfo");

    KeyInfo.esNav.implementation = function (ctx, str, str2,str3, i10) {
        console.log("-----------------esNav-----------------");
        console.log("参数str==>", str);
        console.log("参数str2==>", str2);
        console.log("参数str3==>", str3);
        console.log("参数i10==>", i10);
        var res = this.esNav(ctx, str, str2,str3, i10);
        console.log("返回的值==>", res);
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
参数str==> app_name=shop_android&app_version=7.83.3&client_type=android&dinfo=%7B%22ah1%22%3A%22%22%2C%22ah2%22%3A%22%22%2C%22ah3%22%3A%22%22%2C%22ah4%22%3A%22wifi%22%2C%22ah5%22%3A%221440_2712%22%2C%22ah6%22%3A1900800%2C%22ah7%22%3A8%2C%22ah8%22%3A3839954944%2C%22ah9%22%3A%22Pixel+2+XL%22%2C%22ah10%22%3A%22%22%2C%22ah11%22%3A%22%22%2C%22ah12%22%3A%22%22%2C%22ah13%22%3A%22%22%2C%22as1%22%3A%2211%22%2C%22as2%22%3A%22%22%2C%22as3%22%3A%22%22%2C%22as4%22%3A%22a9c275b871beaa7e%22%2C%22as5%22%3A%22%22%2C%22as6%22%3A%22%22%2C%22as7%22%3A%2230%22%2C%22ac1%22%3A%22ce6f1b65-2456-3f07-b539-1406906ae6e2%22%7D&mars_cid=ce6f1b65-2456-3f07-b539-1406906ae6e2&phone_model=Pixel+2+XL&session_id=ce6f1b65-2456-3f07-b539-1406906ae6e2_shop_android_1763728964037&sys_version=30&vcspKey=4d9e524ad536c03ff203787cf0dfcd29&vcspToken=NGQ5ZTUyNGFkNTM2YzAzZmYyMDM3ODdjZjBkZmNkMjl8fHwxNzY2MzIwOTYyfHx8.1df4a23528cd19db5493196f9d03c037
参数str2==> null
参数str3==> null
参数i10==> 0
返回的值==> ODI0M2E0MzA0NjJkNWU0OC4aV7pdYnvTt4D0BUFIo93wbKrdA4p9/Adj0d0dvqCRTj0eA6Kgny5/BZ2FFrF81N5lfrhsn/XmBtJMpchL0tQG017bbSj6DW3SmobasT3Bhv85X2w1L9pqm9cng62dBRnD+ch7qEkWVzSXJZqs5f6dYZV+02pdtGb01jvdK/5vHjF/0b4ZaOQC0vCEgRlkkrM+mzCpG/kFL8QjgARHjUknTtwjtnhOujN1PgUcyj5ZwZzPB+SdQ7HnHxnW5bl6FVGNLqmVCdbO15nvw/vy8tw7UwUTcDlBEY9k1+U9uWFXfqcDffw4Q9Gcj2Pii3Yn9dX9cAbKAKQnNdnspIajfehj42ldB/BUUNuax11s2IiaM/4UicYd5uflq8p0+G0pWqokdsCnIpPS70fH7dkI07V6LUER4jB60c03+M3XVw6W89arpnLO7g79J3nSFk8DiJjHEtE6mfH7AVSnfc/W3+bZEJ3v6R1jRTpxS6JyA1SlyBQx3MhPPeTMJzIa+dCIt2fsChp+9Ui/6N2UoPSiPxL3axFBTlOX9UupthRY0cSa9vOi2VmjhB3o7QLC6dhjIR72hLNA2/6WtAQ5e0kwYQy0L/shEL5wJguo/wNME6BxljDsPYKU1PWNo3wMUFesA18a0/gfBCr/vx22uNcaYzf+NFg6QQ77+oY2tCOcbEdZXSGbe0zuBpfTiO9+Aw/k4gN4yCf/DrWESdVrxJQKVnj5f7cNPAUvHSkdIJRePrBQ7CsDq6VXd+DksiMeHh8gIAKuGApHKer4Uqh0Fv7IZ6HekJDAI12Of/afoFemI3Zm3VgJwvvJNGxFloiJZkEO2SUn0Oo/AvBvohpXJAKE+Ig0FWYkxDqtrOhMqeL+gu/tDgNoUIMcyS+VARo8dAc95a8LNp5dWAtP3VbWiOseF11TPaDlfMq0pyLhQKak9iZD2cPtRyTGhgsh6uSalZ1Boo9XnRYzf4hA/gWABigZdqpu55LsKzhedbRlU5ige0cWmjQzGIREGjLsWyCHxb2JI6gZ0aI2jdfsnRyD8xzyd9FtXiYLuLquPFqIHvmS5lqy5vtvnVp5uo1ZcQYok7aXi2xKzEsVviTEcLDVLBX1NPMs5qmo5old+hRJL3F0ZWfe9TZLFIKZohpAgxYwZYwZLmWcV292Pw/udXJSGhxEmLFBxOPhAkhGR8WveV0OJuGko3J3YD4IcqnXss4vrgFKIg==

'''