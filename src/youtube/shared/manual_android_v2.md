## Android 平台手动集成

### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝所有 文件到你的工程的 __proj.android/libs__ 目录。

<<[../../shared/copy_jni_lib.md]


### 编辑 `AndroidManifest.xml`
在标签 __application tag__ 上添加下列权限：

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

### 编辑 `Android.mk`
编辑 `proj.android/jni/Android.mk`：

为 __LOCAL_WHOLE_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_WHOLE_STATIC_LIBRARIES += PluginYoutube
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginyoutube)
```

这意味着你的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginyoutube)
```

### 编辑 `Application.mk`
编辑 `proj.android/jni/Application.mk`：

为 __APP_PATFORM__ 添加版本：
```
APP_PLATFORM := android-9
```

### 添加 "Assets" 目录
编辑 `proj.android/build-cfg.json`

```json
    "copy_resources": [
        {
            "from": "../Resources",
            "to": ""
        },
        {
            "from": "plugin_youtube_res_project/Assets",
            "to": ""
        }
    ]
```
