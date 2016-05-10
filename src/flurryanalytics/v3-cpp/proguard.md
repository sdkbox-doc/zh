### 混淆 (release, optional)
* 编辑 `project.properties` 指定一个 `Proguard` 配置文件. 比如:
```
proguard.config=proguard.cfg
```

* 编辑配置文件包含如下内容:
```
-dontwarn android.webkit.**
```
 __注意:__ 混淆只在 __Release__ 编译模式下有效 (i.e `cocos run -m release`) debug 编译下不会调用到混淆规则.
