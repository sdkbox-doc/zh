<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/chartboost/v3-cpp
-->

#Chartboost

## 集成
用如下命令来集成 SDKBOX Chartboost 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import chartboost
```

## 额外的步骤
<<[extra-step.md]
<<[proguard.md]

## 配置
SDKBOX 安装器会自动在你的工程中添加一个样例配置文件 `sdkbox_config.json`.在你编译工程前,请用你自己的应用信息修改里面的参数值

下面给出一个 Chartboost 的配置样例,你需要在[Chartboost](https://www.chartboost.com)注册帐号,然后用对应的信息替换 `<CHARTBOOST ID>` 和 `<CHARTBOOST SIGNATURE>`.
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

## 用法
<<[usage.md]

<<[api-reference.md]
