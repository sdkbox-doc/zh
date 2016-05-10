### 修改 Lua 代码
修改 `./frameworks/runtime-src/Classes/lua_module_register.h` 包含下面这几个必要的头文件,并注册 `AgeCheq` 到lua中.注意他们的参数 __lua_State*__:
```cpp
#include "PluginFacebookLua.hpp"
#include "PluginFacebookLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginFacebookLua(L);
  register_all_PluginFacebookLua_helper(L);
}
```

### 初始化 Facebook
修改您的lua代码来初始化这个插件. 这个初始化,可以在任意地方,但是必须在您调用插件的功能接口之前.
```lua
sdkbox.PluginFacebook:init();
```

### 使用 Facebook
#### 登录
用户在使用前需要登录到 Facebook.
```lua
sdkbox.PluginFacebook:login();
```
用户不想使用 Facebook 时，可以注销.
```lua
sdkbox.PluginFacebook:logout();
```
您可以检查是否已经登录
```lua
sdkbox.PluginFacebook:isLoggedIn();
```
> 注意: 用户只需要登录一次, 除非他们注销

#### 权限
Facebook 要求您在使用前去询问用户要相应的权限,比如 posting 相关的权益
就有两类权限, __read__ and __publish__
您也可以通过[这里](https://developers.facebook.com/docs/facebook-login/permissions/v2.3#reference)得到完整的信息

SDKBOX 提供最常用的几种权限:

* FB_PERM_READ_PUBLIC_PROFILE
* FB_PERM_READ_EMAIL
* FB_PERM_READ_USER_FRIENDS
* FB_PERM_PUBLISH_POST

要获取权限,您可以指定您想要权限,比如:
```lua
sdkbox.PluginFacebook:requestReadPermissions({FB_PERM_READ_PUBLIC_PROFILE, FB_PERM_READ_USER_FRIENDS});
sdkbox.PluginFacebook:requestPublishPermissions({FB_PERM_PUBLISH_POST});
```

#### 分享
提供了两种分享方式.

* __分享__ 会自动发布到用户的信息流中
分享联接:
```lua
local info;
info.type  = "link";
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook:share(info);
```
分享图片:
```lua
local info;
info.type  = "photo";
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook:share(info);
```
* __dialog__ 会显示一个对话框,提示用户可以添加一段他们自己的文字注解:

显示一个分享对话框:
```lua
local info;
info.type  = "link";
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook:dialog(info);
```

分享一个带文字注解的图片:
```lua
local info;
info.type  = "photo";
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook:dialog(info);
```
 > 注意: 分享带有文字注解的图片需要用户的手机上已安装了 __Facebook__ 应用.

### 图谱API
您可以通过 `api` 函数 执行[图谱API](https://developers.facebook.com/docs/graph-api/overview/)

比如,取好友列表:
```
local params;
sdkbox.PluginFacebook:api("/me/friendlists", "GET", params, "/me/friendlists");
```

### Facebook 事件
您可以接收 Facebook 事件,并对不同事件做不同的处理.

```lua
sdkbox.PluginFacebook:setListener(function(args)
    if "onLogin" == args.name then
        local isLogin = args.isLogin;
        local msg = args.msg;
    elseif "onPermission" ==  args.name then
        local isLogin = args.isLogin;
        local msg = args.msg;
    elseif "onAPI" ==  args.name then
        local tag = args.tag;
        local jsonData = args.jsonData;
    elseif "onSharedSuccess" ==  args.name then
        local msg = args.message
    elseif "onSharedFailed" ==  args.name then
        local msg = args.message
    elseif "onSharedCancel" ==  args.name then
    end
end)
```
