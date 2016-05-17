[&#8249; Facebook Doc Home](./)

<h1>Facebook 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
用如下命令来集成 SDKBOX Facebook 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
sdkbox import facebook
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->


### 额外的步骤

下面的步骤假定您已经注册为 Facbbook 开发者，并创建了一个 __APP__

#### iOS的步骤
* 依[iOS快速指导](https://developers.facebook.com/quickstarts/?platform=ios) 来配置您的 __APP__
* 在 `AppController.mm` 中修改如下代码，不是 `AppDelegate.cpp` 中

```
- (void)applicationDidBecomeActive:(UIApplication *)application {
  [FBSDKAppEvents activateApp];
}

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // ...

  //
  // **************************
  // !! 非常重要,非常重要,非常重要 !!
  // **************************
  //
  // 在 app->run() 前调用
  // [[FBSDKApplicationDelegate sharedInstance] application:didFinishLaunchingWithOptions

  BOOL ret = [[FBSDKApplicationDelegate sharedInstance] application:application
                                      didFinishLaunchingWithOptions:launchOptions];
  app->run();
  return ret;
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

#### Android的步骤
* 确保您的 `java -version` >= 1.7
* 依[Android快速指导](https://developers.facebook.com/quickstarts/?platform=android) 来配置您的 __APP__
* 在 `res/values/strings.xml` 中给 `facebook_app_id` 赋值为您的 `Facebook App ID`
* 在 `AndroidManifest.xml` 中给 `_replace_with_your_app_id_` 赋值为您的 `Facebook App ID`
* 在 `project.properties` 中给 target 赋值为 `target=android-15`


### JSON 配置
SDKBOX 安装器会为您自动生成一个 `sdkbox_config.json` 配置文件

下面给出一个例子,您可以打开/关闭Facebook的调试模式
```json
"Facebook":
{
    "debug":true
}
```

<<[sdkbox-config-encrypt.md]

## 使用

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
