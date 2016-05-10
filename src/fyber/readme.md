[&#8249; Fyber Doc Home](./)

<h1>Fyber 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 前提条件

* Android 系统, Fyber 最低系统要求是 4.0.3.

* __Fyber__ 不能 __SOOMLA GROW__ 在一个工程中同时存在.

## 集成
用如下命令来集成 SDKBOX Fyber 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
$ sdkbox import fyber
```

<<[../../shared/notice.md]

### 额外步骤
* 获取 Fyber 开发者账号
* 在 Fyber 网站创建 __APP__

#### iOS
* 配置您的 __APP__: [iOS Quick Start Guide](http://developer.fyber.com/content/ios/)

#### Android
* `java -version` >= 1.7
* 配置您的 __APP__: [Android Quick Start Guide](http://developer.fyber.com/content/android/basics/)
* 编辑 `project.properties`, 设置 target 目标 `target=android-15`

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON 配置
SDKBOX 安装器会自动在您的工程中添加一个样例配置文件`sdkbox_config.json`.

下面给出一个 Fyber 的配置样例
```json
"Fyber":
{
    "debug":true,
    "appid":"12345",
    "token":"34a9643edf4d3052d2bc1928b2e34d00"
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
