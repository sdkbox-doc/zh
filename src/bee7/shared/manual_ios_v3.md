## Manual Integration For iOS
拖拽下列 framework 从 `Bee7` 插件包的 __plugins/ios__ 目录到您的 Xcode 工程中，在添加 frameworks 的时候，请勾选 `Copy items if needed` 。

> sdkbox.framework

> PluginBee7.framework

> Bee7GWResources.bundle

上面的 frameworks 依赖于大量其他 frameworks。如果您没有添加它们，您也需要添加下列这些系统 frameworks：

> MessageUI.framework

> CoreMedia.framework

> SystemConfiguration.framework

> StoreKit.framework

> AdSupport.framework

> libsqlite3.dylib

> CoreText.framework

> GameController.framework

> MediaPlayer.framework

在以下位置添加两个单独的链接选项：
__Target -> Build Settings -> Linking -> Other Linker Flags__:

> -ObjC

