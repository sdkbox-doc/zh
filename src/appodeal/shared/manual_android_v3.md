### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到你的工程的 __proj.android/libs__ 目录。

> PluginAppodeal.jar

> sdkbox.jar

> android-support-v4-22.2.1.jar

> applovin-sdk-6.0.1.jar

> appodeal-1.13.1.jar

> chartboost-5.2.0.jar

> my-target-4.0.13.jar

> unity-ads-1.4.7.jar


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
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

在接近文件底部的位置，拷贝并且粘贴下列定义到 __application tags__ 标签结尾处。
```xml
<meta-data android:name="com.appodeal.framework" android:value="android" />
<activity android:name="com.appodeal.ads.InterstitialActivity"
        android:configChanges="orientation|screenSize"
        android:theme="@android:style/Theme.Translucent.NoTitleBar" />
<activity android:name="com.appodeal.ads.VideoActivity"
        android:configChanges="orientation|screenSize"
        android:theme="@android:style/Theme.Translucent.NoTitleBar" />

<activity android:name="com.appodeal.ads.LoaderActivity"
        android:configChanges="orientation|screenSize"
        android:theme="@android:style/Theme.Translucent.NoTitleBar" />

<meta-data android:name="com.google.android.gms.version" android:value="@integer/google_play_services_version" />

<activity android:name="com.google.android.gms.ads.AdActivity"
        android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|uiMode|screenSize|smallestScreenSize"
        android:theme="@android:style/Theme.Translucent" />

<activity android:name="com.chartboost.sdk.CBImpressionActivity"
        android:theme="@android:style/Theme.Translucent"
        android:excludeFromRecents="true" />

<activity android:name="com.applovin.adview.AppLovinInterstitialActivity"
        android:theme="@android:style/Theme.Translucent" />

<activity android:name="com.mopub.mobileads.MoPubActivity"
        android:configChanges="keyboardHidden|orientation|screenSize"
        android:theme="@android:style/Theme.Translucent" />
<activity android:name="com.mopub.common.MoPubBrowser"
        android:configChanges="keyboardHidden|orientation|screenSize" />
<activity android:name="com.mopub.mobileads.MraidActivity"
        android:configChanges="keyboardHidden|orientation|screenSize" />
<activity android:name="com.mopub.mobileads.MraidVideoPlayerActivity"
        android:configChanges="keyboardHidden|orientation|screenSize" />

<activity android:name="org.nexage.sourcekit.mraid.MRAIDBrowser"
        android:configChanges="orientation|keyboard|keyboardHidden|screenSize"
        android:theme="@android:style/Theme.Translucent" />

<activity android:name="com.amazon.device.ads.AdActivity"
        android:configChanges="keyboardHidden|orientation|screenSize"/>

<activity android:name="com.unity3d.ads.android.view.UnityAdsFullscreenActivity"
        android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
        android:hardwareAccelerated="true" />

<activity android:name="ru.mail.android.mytarget.ads.MyTargetActivity"
        android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|uiMode|screenSize|smallestScreenSize"/>

<activity android:name="org.nexage.sourcekit.vast.activity.VASTActivity"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen" />

<activity android:name="com.facebook.ads.InterstitialAdActivity"
        android:configChanges="keyboardHidden|orientation|screenSize" />

<activity android:name="com.jirbo.adcolony.AdColonyOverlay"
        android:configChanges="keyboardHidden|orientation|screenSize"
        android:theme="@android:style/Theme.Translucent.NoTitleBar.Fullscreen" />
<activity android:name="com.jirbo.adcolony.AdColonyFullscreen"
        android:configChanges="keyboardHidden|orientation|screenSize"
        android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen" />
<activity android:name="com.jirbo.adcolony.AdColonyBrowser"
        android:configChanges="keyboardHidden|orientation|screenSize"
        android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen" />

<activity android:name="com.vungle.publisher.FullScreenAdActivity"
        android:configChanges="keyboardHidden|orientation|screenSize"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen"/>
```

### 编辑 `Android.mk`
编辑 `<project_root>/jni/Android.mk`:

为 __LOCAL_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_WHOLE_STATIC_LIBRARIES += PluginAppodeal
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginappodeal)
```

这意味着你的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginappodeal)
```

  __注意:__ 如果你使用的是 cocos2d-x 预编译库，那么保证这些语句在已有的 `$(call import-module,./prebuilt-mk)` 语句之上非常重要。

### 编辑 `Application.mk` （只限 Cocos2d-x v3.0 到 v3.2 版本）
编辑 `proj.android/jni/Application.mk` 保证 __APP_STL__ 的定义正确。如果 `Application.mk` 包含了 `APP_STL := c++_static` 语句，那么这条语句应该被改为：
```
APP_STL := gnustl_static
```