### 注册 javascript 函数
在使用 Fackbook JS 函数之前，你要把它们注册到 cocos2d-x中.

这样做:
* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginFacebookJS.hpp"
#include "PluginFacebookJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保有如下调用:
```cpp
sc->addRegisterCallback(register_all_PluginFacebookJS);
sc->addRegisterCallback(register_PluginFacebookJS_helper);
```

### 初始化 Facebook
* 在你的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginFacebook.init();
```

### 使用 Facebook
#### 登录
用户在使用前需要登录到 Facebook.
```javascript
sdkbox.PluginFacebook.login();
```
用户不想使用 Facebook 时，可以注销
```javascript
sdkbox.PluginFacebook.logout();
```
你可以检查用户是否已经登录
```javascript
sdkbox.PluginFacebook.isLoggedIn();
```
> 注意: 用户只需要登录一次, 除非他们注销

#### 权限
Facebook 要求你在使用前去询问用户要相应的权限,比如 posting 相关的权益
就有两类权限, __read__ and __publish__
你也可以通过[这里](https://developers.facebook.com/docs/facebook-login/permissions/v2.3#reference)得到完整的信息

要获取权限,你可以指定你想要权限,比如:
```javascript
sdkbox.PluginFacebook.requestReadPermissions(["public_profile", "email"]);
sdkbox.PluginFacebook.requestPublishPermissions(["publish_actions"]);
```

#### 分享
提供了两个分享功能

* __分享__ 会自动发布到用户的信息流中
分享链接:
```javascript
var info = new Object();
info.type  = FB_LINK;
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook.share(info);
```
分享图片:
```javascript
var info = new Object();
info.type  = FB_PHOTO;
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook.share(info);
```
* __对话框__ 可以显示一个对话框,用户可以在其中添加他们自己的文字:

显示一个对话框:
```javascript
var info = new Object();
info.type  = FB_LINK;
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook.dialog(info);
```

分享带有文字注解的图片:
```javascript
var info = new Object();
info.type  = FB_PHOTO;
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook.dialog(info);
```
 > 注意: 分享带有文字注解的图片需要用户的手机上已安装了 __Facebook__ 应用.

### 图谱API
你可以通过 `api` 函数 执行[图谱API](https://developers.facebook.com/docs/graph-api/overview/)

比如,取好友列表:
```javascript
var params = new Object();
sdkbox.PluginFacebook.api("/me/friendlists", "GET", params, "/me/friendlists");
```

### Facebook 事件
你可以接收 `Facebook` 事件, 然后对不同事件做相应的处理.

```javascript
sdkbox.PluginFacebook.setListener({
    onLogin: function(isLogin, msg) {},
    onAPI: function(tag, data) {},
    onSharedSuccess: function(data) {},
    onSharedFailed: function(data) {},
    onSharedCancel: function() {},
    onPermission: function(isLogin, msg) {}
});
```
