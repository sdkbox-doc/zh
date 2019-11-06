[&#8249; AdColony Doc Home](./)

<h1>AdColony 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
用如下命令来集成 SDKBOX AdColony 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import adcolony
```


<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->


### JSON 配置
SDKBOX Installer 将会自动在您的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

下面给出一个AdColony的配置样例,你需要在[AdColony](https://clients.adcolony.com/login)注册帐号,然后对应的信息替换 `<app id>` 和 `<zone id>`.
```json
"AdColony":{
    "id":"<app id>",
    "debug":true,
    "ads":{
        "video":{
            "zone": "<zone id>",
            "v4vc": false
        },
        "v4vc":{
            "zone": "<zone id>",
            "v4vc": true,
            "pre_popup" : true,
            "post_popup": true
        },
        "banner": {
            "zone": "<zone id>",
            "type":"banner",
            "alignment":"bottom",
            "width": 320,
            "height": 50
        }
    }
}
```

banner.width: banner.width 小于 10 为特殊值. 这时会解释为创建AdColony内置的类型, 目前仅用到以下四个值

* 0: kAdColonyAdSizeBanner(standard,320*50)
* 1: kAdColonyAdSizeMediumRectangle(medium,300x250)
* 2: kAdColonyAdSizeLeaderboard(Leaderboard,728x90)
* 3: kAdColonyAdSizeSkyscraper(Skyscraper,160x600)

如上, 如果设置 banner.width 为0, 则会创建一个 standard(320X250) 的 banner, 如果设置 banner.width 为1, 则会创建一个 medium(300x250) 的 banner, 当 banner.width 为特殊值时, banner.height请设置为 0.

banner.alignment: 可用值: 

* center
* top
* bottom
* left
* right
* top_left
* top_right
* bottom_left
* bottom_right
* left_top
* left_bottom
* right_top
* right_bottom

<<[sdkbox-config-encrypt.md]

## 用法
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]

