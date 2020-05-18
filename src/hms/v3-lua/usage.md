### 修改 Lua 代码
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 以包含如下必须头文件, 并调用 `HMS` 的lua注册函数.注意它们的参数 __lua_State*__ :
```cpp
#include "PluginHMSLua.hpp"
#include "PluginHMSLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginHMSLua(L);
  register_all_PluginHMSLua_helper(L);
}
```

### 初始化 HMS
修改您的lua代码去初始插件, 初始化可以在任何地方来做,但是必须要在您想使用插件的功能之前.
```lua
sdkbox.HMS:init()
```

### 登录

HMS 提供了三种登录方式:

* Signing In with HUAWEI ID(ID Token)

```lua
sdkbox.HMS:login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```lua
sdkbox.HMS:login(2);
```

* Silently Signing In With HUAWEI ID

静默登录只能在上一次使用前两种方式已经登录成功的情况下，才能在静态登录下成功

```lua
sdkbox.HMS:login(0);
```

> 以上三种登录方式, 不管成功还是失败, 最终都会触发 `onLogin` 事件.

HMS 帐号相关的 [文档](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### 登出

```lua
sdkbox.HMS:logout();
```

### 处理HMS事件
您可以接收付费过程中的 `HMS` 事件.

```lua
sdkbox.HMS:setListener(function(args)
		if "onLogin" == args.event then
				local code = args.code
				local msg = args.msg
				dump(args, "onLogin:")
		else
				print("unknow event ", args.event)
		end
end)
```
