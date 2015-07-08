
#### 2 初始化 IAP

* 修改 `AppDelegate.cpp` 包括以下头文件:
```cpp
#include "PluginIAPLua.hpp"
#include "PluginIAPLuaHelper.hpp"
```

* 修改 `AppDelegate.cpp` 在函数 `applicationDidFinishLaunching` 中注册IAP的Lua绑定:
```cpp
lua_State *tolua_s = pStack->getLuaState();
register_all_PluginIAPLua(tolua_s);
register_all_PluginIAPLua_helper(tolua_s);
```

* 在你的代码中调用 `ssdkbox.IAP:init()` 来完成初始化


#### 3 获取最新的商品信息
当你的游戏启动时,最好获取一次最新商品信息
要获取商品信息,可以调用 `sdkbox.IAP:refresh()`.

> `onProductRequestSuccess` 获取成功,会收到这个回调

> `onProductRequestFailure` 获取失败

#### 4 购买
购买调用接口 `sdkbox.IAP.purchase(name)`

__提示:__ __name__ 是你在 `sdkbox_config.json` 中的 `items` 项存放在的名字, 而不是你在 iTunes 或 GooglePlay Store 的商品名字

> `onSuccess` 购买成功.

> `onFailure` 购买失败.

> `onCanceled` 用户取消购买.

#### 5 恢复购买
恢复购买调用 `sdkbox.IAP:restore()`.

> `onRestored` 恢复成功

__Note:__ `onRestored` 这个回调可能不至只有一次

#### 6 处理购买事件
允许你接收处理游戏中 `IAP` 返回的各种事件

* 注册lua script listener:
```lua
sdkbox.IAP:setListener(function(args)
        if "onSuccess" == args.event then
                local product = args.product
                dump(product, "onSuccess:")
        elseif "onFailure" == args.event then
                local product = args.product
                local msg = args.msg
                dump(product, "onFailure:")
                print("msg:", msg)
        elseif "onCanceled" == args.event then
                local product = args.product
                dump(product, "onCanceled:")
        elseif "onRestored" == args.event then
                local product = args.product
                dump(product, "onRestored:")
        elseif "onProductRequestSuccess" == args.event then
                local products = args.products
                dump(products, "onProductRequestSuccess:")
        elseif "onProductRequestFailure" == args.event then
                local msg = args.msg
                print("msg:", msg)
        else
                print("unknow event ", args.event)
        end
end)
```
