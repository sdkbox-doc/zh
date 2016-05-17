<h1>LiveOps - 远程配置</h1>

## 远程配置是如何工作的？
当需要修改 SDKBOX 插件配置的时候，您需要修改 `sdkbox_config.json` 文件中的 JSON 代码，重新编译这个应用，并且重新向应用程序商店提交。为了解决这一问题， __Remote Configuration__ 允许您实时更新它的插件配置。举个例子，它将允许您改变 Google Analytics 的追踪代号，AdColony 的广告配置以及 IAP 的可购买项目，而不用重新编译以及发布您的应用。

![chart](/imgs/remote_config.jpg)

!!! 提示
    * 应用程序会自动获取最新的配置并且使它生效。这意味着在您更新配置并将它们发布到云端之后，每一个您应用的客户都会在下一次启动您的应用时获得更新。
    * 为保证安全，在应用程序正常运行期间，配置文件被本地保存在应用程序的私有目录。并且其内容被加密，哪怕该应用程序运行在 root 或者越狱模式下，该内容也不会被看到。

## 关于 Configuration Set 以及版本
* 一个 `Configuration Set` 可以包含多个配置版本，每个版本都有以下3种状态：
    * __Live__: 仅允许一个该状态的配置存在于 Configuration Set 中，并且它将是云端应用到 app 的默认配置。
    * __Debug__: 仅允许一个该状态的配置存在于 Configuration Set 中，并且它将是云端应用到 debug 模式下 app 默认配置。
    * __Draft__: 可以有多个该状态的配置，它们不能被任何应用程序访问。
* 每一个 `Configuration Set` 有一对 __token__ 以及 __secret__ 。它们用于保证 app 与 SDKBOX LiveOps 之间的安全通信。它们不能被改变。并且需要在 app 中配置，请参考 `在 app 中使用远程配置` 这一节。
* 一个 app 将通过指定的 token 应用相应的 `Live` 或者 `Debug` 版本的配置，如上面的流程图所示。
* 每一个 Configuration Set 针对一个平台。但是每个平台可以拥有多个 Configuration Set 。如果一个应用需要发布在 Apple 以及 Google Play上，您需要创建至少两个 Configuration Set 。如下所示：
![chart](/imgs/config_versions.jpg)

## 导入已经存在的应用程序配置
* 当您集成 SDKBOX 插件的时候，一个本地的 `sdkbox_config.json` 文件将会被添加到您的 app 中。它包含了插件的所有配置。
* 为了能让本地配置导入云端，我们提供了一个方便的功能。在您的 applications 页面，单击 “Import Sets” 按钮并且选择您本地的 `sdkbox_config.json` 文件并上传。所有您当前的配置将被载入到一系列新的 Configuration Set 中，每一个平台一个 Configuration Set 。
* 在导入配置之后，您应该让您的远程配置作为 __master__ 版本的配置并保持更新。您的本地拷贝版本仅仅会在网络不可用的时候使用。
* 通过导入本地配置，新生成的 Configuration Set 初始状态是 __Draft__ 的。它们在被您编辑然后发布到云端之前，将不能被访问。


## 在 app 中使用远程配置
* 通过将 `Configuration Set` 中的 __token__ 以及 __secret__ 传递给 __sdkbox::init()__ 函数并调用调用它，可以简单方便的在您的 app 中使用远程配置服务。
```
sdkbox::init( <application token>, <application secret> );
```
* 我们还提供了一种通过 LiveOps 更简单的修改代码的方法。从您的 applications 页面，单击 “Export Sets” 。然后选择您想部署的某一个平台下的配置文件。进行下列步骤：
    * 一个根据平台并且包含了 token/secret 的用于初始化 SDKBOX 的代码片段将会被生成。您可以将其拷贝粘贴到您 app 的 delegate 文件中。
    * 尽管有一个保持更新的 `sdkbox_config.json` 文件存储在云端。但是我们还是建议您在每次将应用发布到应用商店的时候更新本地内置的 `sdkbox_config.json` 文件。一旦您的网络连接不可用，那么本地的配置将会被默认启用。


## 编辑并且发布配置
* 一旦安装完成，您就可以在云端更新配置并且推送到您的 app 。
* 确保 Liveops 的配置处于 __Live__ 或者 __Debug__ 状态，以使其能被 app 下载并应用。
* 确保编辑了正确的配置，该配置的 token/secret 应该与网站上配置的一致。
