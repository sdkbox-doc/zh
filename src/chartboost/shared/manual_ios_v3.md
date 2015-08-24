## iOS 平台手动集成
拖拽下列 framework 从 `Chartboost` 插件包的 __plugins/ios__ 目录到你的 Xcode 工程中，在添加 frameworks 的时候，请勾选 `Copy items if needed` 。

> sdkbox.framework

> PluginChartboost.framework

> Chartboost.framework

上面的 frameworks 依赖于其他 frameworks。如果你没有添加它们，你也需要添加下列这些 frameworks：

> Security.framework

> StoreKit.framework

> Foundation.framework

> CoreGraphics.framework

> UIKit.framework
