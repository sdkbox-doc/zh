### 修改 Lua Code
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 包含必要的头文件,并调用相应的注册函数,同时注意它的参数 __lua_State*__:
```cpp
#include "PluginSoomlaGrowLua.hpp"
#include "PluginSoomlaGrowLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginSoomlaGrowLua(L);
  register_PluginSoomlaGrowLua_helper(L);
}
```

### 初始化 SoomlaGrow
在你的 Lua 代码中 `init()` 插件,初始化可以在任何时候做，但是必须要在你要使用相关的接口前.我们强烈建议在应用启动时就初始化插件.
```lua
sdkbox.PluginSoomlaGrow:init()
```

### 使用 SoomlaGrow 的 user insight 模块
在 `SoomlaGrow` 初始化完成后, 它就会自动记录你的应用中的 `IAP`, `Facebook` 插件的使用情况.同时你还可以你的代码中调用 `refreshInsight`, `getUserInsightInfo` 接口:
```lua
sdkbox.PluginSoomlaGrow:refreshInsight()
sdkbox.PluginSoomlaGrow:getUserInsightInfo()
```

### 接收 SoomlaGrow 事件 (可选)
你可以接收 `SoomlaGrow` 事件，以便对不同的事件做出不同的处理.一个简单的用法可能像这样:
```lua
sdkbox.PluginSoomlaGrow:setListener(function(data)
            if "onHighWayInitialized" == data.event then
                //highway initialized
            elseif "onHighWayConnected" == data.event then
                //highway connected
            elseif "onHighWayDisconnected" == data.event then
                //highway disconnected
            end
        end)
sdkbox.PluginSoomlaGrow:init()
```
