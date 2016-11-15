[&#8249; Google Play Games Services Doc Home](./)

<h1>Google Play Games Services 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 安装
用如下命令来集成 SDKBOX IAP 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
$ sdkbox import gpg
```

## 安装后

### Android

#### 修改 AndroidManifest.xml

在你的 `AndroidManifest.xml` 中添加如下 meta-data.

```
<meta-data android:name="com.google.android.gms.games.APP_ID"
    android:value="@string/google_app_id" />
```

#### 修改 string.xml

添加如下文字到 `proj.android/res/values/string.xml` 中

```
<string name="google_app_id">777734739048</string>
```

请一定要把 `google_app_id` 对应的值修改为你自己的 App Id.

### iOS

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

添加如下 URL types 到你的工程中, 路径为 **your project > Info > URL Types**

+ URL 1:

    + Identifier: `com.google.ReverseClientId`
    + Url schemes: `com.googleusercontent.apps.777734739048-cdkbeieil19d6pfkavddrri5o19gk4ni`
    > (use this as sample, or put your very own application’s url scheme)

+ URL 2:

    + Identifier: `com.google.BundleId`
    + URL schemes: `com.sdkbox.gpg`
    > (use this as sample or put your own application’s bundle id)

#### 更多资料

在[官方文档](https://developers.google.com/games/services/cpp/gettingStartedIOS)中查看更多的相关信息

<<[../../shared/notice.md]

## 用法

### 前期准备

你必须在[Google Play Developer console](https://play.google.com/apps/publish) 创建一个自己的 app , 同时请确保所有的服务都是 enable 状态, 对应的配置也是配置正确的.

* 请根据[安装指南](https://developers.google.com/games/services/console/enabling)来为你的 app 安装 Google Play Games 服务.
* 安装完成后, 请根据[配置指南](https://developers.google.com/games/services/console/configuring) 来为你的 app 打开游戏服务.

> 提示: Google Play Game Services 默认使用 release keystore, 如果你想用 debug 模式来测试, 看下这个[方法](http://stackoverflow.com/questions/17612928/should-i-use-debug-keystore-with-google-play-game-services-during-development)

<<[usage.md]

<<[api-reference.md]

##手动集成
如果用 *SDKBox Installer* 安装失败了, 可以用手动的形式来集成. 如果用 *SDKBox Installer* 安装成功了，那么不用再手动来集成了.

这些步骤放在文档的最后，因为基本上你很少时候会有需要到他们. 当你要手动集成时，请在完成后，再看一个手动集成以上的这些步骤.


<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[../../shared/manual_integration_google_play_step.md]

<<[proguard.md]


