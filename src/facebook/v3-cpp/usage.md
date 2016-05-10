### 初始化 Facebook
在您的代码合适的地方初始化插件, 我们建议您在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保您包含了对应的头文件:

```cpp
#include "PluginFacebook/PluginFacebook.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginFacebook::init();
}
```

### 使用 Facebook
#### 登录
用户在使用前需要登录到 Facebook.
```cpp
sdkbox::PluginFacebook::login();
```
用户不想使用 Facebook 时，可以注销.
```cpp
sdkbox::PluginFacebook::logout();
```
您可以检查是否已经登录
```cpp
sdkbox::PluginFacebook::isLoggedIn();
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
```cpp
sdkbox::PluginFacebook::requestReadPermissions({FB_PERM_READ_PUBLIC_PROFILE, FB_PERM_READ_USER_FRIENDS});
sdkbox::PluginFacebook::requestPublishPermissions({FB_PERM_PUBLISH_POST});
```

#### 分享
提供了两种分享方式.

* __分享__ 会自动发布到用户的信息流中
分享联接:
```cpp
sdkbox::FBShareInfo info;
info.type  = FB_LINK;
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox::PluginFacebook::share(info);
```
分享图片:
```cpp
sdkbox::FBShareInfo info;
info.type  = FB_PHOTO;
info.title = "My Photo";
info.image = __path to image__;
sdkbox::PluginFacebook::share(info);
```
* __dialog__ 会显示一个对话框,让用户可以添加他们自己想说的话:

显一个分享对话框:
```cpp
sdkbox::FBShareInfo info;
info.type  = FB_LINK;
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox::PluginFacebook::dialog(info);
```

分享一个带有文字注解的图片:
```cpp
sdkbox::FBShareInfo info;
info.type  = FB_PHOTO;
info.title = "My Photo";
info.image = __path to image__;
sdkbox::PluginFacebook::dialog(info);
```
 > 注意: 分享带有文字注解的图片需要用户的手机上已安装了 __Facebook__ 应用.

### 图谱API
您可以通过 `api` 函数 执行[图谱API](https://developers.facebook.com/docs/graph-api/overview/)

比如,取好友列表:
```
sdkbox::PluginFacebook::FBAPIParam params;
sdkbox::PluginFacebook::api("/me/friendlists", "GET", params, "/me/friendlists");
```

### Facebook 事件
您可以接收 `Facebook` 事件，以对不同事件做不同的处理.

* 让您的类继承 `sdkbox::FacebookListener` 并重写下面的函数:
```cpp
#include "PluginFacebook/PluginFacebook.h"
class MyClass : public sdkbox::FacebookListener
{
private:
  void onLogin(bool isLogin, const std::string& msg);
  void onPermission(bool isLogin, const std::string& msg);
  void onAPI(const std::string& tag, const std::string& jsonData);
  void onSharedSuccess(const std::string& message);
  void onSharedFailed(const std::string& message);
  void onSharedCancel();
};
```

* 创建一个 __listener__ 监听事件:
```cpp
sdkbox::PluginFacebook::setListener(this);
```
