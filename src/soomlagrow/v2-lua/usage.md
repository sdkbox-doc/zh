### 修改 Lua Code
* 修改 `Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginSoomlaGrowLua.hpp"
#include "PluginSoomlaGrowLuaHelper.h"
```

* 然后,我把这个插件注册到 lua 中. 调用 `register_all_PluginSoomlaGrowLua(<lua_State*>);` 函数可以完成注册.

  __注意:__ 必须要在 `lua_State *tolua_s = pStack->getLuaState();` 之后, `tolua_extensions_ccb_open(tolua_s);` 之前，调用这个函数.

	下面给出一个例子:
```cpp
#include "PluginSoomlaGrowLua.hpp"
#include "PluginSoomlaGrowLuaHelper.h"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginSoomlaGrowLua(tolua_s);
	register_all_PluginSoomlaGrowLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### 初始化 SoomlaGrow
修改你的 Lua 代码来 `init()` 插件. 这可以在任何时候，但必须在你要使用插件的功能前.我们建议在应用启动时就初始化.
```lua
sdkbox.PluginSoomlaGrow:init()
```

### 使用 SoomlaGrow 的 user insight 模块
在完成 SoomlaGrow 的初始化后，它就会自动记录你应用中的 `IAP`, `Facebook` 插件的使用情况.同时你还可以在代码中使用 `refreshInsight`, 'getUserInsightInfo' 接口:
```lua
sdkbox.PluginSoomlaGrow:refreshInsight()
sdkbox.PluginSoomlaGrow:getUserInsightInfo()
```

### 接收 SoomlaGrow 事件 (可选)
你可以接收 `SoomlaGrow` 事件，以像对不同的事件做不同的处理，一个简单的用法可能如下:
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
