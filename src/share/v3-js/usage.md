### 注册 Javascript 函数
您需要在使用之前，在 cocos2d-x 中注册所有的 Youtube JS 函数。

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginShareJS.hpp"
#include "PluginShareJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，添加如下内容：
```cpp
sc->addRegisterCallback(register_all_PluginShareJS);
sc->addRegisterCallback(register_all_PluginShareJS_helper);
```

### 初始化 Share
通过在您的代码合适的位置调用 `init()` 方法来初始化这个插件。我们建议您在 `app.js` 中进行初始化。举例如下：
```javascript
sdkbox.PluginShare.init();
```

### 分享
在初始化之后，您可以开始使用 Share 插件的功能。在任何您想使用分享功能的地方调用 `share` 方法：
```javascript
var shareInfo = {};
shareInfo.text = "#sdkbox(www.sdkbox.com) - the cure for sdk fatigue - from js - ";
shareInfo.title = "sdkbox";
shareInfo.image = "http://www.sdkbox.com/assets/images/logo.png";
shareInfo.link = "http://www.sdkbox.com";

//sdkbox.SocialPlatform.Platform_Select will show platforms list, let user select which platform want to share
//sdkbox.SocialPlatform.Platform_Twitter will share with twitter directly
//sdkbox.SocialPlatform.Platform_Facebook will share with facebook directly
shareInfo.platform = sdkbox.SocialPlatform.Platform_Select;
plugin.share(shareInfo);
```

所有 sdkbox.SocialPlatform 的可用值如下：

- Platform_Unknow
- Platform_Twitter
- Platform_Facebook
- Platform_SMS
- Platform_Mail
- Platform_Native
- Platform_Select
- Platform_All


所有 sdkbox.SocialShareState 的可用值如下：

- SocialShareStateNone
- SocialShareStateUnkonw
- SocialShareStateBegin
- SocialShareStateSuccess
- SocialShareStateFail
- SocialShareStateCancelled
- SocialShareStateSelectShow
- SocialShareStateSelected
- SocialShareStateSelectCancelled

### 系统分享

你也可以使用 ios/android 系统自带提供的分享功能:
```js
var shareInfo = {};
shareInfo.text = "#sdkbox(www.sdkbox.com) - the cure for sdk fatigue ";
shareInfo.title = "sdkbox";
//shareInfo.image = "path/to/image"
shareInfo.link = "http://www.sdkbox.com";
sdkbox::PluginShare::nativeShare(info);

// 使用系统分享，以下两个属性无效
//shareInfo.showDialog = false;
//shareInfo.platform = sdkbox.SocialPlatform.Platform_Select;

sdkbox.PluginShare.nativeShare(shareInfo);
```

*注意*:

* IOS: 分享成功后，会收到分享成功事件，具体分享对应的操作会在 sdkbox::SocialShareResponse 的 error 属性中
* Android: 能收到分享成功事件，但是这个不是真正意义的分享成功, 只是把分享的对话框显示出来了, 因为在 android 上, 无法收到分享成功的事件

### 捕获 Share 事件（可选）
该插件允许您捕获 `Share` 事件以帮助您根据返回的内容进行相应的操作。一个简单的例子如下：
```javascript
var plugin = sdkbox.PluginShare
plugin.setListener({
    onShareState: function(response) {
        console.log("PluginShare onSharestate:" + response.state + " error:" + response.error)
        if (response.state == sdkbox.SocialShareState.SocialShareStateSuccess) {
            console.log("post success")
        }
    }
})
plugin.init();
```
