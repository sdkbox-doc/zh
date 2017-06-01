[&#8249; SdkboxAds Doc Home](./)

<h1>SdkboxPlay 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 前提条件

### Google play
 * 根据 [这篇 google 官方文档](https://developers.google.com/games/services/console/enabling#step_2_add_your_game_to_the_dev_console) 为您的工程打开游戏服务并且创建一个 app 。否则，您的工程将不能连接到 google play 。
 * 使用开发者控制台配置 Leaderboards 以及 Achievements 。

### Game Center
 * 在 XCode 上打开 Game Center 选项。
 * 使用开发者平台配置 Leaderboards 以及 Achievements 。


## 集成
在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Youtube 插件。
```bash
$ sdkbox import sdkboxplay
```

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON 配置
SDKBOX Installer 将会自动在您的 `sdkbox_config.json` 中插入一份配置样例。请修改这份配置样例，使其能用于您自己的 app 。

这里有一份 SdkboxPlay 配置的例子：
```json
    "sdkboxplay" : {
      "leaderboards" : [
        {
          "id" : "CgkI0sux8sMWEAIQAA",
          "name" : "ldb1"
        }
      ],
      "achievements" : [
        {
          "id" : "CgkI0sux8sMWEAIQAg",
          "name" : "ten-games",
          "incremental" : false
        },
        {
          "id" : "CgkI0sux8sMWEAIQAw",
          "name" : "hunter",
          "incremental" : false
        },
        ...
      ],
      "debug" : true,
      "connect_on_start" : false
    }

```


如上例所示，Leaderboards 以及 Achievements 都有一个可读性较高的 name, 以及一个机器生成的 id 。这样做的目的是能够通过它们在不同的平台下使用 API 。相比 Google Play 产生的如上所示的随机 ID ，iOS Game Center 产生的 ID 更具可读性。
无论哪个平台，开发者总是通过 name 去使用 Leaderboards 以及 Achievements， 就像下面的示例代码中所看到的那样。

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

<<[../shared/cloud_save.md]
