[&#8249; HMS Doc Home](./)

<h1>HMS 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
用如下命令来集成 SDKBOX HMS 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import hms
```

<<[../../shared/notice.md]

### JSON 配置
SDKBOX 安装器会自动在您的工程中添加一个样例配置文件`sdkbox_config.json`.在您编译工程前,请修改里面的参数,用您自己的应用信息

这里HMS的配置样例.

```json
"ios" :
{
    "hms":{
    }
},
"android":
{
    "hms":{
        "debug": false
    }
}
```

同时你还需要在 HMS 的 AppGallery 里将对应的应用信息文件 `agconnect-services.json` 下载下来，并放在应用工程目录下(一般来说是在 proj.android/app 目录).

### iOS 测试

-   HMS 不支持 iOS 平台, 在 iOS 其实是一个空的实现

### Android 测试

1.  在 AppGallery 中创建一个 app
2.  启起你想要使用的模块(比如你要使用登录, 就可以启用AccountKit)
3.  添加app的签名hash
4.  下载应用的信息文件 `agconnect-services.json`

HMS 的官方[文档](https://developer.huawei.com/consumer/hms)


<<[sdkbox-config-encrypt.md]

## 使用

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]
