### Proguard (release, optional)
* 修改 `project.properties` 加入您的 `Proguard` 配置文件. 比如:
```
proguard.config=proguard.cfg
```

* 修改这个您的配置文件,并在其中加下以下代码:
```
-keep class com.chartboost.** { *; }
```
 __注意:__ 混淆只在 __Release__ 编译模式下有效 (i.e `cocos run -m release`) debug 编译下不会调用到混淆规则.
