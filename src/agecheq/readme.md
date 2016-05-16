<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/agecheq/v3-cpp
-->

#AgeCheq

## 集成
用如下命令来集成 SDKBOX AgeCheq 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import agecheq
```

## 更新日志

version-x.y.z:
1. `register_PluginAgeCheqLua_helper` -> `register_all_PluginAgeCheqLua_helper`
2. `#include "PluginAgeCheqLuaHelper.hpp"` -> `#include "PluginAgeCheqLuaHelper.h"`
3. `#include "PluginAgeCheqJSHelper.hpp"` -> `#include "PluginAgeCheqJSHelper.h"`

## 额外的步骤
<<[extra-step.md]
<<[proguard.md]

## 配置
SDKBOX 安装器会自动在你的工程中添加一个样例配置文件`res/sdkbox_config.json`.在你编译工程前,请修改里面的参数,用你自己的应用信息

下面给出一个 AgeCheq 的配置样例,你需要在[__AgeCheq ID__](http://developer.agecheq.com/)注册帐号,然后用对应的信息替换 `<AppID>` 和 `<DeveloperKey>`.
```json
"AgeCheq":{
            "AppID":"ca0e20a3-3bb8-42e1-a5ac-55af7f63dbfc",
            "DeveloperKey":"9102be76-232b-49b1-9c4f-1c6806d3a975"
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
