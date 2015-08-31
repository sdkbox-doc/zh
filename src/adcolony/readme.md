<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/adcolony/v3-cpp
-->

#AdColony

## 集成
用如下命令来集成 SDKBOX AdColony 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import adcolony
```

## 更新日志

version-x.y.z:
1. 更新 AdColony iOS SDK 到 2.5.3
2. `register_PluginAdColonyLua_helper` -> `register_all_PluginAdColonyLua_helper`
3. `#include "PluginAdColonyLuaHelper.hpp"` -> `#include "PluginAdColonyLuaHelper.h"`
4. `#include "PluginAdColonyJSHelper.hpp"` -> `#include "PluginAdColonyJSHelper.h"`

## 额外的步骤
<<[extra-step.md]
<<[proguard.md]

## 配置
SDKBOX 安装器会自动在你的工程中添加一个样例配置文件`sdkbox_config.json`.在你编译工程前,请修改里面的参数,用你自己的应用信息

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

