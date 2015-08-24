<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/flurryanalytics/v3-cpp
-->

#Flurry Analytics

## 集成
用如下命令来集成 SDKBOX Flurry Analytics 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import flurryanalytics
```

## 额外的步骤
<<[extra-step.md]
<<[proguard.md]

## 配置
SDKBOX 安装器会自动在你的工程中添加一个样例配置文件 `sdkbox_config.json`.在你编译工程前,请用你自己的应用信息修改里面的参数值

下面给出一个 Flurry Analytics 的配置样例,你需要用在 [__Flurry Analytics ID__](http://www.flurry.com/solutions/analytics)注册的帐号信息,替换 `<API KEY>`.

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

## 用法
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
