### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到您的工程的 __proj.android/libs__ 目录。

> PluginSdkboxPlay.jar

> sdkbox.jar


* 如果您使用 cocos2d-x 源码，拷贝 __jar__ 文件到：

	Android command-line:
	```
	cocos2d/cocos/platform/android/java/libs
	```

	Android Studio:
	```
	cocos2d/cocos/platform/android/libcocos2dx/libs
	```

* 如果您使用 cocos2d-js 或者 lua ，拷贝 __jar__ 文件到:

	Android command-line:
	```
	frameworks/cocos2d-x/cocos/platform/android/java/libs
	```

	Android Studio:
	```
	frameworks/cocos2d-x/cocos/platform/android/libcocos2dx/libs
	```

* 如果您使用 cocos2d-x 预编译包，拷贝 __jar__ 文件到：

	Android command-line:
	```
	proj.android/libs
	```

从 `plugin/android/libs` 目录下拷贝 `sdkboxads_lib` 目录到您的 `proj.android/libs/` 目录下。

<<[../../shared/copy_jni_lib.md]

### 编辑 `AndroidManifest.xml`
在标签 __application tag__ 上添加下列权限：
```xml
<uses-permission android:name="android.permission.GET_ACCOUNTS" />
```

设置 __application tag__ 下的 __hardware acceleration__ 为真。这一选项在新版本的 sdk 上可以生效，但不适用于 2.3.3的 cocos2d-x 版本。
```xml
<android:hardwareAccelerated="true" />
```

### 编辑 `Android.mk`
Edit `proj.android/jni/Android.mk` to:

为 __LOCAL_WHOLE_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_WHOLE_STATIC_LIBRARIES += PluginSdkboxPlay
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginsdkboxplay)
```

Add additional __import-module__ statements at the end:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginsdkboxplay)
```

### 编辑 `Application.mk`
编辑 `proj.android/jni/Application.mk`：

为 __APP_PATFORM__ 添加版本：
```
APP_PLATFORM := android-10
```

