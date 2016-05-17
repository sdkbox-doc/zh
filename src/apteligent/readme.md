[&#8249; Apteligent Doc Home](./)

<h1>Apteligent 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
注册一个 [Apteligent](https://www.apteligent.com/) 帐号并且创建一个 app 。

在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Apteligent 插件。
```bash
$ sdkbox import apteligent
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON 配置
SDKBOX Installer 将会自动在您的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

- id: Apteligent App ID

#### 可选项

---

- monitor_connection [bool]: (iOS only)

    - true [default]
    - false

> Determines whether Service Monitoring should capture network performance information for network calls made through NSURLConnection.

- monitor_session [bool]: (iOS only)

    - true [default]
    - false

> Determines whether Service Monitoring should capture network performance information for network calls made through NSURLSession.

- enable_service_monitoring [bool]:

    - true [default]
    - false

> This flag determines wither Apteligent service monitoring is enabled at all.

- delay_sending_appload [bool]:

    - true
    - false [default]

> Delay to reports an app load event.

- url_filters [array]:

    - ["http://www.gmail.com", "www.other.com"]

> These filters are used to make it so certain network performance information is not reported to Apteligent.

- logcat_reporting_enabled: (Android only) Include Logcat

    - true
    - false [default]

> Including system log data (Logcat) can be helpful for debugging crashes and handled exceptions,
> but it comes at the cost of slightly increasing disk and network usage, which is why this feature
> must be manually enabled. Apteligent collects the last 100 lines of logcat data.

more information:

- [https://docs.crittercism.com/ios/ios.html](https://docs.crittercism.com/ios/ios.html)
- [https://docs.crittercism.com/android/android.html](https://docs.crittercism.com/android/android.html)

Example:
```json
{
    "ios": {
        "Apteligent":{
            "debug":true,
            "id":"956194d922984692a3184816ec3a510300555300",
            "monitor_connection":true,
            "monitor_session":true,
            "enable_service_monitoring":true,
            "delay_sending_appload":false,
            "url_filters":[
                "https://metrics.sdkbox.com",
                "http://www.gmail.com"
            ]
        }
    },
    "android": {
        "Apteligent":{
            "debug":true,
            "id":"3f66168979494ce38374b4d32d637dcc00555300",
            "enable_service_monitoring":true,
            "delay_sending_appload":false,
            "url_filters":[
                "https://metrics.sdkbox.com",
                "http://www.gmail.com"
            ],
            "version":"version:2.0.4 build:4981 codeName:Cactus",
            "version_string_include_version_code":true,
            "logcat_reporting_enabled":true
        }
    }
}

```

## 使用

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
