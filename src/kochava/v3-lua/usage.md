### 修改 Lua 代码
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 文件，包含必要的头文件并且注册 `Kochava` 的 Lua\_State。
__Note:__ 请注意该注册函数需要一个 __lua_State*__ 参数。
```cpp
#include "PluginKochavaLua.hpp"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginKochavaLua(<lua_State*>);
}
```

### 初始化 Kochava
* 修改您的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```lua
sdkbox.PluginKochava:init()
```

### 追踪事件
Kochava 提供了对 __custom__, __spatial__, __referral__ 事件的追踪功能。

* 追踪一个 __custom__ 事件：
```lua
sdkbox.PluginKochava:trackEvent("<EVENT>", "<VALUE>")
```

* 通过提供世界上的地名与位置，追踪一个 __spatial__ 事件：
```lua
sdkbox.PluginKochava:spatialEvent("<TITLE>", <X>, <Y>, <Z>)
```

* 追踪一个 __referral__ 事件（也被称作深链接）：
```lua
sdkbox.PluginKochava:sendDeepLink("<URI>", "<YOUR APP>")
```
__Note:__ 在 Android 平台上，该函数的第二个参数（__<YOUR APP>__）不会被使用。您可以只提供地一个参数 __<URI>__ 。
