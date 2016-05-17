### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到您的工程的 __proj.android/libs__ 目录。

> PluginFyber.jar

> sdkbox.jar

<<[../../shared/copy_jni_lib.md]


### 编辑 `AndroidManifest.xml`
在标签 __application tag__ 上添加下列权限：
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

使 __hardware acceleration__ 属性生效。这一标签是一个在新版本 sdk 上的选项，不能用于2.3.3版本。
```xml
<android:hardwareAccelerated="true" />
```

在接近文件底部的位置，拷贝并且粘贴下列定义到 __application tags__ 标签结尾处。
```xml
<activity
    android:name="com.fyber.ads.ofw.OfferWallActivity"
    android:configChanges="screenSize|orientation" />
<activity
    android:name="com.fyber.ads.videos.RewardedVideoActivity"
    android:configChanges="screenSize|orientation"
    android:hardwareAccelerated="true"
  android:theme="@android:style/Theme.Translucent" />
<activity
    android:name="com.fyber.ads.interstitials.InterstitialActivity"
    android:configChanges="screenSize|orientation"
    android:theme="@android:style/Theme.Translucent" />
<activity
    android:configChanges="screenSize|orientation"
    android:name="com.fyber.cache.CacheVideoDownloadService"
    android:hardwareAccelerated="true"/>
<service android:name="com.fyber.cache.CacheVideoDownloadService" android:exported="false" />
```

### 编辑 `Android.mk`
编辑 `proj.android/jni/Android.mk` :

为 __LOCAL_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_WHOLE_STATIC_LIBRARIES += PluginFyber
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginfyber)
```

这意味着您的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginfyber)
```

### 编辑 `Aplication.mk`
编辑 `proj.android/jni/Application.mk` :

为 __APP_PATFORM__ 添加版本：
```
APP_PLATFORM := android-14
```
