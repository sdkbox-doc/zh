<h1>SDKBOX LiveOps</h1>

## 介绍
__SDKBOX LiveOps__ 能让开发者利用云端的服务进行 [远程配置](./remote-config.md) 实时更新，服务端 [IAP 订单校验](./receipt-verification.md)，以及云端即时 [游戏内商店购买项目配置](catalog-management) 。LiveOps 能帮助开发者快速拓展应用程序功能。

!!! 提示
    当您使用 SDKBOX 集成插件的时候， LiveOps 是一个可选的步骤。所有的 SDBOX 插件均可以在不使用 Liveops 功能的情况下, 在本地正常使用。

## 使用 LiveOps
1. 登录 SDKBOX 官方网站 [SDKBOX.com](http://sdkbox.com) 。
2. 使用 [installer](/installer) 自动为您的 app 集成插件，或者您可以通过在 [这里](http://sdkbox.com/integrations) 下载插件包并手动集成。
3. 单击页面右上角您的登录名字或头像 -> 选择 “My Application” -> 单击 “New application"，填入 app 名字以及其他信息创建一个 Application 。
![](../imgs/login.png)
4. 利用页面的 "__Import__" 功能从您的工程中上传 `sdkbox_config.json` 文件。这将会为每一个平台的 app store 创建一个 __configuration set__ 。
![](../imgs/import.png)
5. 选择 "__Export__" 功能并且根据指示将您的 app 客户端与 LiveOps 的云端服务绑定起来。
![](../imgs/export.png)

!!! 提示
    新创建的 configuration sets 仍然是处于 __Draft__ 状态（没有真正将配置发布到云端）。在您编辑并且将它们发布到云端之前，您的应用程序客户端不能访问它们。（更多的细节请访问：[学习远程实时配置更新](./remote-config.md)）

