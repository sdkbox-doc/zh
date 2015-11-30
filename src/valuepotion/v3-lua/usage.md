### 注册 Lua 函数
* 修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 
```cpp
#include "PluginValuePotionLua.hpp"
#include "PluginValuePotionLuaHelper.h"
```

```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginValuePotionLua(L);
  register_all_PluginValuePotionLua_helper(L);
}
```

### 初始化 Valuepotion
修改你的lua代码用 `init()` 初始化插件. 这个可以在任何地方调用,但是必须在你要想使用 ValuePotion 的功能之前.
```lua
sdkbox.PluginValuePotion:init()
```

### 使用 Valuepotion

```lua
sdkbox.PluginValuePotion:init()
sdkbox.PluginValuePotion:setTest(true)
if not sdkbox.PluginValuePotion:hasCachedInterstitial("default") then
    sdkbox.PluginValuePotion:cacheInterstitial("default")
end

sdkbox.PluginValuePotion:trackEvent("test event")
sdkbox.PluginValuePotion:trackEvent("test event with value 23", 23)
sdkbox.PluginValuePotion:trackEvent("category", "event name", "label", 45)

sdkbox.PluginValuePotion:trackPurchaseEvent("test event", 56, "RMB", "order id", "product id")
sdkbox.PluginValuePotion:trackPurchaseEvent("test event", 67, "USD", "order id", "product id", "campaign id", "content id")
sdkbox.PluginValuePotion:trackPurchaseEvent("categroy", "event name", "label", 78, "ILY", "order id", "product id", "campaign id", "content id");

sdkbox.PluginValuePotion:userinfo("id", "user id")
sdkbox.PluginValuePotion:userinfo("serverid", "server id")
sdkbox.PluginValuePotion:userinfo("birth", "19991111") -- YYYYMMDD
sdkbox.PluginValuePotion:userinfo("gender", "M")
sdkbox.PluginValuePotion:userinfo("level", "9")
sdkbox.PluginValuePotion:userinfo("firends", "3")
sdkbox.PluginValuePotion:userinfo("accounttype", "facebook")
```

### 接收 ValuePotion 事件 (可选)

```lua
sdkbox.PluginValuePotion:init()
sdkbox.PluginValuePotion:setListener(function(data)
        local event = args.event
        print("receive event:", event)
        dump(args, "value potion listener info:")
    end)
```
