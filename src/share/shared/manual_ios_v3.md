## iOS 平台手动集成
拖拽下列 framework 从 `Share` 插件包的 __plugins/ios__ 目录到您的 Xcode 工程中，在添加 frameworks 的时候，请勾选 `Copy items if needed` 。

> sdkbox.framework

> PluginShare.framework

> TwitterCore.framework

> TwitterKit.framework

> TwitterKitResources.bundle -> TwitterKit.framework/TwitterKitResources.bundle

> TwitterShareExtensionUIResources.bundle -> TwitterKit.framework/TwitterShareExtensionUIResources.bundle

如果您没有添加下面这些系统库，您有需要添加它们：

> Accounts.framework

> CoreText.framework

> CoreMedia.framework

> CoreData.framework

> Social.framework

> GameController.framework

> SystemConfiguration.framework

> MediaPlayer.framework

> MessageUI.framework

> CoreMotion.framework

> SafariServices.framework



