### 修改 Lua 代码
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 以包含如下必须头文件, 并调用 `HMS` 的lua注册函数.注意它们的参数 __lua_State*__ :
```cpp
#include "PluginHMSLua.hpp"
#include "PluginHMSLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginHMSLua(L);
  register_all_PluginHMSLua_helper(L);
}
```

### 初始化 HMS
修改您的lua代码去初始插件, 初始化可以在任何地方来做,但是必须要在您想使用插件的功能之前.
```lua
sdkbox.HMS:init()
```

### 登录

HMS 提供了三种登录方式:

* Signing In with HUAWEI ID(ID Token)

```lua
sdkbox.HMS:login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```lua
sdkbox.HMS:login(2);
```

* Silently Signing In With HUAWEI ID

静默登录只能在上一次使用前两种方式已经登录成功的情况下，才能在静态登录下成功

```lua
sdkbox.HMS:login(0);
```

> 以上三种登录方式, 不管成功还是失败, 最终都会触发 `onLogin` 事件.

HMS 帐号相关的 [文档](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### 登出

```lua
sdkbox.HMS:logout();
```

### 请求托管在 HMS 的商品

托管商品是指在 HMS 管理后台配置的商品.

```lua
sdkbox.HMS:iapRequestProducts();
```
这个方法会触发 Listener 中的 `onIAPProducts` 方法

### 购买托管商品

```lua
sdkbox.HMS:iapPurchase("coin");
```
这个方法会触发 Listener 中的 `onIAPPurchase` 方法

### 购买非托管商品

非托管商品是指未在 HMS 后台配置商品, 但使用 HMS IAP 的来支付.

```lua
local productInfo = {
  priceType = 0, -- 0:consumable 1:non-consumable 2:subscription
  productName = 'product name',
  productId = 'product id',
  amount = '1.00',
  currency = 'CNY',
  country = 'CN',
  sdkChannel = '1', -- sdkChannel size must be between 0 and 4
  serviceCatalog = 'X58',
  reservedInfor = '{"a": 1, "b":"s"}', -- reservedInfor must be json string
  developerPayload = 'payload1'
};
sdkbox.HMS:iapPurchaseWithPrice(JSON:encode(productInfo));
```
这个方法会触发 Listener 中的 `onIAPPurchase` 方法

### 请求拥有的商品

请求当前拥有的商品的购买记录, 包括 不可消费，订阅商品 和 非消费的可消费商品.

```lua
sdkbox.HMS:iapRequestOwnedPurchases();
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchases` 方法

### 消费商品

注意: 这里传的是 purchaseToken , 非不是商品名字或id

```lua
sdkbox.HMS:iapConsume(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPPConsume` 方法

### 请求所有的消费记录

请求用户所有的消费记录

```lua
sdkbox.HMS:iapRequestOwnedPurchaseRecords(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchaseRecords` 方法

### 处理HMS事件
您可以接收付费过程中的 `HMS` 事件.

```lua
sdkbox.HMS:setListener(function(args)
		if "onLogin" == args.event then
				local code = args.code
				local msg = args.msg
				dump(args, "onLogin:")
        else if "onIAPReady" == args.event then
                local code = args.code
                local msg = args.msg
        else if "onIAPProducts" == args.event then
                local code = args.code
                local msg = args.msg
        else if "onIAPPurchase" == args.event then
                local code = args.code
                local msg = args.msg
        else if "onIAPPConsume" == args.event then
                local code = args.code
                local msg = args.msg
        else if "onIAPOwnedPurchases" == args.event then
                local code = args.code
                local msg = args.msg
        else if "onIAPOwnedPurchaseRecords" == args.event then
                local code = args.code
                local msg = args.msg
		else
				print("unknow event ", args.event)
		end
end)
```
