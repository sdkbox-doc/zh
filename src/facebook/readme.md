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

##FAQ
1. 切换 Facebook 登录方式，使用应用、浏览器方式登录, [清理 Safari Cookie](https://support.apple.com/en-us/HT201265)
2. 切换 Facebook 登录账号, [清理 Safari Cookie](https://support.apple.com/en-us/HT201265)

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

  [[FBSDKApplicationDelegate sharedInstance] application:application
                                      didFinishLaunchingWithOptions:launchOptions];
  app->run();
  return YES;
}

- (BOOL)application:(UIApplication *)application
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {

  BOOL handled = [[FBSDKApplicationDelegate sharedInstance] application:application
    openURL:url
    sourceApplication:options[UIApplicationOpenURLOptionsSourceApplicationKey]
    annotation:options[UIApplicationOpenURLOptionsAnnotationKey]
  ];
  // Add any custom logic here.
  return handled;
}

- (BOOL)application:(UIApplication *)application
            openURL:(NSURL *)url
  sourceApplication:(NSString *)sourceApplication
         annotation:(id)annotation {

  BOOL handled = [[FBSDKApplicationDelegate sharedInstance] application:application
    openURL:url
    sourceApplication:sourceApplication
    annotation:annotation
  ];
  // Add any custom logic here.
  return handled;
}

```

在 Xcode8 iOS10 模拟器上，不能登录：
```
Go to the `Project Target` and then `Capabilities` and switch `Keychain Sharing ON`.
```
http://stackoverflow.com/a/39788102/5443510


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

### ~~邀请朋友~~
- http://discuss.cocos2d-x.org/t/solved-invite-friends-with-using-cocos2dx-layer/34450

https://developers.facebook.com/docs/ios/change-log-4x/

> The App Invites feature has been deprecated. (4.28.0 - November 7, 2017)

## 使用

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]

## Facebook 编译问题

目前 SDKBox 使用的是 Facebook iOS SDK 7.1.1 的静态库.

Facebook iOS SDK 7.1.1 的静态库与 `Other Linker Flags` -> `-ObjC` 存在冲突.

如果编译遇到以下类似错误, 那很有可能是冲突引起的

```html
Could not find or use auto-linked library 'swiftCompatibilityDynamicReplacements'
Could not find or use auto-linked library 'swiftCore'
Could not find or use auto-linked library 'swiftQuartzCore'
Could not find or use auto-linked library 'swiftDispatch'
Could not find or use auto-linked library 'swiftAVFoundation'
Could not find or use auto-linked library 'swiftCoreMedia'
Could not find or use auto-linked library 'swiftCoreAudio'
Could not find or use auto-linked library 'swiftPhotos'
Could not find or use auto-linked library 'swiftCoreMIDI'
Could not find or use auto-linked library 'swiftCoreLocation'
Undefined symbol: protocol descriptor for Foundation._ErrorCodeProtocol
Undefined symbol: associated conformance descriptor for Foundation._ErrorCodeProtocol._ErrorType: Foundation._BridgedStoredNSError
Undefined symbol: base conformance descriptor for Foundation._BridgedStoredNSError: Foundation.CustomNSError
Undefined symbol: base conformance descriptor for Foundation._BridgedStoredNSError: Swift.Hashable
Undefined symbol: base conformance descriptor for Foundation._ErrorCodeProtocol: Swift.Equatable
Undefined symbol: associated conformance descriptor for Foundation._BridgedStoredNSError.Code: Foundation._ErrorCodeProtocol
Undefined symbol: associated conformance descriptor for Foundation._BridgedStoredNSError.Code: Swift.RawRepresentable
Undefined symbol: method descriptor for Foundation._BridgedStoredNSError.init(_nsError: __C.NSError) -> A
Undefined symbol: base conformance descriptor for Foundation.CustomNSError: Swift.Error
Undefined symbol: method descriptor for static Foundation.CustomNSError.errorDomain.getter : Swift.String
Undefined symbol: method descriptor for Foundation._ObjectiveCBridgeableError.init(_bridgedNSError: __shared __C.NSError) -> A?
Undefined symbol: method descriptor for Swift.Error._code.getter : Swift.Int
Undefined symbol: method descriptor for Swift.Error._userInfo.getter : Swift.AnyObject?
Undefined symbol: method descriptor for Swift.Error._getEmbeddedNSError() -> Swift.AnyObject?
Undefined symbol: protocol conformance descriptor for Swift.Int : Swift.FixedWidthInteger in Swift
Undefined symbol: type metadata for Swift.Int
Undefined symbol: protocol descriptor for Foundation.CustomNSError
Undefined symbol: static Swift._DictionaryStorage.allocate(capacity: Swift.Int) -> Swift._DictionaryStorage<A, B>
Undefined symbol: __swiftEmptyDictionarySingleton
```

### 解决方法A

* 去掉 `Project Setting` -> `Build Settings` -> `Linking` -> `Other Linker Flags` -> `-ObjC` 就可以解决这些错误

### 解决方法B

1. 如果你的工程不能去掉 `-ObjC` , 那你需要将 Facebook 静态库替换为[动态库](https://github.com/facebook/facebook-ios-sdk/releases/download/v7.1.1/FacebookSDK_Dynamic.framework.zip)

2. 解压并替换工程中的 Facebook 相关的文件 `FBSDK*.framework` 文件.

3. 调整 Xcode 设置, `Project Setting` -> `General` -> `Frameworks, Libraries, and Embedded Content` 下的 `FBSDK*.framework` 设置为 `Embed & Sign`


## Facebook 编译问题

如果编译遇到以下类似错误

```html
dyld: Library not loaded: @rpath/libswiftCore.dylib
```

可以尝试这个方法, 调整 Xcode 设置, `Project` -> `target` -> `Build Setting/All` -> `Always Embed Swift Standard Libraries` 设置为 `YES`


## Facebook Crash 问题

如果你遇到了如下错误:

```html
Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '+[NSError fbErrorFromReturnURLParameters:]: unrecognized selector sent to class 0x1e0bdf480'
```

可以尝试添加如下设置到 `Other Linker Flags`:

```
-ObjC
-force_load
${PROJECT_DIR}/Frameworks/FBSDKLoginKit.framework/FBSDKLoginKit
-force_load
${PROJECT_DIR}/Frameworks/FBSDKCoreKit.framework/FBSDKCoreKit
```

## Facebook 登录界面

现象: iOS 13 中, 横屏调用 FB 登录, 当弹出 “在Facebook中打开” 对话框时, 点击无效.

在 `Info.plist` 中的 `LSApplicationQueriesSchemes` 中的不应该包含 `fb-messenger-api20140430` .
`fb-messenger-api20140430` 是旧版FBSDK使用的. 新版可能应该是 `fb-messenger-share-api`
