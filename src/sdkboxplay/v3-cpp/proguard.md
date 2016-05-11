## 使用 Proguard （release模式下可选）
* 编辑 `project.properties` 文件， 指定一个 `Proguard` 配置文件。比如：
```
proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt
```

只要有需要，您可以使用任何 Google Play 的混淆配置文件。
默认的混淆配置如下：

```
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
```

__Note:__ Proguard 只能工作在 __Release__ 模式下 （比如： `cocos run -m release`） debug 模式下不会触发 Proguard 。
