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
        "archive": true,
        "key": "MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAn9U6yC1QI8cXGRkOQxO9QG/WV8dR4jZDCYt/GJBM4OTTtRZeAIEyVifGPutwMAkPBLgdUsJwHuA2t2jrBAi/nagYJvh8UIazKJv5C4Hykw5Z2iKTWMmiMK9rQ2tMtRTAMiY+LwfaOH2258bEyt8mDQxyG3aRSAH28mZki/nGEbNfx7ZY9By/SSkuaCEWRDNYdiWkGDuZLhf8D97DoJJc6tTnrDPmzf1QqkVDjjudkHJwgCMWpLVACzGGuo4YQYt98Pu9cqbiYWJqSHqEbPYN0AmGXdJw+tO5f1wPcZWnJhn4JqCFmD9i/dSENNJWXVDgJc0DG2PiWX5j+qUaT7WkZMs4/WFtL6VRdRUDzITqYwKUUBYENVvkfdKlhjh+6V4BFKPsipvjOsRdXDpZ7sC6MY/7yn0eMOH3RoIQoiWeGYkxRTkKhdm/QQ/Xv/dvMbiicsNmUIkBce3w4hQG9XlhgjNrl5rI4p9Ho3Stq48s7DJlhWuUE6pXcjo2TJUSJ9+nAgMBAAE=",
        "items": {
            "remove_ads": {
                "type": "non_consumable",
                "id": "com.sdkbox.test.app.sample.noad"
            },
            "coin": {
                "id": "com.sdkbox.test.app.sample.coin1"
            },
            "vip": {
                "type": "subs",
                "id": "com.sdkbox.test.app.sample.vip"
            }
        },
        "achievements": [{
            "name": "freshman",
            "id": "A7346279E90AB8910AAC0CB71E552BFA2505DFD7591C79457F84D6B95F50FFEC",
            "incremental": false
        }, {
            "name": "3shoot",
            "id": "BA8B1A486D422AEF28FF82F9BFF85C3F156824396E0BB62D92BECC63C3CAC46A",
            "incremental": true
        }, {
            "name": "5shoot",
            "id": "001D38EC9E1A80A52ED3F47BFBA35F4B5BDF3776180A2B9AD778800C45CD6540",
            "incremental": true
        }],
        "events": [{
            "name": "gencoin",
            "id": "912764D10F0988B9DCB041A4E6FE453BCBDEDC4E35708A60E33C2DEBF05F2D2E"
        }, {
            "name": "consumecoin",
            "id": "E8688F3D9625572F462F5999E7F83EB5628E0FC1F2044E84D026EC4AB33C09F5"
        }],
        "rankings": [{
            "name": "shooter",
            "id": "C8B96FA1EDFC2D87DFE9491409440E3F8B2E39AFB8BD7E95C3BE337FC207C253"
        }]
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
