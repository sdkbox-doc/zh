<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/tune/v3-cpp
-->

# Tune

## 集成
在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Tune 插件。
```bash
sdkbox import tune
```

## 更新日志

version-x.y.z:
1. `register_PluginTuneJS_helper` -> `register_all_PluginTuneJS_helper`
2. `register_PluginTuneLua_helper` -> `register_all_PluginTuneLua_helper`
3. 更新 MobileAppTracker Android SDK 到 3.10.1

## 额外的步骤
<<[extra-step.md]
<<[proguard.md]

## 配置
SDKBOX Installer 将会自动在您的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

对于一个 Tune 插件的配置样例，您需要将其中的 `<TUNE id>` 以及 `<TUNE KEY>` 替换成您特定的 [__Tune ID__](http://vungle.com) 帐号中的信息。
如下是一个添加 `Tune` 插件的配置样例：
```json
"Tune":{
    "id":"<TUNE ID>",
    "key":"<TUNE KEY>",
    "debug":false
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
