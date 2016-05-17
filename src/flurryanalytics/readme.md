[&#8249; Flurry Analytics Doc Home](./)

<h1>Flurry Analytics 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
用如下命令来集成 SDKBOX Flurry Analytics 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import flurryanalytics
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->



### JSON 配置
SDKBOX 安装器会自动在您的工程中添加一个样例配置文件 `sdkbox_config.json`.在您编译工程前,请用您自己的应用信息修改里面的参数值

下面给出一个 Flurry Analytics 的配置样例,您需要用在 [__Flurry Analytics ID__](http://www.flurry.com/solutions/analytics)注册的帐号信息,替换 `<API KEY>`.

下面给出一个 iOS 下的配置例子
```json
"FlurryAnalytics":{
            "APIKey":"<API KEY>",
            "AppVersion":"V0.1",
            "Debug":false,
            "Level":2,
            "SessionTimeout":10,
            "CrashReport":true
}
```

Android上的配置文件要复杂一点，里面包含了 __locations__, __pulse__ and __origin__ 的一些设置,下面给出一个例子:
```json
"FlurryAnalytics":{
            "APIKey":"<API KEY>",
            "AppVersion":"V0.1",
            "Debug":false,
            "LogEvent":true,
            "Level":2,
            "SessionTimeout":10,
            "CrashReport":true,
            "LocationReport":true,
            "DefLocationLat":104.06,
            "DefLocationLon":30.67,
            "Pulse":true,
            "Origin":[
                {
                    "OriginName":"sdkbox",
                    "OriginVersion":"v0.1",
                    "OriginParams":{
                        "Key1":"Val1",
                        "Key2":"Val2",
                        "Key3":"Val3"
                    }
                },
                {
                    "OriginName":"sdkbox",
                    "OriginVersion":"v0.1"
                }
            ]
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
