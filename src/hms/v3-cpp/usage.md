### 初始化 HMS
在您的工程中合适的地方初始化插件.我们推荐在 `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()` 中.确保包含了相关的头文件:
```cpp
#include "PluginHMS/PluginHMS.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::HMS::init();
}
```

### 登录

HMS 提供了三种登录方式:

* Signing In with HUAWEI ID(ID Token)

```cpp
sdkbox::HMS::login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```cpp
sdkbox::HMS::login(2);
```

* Silently Signing In With HUAWEI ID

静默登录只能在上一次使用前两种方式已经登录成功的情况下，才能在静态登录下成功

```cpp
sdkbox::HMS::login(0);
```

> 以上三种登录方式, 不管成功还是失败, 最终都会触发 `onLogin` 事件.

HMS 帐号相关的 [文档](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### 登出

```cpp
sdkbox::HMS::logout();
```

### 请求托管在 HMS 的商品

托管商品是指在 HMS 管理后台配置的商品.

```cpp
sdkbox::HMS::iapRequestProducts();
```
这个方法会触发 Listener 中的 `onIAPProducts` 方法

### 购买托管商品

```cpp
sdkbox::HMS::iapPurchase("coin");
```
这个方法会触发 Listener 中的 `onIAPPurchase` 方法

### 购买非托管商品

非托管商品是指未在 HMS 后台配置商品, 但使用 HMS IAP 的来支付.

```cpp
const std::string productInfo = R"(
{
  "priceType": 0, //0:consumable 1:non-consumable 2:subscription
  "productName": "product name",
  "productId": "product id",
  "amount": "1.00",
  "currency": "CNY",
  "country": "CN",
  "sdkChannel": "1", // sdkChannel size must be between 0 and 4
  "serviceCatalog": "X58",
  "reservedInfor": "{\"a\": 1, \"b\":\"s\"}", // reservedInfor must be json string
  "developerPayload": "payload1"
}
)";
sdkbox::HMS::iapPurchaseWithPrice(productInfo);
```
这个方法会触发 Listener 中的 `onIAPPurchase` 方法

### 请求拥有的商品

请求当前拥有的商品的购买记录, 包括 不可消费，订阅商品 和 非消费的可消费商品.

```cpp
sdkbox::HMS::iapRequestOwnedPurchases();
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchases` 方法

### 消费商品

注意: 这里传的是 purchaseToken , 非不是商品名字或id

```cpp
sdkbox::HMS::iapConsume(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPPConsume` 方法

### 请求所有的消费记录

请求用户所有的消费记录

```cpp
sdkbox::HMS::iapRequestOwnedPurchaseRecords(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchaseRecords` 方法

### 处理HMS事件
允许您接收 `HMS` 的事件.

* 继承这个类 `sdkbox::HMSListener`:
```cpp
    #include "PluginHMS/PluginHMS.h"
    class MyClass : public sdkbox::HMSListener
    {
    private:
        virtual void onLogin(int code, const std::string & msg) override;
        virtual void onIAPReady(int code, const std::string& msg) override;
        virtual void onIAPProducts(int code, const std::string& errorOrJson) override;
        virtual void onIAPPurchase(int code, const std::string& errorOrJson) override;
        virtual void onIAPPConsume(int code, const std::string& errorOrJson) override;
        virtual void onIAPOwnedPurchases(int code, const std::string& errorOrJson) override;
        virtual void onIAPOwnedPurchaseRecords(int code, const std::string& errorOrJson) override;
    }
```

* 创建一个监听类来接收回调事件:
```cpp
sdkbox::HMS::setListener(listener);
```
