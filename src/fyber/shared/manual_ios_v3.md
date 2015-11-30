## iOS 平台手动集成
拖拽下列 framework 从 `Fyber` 插件包的 __plugins/ios__ 目录到你的 Xcode 工程中，在添加 frameworks 的时候，请勾选 `Copy items if needed` 。

> sdkbox.framework

> PluginFyber.framework

上面的 frameworks 依赖于大量其他 frameworks。如果你没有添加它们，你也需要添加下列这些系统 frameworks：

> AdSupport.framework

> CoreGraphics.framework

> CoreLocation.framework

> CoreTelephony.framework

> MediaPlayer.framework

> QuartzCore.framework

> StoreKit.framework

> SystemConfiguration.framework

> Security.framework

> CFNetwork.framework

在以下位置添加两个单独的链接选项：
__Target -> Build Settings -> Linking -> Other Linker Flags__:

> -force_load PluginFyber.framework/PluginFyber

