
<h1>Appnext 整合指南</h1>

##集成
首先，您必须到 [Appnext](https://www.appnext.com/) 注册并配置好你的应用。

第二，用如下命令来集成 SDKBOX AdColony 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
$ sdkbox import appnext
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### 配置
SDKBOX 安装器会自动在你的工程中添加一个样例配置文件`sdkbox_config.json`.在你编译工程前,请修改里面的参数,用你自己的应用信息

- id: 广告 id

- cache: 时候缓存广告

    - true  : 缓存该广告，一种类型广告只能缓存一个广告，配置多个缓存，结果未定义
    - false [默认]: 不缓存广告

- type: 广告类型

    - "interstitial"
    - "fullscreen"
    - "reward"

#### 可选配置

- creative_type:

    - "managed"
    - "video"
    - "static"

- progress_type:

    - "clock"
    - "bar"
    - "none"

- video_lenght:

    - "short"
    - "long"

- button_text
- button_color
- categories
- postback
- can_close

- skip_text
- mute
- autoplay

- progress_color
- show_close_button

更多信息请参考以下链接:

- [https://selfservice.appnext.com/Apps/Tools.aspx#android/interstitial-sdk/native-app/advanced_settings](https://selfservice.appnext.com/Apps/Tools.aspx#android/interstitial-sdk/native-app/advanced_settings)
- [https://selfservice.appnext.com/Apps/Tools.aspx#android/full-screen/rewarded-sdk-beta/advanced_settings](https://selfservice.appnext.com/Apps/Tools.aspx#android/full-screen/rewarded-sdk-beta/advanced_settings)
- [https://selfservice.appnext.com/Apps/Tools.aspx#android/full-screen/rewarded-sdk-beta/app_categories](https://selfservice.appnext.com/Apps/Tools.aspx#android/full-screen/rewarded-sdk-beta/app_categories)


例子:
```json

{
    "ios": {
        "Appnext":{
            "debug":true,
            "ads": {
                "default": {
                    "cache":true,
                    "id":"6d596bc5-b4c1-48ca-be95-3758fd29a3a5",
                    "type":"interstitial"
                }
            }
        }
    },
    "android": {
        "Appnext":{
            "debug":true,
            "ads": {
                "default": {
                    "cache":true,
                    "id":"2f6850dd-190a-499d-aa50-1f4a3dd1ed5f",
                    "type":"interstitial",

                    "button_text":"Button Text",
                    "button_color":"#6AB344",
                    "categories":"Action,Puzzle",
                    "postback":"postback",
                    "can_close":false,

                    "skip_text":"Skip Text",
                    "mute":false,
                    "autoplay":true,
                    "creative_type":"managed"
                },
                "fullscreen": {
                    "cache":true,
                    "id": "17322152-1ef3-4e72-9677-eaf7c09f1054",
                    "type": "fullscreen",

                    "button_text":"Button Text",
                    "button_color":"#6AB344",
                    "categories":"Action,Puzzle",
                    "postback":"postback",
                    "can_close":false,

                    "progress_type":"clock",
                    "progress_color":"#ffffff",
                    "show_close_button":true,
                    "video_lenght":"short"
                },
                "reward": {
                    "cache":true,
                    "id": "8d653a16-129b-4c14-bd22-fae625f70cf4",
                    "type": "reward",

                    "button_text":"Button Text",
                    "button_color":"#6AB344",
                    "categories":"Action,Puzzle",
                    "postback":"postback",
                    "can_close":false,

                    "progress_type":"bar",
                    "progress_color":"#ffff00",
                    "show_close_button":false,
                    "video_lenght":"long"
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
