<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/vungle/v3-cpp
-->

# Vungle

## 集成
在你确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX Vungle 插件。
```bash
sdkbox import vungle
```

## 额外的步骤
<<[extra-step.md]
<<[proguard.md]

## 配置
SDKBOX Installer 将会自动在你的 `sdkbox_config.json` 中插入一个配置样例。请修改这份配置样例，使其能用于你自己的 app 。

对于一个 Vungle 插件的配置样例，你需要将其中的 `<vungle id>` 替换成你特定的 [Vungle](http://vungle.com) 发布帐号的ID。
如下是一个在 IOS 平台，添加 Vungle 插件的样例：
```json
"Vungle" :
{
    "id":"<vungle id>",
    "ads":{
        "video":{

        },
        "reward":{
            "incentivized" : true
        }
    }
}
```

因为多了 __sound__ 和 __backbutton__ 两个选项，在 Android 平台上添加 Vungle 插件会有些许不同。这里有一个在 Android 平台上添加 Vungle 插件的配置样例：
```json
"Vungle" :
{
    "id":"<vungle id>",
    "ads":{
        "video":{
            "sound" : true,
            "backbutton" : true
        },
        "reward":{
            "sound" : false,
            "backbutton" : false,
            "incentivized" : true
        }
    }
}
```

## 使用
<<[usage.md]

<<[api-reference.md]
