[&#8249; Amazon Doc Home](./)

<h1>Amazon Appstore 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 前提条件
- 当前 `Amazon` 插件仅仅支持 __Android__ 平台。请按照 [https://developer.amazon.com/](https://developer.amazon.com/) 的说明注册一个 Amazon 开发者帐号。

- 需要 Amazon Kindle Fire 设备。

### 提示：
当你使用 __Amazon__ 插件时，必须安装 __IAP__ 插件以使它能够正常运行。

## 集成
用如下命令来集成 SDKBOX Amazon 插件,请确保你可以正常执行的 SDKBOX 安装器.

```bash
$ sdkbox import amazon
$ sdkbox set store amazon
```

## 额外步骤
下面的步骤说明都是在假设您已经注册成功 Amazon 开发者帐号并且在其开发者平台创建了一个新的游戏工程的前提下。

### 配置 Android
* 打开 `AndroidManifest.xml` 文件，添加以下内容：

```xml
<meta-data android:name="store" android:value="amazon" />
```

  提示：如果您在其他应用商店提交了 *apk* 包，比如 __Google Play__, 请删除这行配置或者设置 `store` 的值为 `googleplay`。比如：`<meta-data android: name="store" android:value=“googleplay" />`

```bash
$ sdkbox set store googleplay
```

### JSON 配置
SDKBOX Installer 将会自动在您的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

这里有一个添加了 `Amazon` 商店的例子：


```json
{
    "ios":
    {
    },
    "android":
    {
    },
    "amazon" :
    {
        "iap":
        {
            "items":{
                "remove_ads":{
                    "id":"com.cocos2dx.non1",
                    "type":"non_consumable"
                },
                "double_coin":{
                    "id":"com.cocos2dx.non2",
                    "type":"non_consumable"
                },
                "coin_package":{
                    "id":"com.cocos2dx.plugintest2"
                },
                "coin_package2":{
                    "id":"com.cocos2dx.plugintest3"
                }
            }
        }
    }
}
```

## 如何测试
- 安装 [Amazon App Tester](http://www.amazon.com/Amazon-App-Tester/dp/B00BN3YZM2/)
- 上传一个 JSON 数据文件到设备上

    ```
    $ adb push [Your_JSON_File_Folder]/amazon.sdktester.json /mnt/sdcard/
    ```

更多的细节请访问：[https://developer.amazon.com/public/apis/earn/in-app-purchasing](https://developer.amazon.com/public/apis/earn/in-app-purchasing)

### 混淆 (release, 可选)

* 编辑 `project.properties`,写入一个 `Proguard` 配置. Example:

```
proguard.config=proguard.cfg
```

* 编辑这个文件，加入如下内容:

```
# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}

# cocos2d-x
-keep public class org.cocos2dx.** { *; }
-dontwarn org.cocos2dx.**
-keep public class com.chukong.** { *; }
-dontwarn com.chukong.**

# google play service
-keep public class com.google.android.gms.** { public *; }
-dontwarn com.google.android.gms.**

-keep class * extends java.util.ListResourceBundle {
    protected Object[][] getContents();
}

-keep public class com.google.android.gms.common.internal.safeparcel.SafeParcelable {
    public static final *** NULL;
}

-keepnames @com.google.android.gms.common.annotation.KeepName class *
-keepclassmembernames class * {
    @com.google.android.gms.common.annotation.KeepName *;
}

-keepnames class * implements android.os.Parcelable {
    public static final ** CREATOR;
}

#sdkbox
-keep public class com.sdkbox.** { *; }
-dontwarn com.sdkbox.**

#amazon
-dontwarn com.amazon.**
-keep class com.amazon.** {*;}
-keepattributes *Annotation*
```

[https://developer.amazon.com/public/apis/earn/in-app-purchasing/docs/code-obfuscation](https://developer.amazon.com/public/apis/earn/in-app-purchasing/docs/code-obfuscation)

 __注意:__ 混淆只在 __Release__ 模式下有效 (比如 `cocos run -m release`), 在 debug 模式下,不会调到混淆规则.

