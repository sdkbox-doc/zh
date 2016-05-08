<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/valuepotion/v3-cpp
-->

#Valuepotion

## 集成
用如下命令来集成 SDKBOX ValuePotion 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
$ sdkbox import valuepotion
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

## 配置
SDKBOX 安装器会自动在你的工程中添加一个样例配置文件 `sdkbox_config.json` .

下面给出一个 Valuepotion 的配置样例, 您需要替换 `<client id>`  和 `<secret key>` :
- [__Valuepotion ID__](https://www.valuepotion.com/).
- `<sender id>` 在 Android 上有效, 它是 GCM(google cloud message) 项目 id
```json
"ValuePotion":{
    "clientId":"9666f9668a4db516c8aaea439464da44",
    "secretKey":"1c110ebcdeeda25d",
    "senderId":"111111"
}
```

<!--<<[sdkbox-config-encrypt.md]-->

##用法
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
