## 使用 Proguard （release模式下可选）
* 编辑 `project.properties` 文件， 指定一个 `Proguard` 配置文件。比如：
```
proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt
```

* 编辑这个配置文件，加入如下内容：

```

# leadbolt
-dontwarn android.support.v4.**
-keep public class com.google.android.gms.* { public *; }
-dontwarn com.google.android.gms.**

-keep class com.apptracker.** { *; }
-dontwarn com.apptracker.**
-keepclassmembers class **.R$* {
    public static <fields>;
}
-keep class **.R$*


# cocos2d-x
-keep public class org.cocos2dx.** { *; }
-dontwarn org.cocos2dx.**
-keep public class com.chukong.** { *; }
-dontwarn com.chukong.**

#sdkbox
-keep public class com.sdkbox.** { *; }
-dontwarn com.sdkbox.**

```

__Note:__ Proguard 只能工作在 __Release__ 模式下 （比如： `cocos run -m release`） debug 模式下不会触发 Proguard 。
