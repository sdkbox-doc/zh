## iOS 平台手动集成
拖拽下列 framework 从 `InMobi` 插件包的 __plugins/ios__ 目录到你的 Xcode 工程中，在添加 frameworks 的时候，请勾选 `Copy items if needed`：

> sdkbox.framework

> PluginInMobi.framework

上面的 frameworks 依赖于其他 frameworks。如果你没有添加它们，你也需要添加下列这些 frameworks：

> AdSupport.framework

> AudioToolbox.framework

> AVFoundation.framework

> CoreLocation.framework

> CoreTelephony.framework

> EventKit.framework

> EventKitUI.framework

> MediaPlayer.framework

> MessageUI.framework

> Security.framework

> Social.framework

> StoreKit.framework

> SystemConfiguration.framework

> UIKit.framework

> SafariServices.framework

> GameController.framework

> libsqlite3.0.tbd

> libc++.tbd


