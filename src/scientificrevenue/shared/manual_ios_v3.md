## iOS 平台手动集成
拖拽下列 framework 从 `ScientificRevenue` 插件包的 __plugins/ios__ 目录到您的 Xcode 工程中，在添加 frameworks 的时候，请勾选 `Copy items if needed` 。

> sdkbox.framework

> ScientificRevenueSDK.framework

> PluginScientificRevenue.framework

如果您没有添加下面这些系统库，您有需要添加它们：

> Security.framework

> StoreKit.framework

> SystemConfiguration.framework

> AddressBook.framework

> CoreLocation.framework

> MediaPlayer.framework

> GameController.framework

> CFNetwork.framework

> CoreData.framework

> MobileCoreService.framework

添加一个链接选项 “-force_load ScientificRevenueSDK.framework/ScientificRevenue“ 。
