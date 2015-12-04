### 修改 Lua 代码
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 包含下面这几个必要的头文件,并注册 `FlurryAnalytics` 到lua中.注意他们的参数 __lua_State*__:
```cpp
#include "PluginFlurryAnalyticsLua.hpp"
#include "PluginFlurryAnalyticsLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginFlurryAnalyticsLua(L);
  register_all_PluginFlurryAnalyticsLua_helper(L);
}
```

### 初始化 Flurry Analytics
修改你的lua代码来初始化这个插件. 这个初始化,可以在你的代码中任意地方,但是必须在你调用插件的功能接口之前.
```lua
sdkbox.PluginFlurryAnalytics:init()
```

### 使用 Flurry Analytics
在初始化完成后,你就可以使用 Flurry Analytics 提供的功能了. 在你的代码中任意地方,使用 `logevent`:
```lua
local eventName = "test event1"
sdkbox.PluginFlurryAnalytics:logEvent(eventName)
```

### 接收 Flurry Analytics 事件 (可选)
你可以接收 `FlurryAnalytics` 事件, 然后对不同事件做不同的程序响应,一个简单的例子可以会像这样:
```lua
sdkbox.PluginFlurryAnalytics:init()
sdkbox.PluginFlurryAnalytics:setListener(function(data)
        local ret = json.decode(data)
        print("apiKey:", ret.apiKey, "sessionId:", ret.sessionId)
        -- check session state
        print("Flurry analytics session exist: ", f:activeSessionExists())
        print("Flurry analytics session: ", f:getSessionID())
        local eventName = "test event1"
        sdkbox.PluginFlurryAnalytics:logEvent(eventName)
    end)
sdkbox.PluginFlurryAnalytics:startSession()
```

### 结束 Flurry Analytics (只在 Android 上有效)
当你不再使用 `FlurryAnalytics` 或你的游戏结束时, 必须要把 `FlurryAnalytics` 会话结束. 这个在 Android 上必须调用,但是在 iOS 上是可选的. 比如:
```lua
// 这个只在 android 上有效, 但是你在 iOS 调用,也没有关系
sdkbox.PluginFlurryAnalytics:endSession()
```
