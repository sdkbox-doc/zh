<h1>LiveOps - 服务器端订单校验</h1>

## 介绍
关于客户端的订单校验，您可以参考 [SDKBOX IAP 插件](../plugins/iap)，您也可以在 SDKBOX LiveOps 中使用服务器端订单校验。

一旦使用了这一功能，当发生购买时，它会自动判断使用 Google 或者 Apple 平台服务进行校验。不需要客户端或者开发者作任何代码的改动，这个购买收据将会被安全的校验。就和本地校验一样，会有两个公开的插件接口（回调）：`onSuccess()` 以及 `onFailure()` 。它们将被用于通知校验结果。

当远程订单校验失败，系统会自动回滚使用本地订单校验。比如当超时或者网络通信故障的时候。

!!!提示
    使用这一功能您需要
    1. 使用 IAP 的 [远程配置](./remote-confg) 功能。
    2. 在 sdkbox:IAP:init(); 之后调用 sdkbox:IAP:enableUserSideVerification(false);


## 远程校验流程

### iOS 平台流程
1. 玩家进行一次购买。
2. CompleteTransaction 已经被调用，并且拿到了加密后的收据。
3. 如果开发者请求一次收据校验（不管 App 是否已经开通远程配置功能）：
    1. onPayResult 将会伴随着 PaymentTransactionNeedsVerification 状态被调用。插件的 listener 将会得到加密后的商品订单信息，开发者能够进行自己的订单校验流程。
    2. 整个购买流程完毕。
4. 如果开发者没有请求订单校验：
    1. 如果应用程序没有开通远程配置功能：
        1. onPayResult 会伴随着 PaymentTransactionStatePurchased 状态被调用。
        2. 整个购买流程结束。
    2. 如果应用程序开通了远程配置功能：通过调用 checkAuthenticity 方法， 远程 IAP 校验将会开始并校验加密后的购买信息。
        1. 一个用于校验购买信息的请求将被发送到 sdkbox.com 服务器端。
        2. 如果超时或者其他错误在请求时发生， onPayResult 将会伴随着 kPaySuccessAndValidationError 状态被调用。这说明在校验服务器有错误发生。
        3. 如果这个请求被用户丢弃：onPayResult将会伴随着 kPaySuccessAndValidationError 状态被调用。（和上面的情况一样）
        4. 这个校验请求如果被正常处理，那么一个用 Json 作为格式的结果将会被返回：
            1. 如果校验失败：onPayResult 将会伴随着 kPaySuccessAndValidationNotAuthenticated 被调用。
            2. 如果校验成功：onPayResult 将会伴随着 kPaySuccessAndValidationAuthenticated 被调用。
5. 整个交易流程完成。

### Android 平台流程
1. 玩家进行一次购买。
2. 如果购买被取消，onPayResult 将会伴随着 PAYRESULT_CANCEL 被调用。
3. 如果购买发生错误， onPayResult 将会伴随着 PAYRESULT_FAIL 被调用。
4. 如果购买成功：
    1. 收据以及被加密的购买信息将会得到。
    2. 如果开发者请求订单校验，那么 onPayResult 将会被伴随着 PAYRESULT_NEEDS_VERIFICATION 被调用。然后收据和产品信息将会被传递给 listener，这些信息足够用于订单校验。
    3. 否则：
        1. 如果这个应用没有开通远程配置功能： 那么本地的校验流程将会开始：
            1. 应用程序的 private key 必须被设置在 sdkbox_config.json 文件中。
            2. 如果校验成功，onPayResult 将会伴随着 PAYRESULT_SUCCESS 被调用。
            3. 如果校验失败：onPayResult 将会伴随着 PAYRESULT_FAIL 被调用。
        2. 如果这个应用程序已经有了远程 Configuration Set: 那么远程的校验流程将会开始。
            1. 如果校验请求超时或者出错（两种情况都和网络状况有关），远程校验将会回退到本地校验。
            2. 如果这个校验请求被丢弃：onPayResult 将会伴随着 PAYRESULT_FAIL 被调用。
            3. 如果这个校验请求被正常处理：
                1. 如果校验失败，那么这个校验流程将回退到本地校验。
                2. 如果校验成功，onPayResult 将会伴随着 PAYRESULT_SUCCESS 被调用。
5. 整个交易流程完成。


## 安装

### Android Play
* 确保已经在您的 app 中使用 [Remote Configuration](./remote-config) 。
* 在 Android 平台上创建并且选择一个配置，并且在插件页面添加 __Essentials__ 下的 `Google Play IAP` 插件。并将 __Google Play__ 开发者平台下的应用程序 private key 填写正确。如果不提供 __private key__， 那么将总是进行本地校验。

### Apple App Store
* TBD
