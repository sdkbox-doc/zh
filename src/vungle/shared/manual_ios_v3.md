## iOS 平台手动集成
拖拽下列 framework 从 `Vungle` 插件包的 __plugins/ios__ 目录到你的 Xcode 工程中，在添加 frameworks 的时候，请勾选 `Copy items if needed` 。

> sdkbox.framework

> PluginVungle.framework

> VungleSDK.framework

上面的 frameworks 依赖于大量其他 frameworks。如果你没有添加它们，你也需要添加下列这些系统 frameworks：

> AdSupport.framework

> AudioToolbox.framework

> AVFoundation.framework

> CFNetwork.framework

> CoreGraphics.framework

> CoreMedia.framework

> Foundation.framework

> libz.dylib

> libsqlite3.dylib

> MediaPlayer.framework

> QuartzCore.framework

> Security.framework

> StoreKit.framework

> SystemConfiguration.framework

> UIKit.framework
