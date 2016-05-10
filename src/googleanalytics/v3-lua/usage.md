### 修改 Lua 代码
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 文件，包含必要的头文件并且注册 `Google Analytics` 的 Lua\_State。
__Note:__ 请注意该注册函数需要一个 __lua_State*__ 参数。
```cpp
#include "PluginGoogleAnalyticsLua.hpp"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginGoogleAnalyticsLua(L);
}
```

### 初始化 Google Analytics
* 修改您的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```lua
sdkbox.PluginGoogleAnalytics:init()
```
