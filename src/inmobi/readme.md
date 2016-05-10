[&#8249; InMobi Doc Home](./)

<h1>InMobi 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

- [收益化最佳实践](https://support.inmobi.com/monetize/best-practices/)

## 集成
用如下命令来集成 SDKBOX InMobi 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
$ sdkbox import inmobi
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON 配置
SDKBOX 安装器会为您自动生成一个 `sdkbox_config.json` 配置文件, 请先修改再使用.

下面给出一个例子, 您必须替换掉 `<account_id>`, 这个账号从 [__InMobi__](http://www.inmobi.com/)
获取.

```json
"InMobi":{
	"interstitial_placement_id": "1449919424310", 		// 插屏广告的 id
    "account_id": "922cc696d9fa475097651b5cad78567d",	// 从官网获取
    "banner_h": 50, 									// 横幅广告得高度
    "banner_placement_id": "1447081423897" 				// 横幅广告的 id, 不需要可以删除
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
