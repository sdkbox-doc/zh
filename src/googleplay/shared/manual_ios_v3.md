## iOS手动集成步骤

把 `GooglePlay` 包中 __plugins/ios__ 目录下的如下 frameworks 拖到你的 Xcode 工程中, 请确保 `Copy items if needed` 是选中状态:

> sdkbox.framework

> PluginGPG.framework

> GoogleAppUtilities.framework

> GoogleAuthUtilities.framework

> GoogleNetworkingUtilities.framework

> GoogleOpenSource.framework

> GooglePlus.bundle

> GooglePlus.framework

> GoogleSignIn.bundle

> GoogleSignIn.framework

> GoogleSymbolUtilities.framework

> GoogleUtilities.framework

> gpg.bundle

> gpg.framework


以上 framwork 是依赖于如下 framework 的，如果你的工程中还没有如下 framework , 添加上:

> AddressBook.framework

> AssetsLibrary.framework

> CoreData.framework

> CoreLocation.framework

> CoreMotion.framework

> CoreTelephony.framework

> CoreText.framework

> Foundation.framework

> MediaPlayer.framework

> QuartzCore.framework

> SafariServices

> Security.framework

> StoreKit

> Security.framework

> SystemConfiguration.framework

> libc++.dylib

> libz.dylib

在工程中添加如下 linker flag ,工程路径为 __Target -> Build Settings -> Linking -> Other Linker Flags__:

> -ObjC

### 代码修改

#### 修改 `proj.ios_mac/ios/AppController.mm`

在 `AppController.mm` 中添加如下代码:
```
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary *)options {
    return [[GIDSignIn sharedInstance] handleURL:url
                               sourceApplication:options[UIApplicationOpenURLOptionsSourceApplicationKey]
                                      annotation:options[UIApplicationOpenURLOptionsAnnotationKey]];
}
```

#### 设置自己的 Google Play Signin Listener (可选)

设置 GPG(Google Play Game Services) SignIn 的回调
这不是必选的，`SDKBox GPG` 已经在内部设置了对应的 Delegate, 当你在外面自己手动设置 GIDSignInUIDelegate 时，内部的就会被忽略

在外面自己手动设置 `GIDSignInUIDelegate` , 如下步骤:

修改 `proj.ios_mac/ios/RootViewController.h`
让 `RootviewController` 实现 `GIDSignInUIDelegate`:

```
#import <GoogleSignIn/GoogleSignIn.h>

// 在 RootViewController 类的定义中加上:
@interface RootViewController : UIViewController<GIDSignInUIDelegate>
```

设置 Google SignIn Listener

修改 `proj.ios_mac/ios/AppController.mm`

添加如下代码:
```
(BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
```

在 return 前添加如下代码:

```
    // _viewController could also be named
    //  viewController, depending of the project type.
    [GIDSignIn sharedInstance].uiDelegate = _viewController;
```

#### 添加 URL types

添加如下 URL types 到你的工程中, 路径位置 **your project > Info > URL Types**

+ URL 1:

    + Identifier: `com.google.ReverseClientId`
    + Url schemes: `com.googleusercontent.apps.777734739048-cdkbeieil19d6pfkavddrri5o19gk4ni`
    > (这里要使用你自己的 application URL scheme)

+ URL 2:

    + Identifier: `com.google.BundleId`
    + URL schemes: `com.sdkbox.gpg`
    > (这里要使用你自己的 application 包名)

#### 更多信息

在[官方文档](https://developers.google.com/games/services/cpp/gettingStartedIOS)上有更多信息
