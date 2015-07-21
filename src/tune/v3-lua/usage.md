### 修改 Lua 代码
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 文件，包含必要的头文件并且注册 `Tune` 的 Lua\_State。
__Note:__ 请注意该注册函数需要一个 __lua_State*__ 参数。
```cpp
#include "PluginTuneLua.hpp"
#include "PluginTuneLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginTuneLua(L);
  register_PluginTuneLua_helper(L);
}
```

### 初始化 Tune
* 修改你的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```cpp
sdkbox.PluginTune:init()
```

### 使用 Tune
在初始化之后，您可以开始使用 Tune 插件的功能了。Tune 使用 __events__ 这个概念（就像 __MAT Native Event Types__一样）。您可以在您需要的地方将 __events__ 记入日志，并且在稍后通过基于 web 的报告阅读器查看它们。Tune 在文档中为这些 events 提供一种结构。举例如下：
```lua
sdkbox.PluginTune:measureEventName("login")
sdkbox.PluginTune:measureEventId(0123456789)

local event = {}
event.eventName = "purchase"
event.refId = "RJ1357"
event.searchString = "sweet srisp red apples"
event.attribute1 = "srisp"
event.attribute2 = "red"
event.quantity = 3
sdkbox.PluginTune:measureEventForScript(json.encode(event))
```

### 捕捉 Tune 事件（可选）
您可以捕捉 `Tune` 事件，根据响应来执行操作。一个简单的例子如下：
```lua
sdkbox.PluginTune:setListener(function(eventName, eventData)
        print(eventName, eventData)
    end)
```
