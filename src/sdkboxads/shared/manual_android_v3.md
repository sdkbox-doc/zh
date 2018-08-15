### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到您的工程的 __proj.android/libs__ 目录。

> PluginSdkboxAds.jar

> sdkbox.jar


<<[../../shared/copy_jars.md]

从 `plugin/android/libs` 目录下拷贝 `sdkboxads_lib` 目录到您的 `proj.android/libs/` 目录下。

<<[../../shared/copy_jni_lib.md]


### 编辑 `AndroidManifest.xml`
在标签 __application tag__ 上添加下列权限：
```xml
  <uses-permission android:name="android.permission.INTERNET" />
```

### 编辑 `Android.mk`
编辑 `proj.android/jni/Android.mk`：

为 __LOCAL_WHOLE_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_WHOLE_STATIC_LIBRARIES += PluginSdkboxAds
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginsdkboxads)
```

这意味着您的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginsdkboxads)
```

  __Note:__ 如果您使用的是 cocos2d-x 预编译库，那么保证这些语句在已有的 `$(call import-module,./prebuilt-mk)` 语句之上非常重要。

### 编辑 `Application.mk` （只限 Cocos2d-x v3.0 到 v3.2 版本）
编辑 `proj.android/jni/Application.mk` 保证 __APP_STL__ 的定义正确。如果 `Application.mk` 包含了 `APP_STL := c++_static` 语句，那么这条语句应该被改为：
```
APP_STL := gnustl_static
```


### 重要事项

对于每一个 AdUnit 您必须添加以下文件：

JNI ： 每一个 AdUnit 的 JNI 库文件。

Manifest： 每一个 AdUnit 插件的所有 Manifest 文件的改动。

__jar__： Jar文件对于被包含的 AdUnit 来说是必须的。基本所有的在插件 lib 目录下的 jar 文件都需要。


为项 __LOCAL_WHOLE_STATIC_LIBRARIES__ 针对每一个 Adunit 添加库, 比如：

```
LOCAL_WHOLE_STATIC_LIBRARIES += pluginvungle
LOCAL_WHOLE_STATIC_LIBRARIES += pluginadcolony
```

为每一个 AdUnit 添加 Android.mk 中的 __import-module__ 项，比如：

```
$(call import-module, ./pluginadcolony)
$(call import-module, ./pluginvungle)
```
