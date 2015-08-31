<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/chartboost/v3-cpp
-->

#Chartboost

## 集成
用如下命令来集成 SDKBOX Chartboost 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import chartboost
```

## 更新日志

version-x.y.z:
1. `register_PluginChartboostJS_helper` -> `register_all_PluginChartboostJS_helper`
2. `register_PluginChartboostLua_helper` -> `register_all_PluginChartboostLua_helper`
3. 更新 Chartboost iOS SDK 到 5.5.3
4. 更新 Chartboost Android SDK 到 5.5.3
5. `#include "PluginChartboostLuaHelper.hpp"` -> `#include "PluginChartboostLuaHelper.h"`

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

<<[sdkbox-config-encrypt.md]

## 用法

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
