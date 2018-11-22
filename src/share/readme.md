[&#8249; Share Doc Home](./)

<h1>Share 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 简介
SDKBOX Share 插件为开发者提供一种终极的解决方案实现所有社交平台的分享功能。

当前 Sdkbox Share 支持 分享到 **twitter** 以及 **facebook** 。

在使用前，请确保您已经在下面两个平台创建了开发者帐号。

* [Facebook](http://developers.facebook.com/)
* [Twitter](http://apps.twitter.com/)

## 集成
在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Share 插件。
```bash
$ sdkbox import share
```

如果您希望使用分享到 Facebook 功能，您必须安装 SDKBOX Facebook 插件。
```bash
$ sdkbox import facebook
```

Facebook 插件的安装集成还需要一些额外的集成步骤，请参考 [这篇文档](http://docs.sdkbox.com/en/plugins/facebook/v3-cpp/#extra-steps) 。

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON 配置
SDKBOX Installer 将会自动在您的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

这里有一个 Sdkbox Share 的配置示例如下：
```json
    "android": {
        "Facebook": {
            "debug": false
        },
        "Share": {
            "platforms": {
                "Twitter": {
                    "params": {
                        "secret": "nlmUdPNcFGLWhyLu9cD794EDuDrVQnjd0YjTpB6sX8oHIQRrne",
                        "key": "EuovpLL0UhSGB7Jv5eKFJNMqO"
                    }
                },
                "Facebook": {}    //support facebook share
            }
        }
    },
    "ios": {
        "Facebook": {
            "debug": true
        },
        "Share": {
            "platforms": {
                "Twitter": {
                    "params": {
                        "secret": "haVcKarM96Sr4390XLQoHjyRUSyuHdkMX6letcc38h8TOWyiR9",
                        "key": "BUJTV6NEM7BAhhm82B12VbKGy"
                    }
                },
                "Facebook": {}    //support facebook share
            }
        }
    }
```

**Twitter 配置**

you need to replace `<key>`, `<secret>` item with your specific [Twitter](http://apps.twitter.com/) account.
您需要用您自己的 Twitter 开发者帐号信息替换配置文中所有的 `<key>`，`<secret>` 项。

**Facebook 配置**

您需要添加 `Facebook` 相关配置到配置文件中。

### iOS 配置
* `Twitter` 支持的 iOS 版本为 9.0+
* 在 `AppController.mm` 中做如下修改

```object-c
#import <TwitterKit/TWTRKit.h>

- (BOOL)application:(UIApplication *)app
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
    return [[Twitter sharedInstance] application:app openURL:url options:options];
}
```

* 在 `Info.plist` 中增加如下内容
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>

    ...

    <key>CFBundleURLTypes</key>
    <array>

        ...

        <dict>
            <key>CFBundleURLSchemes</key>
            <array>
                <string>twitterkit-(your-appkey)</string>
            </array>
        </dict>

        ...

    </array>

    <key>LSApplicationQueriesSchemes</key>
    <array>

        ...

        <string>twitter</string>
        <string>twitterauth</string>

        ...

    </array>

    ...

</dict>
</plist>

```

<!--<<[sdkbox-config-encrypt.md]-->

## 使用
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
