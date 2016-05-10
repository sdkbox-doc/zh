### 修改 Lua Code
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 包含必要的头文件,并调用相应的注册函数,同时注意它的参数 __lua_State*__:
```cpp
#include "PluginReviewLua.hpp"
#include "PluginReviewLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginReviewLua(L);
  register_all_PluginReviewLua_helper(L);
}
```

### 初始化 Review
在您的 Lua 代码中 `init()` 插件,初始化可以在任何时候做，但是必须要在您要使用相关的接口前.我们强烈建议在应用启动时就初始化插件.
```lua
sdkbox.PluginReview:init()
```

### 设置 Review (可选)
如果您不要使用默认的提示字串,您可以设置自己的字串

`注意:` 如果您在 `sdkbox.config` 中把 `tryPromptWhenInit` 项设置为真,那必须在 `init()` 之前调用以下函数
```cpp
sdkbox.PluginReview:setCustomPromptTitle("custom title");
sdkbox.PluginReview:setCustomPromptMessage("custom message");
sdkbox.PluginReview:setCustomPromptCancelButtonTitle("custom cancel");
sdkbox.PluginReview:setCustomPromptRateButtonTitle("custom rate");
sdkbox.PluginReview:setCustomPromptRateLaterButtonTitle("custom rate later");
```

如果您的 `sdkbox.config` 中把 `tryPromptWhenInit` 项为 false, 那您可以调用 `tryToShowPrompt` 尝试提示用户评价您的应用,
如果所有的限制条件都满足,那提示框就会显示
```cpp
sdkbox.PluginReview:tryToShowPrompt();
```

您也可以强制显示评价提示框
```cpp
sdkbox.PluginReview:forceToShowPrompt();
```

如果您的 `sdkbox.config` 中的 `UserEventLimit` 项大于0的话，那您需要自已增加用户事件记数
```cpp
sdkbox.PluginReview:userDidSignificantEvent(true);
```

### 接收 Review 事件 (可选)
您可以接收 `Review` 事件，以像对不同的事件做不同的处理，一个简单的用法可能如下:
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
