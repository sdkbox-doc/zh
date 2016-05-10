### Proguard (release, optional)
* 修改 `project.properties` 加入您的 `Proguard` 配置文件. 比如：
```
proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt
```

* 修改这个您的配置文件,并在其中加下以下代码：

```
# inmobi
-keep class com.inmobi.** { *; }
-dontwarn com.inmobi.**


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
```

 __注意:__ 混淆只在 __Release__ 模式下有效 (比如 `cocos run -m release`), 在 debug 模式下,不会调到混淆规则.
