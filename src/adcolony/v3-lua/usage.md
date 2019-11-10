### Modify Lua Code
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 以包含如下必须头文件, 并调用 `AdColony` 的lua注册函数.注意它们的参数 __lua_State*__ :
```cpp
#include "PluginAdColonyLua.hpp"
#include "PluginAdColonyLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginAdColonyLua(L);
  register_all_PluginAdColonyLua_helper(L);
}
```

### 初始化 AdColony
修改您的lua代码用 `init()` 初始化插件. 这个可以在任何地方调用,但是必须在您要想使用 AdColony 的功能之前.
```lua
sdkbox.PluginAdColony:init()
```

### 显示广告
在您的代码中想要显示广告的地方,输入如下代码:
```lua
sdkbox.PluginAdColony:show("video")
```
或:
```lua
sdkbox.PluginAdColony:show("v4vc")
```

### 接收 AdColony 事件 (可选)
您可以接收 `AdColony` 的事件, 这样您可以在玩家观看完广告后给他相应的奖励.

* 创建一个监听:
```lua
sdkbox.PluginAdColony:setListener(function(args)
    if args.name == "onAdColonyChange" or args.name == "onAdColonyReward" or args.name == "onAdColonyStarted" or args.name == "onAdColonyFinished" then
        print("those four event is deprecated")
        return
    end

    dump(args)
    if "adColonyReward" ==  args.name then
    elseif "adColonyInterstitialDidLoad" ==  args.name then
    elseif "adColonyInterstitialDidFailToLoad" ==  args.name then
    elseif "adColonyAdViewDidLoad" ==  args.name then
    elseif "adColonyAdViewDidFailToLoad" ==  args.name then
    end
end)
```
