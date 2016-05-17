[&#8249; SdkboxAds Doc Home](./)

<h1>SdkboxAds 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX SdkboxAds 插件。
```bash
$ sdkbox import sdkboxads
```

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON 配置
SDKBOX Installer 将会自动在您的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

这里有一个 SdkboxAds 配置的例子：
```json
    "SdkboxAds": {
        "units": [
                "AdColony",
                "Fyber",
                "Chartboost",
                "Vungle"
            ],
        "placements": [
            {
                "id" : "placement-1",
                "strategy" : "round-robin",
                "units" : [
                    {
                      "unit": "AdColony",
                      "name": "video"
                    },
                    {
                      "unit": "Chartboost",
                      "name": "Default"
                    }
                ]
            },
            {
                "id" : "placement-2",
                "strategy" : "round-robin",
                "units" : [
                    {
                      "unit": "Vungle",
                      "name": "reward"
                    },
                    {
                      "unit": "AdColony",
                      "name": "v4vc"
                    },
                    {
                      "unit": "Chartboost",
                      "name": "Next Level"
                    }
                ]
            }
        ]
    }
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
