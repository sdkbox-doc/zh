## 使用 Proguard （release模式下可选）
* 编辑 `project.properties` 文件， 指定一个 `Proguard` 配置文件。比如：
```
proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt
```

* 编辑这个配置文件加入每一个 AdUnit 在使用混淆时所需要的配置内容。

__Note:__ Proguard 只能工作在 __Release__ 模式下 （比如： `cocos run -m release`） debug 模式下不会触发 Proguard 。
