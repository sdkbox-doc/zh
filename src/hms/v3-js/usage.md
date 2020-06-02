### 初始化 HMS
* 在您的代码合适的地方调用 `init()` 完成初始化. 我们推荐在 `app.js` 中完成初始化.比如:
```javascript
sdkbox.HMS.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginHMSJS.hpp"
#include "PluginHMSJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保调用了如下函数:
```cpp
sc->addRegisterCallback(register_all_PluginHMSJS);
sc->addRegisterCallback(register_all_PluginHMSJS_helper);
```

### 登录

HMS 提供了三种登录方式:

* Signing In with HUAWEI ID(ID Token)

```javascript
sdkbox.HMS.login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```javascript
sdkbox.HMS.login(2);
```

* Silently Signing In With HUAWEI ID

静默登录只能在上一次使用前两种方式已经登录成功的情况下，才能在静态登录下成功

```javascript
sdkbox.HMS.login(0);
```

> 以上三种登录方式, 不管成功还是失败, 最终都会触发 `onLogin` 事件.

HMS 帐号相关的 [文档](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### 登出

```javascript
sdkbox.HMS.logout();
```

### 请求托管在 HMS 的商品

托管商品是指在 HMS 管理后台配置的商品.

```javascript
sdkbox.HMS.iapRequestProducts();
```
这个方法会触发 Listener 中的 `onIAPProducts` 方法

### 购买托管商品

```javascript
sdkbox.HMS.iapPurchase("coin");
```
这个方法会触发 Listener 中的 `onIAPPurchase` 方法

### 购买非托管商品

非托管商品是指未在 HMS 后台配置商品, 但使用 HMS IAP 的来支付.

```javascript
let productInfo = {
  priceType: 0, // 0:consumable 1:non-consumable 2:subscription
  productName: 'product name',
  productId: 'product id',
  amount: '1.00',
  currency: 'CNY',
  country: 'CN',
  sdkChannel: '1', // sdkChannel size must be between 0 and 4
  serviceCatalog: 'X58',
  reservedInfor: '{"a": 1, "b":"s"}', // reservedInfor must be json string
  developerPayload: 'payload1'
};
sdkbox.HMS.iapPurchaseWithPrice(JSON.stringify(productInfo));
```
这个方法会触发 Listener 中的 `onIAPPurchase` 方法

### 请求拥有的商品

请求当前拥有的商品的购买记录, 包括 不可消费，订阅商品 和 非消费的可消费商品.

```javascript
sdkbox.HMS.iapRequestOwnedPurchases();
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchases` 方法

### 消费商品

注意: 这里传的是 purchaseToken , 非不是商品名字或id

```javascript
sdkbox.HMS.iapConsume(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPPConsume` 方法

### 请求所有的消费记录

请求用户所有的消费记录

```javascript
sdkbox.HMS.iapRequestOwnedPurchaseRecords(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchaseRecords` 方法

### 处理HMS事件
您可以接收 `HMS` 事件, 不同事件对您的用户及 HMS 服务器做不同的处理.
```javascript
sdkbox.HMS.setListener({
    onLogin : function (code, msg) {
        // login event
    },
    onIAPReady: function(code, msg) {
        self.log('HMS Listener onIAPReady:' + code);
        cc.log(msg);
    },
    onIAPProducts: function(code, msg) {
        self.log('HMS Listener onIAPProducts:' + code);
        cc.log(msg);
    },
    onIAPPurchase: function(code, msg) {
        self.log('HMS Listener onIAPPurchase:' + code);
        cc.log(msg);
    },
    onIAPPConsume: function(code, msg) {
        self.log('HMS Listener onIAPPConsume:' + code);
        cc.log(msg);
    },
    onIAPOwnedPurchases: function(code, msg) {
        self.log('HMS Listener onIAPOwnedPurchases:' + code);
        cc.log(msg);
    },
    onIAPOwnedPurchaseRecords: function(code, msg) {
        self.log('HMS Listener onIAPOwnedPurchaseRecords:' + code);
        cc.log(msg);
    }
});
```
