### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到你的工程的 __proj.android/libs__ 目录。

> valuepotion.jar

> PluginValuePotion.jar

> sdkbox.jar


* 如果你使用 cocos2d-x 源码，拷贝 __jar__ 文件到：

	Android command-line:
	```
	cocos2d/cocos/platform/android/java/libs
	```

	Android Studio:
	```
	cocos2d/cocos/platform/android/libcocos2dx/libs
	```

* 如果你使用 cocos2d-js 或者 lua ，拷贝 __jar__ 文件到:

	Android command-line:
	```
	frameworks/cocos2d-x/cocos/platform/android/java/libs
	```

	Android Studio:
	```
	frameworks/cocos2d-x/cocos/platform/android/libcocos2dx/libs
	```

* 如果你使用 cocos2d-x 预编译包，拷贝 __jar__ 文件到：

	Android command-line:
	```
	proj.android/libs
	```

<<[../../shared/copy_jni_lib.md]


### 编辑 `AndroidManifest.xml`
在标签 __application tag__ 上添加下列权限：
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
```

在接近文件底部的位置，拷贝并且粘贴下列3个 activity 定义到 __application tags__ 标签结尾处。

```xml
<application>

......

<meta-data android:name="com.google.android.gms.version"
            android:value="@integer/google_play_services_version" />

<!-- Valuepotion Components -->
<!-- for interstital ad interface -->
<activity
        android:name="com.valuepotion.sdk.VPInterstitialActivity"
        android:theme="@android:style/Theme.Translucent" >
</activity>

<!-- for CPI tracking -->
<receiver
        android:name="com.valuepotion.sdk.VPInstallReceiver"
        android:exported="true" >
        <intent-filter>
                <action android:name="com.android.vending.INSTALL_REFERRER" />
        </intent-filter>
</receiver>
<!-- Valuepotion Components End -->

.....

</application>
```

### 编辑 `Android.mk`
编辑 `<project_root>/jni/Android.mk` :

为 __LOCAL_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_WHOLE_STATIC_LIBRARIES += PluginValuePotion
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginvaluepotion)
```

这意味着你的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginvaluepotion)
```

  __Note:__ 如果你使用的是 cocos2d-x 预编译库，那么保证这些语句在已有的 `$(call import-module,./prebuilt-mk)` 语句之上非常重要。

### 编辑 `Application.mk` （只限 Cocos2d-x v3.0 到 v3.2 版本）
编辑 `proj.android/jni/Application.mk` 保证 __APP_STL__ 的定义正确。如果 `Application.mk` 包含了 `APP_STL := c++_static` 语句，那么这条语句应该被改为：
```
APP_STL := gnustl_static
```
