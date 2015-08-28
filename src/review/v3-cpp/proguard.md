### 混淆 (release 模式有效, 可选)
* 编辑 `project.properties` 指定一个 `Proguard` 配制文件. 例如:
```
proguard.config=proguard.cfg
```

* 编辑这个文件,包含如下内容:
```
# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}
```
 __注意:__ 混淆只在 __Release__ 模式下有效 (例如 `cocos run -m release`) ,在 debug 模式下不会调用混淆配置文件.
