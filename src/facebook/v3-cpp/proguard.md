### 混淆 (release模式下可选)
* 编辑 `project.properties` 指定 `Proguard` 到一个配置文件. 比如:
```
proguard.config=proguard.cfg
```

* 编辑这个配置文件,包含以下内容:
```
-libraryjars libs/facebook_lib/libs/android-support-v4.jar

-keep class * extends java.util.ListResourceBundle {
    protected Object[][] getContents();
}
```
 __注意:__ 混淆只在 __Release__ 模式下有效 (比如 `cocos run -m release`), 在 debug 模式下,不会调到混淆规则.
