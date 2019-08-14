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

# cocos2d-x
-keep public class org.cocos2dx.** { *; }
-dontwarn org.cocos2dx.**
-keep public class com.chukong.** { *; }
-dontwarn com.chukong.**

# google play service
-keep public class com.google.android.gms.** { public *; }
-dontwarn com.google.android.gms.**

-keep class com.google.protobuf.** { *; }
-dontwarn com.google.protobuf.**

-keep class * extends java.util.ListResourceBundle {
    protected Object[][] getContents();
}

-keep public class com.google.android.gms.common.internal.safeparcel.SafeParcelable {
    public static final *** NULL;
}

-keepnames @com.google.android.gms.common.annotation.KeepName class *
-keepclassmembernames class * {
    @com.google.android.gms.common.annotation.KeepName *;
}

-keepnames class * implements android.os.Parcelable {
    public static final ** CREATOR;
}

#sdkbox
-keep public class com.sdkbox.** { *; }
-dontwarn com.sdkbox.**

```
 __注意:__ 混淆只在 __Release__ 模式下有效 (例如 `cocos run -m release`) ,在 debug 模式下不会调用混淆配置文件.
