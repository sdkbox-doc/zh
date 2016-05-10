## iOS 平台手动集成
拖拽下列 framework 从 `Kochava` 插件包的 __plugins/ios__ 目录到您的 Xcode 工程中，在添加 frameworks 的时候，请勾选 `Copy items if needed` 。

> sdkbox.framework

> PluginKochava.framework

上面的 frameworks 依赖于其他 frameworks。如果您没有添加它们，您也需要添加下列这些 frameworks：

> Security.framework

> SystemConfiguration.framework

> UIKit.framework

> Foundation.framework

> AdSupport.framework

> iAd.framework

> CoreLocation.framework
