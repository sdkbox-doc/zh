<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/googleanalytics/v3-cpp
-->

# Google Analytics

## 集成
在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Google Analytics 插件。
```bash
sdkbox import googleanalytics
```

## 额外的步骤
<<[extra-step.md]
<<[proguard.md]

## 配置
SDKBOX Installer 将会自动在您的 `res/sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

对于一个 Google Analytics 插件的配置样例，您需要将其中的 `<TRACKING_CODE>` 替换成您特定的 [__Google Analytics__](https://support.google.com/analytics/answer/1008080?hl=en) 帐号中的信息。
```json
"GoogleAnalytics" : {
    "trackingCode" : "<TRACKING_CODE>"
}
```

## 使用
<<[usage.md]

<<[api-reference.md]
