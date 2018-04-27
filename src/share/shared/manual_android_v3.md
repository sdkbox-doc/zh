### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到您的工程的 __proj.android/libs__ 目录。

> sdkbox.jar

> PluginShare.jar

> converter-gson-2.1.0.jar

> gson-2.7.jar

> okhttp-3.4.2.jar

> okio-1.9.0.jar

> picasso-2.5.2.jar

> retrofit-2.1.0.jar

> twitter-text-1.14.3.jar

> tweet-composer

> twitter-core


* 如果您使用 cocos2d-x 源码，拷贝 __jar__ 文件到：

    Android command-line:
    ```
    cocos2d/cocos/platform/android/java/libs
    ```

* 如果您使用 cocos2d-js 或者 lua ，拷贝 __jar__ 文件到:

    Android command-line:
    ```
    frameworks/cocos2d-x/cocos/platform/android/java/libs
    ```

* 如果您使用 cocos2d-x 预编译包，拷贝 __jar__ 文件到：

    Android command-line:
    ```
    proj.android/libs
    ```

* 如果您使用 android-stdio, 请编辑 `proj.android-studio/app/build.gradle` 文件， 如下所示：

文件 `proj.android-studio/app/build.gradle` 中 __dependencies tag__ 的内容：


``` gradle
    dependencies {

        ...

        implementation 'com.twitter.sdk.android:twitter-core:3.1.1'
        implementation 'com.twitter.sdk.android:tweet-composer:3.1.1'

        ...

    }
```


<<[../../shared/copy_jni_lib.md]


### 编辑 `AndroidManifest.xml`
在标签 __application tag__ 上添加下列权限：

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
```

* 在标签 __application tag__ 上包含以下内容：

```xml
<activity
    android:name="com.twitter.sdk.android.core.identity.OAuthActivity"
    android:configChanges="orientation|screenSize"
    android:excludeFromRecents="true"
    android:exported="false" />

<service
    android:name="com.twitter.sdk.android.tweetcomposer.TweetUploadService"
    android:enabled="true"
    android:exported="false" />
```

### 编辑 `Android.mk`
编辑 `proj.android/jni/Android.mk`：

为 __LOCAL_WHOLE_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_WHOLE_STATIC_LIBRARIES += PluginShare
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginshare)
```

这意味着您的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginshare)
```

  __Note:__ 如果您使用的是 cocos2d-x 预编译库，那么保证这些语句在已有的 `$(call import-module,./prebuilt-mk)` 语句之上非常重要。

### 编辑 `Application.mk` （只限 Cocos2d-x v3.0 到 v3.2 版本）
编辑 `proj.android/jni/Application.mk` 保证 __APP_STL__ 的定义正确。如果 `Application.mk` 包含了 `APP_STL := c++_static` 语句，那么这条语句应该被改为：
```
APP_STL := gnustl_static
```
