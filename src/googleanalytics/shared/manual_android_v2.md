## Android 平台手动集成

### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到你的工程的 __proj.android/libs__ 目录。

> PluginGoogleAnalytics.jar

> sdkbox.jar

从 `plugin/android/jni` 目录拷贝 `plugingoogleanalytics` 以及 `sdkbox` 目录到你的工程的 `proj.android/jni` 目录。如果 `sdkbox` 目录在工程中已经存在，请覆盖它。

### 编辑 `AndroidManifest.xml`
在标签 __application tag__ 上添加下列权限：
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
```

使 __hardware acceleration__ 属性生效。这一标签是一个在新版本 sdk 上的选项，不能用于2.3.3版本。
```xml
<android:hardwareAccelerated="true" />
```

还有一些必要的元数据标签需要添加：
```xml
<meta-data android:name="com.google.android.gms.version"
    android:value="@integer/google_play_services_version" />
<meta-data
    android:name="com.google.android.gms.analytics.globalConfigResource"
    android:resource="@xml/global_tracker" />
```

### 编辑元数据文件
在上面的步骤中，会指定一个名为 `global_tracker.xml` 的文件。这个文件必须放在 `proj.android/res/xml/` 目录下，并包含一些必要的设置。如下：
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <integer name="ga_dispatchPeriod">300</integer>
    <string name="ga_logLevel">verbose</string>
</resources>
```

### 编辑 `Android.mk`
编辑 `proj.android/jni/Android.mk`：

为 __LOCAL_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_STATIC_LIBRARIES += PluginGoogleAnalytics
LOCAL_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./plugingoogleanalytics)
```

这意味着你的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./plugingoogleanalytics)
```

### 编辑 `Application.mk`
编辑 `proj.android/jni/Application.mk`：

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-9
```
