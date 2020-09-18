[&#8249; SignInWithApple Doc Home](./)

<h1>Sign in with Apple 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
用如下命令来集成 SDKBOX SignInWithApple 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import signinwithapple
```

<<[../../shared/notice.md]

## 额外步骤

安装完成后, 请在 Xcode 中添加 `Sign In with Apple` Capability. 添加路径如下: `Xcode` -> `Signing & Capabilities` -> `+Capability` -> `Sign In with Apple`.

### JSON 配置
SDKBOX 安装器会自动在您的工程中添加一个样例配置文件`sdkbox_config.json`.在您编译工程前,请修改里面的参数,用您自己的应用信息

这里SignInWithApple的配置样例.

```json
"ios" :
{
    "SignInWithApple":{
    }
},
"android":
{
    "SignInWithApple":{
    }
}
```

### Android 测试

-   SignInWithApple 不支持 Android 平台, 在 Android 其实是一个空的实现

<<[sdkbox-config-encrypt.md]

## 使用

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]
