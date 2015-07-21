### 修改 Lua 代码
* 修改 `Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginAgeCheqLua.hpp"
#include "PluginAgeCheqLuaHelper.h"
```

* 然后,我们需要通过调用 `register_all_PluginAgeCheqLua(<lua_State*>);` 把插件注册到lua中.

  __注意:__ 必须在 `lua_State *tolua_s = pStack->getLuaState();` 之后, 并且在 `tolua_extensions_ccb_open(tolua_s);` 之前调用上面的注册函数.

	下面给出一个例子:
```cpp
#include "PluginAgeCheqLua.hpp"
#include "PluginAgeCheqLuaHelper.hpp"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginAgeCheqLua(tolua_s);
	register_all_PluginAgeCheqLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### 初始化 AgeCheq
修改你的lua代码来初始化这个插件. 这个初始化,可以在任意地方,但是必须在你调用插件的功能接口之前.
```lua
sdkbox.PluginAgeCheq:init()
```

### 使用 AgeCheq
初始化完成后,你可以在你的代码任意需要的地方调用 `check` 功能:
```lua
sdkbox.PluginAgeCheq:check("agecheqPin")
```

### 接收 AgeCheq 事件 (可选)
你可以接收 AgeCheq 事件,然后对不同的事件在程序中做出不同的响应.一个简单的例子可能会如下:
```lua
sdkbox.PluginAgeCheq:init()
sdkbox.PluginAgeCheq:setListener(function(data)
	    if "checkResponse" == data.event then
	        dump(data)
	    elseif "associateDataResponse" == data.event then
	        dump(data)
	    end
	end)
sdkbox.PluginAgeCheq:check("agecheqPin")
```
