### 修改 Lua 代码
* 修改 `Classes/AppDelegate.cpp` 包含以下头文件:
```cpp
#include "PluginFlurryAnalyticsLua.hpp"
#include "PluginFlurryAnalyticsLuaHelper.h"
```

* 然后,我们需要调用 `register_all_PluginFlurryAnalyticsLua(<lua_State*>);` 来把插件注册到lua中.

  __注意:__ 必须在 `lua_State *tolua_s = pStack->getLuaState();` 之后, 并且在 `tolua_extensions_ccb_open(tolua_s);` 之前调用上面的注册函数.

    下面给出一个例子:
```cpp
#include "PluginFlurryAnalyticsLua.hpp"
#include "PluginFlurryAnalyticsLuaHelper.h"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginFlurryAnalyticsLua(tolua_s);
	register_all_PluginFlurryAnalyticsLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### 初始化 Flurry Analytics
修改您的lua代码来初始化这个插件. 这个初始化,可以在您的代码中任意地方,但是必须在您调用插件的功能接口之前.
```lua
sdkbox.PluginFlurryAnalytics:init()
```

### 使用 Flurry Analytics
在初始化完成后,您就可以使用 Flurry Analytics 提供的功能了. 在您的代码中任意地方,使用 `logevent`:
```lua
local eventName = "test event1"
sdkbox.PluginFlurryAnalytics:logEvent(eventName)
```

### 接收 Flurry Analytics 事件 (可选)
您可以接收 `FlurryAnalytics` 事件, 然后对不同事件做不同的程序响应,一个简单的例子可以会像这样:
```lua
sdkbox.PluginFlurryAnalytics:init()
sdkbox.PluginFlurryAnalytics:setListener(function(data)
        local ret = json.decode(data)
        print("apiKey:", ret.apiKey, "sessionId:", ret.sessionId)
        -- check session state
        print("Flurry analytics session exist: ", f:activeSessionExists())
        print("Flurry analytics session: ", f:getSessionID())
        local eventName = "test event1"
        sdkbox.PluginFlurryAnalytics:logEvent(eventName);
    end)
sdkbox.PluginFlurryAnalytics:startSession()
```

### 结束 Flurry Analytics (只在 Android 上有效)
当您不再使用 `FlurryAnalytics` 或您的游戏结束时, 必须要把 `FlurryAnalytics` 会话结束. 这个在 Android 上必须调用,但是在 iOS 上是可选的. 比如:
```lua
// 这个只在 android 上有效, 但是您在 iOS 调用,也没有关系
sdkbox.PluginFlurryAnalytics:endSession()
```
