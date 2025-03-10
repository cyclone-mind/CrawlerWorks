---
created: 2024-12-25T15:46:41 (UTC +08:00)
tags: [爬虫无限debug]
source: https://blog.csdn.net/qq_40558166/article/details/122428096
author: 成就一亿技术人!
---

# 爬虫从入门到精通(12) | js调试中的一些问题（无限debugger，调试干扰，内存爆破）_爬虫无限debug-CSDN博客

> ## Excerpt
> 文章浏览阅读3.9k次，点赞8次，收藏38次。无限debugger+调试干扰+内存爆破解决方案_爬虫无限debug

---
## 一、调试检测

### 1.无法打开f12

**解决方案：**

-   使用鼠标右键打开
-   更换其他浏览器，例如火狐浏览器

### 2.开发工具js干扰

**解决方案：**

打script[断点](https://so.csdn.net/so/search?q=%E6%96%AD%E7%82%B9&spm=1001.2101.3001.7020)找到检测点，重写该方法  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/13ff555cdd3af78245c9b5077d08106a.png)

## 二、内存爆破

-   内存爆破指js通过死循环/**频繁**操作数据库(包括cookie)/频繁调取history等方式，使浏览器崩溃的一种反调试手段。
-   还有一种特殊情况：js文件很大，电脑内存不足（这种情况在调试层面几乎无解）
-   同样的js代码，在浏览器可以运行，自己调试却内存疯长，大部分情况是检测到了代码格式化（利用正则/toString() 判断代码是否进行格式化），其他情况可能就是检测了浏览器的指纹，判断是否为浏览器环境

**解决是否判断js格式化的内存爆破**

如果是使用正则或者toString的方式检测代码格式化，那么我们在本地运行的时候，搜索`RegExp`，把可以项删除或者取反即可

## 三、无限debugger

### 1.js中创建debugger的常见方式

#### 1.1.直接创建debugger

```
debugger;
```

#### 1.2.通过eval关键字创建debugger

**此类为虚拟机中创建**

```
eval('debugger');
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/95c7932ca11839aa66dcc18d9d39e9ce.png)

#### 1.3.通过Function创建debugger

**此类为虚拟机中创建**

Function是创建匿名函数，然后去执行

```
Function('debugger').call()
Function('debugger').apply()
Function().constructor('debugger').apply('action')
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/20c444c84ea0ae2d797ec6273bc663c6.png)  
**大部分debugger都是这三种的变形或者叠加**

### 2.创建无限debugger

-   无限debugger是指很频繁的执行debugger逻辑，并不是死循环，这样会造成浏览器卡死。
-   常见的无限debugger就是通过上述三种方式变形，再配合定时器或者一个循环来创建的。

### 3.解决无限debugger

#### 3.1.Never pause here 不在此处下断

在 debugger 位置，点击行号，右键 Never pause here，永远不在此处断下即可：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/d60595c3380cb914c2b1c94ec466a4c9.png)

#### 3.2.Add conditional breakpoint 条件断点

**不适用于一直新开虚拟机的debugger**  
同样右键选择 Add conditional breakpoint，输入 false 即可跳过无限 debugger，其原理是添加条件断点，不管前面代码的逻辑是什么，运行到 debugger 的时候必定是 true 才能执行，只需要将其改为 false，那么它就不执行了：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/43ba409804a029008b6587979a634082.png)

#### 3.3.重写定时器debugger

setInterval这种我们可以通过hook，即重写或者置空的方式过掉

```
setInterval_back = setInterval;

setInterval = function(a,b){
if(a.toStirng().indexOf('debugger')!= -1){
return setInterval_back;
}
}
```

#### 3.4.重写constructor的debugger

基本搞Function的通用形式

```
Function.prototype.constructor_back= Function.prototype.constructor_back;

Function.prototype.constructor_back= function(a,b){
if(arguments==='debugger'){
}else{
// arguments由于不知道多少参数，所以用apply
return Function.prototype.constructor_back.apply(this,arguments);
}
}
```

#### 3.5.重写eval形式的debugger

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/529388ace180231ccf963c3035791c2a.png)

```
eval_back=eval
eval=function(a){
if (a==="debugger"){
}else{
return eval_back(a);
}
}
```

#### 3.6.中间人拦截替换无限debugger

**①简单的静态js可以使用浏览器替换**

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/cfa6a098b2242b57ee121ef7b74b80b7.png)  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/5568dcf76274f64a15a8888713b5e7c8.png)  
此时文件变为紫色，此时可以修改该文件，ctrl+s保存刷新可以生效  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/53d86db22cceab91a582e635783f68a2.png)

**②通过fiddler替换**

fiddler界面右屏幕的AutoResponseder配置好，然后将需要修改的文件拖过来，选择find a file，找到我们已经修改好的源码文件  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/bc357dd5865bef8c7c02e90075deb3e3.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/010dd0213433a3ed65ee888b90bbffc6.png)

#### 3.7.其他情况

如果上述方法失效，我们断到无限debugger的地方，向上找函数，把包含无限debugger的函数中的触发无限debugger的语句删掉即可。
