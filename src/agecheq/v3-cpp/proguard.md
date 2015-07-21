### 混淆 (release, 可选)
* 修改 `project.properties` 加入一个特定的 `Proguard` 配置文件. 比如:
```
proguard.config=proguard.cfg
```

* 编辑你特定的文件,以包含以下内容:
```
# 如果你的JS工程用到了WebView,不要注释下面的代码,并输入完全合法的 JavasSript 接口类名
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}
```
 __注意:__ 混淆只在 __Release__ 编译模式下有效 (i.e `cocos run -m release`) debug 编译下不会调用到混淆规则.
