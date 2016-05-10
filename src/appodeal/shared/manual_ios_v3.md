## iOS 平台手动集成
拖拽下列 framework 从 `AdColony` 插件包的 __plugins/ios__ 目录到您的 Xcode 工程中，在添加 frameworks 的时候，请勾选 `Copy items if needed` 。

> sdkbox.framework

> PluginAppodeal.framework

> Appodeal.framework

> plugin_appodeal_res_bundle

上面的 frameworks 依赖于大量其他 frameworks。如果您没有添加它们，您也需要添加下列这些系统 frameworks：

> AdSupport.framework

> AudioToolbox.framework

> AVFoundation.framework

> CFNetwork.framework

> CoreFoundation.framework

> CoreGraphics.framework

> CoreImage.framework

> CoreLocation.framework

> CoreMedia.framework

> CoreMotion.framework

> CoreTelephony.framework

> EventKit.framework

> EventKitUI.framework

> libc++.tbd

> libsqlite3.tbd

> libxml2.2.tbd

> libz.tbd

> MediaPlayer.framework

> MessageUI.framework

> MobileCoreServices.framework

> QuartzCore.framework

> Security.framework

> Social.framework

> StoreKit.framework

> SystemConfiguration.framework

> Twitter.framework

> UIKit.framework

> WebKit.framework

> GameController.framework

