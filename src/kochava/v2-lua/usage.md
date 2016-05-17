### 修改 `AppDelegate.cpp`
* 修改 `Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginKochavaLua.hpp"
#include "PluginKochavaLuaHelper.h"
```

* 然后，我们需要通过调用 `register_all_PluginKochavaLua(<lua_State*>);` 注册插件的 Lua\_State。

  __Note:__ 需要特别注意的是，该函数调用必须在 `lua_State *tolua_s = pStack->getLuaState();` 之后，并且在 `tolua_extensions_ccb_open(tolua_s);` 之前。

    这里为您准备了一个例子如下：
```cpp
#include "PluginKochavaLua.hpp"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginKochavaLua(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### 初始化 Kochava
修改您的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
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
