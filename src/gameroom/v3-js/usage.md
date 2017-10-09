关于本章下面提到的方法的细节，你可以访问 [API Reference](#api_reference) 一节。并且如果你想进一步了解这些方法在 Facebook Gameroom SDK 中相应的细节，你可以参考 [Facebook Gameroom SDK 官方网页](https://developers.facebook.com/docs/games/gameroom/sdk) 。

### 初始化 Gameroom 插件

在你调用其他 API 之前，你应该在 `app.js` 中初始化插件。

```
sdkbox.PluginGameroom.init('your_facebook_app_id');
```

### 设置 Listener

与其他 SDKBOX 插件一样， 你需要设置一个 listener 对象去处理回调事件。

```
sdkbox.PluginGameroom.setListener({
    onLoginAccessTokenMsg: function (handle) {
    },

    onFeedShareMsg: function (handle) {
    },

    onPurchaseIAPMsg: function (handle) {
    },

    onHasLicenseMsg: funciton (handle) {
    },

    onAppRequestMsg: function (handle) {
    }
});
```

这个对象中的每一个回调函数将在下面的小节中解释。


### 用户登录

在插件初始化之后，当你的游戏在 Gameroom 运行时，你应该让玩家登录你的游戏并且获取玩家的信息。你可以使用简单的 `login()` 方法或者另一个稍复杂的 `loginWithScopes()` 方法去完成这一功能。

这两个方法的不同之处在于 `login()` 方法在完成用户登录时总是申请使用以下3种权限: `user_friends`，`email` 以及 `public_profile` 。

```
sdkbox.PluginGameroom.login()
```

而使用另一个方法 `loginWithScopes()` ，你可以在玩家登录时指定申请的权限。在下面的例子里，`user_friends` 和 `email` 权限将被申请使用。


```
sdkbox.PluginGameroom.loginWithScopes(2, ['public_profile', 'email']);
```

你也可以像下面的例子那样来检测用户是否已经完成登录：

```
ret = sdkbox.PluginGameroom.isLoggedIn();
```

玩家登录将会触发 listener 对象中的 `onLoginAccessTokenMsg` 回调。你可以像下面例子中那样从参数 `handle` 中的属性取得玩家的信息。

```
onLoginAccessTokenMsg: function (handle) {
    cc.log('============');
    cc.log('onLoginAccessTokenMsg');
    cc.log(JSON.stringify(handle, null, 2));
    if (handle.isValidToken) {
        self.showText('login successful');
    }
    else {
        self.showText('login failed');
    }
}
```

### 分享至 Facebook

在你的游戏中，你可以给玩家提供分享功能：

```
sdkbox.PluginGameroom.feedShare(
        '',
        'https://www.facebook.com',
        'Testing Link Name',
        'Testing Link Caption',
        'Testing Link Description',
        'http://www.pamperedpetz.net/wp-content/uploads/2015/09/Puppy1.jpg',
        ''
);
```

上面的例子将会分享一张图片到玩家的 Facebook 。

在分享发生之后，listener 对象里的 `onFeedShareMsg` 回调将会被调用。你可以通过 `handle` 的属性取到 `Post ID` 。

```
onFeedShareMsg: function (handle) {
    cc.log('============');
    cc.log('onFeedShareMsg');
    self.showText('onFeedShareMsg');
    cc.log('shared post id = ' + handle.postID);

}
```

### IAP

插件的 IAP 功能包括以下3种类型：

-   通过配置在 Facebook App 中的 product ID 进行 IAP 。

```
sdkbox.PluginGameroom.purchaseIAP(
        'sdkbox_product_1',
        1,
        1,
        1,
        '',
        '',
        ''
);
```

-   通过一个商品的 url 进行 IAP 。

```
sdkbox.PluginGameroom.purchaseIAPWithProductURL(
        'https://friendsmash-unity.herokuapp.com/payments/100coins.php',
        1,
        1,
        1,
        '',
        '',
        ''
);
```

-   购买付费版本或者许可证。

```
sdkbox.PluginGameroom.payPremium();
```

这3种类型的 IAP 都会触发 `onPurchaseIAPMsg` 回调。这里有一个例子说明了如何在这个回调中通过 `handle` 对象的属性得到 IAP 相关的结果。

```
onPurchaseIAPMsg: function (handle) {
    cc.log('============');
    cc.log('onPurchaseIAPMsg');
    self.showText('onPurchaseIAPMsg');
    cc.log('payment ID = '+ handle.paymentID);
    cc.log('amount = ' + handle.amount);
    cc.log('curency = ' + handle.currency);
    cc.log('purchase time = ' + handle.purchaseTime);
    cc.log('product ID = ' + handle.productID);
    cc.log('purchase token = ' + handle.purchaseToken);
    cc.log('quantity = ' + handle.quantity);
    cc.log('request id = ' + handle.requestID);
    cc.log('status = ' + handle.status);
    cc.log('signed req = ' + handle.signedReq);
    cc.log('error code = ' + handle.errorCode);
    cc.log('error msg = ' + handle.errorMsg);

}
```

另外，你可以调用 `hasLicense()` 方法去检测该玩家是否购买了许可证或者付费版。

```
sdkbox.PluginGameroom.hasLicense();
```

值得注意的是，这个方法将会触发 `onHasLicenseMsg` 回调。奇怪之处在于，你必须在这个回调中通过用 `handle` 对象的属性去取得许可证或者付费版的 ID 。（Facebook Gameroom SDK 要求这样做）

```
onHasLicenseMsg: function (handle) {
    cc.log('============');
    cc.log('onHasLicenseMsg');
    self.showText('onHasLicenseMsg');
    cc.log('has license = ' + handle.hasLicense);
}

```

### 发送 App 日志事件

你可以通过下面的方法将你的游戏事件日志记录到 Facebook Analytics：

```
sdkbox.PluginGameroom.logAppEvent('test_event_1', { 'key1': 'val1', 'key2': 'val2' });
sdkbox.PluginGameroom.logAppEventWithValueToSum('test_event_2', { 'key3': 'val3', 'key4': 'val4' }, 10.24);
```

The key-value pairs are carried in an JavaScript object. And if you intend to offer an extra value in an event, you should use `logAppEventWithValueToSum` method.
键值对数据存储在一个 JavaScript 对象中。如果你想在事件中提供额外的值，你应该使用 `logAppEventWithValueToSum()` 方法。

### 发送游戏请求

你可以使用下面的方法触发一个对话框以在你的游戏内发送游戏请求：

```
sdkbox.PluginGameroom.appRequest('hello, try this js demo.', '', '', 'faceboo_user_id_1, facebook_user_id_2', '', '', 20, '', 'hello');
```

通常情况下，你不需要设置用户 ID ，这样就可以让玩家在对话框里选择他想发送请求的朋友。

```
sdkbox.PluginGameroom.appRequest('hello, try this js demo.', '', '', '', '', '', 20, '', 'hello');
```

在游戏请求的回调里，你可以像下面这样得到请求的相关属性和结果：

```
onAppRequestMsg: function (handle) {
    cc.log('============');
    cc.log('onAppRequestMsg');
    self.showText('onAppRequestMsg');
    cc.log('objectID = ' + handle.objectID);
    cc.log('to user: ' + handle.toUser);
}
```
