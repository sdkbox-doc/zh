### 修改 `AppDelegate.cpp`
* 修改 `Classes/AppDelegate.cpp` 包含以下头文件:
```cpp
#include "PluginChartboostLua.hpp"
#include "PluginChartboostLuaHelper.h"
```

* 然后,我们需要调用 `register_all_PluginChartboostLua(<lua_State*>);` 来把插件注册到lua中.

  __注意:__ 必须在 `lua_State *tolua_s = pStack->getLuaState();` 之后, 并且在 `tolua_extensions_ccb_open(tolua_s);` 之前调用上面的注册函数.

	下面给出一个例子:
```cpp
#include "PluginChartboostLua.hpp"
#include "PluginChartboostLuaHelper.h"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginChartboostLua(tolua_s);
	register_all_PluginChartboostLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### 初始化 Chartboost
修改您的lua代码来初始化这个插件. 这个初始化,可以在任意地方,但是必须在您调用插件的功能接口之前.
```lua
sdkbox.PluginChartboost:init()
```

### 显示广告
在您的代码中任何地方都可以显示广告:
```lua
// To use the Chartboost predefined locations
sdkbox.PluginChartboost:show("Default")
// To use customized location
sdkbox.PluginChartboost:show("your_ad_name")
```

### 接收 Chartboost 事件 (可选)
您可以接收 `Chartboost` 事件, 当玩家观看了广告过,您可以在代码中做某些操作,比如奖励玩家.

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
