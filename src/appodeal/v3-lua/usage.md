### 修改 `AppDelegate.cpp`
* 修改 `Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginAppodealLua.hpp"
#include "PluginAppodealLuaHelper.hpp"
```

* 然后, 我们需要调用 `register_all_PluginAppodealLua(<lua_State*>);` 把插件注册到lua中.

  __注意:__ 上面的调用必须在 `lua_State *tolua_s = pStack->getLuaState();` 之后,而且在 `tolua_extensions_ccb_open(tolua_s);` 之前.

    如下是一个修改例子:
```cpp
#include "PluginAppodealLua.hpp"
#include "PluginAppodealLuaHelper.hpp"
bool AppDelegate::applicationDidFinishLaunching()
{
    lua_State *tolua_s = pStack->getLuaState();
    register_all_PluginAppodealLua(tolua_s);
    register_all_PluginAppodealLua_helper(tolua_s);
    tolua_extensions_ccb_open(tolua_s);
}
```

### 初始化 Appodeal
修改您的lua代码用 `init()` 初始化插件. 这个可以在任何地方调用,但是必须在您要想使用 Appodeal 的功能之前.
```lua
sdkbox.PluginAppodeal:init()
```

### 使用 Appodeal
```lua
local plugin = sdkbox.PluginAppodeal
plugin:init()
plugin:setUserVkId("user id");
plugin:cacheAd(15);
```

### 接收 Appodeal events (可选)

```lua
local plugin = sdkbox.PluginAppodeal
plugin:setListener(function(args)
    local event = args.event
    dump(args, "appodeal listener info:")
end)
plugin:init()
```
