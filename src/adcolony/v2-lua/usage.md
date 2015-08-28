### 修改 `AppDelegate.cpp`
* 修改 `Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginAdColonyLua.hpp"
#include "PluginAdColonyLuaHelper.h"
```

* 然后, 我们需要调用 `register_all_PluginAdColonyLua(<lua_State*>);` 把插件注册到lua中.

  __注意:__ 上面的调用必须在 `lua_State *tolua_s = pStack->getLuaState();` 之后,而且在 `tolua_extensions_ccb_open(tolua_s);` 之前.

	如下是一个修改例子:
```cpp
#include "PluginAdColonyLua.hpp"
#include "PluginAdColonyLuaHelper.h"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginAdColonyLua(tolua_s);
	register_all_PluginAdColonyLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### 初始化 AdColony
修改你的lua代码用 `init()` 初始化插件. 这个可以在任何地方调用,但是必须在你要想使用 AdColony 的功能之前.
```lua
sdkbox.PluginAdColony:init()
```

### Showing Ads
在你的代码中想要显示广告的地方,输入如下代码:
```lua
sdkbox.PluginAdColony:show("video")
```
或:
```lua
sdkbox.PluginAdColony:show("v4vc")
```

### 接收 AdColony 事件 (可选)
你可以接收 `AdColony` 的事件, 这样你可以在玩家观看完广告后给他相应的奖励.

* 创建一个监听:
```lua
sdkbox.PluginAdColony:setListener(function(args)
    if "onAdColonyChange" == args.name then
        local info = args.info  -- sdkbox::AdColonyAdInfo
        local available = args.available -- boolean
				dump(info, "onAdColonyChange:")
        print("available:", available)
    elseif "onAdColonyReward" ==  args.name then
        local info = args.info  -- sdkbox::AdColonyAdInfo
        local currencyName = args.currencyName -- string
        local amount = args.amount -- int
        local success = args.success -- boolean
				dump(info, "onAdColonyReward:")
        print("currencyName:", currencyName)
        print("amount:", amount)
        print("success:", success)
    elseif "onAdColonyStarted" ==  args.name then
        local info = args.info  -- sdkbox::AdColonyAdInfo
				dump(info, "onAdColonyStarted:")
    elseif "onAdColonyFinished" ==  args.name then
        local info = args.info  -- sdkbox::AdColonyAdInfo
				dump(info, "onAdColonyFinished:")
    end
end)
```
