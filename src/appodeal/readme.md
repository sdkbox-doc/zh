[&#8249; Appodeal Doc Home](./)

<h1>Appodeal 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Appodeal 插件。
```bash
$ sdkbox import appodeal
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON 配置
SDKBOX Installer 将会自动在您的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

对于一个 Appodeal 插件的配置样例，您需要将其中的 `<app_key>` 替换成您特定的 [__Appodeal__](http://www.appodeal.com/) 帐号中的信息。
```json
"Appodeal":{
    "app_key":"2cfc9cc638980eb7f5ff35d6eb63dbe404503151ccc451ed"
}
```

<!--<<[sdkbox-config-encrypt.md]-->

## 使用

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
