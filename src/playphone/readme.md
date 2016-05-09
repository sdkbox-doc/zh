[&#8249; Playphone Doc Home](./)

<h1>Playphone 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 前提条件

当前, `Playphone` 只支持 __Android__ 平台.  __Playphone__ 是一个专业的游戏发布平台, 从 [http://playphone.com](http://playphone.com) 获取更多信息.

## 集成
用如下命令来集成 SDKBOX Playphone 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
$ sdkbox import playphone
```

### 额外步骤
确保您已经拥有 __Playphone Developer__ 开发者账号, 并且在 __Playphone__ 网站上创建了 __游戏__.

### 配置 Android
* 打开 `AndroidManifest.xml` 文件, 并添加一下信息:

```xml
<meta-data android:name="store" android:value="playphone" />
<meta-data android:name="leaderboard" android:value="playphone" />
```

  __注意__:
  如果您想把游戏提交到其他商店, 比如 __Google Play__, 请把 `store` 的值修改为 `googleplay`, 否则你将得到错误的配置信息.

  `<meta-data android:name="store" android:value="googleplay" />`

  或者使用 `sdkbox` 命令来修改 `store` 的值
  ```bash
  $ sdkbox set store googleplay
  ```

### JSON 配置
SDKBox 安装器会在 `sdkbox_config.json` 中注入一个简单配置, 您需要提供一些适合您游戏使用的数据.

比如, 您需要替换 `<base64EncodedPublicKey>` 和 `<your secret key>`, 这些能在 __Playphone__ 的网站上找到.

一个例子:
```json
{
    "ios":
    {
    },
    "android":
    {
    },
    "playphone" :
    {
        "skey":"<your secret key>",
        "iap":
        {
            "key":"<base64EncodedPublicKey>",
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

## 混淆 (release, 可选)

* 编辑 `project.properties`,写入一个 `Proguard` 配置. Example:

```
proguard.config=proguard.cfg
```

* proguard.cfg

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

# sdkbox
-keep public class com.sdkbox.** { *; }
-dontwarn com.sdkbox.**

# playphone
-keep public class com.playphone.psgn.** { *; }
-dontwarn com.playphone.psgn.**
```

 __注意:__ 混淆只在 __Release__ 模式下有效 (比如 `cocos run -m release`), 在 debug 模式下,不会调到混淆规则.

