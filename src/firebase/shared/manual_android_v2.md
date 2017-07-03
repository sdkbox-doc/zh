## Android 平台手动集成

### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到您的工程的 __proj.android/libs__ 目录。

> sdkbox-firebase.jar

> android-support-v4.jar

> PluginFirebase.jar

> sdkbox.jar

<<[../../shared/copy_jni_lib.md]


### 编辑 `AndroidManifest.xml`
* 在标签 __application tag__ 上添加下列权限：

```xml
<uses-permission android:name="android.permission.INTERNET"/>
```

* 在标签 __application tag__ 上添加一下元数据:

```xml
<!--Required for Google Play Services-->

<meta-data android:name="com.google.android.gms.version"
            android:value="@integer/google_play_services_version"/>
```

### 编辑 `Android.mk`
编辑 `proj.android/jni/Android.mk` :

为 __LOCAL_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_WHOLE_STATIC_LIBRARIES += PluginFirebase
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginfirebase)
```

这意味着您的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginfirebase)
```

### 编辑 `Aplication.mk`
编辑 `proj.android/jni/Application.mk` to:

为 __APP_PATFORM__ 添加版本：
```
APP_PLATFORM := android-14
```
