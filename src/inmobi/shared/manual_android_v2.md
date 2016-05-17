## Android 平台手动集成

### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到您的工程的 __proj.android/libs__ 目录。

> InMobi-5.1.0.jar

> PluginInMobi.jar

> sdkbox.jar

<<[../../shared/copy_jni_lib.md]


### 编辑 `AndroidManifest.xml`
* 在标签 __application tag__ 上添加下列权限：

```xml
<!--Mandatory permissions to receive ads-->
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

<!--Recommended permissions to receive brand‐centric ads with interactive functionality for better eCPMs-->
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>
<uses-permission android:name="android.permission.VIBRATE"/>
<uses-permission android:name="android.permission.RECORD_AUDIO"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="com.google.android.gms.permission.ACTIVITY_RECOGNITION"/>
<uses-permission android:name="android.permission.READ_CALENDAR"/>
<uses-permission android:name="android.permission.WRITE_CALENDAR"/>
<uses-permission android:name="android.permission.GET_TASKS"/>
```

* 在标签 __application tag__ 上添加一下元数据:

```xml
<!--Required Activity for rendering ads in the embedded browser-->
<activity android:name="com.inmobi.rendering.InMobiAdActivity"
            android:configChanges="keyboardHidden|orientation|keyboard|smallestScreenSize|screenSize"
            android:theme="@android:style/Theme.Translucent.NoTitleBar"
            android:hardwareAccelerated="true" />


<!--Required Receiver for enhanced targeting for better ads.-->

<receiver android:name="com.inmobi.commons.core.utilities.uid.ImIdShareBroadCastReceiver"
            android:enabled="true"
            android:exported="true" >
    <intent-filter>
       <action android:name="com.inmobi.share.id" />
    </intent-filter>
</receiver>

<service android:enabled="true" android:name="com.inmobi.signals.activityrecognition.ActivityRecognitionManager" />

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
LOCAL_WHOLE_STATIC_LIBRARIES += PluginInMobi
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./plugininmobi)
```

这意味着您的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./plugininmobi)
```

### 编辑 `Aplication.mk`
编辑 `proj.android/jni/Application.mk` to:

为 __APP_PATFORM__ 添加版本：
```
APP_PLATFORM := android-9
```
