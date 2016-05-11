[&#8249; Share Doc Home](./)

<h1>Share 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 简介
SDKBOX Share 插件为开发者提供一种终极的解决方案实现所有社交平台的分享功能。

当前 Sdkbox Share 支持 分享到 **twitter** 以及 **facebook** 。

在使用前，请确保您已经在下面两个平台创建了开发者帐号。

* [Facebook](http://developers.facebook.com/)
* [Twitter](http://apps.twitter.com/) (For twitter you'll also need [Fabric](https://fabric.io))

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

您还需要用您自己的 [fabric organization](https://fabric.io/settings/organizations) 中的 api_key 替换 `AndroidManifest.xml` 中的 api_key 。
``` xml
<meta-data
            android:name="io.fabric.ApiKey"
            android:value="api_key" />
```

你可以从 Fabric organization 页面找到 api\_key 。
![](../../imgs/share_twitter_organization_info.png)

**Facebook 配置**

您需要添加 `Facebook` 相关配置到配置文件中。


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
