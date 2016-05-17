## Android 手动集成步骤.

### 拷贝文件
从安装包中的 `plugin/android/libs` 文件夹下拷贝下面的 __jar__ 文件到您的工程中的 __proj.android/libs__ 文件夹.

> PluginReview.jar

> sdkbox.jar


* 如果您用的是 cocos2d-x源码 工程, 拷贝 __jar__ 文件到这里:

  ```
  cocos2d/cocos/platform/android/java/libs
  ```

* 如果您用的是 cocos2d-js 或 lua, 拷贝 __jar__ 文件到这里:

  ```
  frameworks/cocos2d-x/cocos/platform/android/java/libs
  ```

* 如果您用的是预编译的 cocos2d-x ，那拷贝 __jar__ 到这里:

  ```
  proj.android/libs
  ```

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

  __注意:__ 如果您使用预编译包, 必须要保证这些修改是在 `$(call import-module,./prebuilt-mk)` 这一项之前.

### 修改 `Application.mk` (只有Cocos2d-x v3.0 到 v3.2 版本需要)
编辑 `proj.android/jni/Application.mk` 确保 __APP_STL__ 定义正确. 如果 `Application.mk` 中包含 `APP_STL := c++_static`, 那么把它修改为:
```
APP_STL := gnustl_static
```
