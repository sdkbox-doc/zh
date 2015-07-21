### 修改 Lua 代码
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 文件，包含必要的头文件并且注册 `Vungle` 的 Lua\_State。请注意该注册函数需要一个 __lua_State*__ 参数。
```cpp
#include "PluginVungleLua.hpp"
#include "PluginVungleLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginVungleLua(L);
  register_PluginVungleLua_helper(L);
}
```

### 初始化 Vungle
* 修改你的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
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
