### 初始化 IAP
* 在你的代码合适的地方调用 `init()` 完成初始化. 我们推荐在 `app.js` 中完成初始化.比如:
```javascript
sdkbox.IAP.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginIAPJS.hpp"
#include "PluginIAPJSHelper.hpp"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保调用了如下函数:
```cpp
sc->addRegisterCallback(register_all_PluginIAPJS);
sc->addRegisterCallback(register_all_PluginIAPJS_helper);
```

### 获取最新的价格
在你的游戏开始时,最好先从商店中取最新的商品价格信息.

要获取最新的 IAP 数据,只需要简单地调用 `sdkbox.IAP.refresh()`.

> `onProductRequestSuccess` 购买成功会收到这个事件.

> `onProductRequestFailure` 购买失败事件.

### 购买
购买调用 `sdkbox.IAP.purchase(name)`

__注意:__ __name__ 是在你的配置文件中 `items` 项的名字,不是你在 iTunes 或 GooglePlay Store中的产品id.

> `onSuccess` 购买成功事件.

> `onFailure` 购买失败事件.

> `onCanceled` 用户取消购买会触发这个事件.

### 恢复购买
恢复购买调用 `sdkbox.IAP.restore()`.

> `onRestored` 恢复购买成功.

__注意:__ `onRestored` 可能会触发多次

### 处理付费事件
你可以接收 `IAP` 事件, 不同事件对你的用户及 IAP 服务器做不同的处理.
```Javascript
sdkbox.IAP.setListener({
    onSuccess : function (product) {
        //Purchase success
    },
    onFailure : function (product, msg) {
        //Purchase failed
        //msg is the error message
    },
    onCanceled : function (product) {
        //Purchase was canceled by user
    },
    onRestored : function (product) {
        //Purchase restored
    },
    onProductRequestSuccess : function (products) {
        //Returns you the data for all the iap products
        //You can get each item using following method
        for (var i = 0; i < products.length; i++) {
            // loop
        }
    },
    onProductRequestFailure : function (msg) {
        //When product refresh request fails.
    }
});
```
