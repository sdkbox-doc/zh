<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/soomlagrow/v3-cpp
-->

# SoomlaGrow
SoomlaGrow 可以收集你的应用中的插件使用情况,现在支持 `Facebook` 和 `IAP` 插件

## 集成
在您确保正确安装了 SDKBOX installer 的情况下，运行下面的命令来集成 SDKBOX SoomlaGrow 插件。
```bash
$ sdkbox import soomlagrow
```

## Android 的额外步骤
<<[extra-step.md]
<<[proguard.md]

## 配置
SDKBOX 安装器会为你自动生成一个配置文件 `res/sdkbox_config.json`,在你使用前,请修改里面的值为你自己的应用.

下面给给一个 SoomlaGrow 的配置,你需要注册 [__Soomla ID__](http://soom.la/)帐号信息，然后替换配置文件中的 `<game key>` 和 `<envkey id>` 项.
```json
"SoomlaGrow":{
            "GameKey":"0cbc07e3-0f0c-4b68-bb0c-061c1b5fb553",
            "EnvKey":"8b865add-4541-4db1-be18-f6c7e5e00564"
        }
```

<<[sdkbox-config-encrypt.md]

## 用法
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]
