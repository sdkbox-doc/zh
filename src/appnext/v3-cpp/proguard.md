### 混淆 (release, 可选)
* 修改 `project.properties` 加入一个特定的 `Proguard` 配置文件. 比如:
```
proguard.config=proguard.cfg
```

* 编辑您特定的文件,以包含以下内容:
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

#appnext
-keep class com.appnext.** { *; }
-dontwarn com.appnext.**

```
 __注意:__ 混淆只在 __Release__ 编译模式下有效 (i.e `cocos run -m release`) debug 编译下不会调用到混淆规则。
