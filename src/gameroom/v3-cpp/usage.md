关于本章下面提到的方法的细节，你可以访问 [API Reference](#api_reference) 一节。并且如果你想进一步了解这些方法在 Facebook Gameroom SDK 中对应的细节，你可以参考 [Facebook Gameroom SDK 官方网页](https://developers.facebook.com/docs/games/gameroom/sdk) 。

### 初始化 Gameroom 插件

在你调用其他 API 之前，你应该初始化插件。我们建议你在 `AppDelegate::applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 函数中调用初始化语句。并且确保你包含了正确的头文件：

```
#ifdef SDKBOX_ENABLED
#include "PluginGameroom.h"
#endif


bool AppDelegate::applicationDidFinishLaunching() {
#ifdef SDKBOX_ENABLED
    // fill your Facebook Application ID
    sdkbox::PluginGameroom::init("1234567890");
#endif
}
```

### 设置 Listener

与其他 SDKBOX 的插件一样，你需要设置一个 listener 类去处理回调事件。

```
sdkbox::PluginGameroom::setListener(pointer_to_listener_class);
```

这个 listener 类应该继承至 `sdkbox::GameroomListener` 。

```
class HelloWorldListener : public sdkbox::GameroomListener
{
    public:
        // ...

        virtual void onLoginAccessTokenMsg(sdkbox::AccessTokenHandle);
        virtual void onFeedShareMsg(sdkbox::FeedShareHandle);
        virtual void onPurchaseIAPMsg(sdkbox::PurchaseHandle);
        virtual void onHasLicenseMsg(sdkbox::HasLicenseHandle);
        virtual void onAppRequestMsg(sdkbox::AppRequestHandle);

};
```

这个类中的每一个回调函数将在下面的小节中解释。

### 用户登录

在插件初始化之后，当你的游戏在 Gameroom 运行时，你应该让玩家登录你的游戏并且获取玩家的信息。你可以使用简单的 `login()` 方法或者另一个稍复杂的 `loginWithScopes()` 方法去完成这一功能。

这两个方法的不同之处在于 `login()` 方法在完成用户登录时总是申请使用以下3种权限: `user_friends`，`email` 以及 `public_profile` 。

```
SDKBOX::PluginGameroom::login();
```

而使用另一个方法 `loginWithScopes()` ，你可以在玩家登录时指定申请的权限。在下面的例子里，`user_friends` 和 `email` 权限将被申请使用。

```
std::vector<std::string> loginScopes{ "user_friends", "email" };
sdkbox::PluginGameroom::loginWithScopes(2, loginScopes);
```

你也可以像下面的例子那样来检测用户是否已经完成登录：

```
auto ret = sdkbox::PluginGameroom::isLoggedIn();
if (!ret) {
    // do something
}
```

玩家登录将会触发 listener 类中的 `onLoginAccessTokenMsg` 回调。你可以通过使用下面例子中的一些方法从回调函数的参数 `accessTokenHandle` 中取得玩家的信息。

```
void HelloWorld::onLoginAccessTokenMsg(sdkbox::AccessTokenHandle accessTokenHandle) {
    auto isValid = sdkbox::PluginGameroom::accessTokenIsValid(accessTokenHandle);
    if (!isValid) {
        // user not logged in
        return;
    }
    auto userid = sdkbox::PluginGameroom::accessTokenGetUserID(accessTokenHandle);

    char token_string[512];
    auto size = sdkbox::PluginGameroom::accessTokenGetTokenString(accessTokenHandle, token_string, 512);
    auto expiration_timestamp = sdkbox::PluginGameroom::accessTokenGetExpirationTimestamp(accessTokenHandle);

    fbgLoginScope permissions[512];
    auto permission_size = sdkbox::PluginGameroom::accessTokenGetPermissions(accessTokenHandle, permissions, 512);

    ::CCLOG(
        "OnLoginAccessTokenMsg, User ID: %lld\\nAccess Token: %s\\nExpiration Timestamp: %lld, Permission Count: %zu\\nPermissions: ",
        (long long)userid,
        token_string,
        (long long)expiration_timestamp,
        permission_size
    );

    for (size_t i = 0; i < permission_size; i++) {
        ::CCLOG("%s", sdkbox::PluginGameroom::loginScopeToString(permissions[i]));
    }
    ::CCLOG("\\n");
}
```

### 分享至 Facebook

在你的游戏中，你可以给玩家提供分享功能：

```
sdkbox::PluginGameroom::feedShare(
    nullptr,
    "https://www.facebook.com",
    "Testing Link Name",
    "Testing Link Caption",
    "Testing Link Description",
    "http://www.pamperedpetz.net/wp-content/uploads/2015/09/Puppy1.jpg",
    nullptr
);

```

上面的例子将会分享一个图片到玩家的 Facebook 。

在分享发生之后，listener 类里的 `onFeedShareMsg` 回调将会被调用。你可以通过 `feedShareGetPostID()` 方法从它的参数 `feedShareHandle` 中取到 `Post ID` 。

```
void HelloWorld::onFeedShareMsg(sdkbox::FeedShareHandle feedShareHandle) {
    auto postId = sdkbox::PluginGameroom::feedShareGetPostID(feedShareHandle);
    ::CCLOG(
        "onFeedShareMsg, Feed Share Post ID: %ld\\n",
        (long)postId
    );
}
```

### IAP

插件的 IAP 功能包括以下3种类型：

-   IAP with a product ID configured in your Facebook App.
-   通过配置在 Facebook App 中的 product ID 进行 IAP 。

```
sdkbox::PluginGameroom::purchaseIAP(
    "sdkbox_product_2",
    1,
    1,
    1,
    nullptr,
    nullptr,
    nullptr
);
```

-   通过一个商品的 url 进行 IAP 。

```
sdkbox::PluginGameroom::purchaseIAPWithProductURL(
    "https://friendsmash-unity.herokuapp.com/payments/100coins.php",
    1,
    1,
    1,
    nullptr,
    nullptr,
    nullptr
);
```

-   购买付费版本或者许可证。

```
sdkbox::PluginGameroom::payPremium();
```

这3种类型的 IAP 都会触发 `onPurchaseIAPMsg` 回调。这里有一个例子说明了如何在这个回调中通过 `handle` 对象的属性得到 IAP 相关的结果。

```
void HelloWorld::onPurchaseIAPMsg(sdkbox::PurchaseHandle payHandle) {
    size_t size;
    char paymentId[512];
    size = sdkbox::PluginGameroom::purchaseGetPaymentID(payHandle, paymentId, 512);

    auto amount = sdkbox::PluginGameroom::purchaseGetAmount(payHandle);

    char currency[512];
    size = sdkbox::PluginGameroom::purchaseGetCurrency(payHandle, currency, 512);

    auto purchaseTime = sdkbox::PluginGameroom::purchaseGetPurchaseTime(payHandle);

    char productId[512];
    size = sdkbox::PluginGameroom::purchaseGetProductID(payHandle, productId, 512);

    char purchaseToken[512];
    size = sdkbox::PluginGameroom::purchaseGetPurchaseToken(payHandle, purchaseToken, 512);

    auto quantity = sdkbox::PluginGameroom::purchaseGetQuantity(payHandle);

    char requestId[512];
    size = sdkbox::PluginGameroom::purchaseGetRequestID(payHandle, requestId, 512);

    char status[512];
    size = sdkbox::PluginGameroom::purchaseGetStatus(payHandle, status, 512);

    char signedRequest[512];
    size = sdkbox::PluginGameroom::purchaseGetSignedRequest(payHandle, signedRequest, 512);

    auto errorCode = sdkbox::PluginGameroom::purchaseGetErrorCode(payHandle);

    char errorMessage[512];
    size = sdkbox::PluginGameroom::purchaseGetErrorMessage(payHandle, errorMessage, 512);

    ::CCLOG(
        "onPurchaseIAPMsg, Purchase Handle: %s\\nAmount: %d\\nCurrency: %s\\nPurchase Time: %lld\\n"
        "Product Id:%s\\nPurchase Token: %s\\nQuantity: %d\\nRequest Id: %s\\n"
        "Status: %s\\nSignedRequest: %s\\nError Code: %lld\\nErrorMessage: %s\\n",
        paymentId,
        (int)amount,
        currency,
        (long long)purchaseTime,
        productId,
        purchaseToken,
        (int)quantity,
        requestId,
        status,
        signedRequest,
        (long long)errorCode,
        errorMessage
    );
}
```

另外，你可以调用 `hasLicense()` 方法去检测该玩家是否购买了许可证或者付费版。

```
sdkbox::PluginGameroom::hasLicense();
```

值得注意的是，这个方法将会触发 `onHasLicenseMsg` 回调。奇怪之处在于，你必须在这个回调中用 `purchaseGetLicense()` 方法去取得许可证或者付费版的 ID 。（Facebook Gameroom SDK 要求这样做）

```
void HelloWorld::onHasLicenseMsg(sdkbox::HasLicenseHandle hasLicenseHandle) {
    auto hasLicense = sdkbox::PluginGameroom::purchaseGetLicense(hasLicenseHandle);
    ::CCLOG(
            "onHasLicenseMsg, Has License: %llu",
            hasLicense
    );
}
```

### 发送 App 日志事件

你可以通过下面的方法将你的游戏事件日志记录到 Facebook Analytics：

```
auto formData = sdkbox::PluginGameroom::formDataCreateNew();
char key[sdkbox::FBG_BUFFER_SIZE]{"sdkbox_key"};
char value[sdkbox::FBG_BUFFER_SIZE]{"3.1415"};
sdkbox::PluginGameroom::formDataSet(formData, key, sdkbox::FBG_BUFFER_SIZE, value, sdkbox::FBG_BUFFER_SIZE);
sdkbox::PluginGameroom::logAppEvent("test_event", formData);

::CCLOG("Gameroom Send App Event with sum value");
sdkbox::PluginGameroom::logAppEventWithValueToSum("test_event", formData, 1024.2);
sdkbox::PluginGameroom::formDataDispose(formData);
```

键值对数据存储在 `FormData` 结构中。如果你想在事件中提供额外的值，你应该使用 `logAppEventWithValueToSum()` 方法。

### 发送游戏请求

你可以使用下面的方法触发一个对话框以在你的游戏内发送游戏请求：

```
sdkbox::PluginGameroom::appRequest(
    "hello world, try this gameroom sdk demo.",
    nullptr,
    nullptr,
    "faceboo_user_id_1,facebook_user_id_2",
    nullptr,
    nullptr,
    20,
    nullptr,
    "hello"
);
```

通常情况下，你不需要设置用户 ID ，这样就可以让玩家在对话框里选择他想发送请求的朋友。

```
sdkbox::PluginGameroom::appRequest(
    "hello world, try this gameroom sdk demo.",
    nullptr,
    nullptr,
    nullptr,
    nullptr,
    nullptr,
    20,
    nullptr,
    "hello"
);
```

在游戏请求的回调里，你可以像下面这样得到请求的相关属性和结果：

```
void HelloWorld::onAppRequestMsg(fbgAppRequestHandle appRequestHandle) {
    char objectID[sdkbox::FBG_BUFFER_SIZE];
    //auto size = sdkbox::PluginGameroom::appRequestGetRequestObjectID(appRequestHandle, objectID, sdkbox::FBG_BUFFER_SIZE);
    auto size = fbg_AppRequest_GetRequestObjectId(appRequestHandle, objectID, sdkbox::FBG_BUFFER_SIZE);
    ::CCLOG("onAppRequestMsg");
    ::CCLOG("size = %lu\\n", size);  // return 0 here, indicating that appRequestHandle is invalid.

    char toUser[sdkbox::FBG_BUFFER_SIZE];
    size = sdkbox::PluginGameroom::appRequestGetTo(appRequestHandle, toUser, sdkbox::FBG_BUFFER_SIZE);
    ::CCLOG("size = %lu\\n", size);

    ::CCLOG(
        "object id: %s, to user: %s",
        objectID,
        toUser
    );
}
```
