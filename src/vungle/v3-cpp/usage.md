### 初始化 Vungle
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下：
```cpp
#include "PluginVungle/PluginVungle.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginVungle::init();
}
```

### 显示广告
无论 __video__ 还是 __reward__ 类型的广告，可以在任何您想显示它们的地方加入代码：
```cpp
sdkbox::PluginVungle::show("video");
sdkbox::PluginVungle::show("reward");
```

### 捕捉 Vungle 事件（可选）
您可以捕捉 `Vungle` 事件来暂停或者恢复您的游戏。

* 写一个继承于 `sdkbox::VungleListener` 的类。
```cpp
#include "PluginVungle/PluginVungle.h"
class MyClass : public sdkbox::VungleListener
{
private:
  void onVungleCacheAvailable();
  void onVungleStarted();
  void onVungleFinished();
  void onVungleAdViewed(bool isComplete);
  void onVungleAdReward(std::string adName);
}
```

* 创建一个 __listener__ 用于事件回调（可选）：
```cpp
sdkbox::PluginVungle::setListener(this);
```
