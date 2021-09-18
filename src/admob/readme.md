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

#### 智能横幅(smart banner)

设置 width 和 height 的值为 0
```
    "width":0,
    "height":0
```

#### 自适应横幅(adaptive banner)

```
    "width":-1,
    "height":-1
```
#### 自动缓存

不需要配置，该插件会自动缓存广告类型中的广告。当 插屏广告/视频广告 关闭时，也会自动缓存它。
失败时，需要开发者调用 `cache` 接口去缓存。

type:

    - "banner"
    - "interstitial"
    - "rewarded_video"
    - "rewarded_interstitial"
    - "appopen"

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

#### Test ID (Google)

[Android](https://developers.google.com/admob/ios/test-ads)

| type               | id                                     |
| ------------------ | -------------------------------------- |
| Banner             | ca-app-pub-3940256099942544/6300978111 |
| Interstitial       | ca-app-pub-3940256099942544/1033173712 |
| Interstitial Video | ca-app-pub-3940256099942544/8691691433 |
| Rewarded Video     | ca-app-pub-3940256099942544/5224354917 |
| AppOpen            | ca-app-pub-3940256099942544/1033173712 |

[iOS](https://developers.google.com/admob/android/test-ads)

| type               | id                                     |
| ------------------ | -------------------------------------- |
| Banner             | ca-app-pub-3940256099942544/2934735716 |
| Interstitial       | ca-app-pub-3940256099942544/4411468910 |
| Interstitial Video | ca-app-pub-3940256099942544/5135589807 |
| Rewarded Video     | ca-app-pub-3940256099942544/1712485313 |
| AppOpen            | ca-app-pub-3940256099942544/5662855259 |

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
                    "id":"ca-app-pub-3940256099942544/4411468910",
                    "type":"interstitial"
                },
                "appopen":{
                    "type": "appopen",
                    "id": "ca-app-pub-3940256099942544/5662855259"
                }
            }
        }
    },
    "android": {
        "AdMob":{
            "ads":{
                "home":{
                    "id":"ca-app-pub-3940256099942544/6300978111",
                    "type":"banner",
                    "alignment":"bottom",
                    "width":300,
                    "height":100
                },
                "gameover":{
                    "id":"ca-app-pub-3940256099942544/1033173712",
                    "type":"interstitial"
                },
                "appopen":{
                    "id":"ca-app-pub-3940256099942544/1033173712",
                    "type":"appopen"
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
