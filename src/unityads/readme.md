[&#8249; UnityAds Doc Home](./)

<h1>UnityAds 集成指南</h1>
<<[../../shared/-VERSION-/version.md]


## 集成
用如下命令来集成 SDKBOX UnityAds 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
$ sdkbox import unityads
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON 配置
SDKBOX 安装器会为您自动生成一个 `sdkbox_config.json` 配置文件, 请先修改再使用.

下面给出一个例子, 您必须替换掉 `<gameId>`, 这个账号从 [__UnityAds__](http://www.unityads.com/)
获取.

```json
"UnityAds":{
    "gameId": "1493045",
    "testMode": true,
    "ads": {
        "banner": {
            "placement": "banner",
            "type":"banner"
        },
        "interstitial1": {
            "placement": "video"
        },
        "interstitial2": {
            "placement": "rewarded_video"
        },
    }
}
```

如果你想显示 banner , 那么你需要在 sdkbox_config.json 中的 ads 下配置 banner 信息.
同时在 ads 下也可以配置弹出广告, 弹出广告不是必须要配置, 但是推荐采用.

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
