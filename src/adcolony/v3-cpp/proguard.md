### 混淆 (release, 可选)
* 编辑 `project.properties`,写入一个 `Proguard` 配置. Example:
```
proguard.config=proguard.cfg
```

* 编辑这个文件，加入如下内容:
```
-dontwarn android.webkit.**
```
 __注意:__ 混淆只在 __Release__ 模式下有效 (比如 `cocos run -m release`), 在 debug 模式下,不会调到混淆规则.
