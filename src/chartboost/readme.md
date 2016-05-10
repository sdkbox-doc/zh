[&#8249; Chartboost Doc Home](./)

<h1>Chartboost 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
用如下命令来集成 SDKBOX Chartboost 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import chartboost
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->


## JSON 配置
SDKBOX 安装器会自动在您的工程中添加一个样例配置文件 `sdkbox_config.json`.在您编译工程前,请用您自己的应用信息修改里面的参数值

下面给出一个 Chartboost 的配置样例,您需要在[Chartboost](https://www.chartboost.com)注册帐号,然后用对应的信息替换 `<CHARTBOOST ID>` 和 `<CHARTBOOST SIGNATURE>`.
```json
"Chartboost":{
    "id":"<CHARTBOOST ID>",
    "signature":"<CHARTBOOST SIGNATURE>",
    "ads":{
        "Default":{
            "type":"interstitial"
        },
        "Level Complete":{
            "type":"rewarded_video"
        },
        "MoreApp":{
            "type":"more_app"
        }
    }
}
```

<<[sdkbox-config-encrypt.md]

## 使用

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
