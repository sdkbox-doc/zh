### 修改 Lua 代码
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 包含下面这几个必要的头文件,并注册 `AgeCheq` 到lua中.注意他们的参数 __lua_State*__:
```cpp
#include "PluginAgeCheqLua.hpp"
#include "PluginAgeCheqLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginAgeCheqLua(L);
  register_PluginAgeCheqLua_helper(L);
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
