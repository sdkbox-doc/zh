### 修改 Lua Code
* 修改 `Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginReviewLua.hpp"
#include "PluginReviewLuaHelper.h"
```

* 然后,我把这个插件注册到 lua 中. 调用 `register_all_PluginReviewLua(<lua_State*>);` 函数可以完成注册.

  __注意:__ 必须要在 `lua_State *tolua_s = pStack->getLuaState();` 之后, `tolua_extensions_ccb_open(tolua_s);` 之前，调用这个函数.

	下面给出一个例子:
```cpp
#include "PluginReviewLua.hpp"
#include "PluginReviewLuaHelper.h"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginReviewLua(tolua_s);
	register_PluginReviewLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### 初始化 Review
修改你的 Lua 代码来 `init()` 插件. 这可以在任何时候，但必须在你要使用插件的功能前.我们建议在应用启动时就初始化.
```lua
sdkbox.PluginReview:init()
```

### 设置 Review (可选)
如果你不要使用默认的提示字串,你可以设置自己的字串

`注意:` 如果你在 `sdkbox.config` 中把 `tryPromptWhenInit` 项设置为真,那必须在 `init()` 之前调用以下函数
```cpp
sdkbox.PluginReview:setCustomPromptTitle("custom title");
sdkbox.PluginReview:setCustomPromptMessage("custom message");
sdkbox.PluginReview:setCustomPromptCancelButtonTitle("custom cancel");
sdkbox.PluginReview:setCustomPromptRateButtonTitle("custom rate");
sdkbox.PluginReview:setCustomPromptRateLaterButtonTitle("custom rate later");
```

如果你的 `sdkbox.config` 中把 `tryPromptWhenInit` 项为 false, 那你可以调用 `tryToShowPrompt` 尝试提示用户评价你的应用,
如果所有的限制条件都满足,那提示框就会显示
```cpp
sdkbox.PluginReview:tryToShowPrompt();
```

你也可以强制显示评价提示框
```cpp
sdkbox.PluginReview:forceToShowPrompt();
```

如果你的 `sdkbox.config` 中的 `UserEventLimit` 项大于0的话，那你需要自已增加用户事件记数
```cpp
sdkbox.PluginReview:userDidSignificantEvent(true);
```

### 接收 Review 事件 (可选)
你可以接收 `Review` 事件，以像对不同的事件做不同的处理，一个简单的用法可能如下:
```lua
local plugin = sdkbox.PluginReview
plugin:setListener(function(args)
    local event = args.event
    if "didDisplayAlert" == event then
        print("didDisplayAlert")
    elseif "didDeclineToRate" == event then
        print("didDeclineToRate")
    elseif "didToRate" == event then
        print("didToRate")
    elseif "didToRemindLater" == event then
        print("didToRemindLater")
    end
end)
plugin:init()
```
