## Android 平台手动集成

### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到您的工程的 __proj.android/libs__ 目录。

> adcolony.jar

> PluginAdColony.jar

> sdkbox.jar

从 `plugin/android/jni` 目录拷贝 `PluginAdColony` 以及 `sdkbox` 目录到您的工程的 `proj.android/jni` 目录。如果 `sdkbox` 目录在工程中已经存在，请覆盖它。

### 编辑 `AndroidManifest.xml`
在标签 __application tag__ 上添加下列权限：
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.VIBRATE" />
```

使 __hardware acceleration__ 属性生效。这一标签是一个在新版本 sdk 上的选项，不能用于2.3.3版本。
```xml
<android:hardwareAccelerated="true" />
```

在接近文件底部的位置，拷贝并且粘贴下列3个 activity 定义到 __application tags__ 标签结尾处。
```xml
<activity android:name="com.jirbo.adcolony.AdColonyOverlay"
	  android:configChanges="keyboardHidden|orientation"
	  android:theme="@android:style/Theme.Translucent.NoTitleBar.Fullscreen" />
<activity android:name="com.jirbo.adcolony.AdColonyFullscreen"
	  android:configChanges="keyboardHidden|orientation"
	  android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen" />
<activity android:name="com.jirbo.adcolony.AdColonyBrowser"
	  android:configChanges="keyboardHidden|orientation"
	  android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen" />
```

 __Note:__ 如果您的 app targets 版本低于 __API 13__，您可能需要从上面的 __activity tags__ 的 __configChanges__ 属性里删除 `screenSize` 。

### 编辑 `Android.mk`
编辑 `proj.android/jni/Android.mk`：

为 __LOCAL_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_STATIC_LIBRARIES += PluginAdColony
LOCAL_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginadcolony)
```
这意味着您的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginadcolony)
```

### 编辑 `Application.mk`
编辑 `proj.android/jni/Application.mk`：

为 __APP_PATFORM__ 添加版本：
```
APP_PLATFORM := android-9
```
