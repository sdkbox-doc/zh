[&#8249; Review Doc Home](./)

<h1>Review 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Review 插件。
```bash
$ sdkbox import review
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->


### JSON 配置
SDKBOX 安装器会为您自动生成一个配置文件 `res/sdkbox_config.json`,在您使用前,请修改里面的值为您自己的应用所需的值.

下面给一个 Review 的配置.
```json
"Review":{
    "ios": {
        "Review":{
            "AppID":"587767923",            //appid, ios 上有效
            "DayLimit": 0,                  //在评价弹出框显示前的天数限制
            "LaunchLimit": 3,               //在评价弹出框显示前的启动次数限制
            "UserEventLimit": 0,            //在评价弹出框显示前的用户事件限制, 用户事件是集成应用来增加事件记数的,调用 userDidSignificantEvent 增加用户事件记数
            "DayForReminding": 1,           //用户选择 稍后提示 后再次弹出的天数限制
            "LaunchForReminding": 2,        //用户选择 稍后提示 后再次弹出的启动次数限制
            "tryPromptWhenInit": true       //在初始化后，是否自动弹出评价提示框
        }
    },
    "android": {
        "Review":{
            "DayLimit": 0,
            "LaunchLimit": 3,
            "UserEventLimit": 0,
            "DayForReminding": 1,
            "LaunchForReminding": 2,
            "tryPromptWhenInit": true
        }
    }
}
```

<<[sdkbox-config-encrypt.md]

## 使用
<<[usage.md]

##本地化字符

如果你想要在弹出框中显示定制的字符, 有以下两种方式:

 - 修改 `plugin_review_res_project` 工程中的资源 (强烈推荐使用这种)

 - 也可以在 `sdkbox_config.json` 中配置字符串, 如下

```json
{
    "ios": {
        "Review":{
            ...
            "promptTitle":"cutom tile",
            "promptMessage":"this is custom message",
            "promptCancel":"取消",
            "promptRate":"rate打分",
            "promptRateLater":"稍后later"
            ...
        }
    }
}
```

在 `sdkbox_config.json` 中配置会关掉字符串本地化, 只有你不需要本地化时，可以使用这种方式.

## Amazon Market

如果你的 App 是针对 Amazon 市场, 请用如下配置:

```
"Review":{
    "android": {
        "Review":{

            ...

            "market": "amazon"
        }
    }
}
```

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]

