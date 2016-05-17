## iOS 平台手动集成
拖拽下列 framework 从 `SdkboxAds` 插件包的 __plugins/ios__ 目录到您的 Xcode 工程中，在添加 frameworks 的时候，请勾选 `Copy items if needed` 。

> sdkbox.framework

> PluginSdkboxAds.framework

如果您没有添加下面这些系统库，您有需要添加它们：

> Security.framework

> AdSupport.framework

另外，每一个 AdUnit 需要的 *所有的* 库文件都需要被添加。
