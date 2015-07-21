<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/tune/v3-cpp
-->

# Tune

## 集成
在你确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Tune 插件。
```bash
sdkbox import tune
```

## 额外的步骤
<<[extra-step.md]
<<[proguard.md]

## 配置
SDKBOX Installer 将会自动在你的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于你自己的 app 。

对于一个 Tune 插件的配置样例，你需要将其中的 `<TUNE id>` 以及 `<TUNE KEY>` 替换成你特定的 [__Tune ID__](http://vungle.com) 帐号中的信息。
如下是一个添加 `Tune` 插件的配置样例：
```json
"Tune":{
    "id":"<TUNE ID>",
    "key":"<TUNE KEY>",
    "debug":false
}
```

## 使用
<<[usage.md]

<<[api-reference.md]
