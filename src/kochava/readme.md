[&#8249; Kochava Doc Home](./)

<h1>Kochava 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Kochava 插件。
```bash
sdkbox import kochava
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->


### JSON 配置
SDKBOX Installer 将会自动在您的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

对于一个 Kochava 插件的配置样例，您需要将其中的 `<KOCHAVA_APP_ID>` 替换成您特定的 [__Kochava __](http://kochava.com/) 帐号中的信息。
如下是一个添加 `Kochava` 插件的配置样例：
```json
"kochava" :
{
    "kochavaAppId" : "<KOCHAVA_APP_ID>",
    "enableLogging" : 1,
    "retrieveAttribution" : 1
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
