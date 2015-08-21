<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/facebook/v3-cpp
-->

#Facebook

## 集成
用如下命令来集成 SDKBOX Facebook 插件,请确保你可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import facebook
```

## 额外的步骤

下面的步骤假定你已经注册为 Facbbook 开发者，并创建了一个 __APP__

### iOS的步骤
* 依[iOS快速指导](https://developers.facebook.com/quickstarts/?platform=ios) 来配置你的 __APP__
* 在 `AppController.mm` 中修改如下代码，不是 `AppDelegate.cpp` 中

```
- (void)applicationDidBecomeActive:(UIApplication *)application {
  [FBSDKAppEvents activateApp];
}

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  return [[FBSDKApplicationDelegate sharedInstance] application:application
                                    didFinishLaunchingWithOptions:launchOptions];
}

- (BOOL)application:(UIApplication *)application
            openURL:(NSURL *)url
  sourceApplication:(NSString *)sourceApplication
         annotation:(id)annotation {
  return [[FBSDKApplicationDelegate sharedInstance] application:application
                                                         openURL:url
                                               sourceApplication:sourceApplication
                                                      annotation:annotation];
}
```

### Android的步骤
* 确保你的 `java -version` >= 1.7
* 依[Android快速指导](https://developers.facebook.com/quickstarts/?platform=android) 来配置你的 __APP__
* 在 `res/values/strings.xml` 中给 `facebook_app_id` 赋值为你的 `Facebook App ID`
* 在 `AndroidManifest.xml` 中给 `_replace_with_your_app_id_` 赋值为你的 `Facebook App ID`
* 在 `project.properties` 中给 target 赋值为 `target=android-15`

<<[extra-step.md]
<<[proguard.md]

## 配置
SDKBOX 安装器会为你自动生成一个 `sdkbox_config.json` 配置文件

下面给出一个例子,你可以打开/关闭Facebook的调试模式
```json
"Facebook":
{
    "debug":true
}
```

<<[sdkbox-config-encrypt.md]

##用法

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
