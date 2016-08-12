[&#8249; AdMob Doc Home](./)

<h1>AdMob 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
首先，您需要在 [AdMob](https://www.google.com/admob/) 官网注册一个帐号。

然后，用如下命令来集成 SDKBOX AdMob 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
$ sdkbox import admob
```

最后，请您仔细阅读官方的 [iOS FAQ](https://developers.google.com/admob/ios/quick-start#faq) 以及 [Android FAQ](https://developers.google.com/admob/android/quick-start#faq) 。

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON 配置
SDKBOX Installer 将会自动在您的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

#### 智能横幅

设置 width 和 height 的值为 0
```
    "width":0,
    "height":0
```

#### 自动缓存

不需要配置，该插件会自动缓存广告类型中的广告。当 插屏广告 关闭时，也会自动缓存它。

type:

    - "banner"
    - "interstitial"

alignment:

    - "top"
    - "bottom"
    - "left"
    - "right"
    - "center"
    - "top_left" or "left_top"
    - "top_right" or "right_top"
    - "bottom_left" or "left_bottom"
    - "bottom_right" or "right_bottom"

width x height:

    - 320x50
    - 468x60
    - 320x100
    - 728x90
    - 300x250
    - 160x600
    - 0x0    # 0x0 means auto size.

Example:
```json

{
    "ios": {
        "AdMob":{
            "ads":{
                "home":{
                    "id":"ca-app-pub-3940256099942544/2934735716",
                    "type":"banner",
                    "alignment":"bottom",
                    "width":300,
                    "height":50
                },
                "gameover":{
                    "id":"ca-app-pub-1329374026572143/4185543717",
                    "type":"interstitial"
                }
            }
        }
    },
    "android": {
        "AdMob":{
            "ads":{
                "home":{
                    "id":"ca-app-pub-1329374026572143/2685130917",
                    "type":"banner",
                    "alignment":"bottom",
                    "width":300,
                    "height":100
                },
                "gameover":{
                    "id":"ca-app-pub-1329374026572143/1092476511",
                    "type":"interstitial"
                }
            }
        }
    }
}

```

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
