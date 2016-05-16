### 修改 `AppDelegate.cpp`
* 修改 `Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginTuneLua.hpp"
#include "PluginTuneLuaHelper.h"
```

* 然后，我们需要通过调用 `register_all_PluginTuneLua(<lua_State*>);` 注册插件的 Lua\_State。

  __Note:__ 需要特别注意的是，该函数调用必须在 `lua_State *tolua_s = pStack->getLuaState();` 之后，并且在 `tolua_extensions_ccb_open(tolua_s);` 之前。

    这里为您准备了一个例子如下：
```cpp
#include "PluginTuneLua.hpp"
#include "PluginTuneLuaHelper.h"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginTuneLua(tolua_s);
	register_all_PluginTuneLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### 初始化 Tune
修改你的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```cpp
sdkbox.PluginTune:init()
```

### 使用 Tune
在初始化之后，您可以开始使用 Tune 插件的功能了。Tune 使用 __events__ 这个概念（就像 __MAT Native Event Types__一样）。您可以在您需要的地方将 __events__ 记入日志，并且在稍后通过基于 web 的报告阅读器查看它们。Tune 在文档中为这些 events 提供一种结构。举例如下：
```lua
sdkbox.PluginTune:measureEventName("login");
sdkbox.PluginTune:measureEventId(0123456789);
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
sdkbox.PluginTune:setListener(function(eventName, eventData, timeout)
        -- 当eventName为 "onReceiveDeeplink" 时,第三个参数timeout才有效
       print(eventName, eventData, timeout)
   end)
```
