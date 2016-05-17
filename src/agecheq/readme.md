[&#8249; AgeCheq Doc Home](./)

<h1>AgeCheq 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
用如下命令来集成 SDKBOX AgeCheq 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import agecheq
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->


### JSON 配置
SDKBOX 安装器会自动在您的工程中添加一个样例配置文件`res/sdkbox_config.json`.在您编译工程前,请修改里面的参数,用您自己的应用信息

下面给出一个 AgeCheq 的配置样例,您需要在[__AgeCheq ID__](http://developer.agecheq.com/)注册帐号,然后用对应的信息替换 `<AppID>` 和 `<DeveloperKey>`.
```json
"AgeCheq":{
            "AppID":"ca0e20a3-3bb8-42e1-a5ac-55af7f63dbfc",
            "DeveloperKey":"9102be76-232b-49b1-9c4f-1c6806d3a975"
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
