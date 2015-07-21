<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/kochava/v3-cpp
-->

# Kochava

## 集成
在你确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Kochava 插件。
```bash
sdkbox import kochava
```

## 额外的步骤
<<[extra-step.md]

## 配置
SDKBOX Installer 将会自动在你的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于你自己的 app 。

对于一个 Kochava 插件的配置样例，你需要将其中的 `<KOCHAVA_APP_ID>` 替换成你特定的 [__Kochava __](http://kochava.com/) 帐号中的信息。
如下是一个添加 `Kochava` 插件的配置样例：
```json
"kochava" :
{
    "kochavaAppId" : "<KOCHAVA_APP_ID>",
    "enableLogging" : 1,
    "retrieveAttribution" : 1
}
```

## 使用
<<[usage.md]

<<[api-reference.md]
