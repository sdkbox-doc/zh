[&#8249; LeadBolt Doc Home](./)

<h1>LeadBolt 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX LeadBolt 插件。
```bash
$ sdkbox import leadbolt
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON 配置
SDKBOX Installer 将会自动在您的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

这里有一个 LeadBolt 配置的例子，您需要用您自己的 [LeadBolt](http://leadbolt.com/) 帐号信息替换 `<api_key>`，`<name>` 。
```json
{
	"ios": {
		"LeadBolt": {
			"api_key": "8uc8Kd5b6LoyJZCAsFUCY2sWmSJkXZ6c",
			"ads": {
				"directdeal": {
					"name": "inapp"
				},
				"rewardedvideo": {
					"name": "video"
				}
			}
		}
	},
	"android": {
		"LeadBolt": {
			"api_key": "is2byYEVjbXiFjVjaYIt6sM4aEIqMWZ3",
			"ads": {
				"directdeal": {
					"name": "inapp"
				},
				"rewardedvideo": {
					"name": "video"
				}
			}
		}
	}
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
