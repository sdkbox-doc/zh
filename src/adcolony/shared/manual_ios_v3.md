## iOS 平台手动集成
拖拽下列 framework 从 `AdColony` 插件包的 __plugins/ios__ 目录到你的 Xcode 工程中，在添加 frameworks 的时候，请勾选 `Copy items if needed` 。

> sdkbox.framework

> PluginAdColony.framework

> AdColony.framework

上面的 frameworks 依赖于大量其他 frameworks。如果你没有添加它们，你也需要添加下列这些系统 frameworks：

> libz.1.2.5.dylib

> AdSupport.framework (Set to Optional)

> AudioToolbox.framework

> AVFoundation.framework

> CoreGraphics.framework

> CoreMedia.framework

> CoreTelephony.framework

> EventKit.framework

> EventKitUI.framework

> MediaPlayer.framework

> MessageUI.framework

> QuartzCore.framework

> Security.framework

> GameController.framework

> Social.framework (Set to Optional)

> StoreKit.framework (Set to Optional)

> SystemConfiguration.framework

> WebKit.framework (Set to Optional)

在以下位置添加两个单独的链接选项：
__Target -> Build Settings -> Linking -> Other Linker Flags__:

> -ObjC

> -fobjc-arc (this allows AdColony to use ARC even if your project does not)
