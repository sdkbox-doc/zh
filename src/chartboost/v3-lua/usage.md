### 修改 Lua 代码
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 包含下面这几个必要的头文件,并注册 `Chartboost` 到lua中.注意他们的参数 __lua_State*__:
```cpp
#include "PluginChartboostLua.hpp"
#include "PluginChartboostLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginChartboostLua(L);
  register_all_PluginChartboostLua_helper(L);
}
```

### 初始化 Chartboost
修改你的lua代码来初始化这个插件. 这个初始化,可以在任意地方,但是必须在你调用插件的功能接口之前.
```lua
sdkbox.PluginChartboost:init()
```

### 显示广告
在你的代码中任何地方都可以显示广告:
```lua
// To use the Chartboost predefined locations
sdkbox.PluginChartboost:show("Default")
// To use customized location
sdkbox.PluginChartboost:show("your_ad_name")
```

### 接收 Chartboost 事件 (可选)
你可以接收 `Chartboost` 事件, 当玩家观看了广告过,你可以在代码中做某些操作,比如奖励玩家.

* 注册回调(通过log演示结果):
```lua
sdkbox.PluginChartboost:setListener(function(args)
    if "onChartboostCached" == args.func then
        local name = args.name -- string
        print("onChartboostCached")
        print("name:", args.name)
    elseif "onChartboostShouldDisplay" == args.func then
        local name = args.name -- string
        print("onChartboostShouldDisplay")
        print("name:", args.name)
    elseif "onChartboostDisplay" == args.func then
        local name = args.name -- string
        print("onChartboostDisplay")
        print("name:", args.name)
    elseif "onChartboostDismiss" == args.func then
        local name = args.name -- string
        print("onChartboostDismiss")
        print("name:", args.name)
    elseif "onChartboostClose" == args.func then
        local name = args.name -- string
        print("onChartboostClose")
        print("name:", args.name)
    elseif "onChartboostClick" == args.func then
        local name = args.name -- string
        print("onChartboostClick")
        print("name:", args.name)
    elseif "onChartboostReward" == args.func then
        local name = args.name -- string
        local reward = args.reward -- int
        print("onChartboostReward")
        print("name:", args.name)
        print("reward:", reward)
    elseif "onChartboostFailedToLoad" == args.func then
        local name = args.name -- string
        local e = args.e -- int
        print("onChartboostFailedToLoad")
        print("name:", args.name)
        print("error:", e)
    elseif "onChartboostFailToRecordClick" == args.func then
        local name = args.name -- string
        local e = args.e -- int
        print("onChartboostFailToRecordClick")
        print("name:", args.name)
        print("error:", e)
    elseif "onChartboostConfirmation" == args.func then
        local name = args.name -- string
        print("onChartboostConfirmation")
    elseif "onChartboostCompleteStore" == args.func then
        local name = args.name -- string
        print("onChartboostCompleteStore")
    end
end)
```
