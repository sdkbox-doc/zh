## Android 平台手动集成

### 拷贝文件
从插件安装包中的 `plugin/android/libs` 目录拷贝下列 __jar__ 文件到您的工程的 __proj.android/libs__ 目录。

> PluginHMS.jar

> sdkbox.jar


<<[../../shared/copy_jars.md]

从 `plugin/android/jni` 目录拷贝 `pluginhms` 以及 `sdkbox` 目录到您的工程的 `proj.android/jni` 目录。如果 `sdkbox` 目录在工程中已经存在，请覆盖它。

### 修改 `build.gradle`

你对 build.gradle 的修改可能会类似于下面的修改:

工程的根目录下的 build.gradle 修改
```gradle

buildscript {
    repositories {
        google()
        jcenter()
        maven { url 'https://developer.huawei.com/repo/' } // for hms
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:3.4.1'
        classpath 'com.huawei.agconnect:agcp:1.2.1.301' // for hms
    }
}

allprojects {
    repositories {
        google()
        jcenter()
        maven { url 'https://developer.huawei.com/repo/' } // for hms
    }
}

```

应用级的 build.gradle 修改
```gradle
apply plugin: 'com.android.application'
apply plugin: 'com.huawei.agconnect' // for hms

...

dependencies {
    ...
    implementation 'com.huawei.hms:hwid:4.0.1.301' // for hms
}

```

### 编辑 `AndroidManifest.xml`
在标签 __application tag__ 上添加下列权限：
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="com.android.vending.BILLING"/>
```

### 编辑 `Android.mk`
编辑 `proj.android/jni/Android.mk`：

为 __LOCAL_STATIC_LIBRARIES__ 添加额外的库：
```
LOCAL_STATIC_LIBRARIES += PluginHMS
LOCAL_STATIC_LIBRARIES += sdkbox
```

在所有 __import-module__ 语句之前添加一条 call 语句：
```
$(call import-add-path,$(LOCAL_PATH))
```

在最后添加额外的 __import-module__ 语句：
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginhms)
```

这意味着您的语句顺序看起来像是这样：
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginhms)
```

  __Note:__ 如果您使用的是 cocos2d-x 预编译库，那么保证这些语句在已有的 `$(call import-module,./prebuilt-mk)` 语句之上非常重要。

### 编辑 `Application.mk` （只限 Cocos2d-x v3.0 到 v3.2 版本）
编辑 `proj.android/jni/Application.mk` 保证 __APP_STL__ 的定义正确。如果 `Application.mk` 包含了 `APP_STL := c++_static` 语句，那么这条语句应该被改为：
```
APP_STL := gnustl_static
```
