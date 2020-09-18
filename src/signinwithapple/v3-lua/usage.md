### 修改 Lua 代码
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 以包含如下必须头文件, 并调用 `SignInWithApple` 的lua注册函数.注意它们的参数 __lua_State*__ :
```cpp
#include "PluginSignInWithAppleLua.hpp"
#include "PluginSignInWithAppleLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginSignInWithAppleLua(L);
  register_all_PluginSignInWithAppleLua_helper(L);
}
```

### 初始化 SignInWithApple
修改您的lua代码去初始插件, 初始化可以在任何地方来做,但是必须要在您想使用插件的功能之前.
```lua
sdkbox.PluginSignInWithApple:init()
```

### 登录

Sign in with Apple

```lua
sdkbox.PluginSignInWithApple:sign();
```

如果用户已经登录, 那么可以在应用启动时, 调下如下:

```lua
sdkbox.PluginSignInWithApple:signWithExistingAccount();
```

### 处理SignInWithApple事件
您可以接收 `SignInWithApple` 事件.

```lua
sdkbox.PluginSignInWithApple:setListener(function(args)
    if "onAuthorizationDidComplete" == args.event then
        -- authorization success
        dump(args, "onAuthorizationDidComplete:")
    else if "onAuthorizationCompleteWithError" == args.event then
        -- authorization fail
        dump(args, "onAuthorizationCompleteWithError:")
    else if "onAuthorizationStatus" == args.event then
        -- authorization status
        dump(args, "onAuthorizationStatus:")
    else
        print("unknow event ", args.event)
    end
end)
```
