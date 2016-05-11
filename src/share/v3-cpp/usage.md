### 初始化 Share
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下：
```cpp
#include "PluginShare/PluginShare.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginShare::init();
}
```

### 分享内容
在初始化之后，您可以开始使用内容分享功能了：
```cpp
sdkbox::SocialShareInfo info;
info.text = "#sdkbox(www.sdkbox.com) - the cure for sdk fatigue ";
info.title = "sdkbox";
info.image = "http://www.sdkbox.com/assets/images/logo.png";
info.link = "http://www.sdkbox.com";

//sdkbox::SocialPlatform::Platform_Select will show platforms list, let user select which platform want to share
//sdkbox::SocialPlatform::Platform_Twitter will share with twitter directly
//sdkbox::SocialPlatform::Platform_Facebook will share with facebook directly
info.platform = sdkbox::SocialPlatform::Platform_Select;
sdkbox::PluginShare::share(info);
```


### 捕获 Share 事件（可选）
该插件允许您捕获 `Share` 事件以帮助您根据返回的内容进行相应的操作。一个简单的例子如下：

* 允许您的类继承 `sdkbox::ShareListener` 类
```cpp
#include "PluginShare/PluginShare.h"
class SListener : public sdkbox::ShareListener {
public:
    virtual void onShareState(const sdkbox::SocialShareResponse& response) {
        switch (response.state) {
            case sdkbox::SocialShareState::SocialShareStateNone: {
                CCLOG("SharePlugin::onShareState none");
                break;
            }
            case sdkbox::SocialShareState::SocialShareStateUnkonw: {
                CCLOG("SharePlugin::onShareState unkonw");
                break;
            }
            case sdkbox::SocialShareState::SocialShareStateBegin: {
                CCLOG("SharePlugin::onShareState begin");
                break;
            }
            case sdkbox::SocialShareState::SocialShareStateSuccess: {
                CCLOG("SharePlugin::onShareState success");
                break;
            }
            case sdkbox::SocialShareState::SocialShareStateFail: {
                CCLOG("SharePlugin::onShareState fail, error:%s", response.error.c_str());
                break;
            }
            case sdkbox::SocialShareState::SocialShareStateCancelled: {
                CCLOG("SharePlugin::onShareState cancelled");
                break;
            }
            case sdkbox::SocialShareStateSelectShow: {
                CCLOG("SharePlugin::onShareState show pancel %d", response.platform);
                break;
            }
            case sdkbox::SocialShareStateSelectCancelled: {
                CCLOG("SharePlugin::onShareState show pancel cancelled %d", response.platform);
                break;
            }
            case sdkbox::SocialShareStateSelected: {
                CCLOG("SharePlugin::onShareState show pancel selected %d", response.platform);
                break;
            }
            default: {
                CCLOG("SharePlugin::onShareState");
                break;
            }
        }
    }
};
```

* 创建一个 __listener__ 处理回调：
```cpp
sdkbox::PluginShare::setListener(this);
```
