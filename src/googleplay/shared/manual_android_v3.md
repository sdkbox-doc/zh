### 拷贝文件

把安装包中的 `plugin/android/libs` 目录下的如下 __jar__ 文件拷贝到你的工程中的 __<project_root>/libs__ 目录下.

<<[../../shared/copy_jars.md]

<<[../../shared/copy_jni_lib.md]


### 修改 `AndroidManifest.xml`

添加如下 meta-data :
```xml
<meta-data android:name="com.google.android.gms.version"
    android:value="@integer/google_play_services_version" />
<meta-data android:name="com.google.android.gms.games.APP_ID"
    android:value="@string/google_app_id" />
```
请确保添加如下 `<string name="google_app_id">777734739048</string>` 到 `res/values/string.xml` 中.
一定要用你自己的 google app id 来代替.

### 修改 `Android.mk`

将 `gpg` 拷贝到 `proj.andrid/jni` 目录下

添加如下内容到你的 `android.mk` 文件中

#### 添加头文件目录
```
LOCAL_C_INCLUDES += ./gpg/include/
```

#### 添加静态库

添加静态库到 __LOCAL_WHOLE_STATIC_LIBRARIES__:

```
LOCAL_WHOLE_STATIC_LIBRARIES += gpg-1
LOCAL_WHOLE_STATIC_LIBRARIES += PluginGPG
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

在 __import-module__ 语句之前添加如下调用:

```
$(call import-add-path,$(LOCAL_PATH))
```

在 __import-module__ 语句之后添加如下语句:
```
$(call import-module, ./gpg)
$(call import-module, ./sdkbox)
$(call import-module, ./plugingpg)
```

  __注意:__ 如果你使用的是预编译版本, 请一定要确保以上语句是在 `$(call import-module,./prebuilt-mk)` 之前.

### 修改 `Application.mk` (只适用于 Cocos2d-x v3.0 to v3.2)
查看 `<project_root>/jni/Application.mk` 中的 __APP_STL__ 是否定义正确. 如果 `Application.mk` 包含了 `APP_STL := c++_static` 语句, 那么请改为:
```
APP_STL := gnustl_static
```
