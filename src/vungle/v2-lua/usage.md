### 修改 `AppDelegate.cpp`
* 修改 `Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginVungleLua.hpp"
#include "PluginVungleLuaHelper.h"
```

* 然后，我们需要通过调用 `register_all_PluginVungleLua(<lua_State*>);` 注册插件的 Lua\_State。

  __Note:__ 需要特别注意的是，该函数调用必须在 `lua_State *tolua_s = pStack->getLuaState();` 之后，并且在 `tolua_extensions_ccb_open(tolua_s);` 之前。

    这里为您准备了一个例子如下：
```cpp
#include "PluginVungleLua.hpp"
#include "PluginVungleLuaHelper.hpp"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginVungleLua(tolua_s);
	register_all_PluginVungleLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### 初始化 Vungle
修改你的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```lua
sdkbox.PluginVungle:init()
```

### 显示广告
无论 __video__ 还是 __reward__ 类型的广告，可以在任何您想显示它们的地方加入代码：
```lua
sdkbox.PluginVungle:show("video")
sdkbox.PluginVungle:show("reward")
```

### 捕捉 Vungle 事件（可选）
您可以捕捉 `Vungle` 事件来执行一些操作，比如在玩家观看了视频广告后给其发放奖励。

* 创建一个 __listener__ 用于事件回调 (通过写入事件日志举例如下)：
```lua
sdkbox.PluginVungle:setListener(function(name, isComplete)
    if "onVungleCacheAvailable" == name then
        print("onVungleCacheAvailable")
    elseif "onVungleStarted" ==  name then
        print("onVungleStarted")
    elseif "onVungleFinished" ==  name then
        print("onVungleFinished")
    elseif "onVungleAdViewed" ==  name then
        print("onVungleAdViewed:", isComplete)
    end
end)
```
