### 注册 Lua 函数
首先要把 Firebase 的接口注册到 Lua 环境中

步骤如下:
* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginFirebaseLua.hpp"
#include "PluginFirebaseLuaHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 调用:
```cpp
    register_all_PluginFirebaseLua(LuaEngine::getInstance()->getLuaStack()->getLuaState());
    register_all_PluginFirebaseLua_helper(LuaEngine::getInstance()->getLuaStack()->getLuaState());
```

### Initialize Firebase
修改您的lua代码来初始化这个插件. 这个初始化,可以在任意地方,但是必须在您调用插件的功能接口之前.
```lua
sdkbox.firebase.Analytics:init()
```

### 统计事件

```lua
local evt = {
    [sdkbox.firebase.Analytics.Param.kFIRParameterItemID] = 'id123456',
    [sdkbox.firebase.Analytics.Param.kFIRParameterItemName] = 'name123456',
    [sdkbox.firebase.Analytics.Param.kFIRParameterItemCategory] = 'category123456',
    [sdkbox.firebase.Analytics.Param.kFIRParameterPrice] = '123.4'
    }
sdkbox.firebase.Analytics:logEvent(sdkbox.firebase.Analytics.Event.kFIREventViewItem, evt)
```
