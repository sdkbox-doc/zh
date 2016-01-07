## Android 平台手动集成

### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到你的工程的 __proj.android/libs__ 目录。

> vungle-publisher-adaptive-id-3.3.0..jar

> PluginVungle.jar

> sdkbox.jar

> android-support-v4.jar

> nineoldandroids-2.4.0.jar

> javax.inject-1.jar

> dagger-1.2.2.jar

从 `plugin/android/jni` 目录拷贝 `pluginvungle` 以及 `sdkbox` 目录到你的工程的 `proj.android/jni` 目录。如果 `sdkbox` 目录在工程中已经存在，请覆盖它。

### 编辑 `AndroidManifest.xml`
在标签 __application tag__ 上添加下列权限：
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

在接近文件底部的位置，拷贝并且粘贴下列 activity 定义到 __application tags__ 标签结尾处。
```xml
<activity
  android:name="com.vungle.publisher.FullScreenAdActivity"
  android:configChanges="keyboardHidden|orientation"
  android:theme="@android:style/Theme.NoTitleBar.Fullscreen"/>
```

 __Note:__ 如果你的 app targets 版本低于 __API 13__，你可能需要从上面的 __activity tags__ 的 __configChanges__ 属性里删除 `screenSize` 。

### 编辑 `Android.mk`
编辑 `proj.android/jni/Android.mk`：

为 __LOCAL_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_STATIC_LIBRARIES += PluginVungle
LOCAL_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginvungle)
```

这意味着你的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginvungle)
```

### 编辑 `Application.mk`
编辑 `proj.android/jni/Application.mk`：

为 __APP_PATFORM__ 添加版本：
```
APP_PLATFORM := android-9
```
