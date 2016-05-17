## Android 手动集成步骤.

### 拷贝文件
从安装包中的 `plugin/android/libs` 文件夹下拷贝下面的 __jar__ 文件到您的工程中的 __proj.android/libs__ 文件夹.

> ReviewLite.jar

> PluginReview.jar

> sdkbox.jar

从 `plugin/android/jni` 拷贝 `pluginreview` 和 `sdkbox` 目录到您的工程的 `proj.android/jni/` 目录.如果 `sdkbox` 目录已存在，覆盖它.

从 `plugin/android` 拷贝 `plugin_review_res_project` 到您工程中的 `proj.android`,同时让您的工程引用到 `plugin_review_res_project` 这个工程

### 编辑 `AndroidManifest.xml`
在 __application tag__ 这个项前面添加如下权限:
```xml
<uses-permission android:name="android.permission.INTERNET"/>
```

### 编辑 `Android.mk`
在 `proj.android/jni/Android.mk` 中:

给 __LOCAL_STATIC_LIBRARIES__ 添加如下要求:
```
LOCAL_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_STATIC_LIBRARIES += PluginReview
LOCAL_STATIC_LIBRARIES += sdkbox
```

在所有的 __import-module__ 项前，添加如下调用:
```
$(call import-add-path,$(LOCAL_PATH))
```

在所有的 __import-module__ 后，新增如下项:
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginreview)
```

修改后，应该和下面的修改类似:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginreview)
```

### 编辑 `Aplication.mk`
在 `proj.android/jni/Application.mk` 中:

添加 __APP_PATFORM__ 的版本要求:
```
APP_PLATFORM := android-9
```
