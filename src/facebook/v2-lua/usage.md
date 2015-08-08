### 修改 `AppDelegate.cpp`
* 修改 `Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginFacebookLua.hpp"
#include "PluginFacebookLuaHelper.hpp"
```

* 然后,我们可以调用`register_all_PluginFacebookLua(<lua_State*>);` 把这个插件注册到 Lua 中.

  __注意:__ 这个调用必须在 `lua_State *tolua_s = pStack->getLuaState();` 之后, `tolua_extensions_ccb_open(tolua_s);` 之前.

	下面给出一个例子:
```cpp
#include "PluginFacebookLua.hpp"
#include "PluginFacebookLuaHelper.hpp"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginFacebookLua(tolua_s);
	register_all_PluginFacebookLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### 初始化 Facebook
* 修改你的应用的 __Info.plist__ 项,增加下面这些项,用你自己的 __<APP ID>__ 替换里面对应的项:
```xml
<key>CFBundleURLTypes</key>
<array>
<dict
    <key>CFBundleURLName</key>
    <string></string>
    <key>CFBundleURLSchemes</key>
    <array>
        <string>fb<APP ID></string>
    </array>
</dict>
</array>
<key>FacebookAppID</key>
<string><APP ID></string>
<key>FacebookDisplayName</key>
<string>MyTestApp</string>
```

假定你的Facebook __APP ID__ 是 `655158077954837`, 那么一个完整的例子可能像这样:
```xml
<key>CFBundleURLTypes</key>
<array>
<dict>
    <key>CFBundleURLName</key>
    <string></string>
    <key>CFBundleURLSchemes</key>
    <array>
        <string>fb655158077954837</string>
    </array>
</dict>
</array>
<key>FacebookAppID</key>
<string>655158077954837</string>
<key>FacebookDisplayName</key>
<string>MyTestApp</string>
```

* 修改你的lua代码来初始化这个插件. 这个初始化,可以在任意地方,但是必须在你调用插件的功能接口之前.
```lua
sdkbox.PluginFacebook:init()
```

### 使用 Facebook
Facebook中有很多操作，你都可以用到.但是在使用前，你要先登陆，比如:
```lua
sdkbox.PluginFacebook:login();
```

* 你可以分享链接，比如：
```lua
FBShareInfo info;
info.type  = "link";
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook.share(info);
```

* 你还可以分享链接，同时文字注解它，但需要当前的设备上已安装了 __Facebook__ 这个应用，比如:
```lua
FBShareInfo info;
info.type  = "link";
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook.dialog(info);
```

* 你可以分享一个图片:
```lua
FBShareInfo info;
info.type  = "photo";
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook.share(info);
```

* 你还可以分享图片，同时文字注解它，比如：
```lua
FBShareInfo info;
info.type  = "photo";
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook.dialog(info);
```

* 虽然登陆了，你还是需要获取 `read()` 和 `publish()` 权限才能发布。比如:
```lua
sdkbox.PluginFacebook.requestReadPermissions({FB_PERM_READ_USER_FRIENDS});
sdkbox.PluginFacebook.requestPublishPermissions({FB_PERM_PUBLISH_POST});
```

* 当所有操作完成后，可以注销，比如：
```lua
sdkbox.PluginFacebook.logout();
```

### 接收 Facebook 事件 (可选)
你可以接收 Facebook 事件，当 Facebook 事件发生时，你可以做相应的处理

* 设置 Facebook 的 监听:
```lua
sdkbox.PluginFacebook:setListener(function(event)
    print("PluginFacebook callback")
    dump(event)
end)
```
