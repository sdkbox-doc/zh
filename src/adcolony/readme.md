[&#8249; AdColony Doc Home](./)

<h1>AdColony 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
用如下命令来集成 SDKBOX AdColony 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import adcolony
```


<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->


### JSON 配置
SDKBOX 安装器会自动在你的工程中添加一个样例配置文件`sdkbox_config.json`.在你编译工程前,请修改里面的参数,用你自己的应用信息

下面给出一个AdColony的配置样例,你需要在[AdColony](https://clients.adcolony.com/login)注册帐号,然后对应的信息替换 `<app id>` 和 `<zone id>`.
```json
"AdColony":{
    "id":"<app id>",
    "debug":true,
    "ads":{
        "video":{
            "zone": "<zone id>",
            "v4vc": false
        },
        "v4vc":{
            "zone": "<zone id>",
            "v4vc": true,
            "pre_popup" : true,
            "post_popup": true
        }
    }
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

