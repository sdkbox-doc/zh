<h1>即时可购买项目管理</h1>

Apple's AppStore 以及 Google‘s Play 都允许移动开发者通过 web 开发者控制台创建 IAP 购买项目。一般情况这些项目都由名字，类型以及价格组成。SDKBOX LiveOps 允许您在云端即时配置哪些项目可以在您的 app 中被出售。

比如在您的 app 中有一个名叫 ”一箱金币“ 的可购买项目，售价 $3.99 。为了迎接假期，您打算把它的价格降低到 $0.99  。我们将用 [SDKBOX IAP 示例工程](https://github.com/sdkbox/sdkbox-iap-sample) 向您展示如何实现这一降价活动而不用重新发一个版本。

## 安装示例工程
* 克隆 github 仓库 [SDKBOX IAP 示例工程](https://github.com/sdkbox/sdkbox-iap-sample)
* 编译生成该工程。您可以选择 C++, Lua 或者 Javascript 语言。下面的步骤中我们以 Javascript 语言为例。
* 在 xcode console 中， 当 app 启动的时候所有的可购买项目初始化的信息都会被显示。其中有一个可购买项目叫做 “一箱金币”，售价 $3.99 。我们将在接下来修改它的价格。

## 远程配置
* 打开 AppDelegate.cpp 文件， 您能找到如下的代码：`sdkbox::init(...)` 。这句代码的函数调用可以实现让 app 使用远程配置。现在它是使用本地配置的。
* 访问 [sdkbox.com](https://www.sdkbox.com)，创建一个 application，并且从您本地的示例工程，上传 `sdkbox_config.json`。记住在上传后将其发布到云端。
* Overwrite the token and secret in the AppDelegate.cpp the yours which were generated with the new application on sdkbox.com
* 将 sdkbox.com 上生成 application 的 token 和 secret 写到 AppDelegate.cpp 文件中。
* [学习更多关于远程实施配置更新的细节](./remote-config)

## 测试
* 现在您可以准备开始测试即时可购买项目管理了。
* 访问 sdkbox.com -> My Applications -> App -> iOS config -> iOS IAP Plugin 。
您应该可以看到下列的从本地示例工程上传的可购买项目配置：
![](../imgs/IAP_products.png)
* 其中名字是 `coin_package` 的项目对应着 `com.cocos2dx.plugintest2`，价格是 $3.99 。
* 单击并且编辑这一项目，修改它的 ID 为 `com.cocos2dx.sale.1` 。如下：
![](../imgs/IAP_products_sale.png).
* 保存这一配置并且将其发布到云端。
* 现在，重启您的 app 。您应该可以看到可购买项目的初始化信息，“coin_package” 已经被修改为了促销价格 $0.99 。
