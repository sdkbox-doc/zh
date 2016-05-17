### 混淆 (release, 可选)
* 编辑 `project.properties`,写入一个 `Proguard` 配置. Example:
```
proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt
```

* 编辑这个文件,填入以下内容：

```
# Fyber

-keep class com.fyber.** { *; }
-dontwarn com.fyber.**
-keep class com.sponsorpay.mediation.** { *;}
-keepattributes JavascriptInterface
-keep class com.sponsorpay.publisher.mbe.mediation.SPBrandEngageMediationJSInterface {
    void setValue(java.lang.String);
}
-keep class android.webkit.JavascriptInterface


# cocos2d-x
-keep public class org.cocos2dx.** { *; }
-dontwarn org.cocos2dx.**
-keep public class com.chukong.** { *; }
-dontwarn com.chukong.**

# google play service
-keep class com.google.android.gms.** { *; }
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
-keep class com.sdkbox.** { *; }
-dontwarn com.sdkbox.**
```

 __注意:__ 混淆只在 __Release__ 模式下有效 (比如 `cocos run -m release`), 在 debug 模式下,不会调到混淆规则.
