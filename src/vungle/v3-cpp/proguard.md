### 使用 Proguard （release模式下可选）
* 编辑 `project.properties` 文件， 指定一个 `Proguard` 配置文件。比如：

```
proguard.config=proguard.cfg
```

* 编辑这个配置文件，加入如下内容：
```
-dontwarn com.vungle.**
-keep class com.vungle.** { public *; }
-keep class javax.inject.*
```
__Note:__ Proguard 只能工作在 __Release__ 模式下 （比如： `cocos run -m release`） debug 模式下不会触发 Proguard。
