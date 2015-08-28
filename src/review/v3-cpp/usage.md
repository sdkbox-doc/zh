### 初始化 Review
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下:
```cpp
#include "PluginReview/PluginReview.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginReview::init();
}
```

### 设置 Review (可选)
如果你不要使用默认的提示字串,你可以设置自己的字串

`注意:` 如果你在 `sdkbox.config` 中把 `tryPromptWhenInit` 项设置为真,那必须在 `init()` 之前调用以下函数
```cpp
sdkbox::PluginReview::setCustomPromptTitle("custom title");
sdkbox::PluginReview::setCustomPromptMessage("custom message");
sdkbox::PluginReview::setCustomPromptCancelButtonTitle("custom cancel");
sdkbox::PluginReview::setCustomPromptRateButtonTitle("custom rate");
sdkbox::PluginReview::setCustomPromptRateLaterButtonTitle("custom rate later");
```

如果你的 `sdkbox.config` 中把 `tryPromptWhenInit` 项为 false, 那你可以调用 `tryToShowPrompt` 尝试提示用户评价你的应用,
如果所有的限制条件都满足,那提示框就会显示
```cpp
sdkbox::PluginReview::tryToShowPrompt();
```

你也可以强制显示评价提示框
```cpp
sdkbox::PluginReview::forceToShowPrompt();
```

如果你的 `sdkbox.config` 中的 `UserEventLimit` 项大于0的话，那你需要自已增加用户事件记数
```cpp
sdkbox::PluginReview::userDidSignificantEvent(true);
```

### 接收 Review 事件 (可选)
你可以接收 `Review` 事件,以便对不同事件做不同处理.一个简单的用法可以像下面这样:

* 让你的类继承 `sdkbox::ReviewListener`
```cpp
#include "PluginReview/PluginReview.h"
class MyClass : public sdkbox::ReviewListener
{
private:
    void didDisplayAlert();
    void didDeclineToRate();
    void didToRate();
    void didToRemindLater();
};
```

* 使用 __listener__ 来监听事件:
```cpp
sdkbox::PluginReview::setListener(this);
```

