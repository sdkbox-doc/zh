[&#8249; Google Analytics Doc Home](./)

<h1>Google Analytics 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Google Analytics 插件。
```bash
sdkbox import googleanalytics
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->


### JSON 配置
SDKBOX Installer 将会自动在您的 `res/sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

对于一个 Google Analytics 插件的配置样例，您需要将其中的 `<TRACKING_CODE>` 替换成您特定的 [__Google Analytics__](https://support.google.com/analytics/answer/1008080?hl=en) 帐号中的信息。
```json
"GoogleAnalytics" : {
    "trackingCode" : "<TRACKING_CODE>",
    "anonymizeIp": true
}
```

### 追踪器
一个 __追踪器__ 用于统计被追踪的事件。这里有以下几点需要开发人员注意：

* 您必须创建一个移动追踪器或者使用之前创建的追踪器。

* 如果这个追踪器是新创建的，它将在24小时之后才能显示追踪的数据。

* 一旦您在追踪器上看见历史活动记录，您也能看见当前的实时数据。

* 您可以创建任意数量的追踪器，但是插件配置里仅仅允许您定义一个（用于基本情况）。

* 如果没有追踪器在配置里被设置，将不会有追踪会话。这意味着，一个（或者多个）追踪器可能在之后被创建。在这种情况下，需要显示的调用 `startSession()` 。

* 不管这个追踪器是设置在插件配置中还是被手动创建，所有的追踪事件将被自动发往服务器。这一功能的实现是先缓存追踪事件，然后集中一批发往服务器。

<<[sdkbox-config-encrypt.md]

## 使用
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
