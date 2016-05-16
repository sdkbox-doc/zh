<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/bee7/v3-cpp
-->

#Bee7

##前提
* Android 系统, Bee7 要求的最低的系统版本是 4.0.3. 

* iOS 系统, Bee7 的游戏墙支持竖屏.

##集成
用如下命令来集成 SDKBOX Bee7 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
$ sdkbox import bee7
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### 配置
SDKBOX 安装器会自动在你的工程中添加一个样例配置文件`sdkbox_config.json`.在你编译工程前,请修改里面的参数,用你自己的应用信息

下面给出一个Bee7的配置样例:

```json
"Bee7":
{
    "debug":true,
    "key":"FE74A9C4-1288-4F6F-8D6E-C365699F2C72"
}
```

<!--<<[sdkbox-config-encrypt.md]-->

##额外步骤
以下操作，确保您在 [Bee7](http://bee7.com/) 创建了一个新的 __APP__ 并且将它激活.

###iOS
* 修改 `Info.plist`, 添加 `URL Schemes`:

	__Target -> Info -> URL Types__:

	1. click "+"
	2. fill "URL Schemes" with "your bee7 scheme"

###Android
* 编辑 `AndroidManifest.xml`, 用自己的 `bee7 scene` 替换 `_replace_with_your_bee7_scheme_`.
* 编辑 `project.properties`, 修改 target 版本 `target=android-21`

##用法

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
