### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到您的工程的 __proj.android/libs__ 目录。

> PluginSdkboxAds.jar
> sdkbox.jar

从 `plugin/android/libs` 目录下拷贝 `sdkboxads_lib` 目录到您的 `proj.android/libs/` 目录下。


<<[../../shared/copy_jni_lib.md]

### 编辑 `AndroidManifest.xml`
在标签 __application tag__ 上添加下列权限：
```xml
<uses-permission android:name="android.permission.INTERNET" />
```

设置 __application tag__ 下的 __hardware acceleration__ 为真。这一选项在新版本的 sdk 上可以生效，但不适用于 2.3.3的 cocos2d-x 版本。
```xml
<android:hardwareAccelerated="true" />
```

### 编辑 `Android.mk`
编辑 `proj.android/jni/Android.mk`：

为 __LOCAL_WHOLE_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
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

### 编辑 `Application.mk`
编辑 `proj.android/jni/Application.mk`：

为 __APP_PATFORM__ 添加版本：
```
APP_PLATFORM := android-10
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
