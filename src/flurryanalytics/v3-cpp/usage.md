### 初始化 Flurry Analytics
* 在你的代码合适的地方初始化插件, 我们建议你在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保你包含了对应的头文件:
```cpp
#include "PluginFlurryAnalytics/PluginFlurryAnalytics.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginFlurryAnalytics::init();
     // start session
     sdkbox::PluginFlurryAnalytics::startSession();
}
```

### 使用 Flurry Analytics
在初始化完成后,你就可以使用 Flurry Analytics 提供的功能了. 在你的代码中任意地方,使用 `logevent`:
```cpp
std::string eventName = "test event1";
sdkbox::PluginFlurryAnalytics::logEvent(eventName);
```

### 接收 Flurry Analytics 事件 (可选)
你可以接收 `Flurry Analytics` 事件, 确定 Flurry 会话是否创建成功.

* 让你的类继承 `sdkbox::FlurryAnalyticsListener`
```cpp
#include "PluginFlurryAnalytics/PluginFlurryAnalytics.h"
class MyClass : public sdkbox::FlurryAnalyticsListener
{
public:
      void flurrySessionDidCreateWithInfo(std::map<std::string, std::string>& info);
};
```

* 创建一个 __listener__ 来处理回调:
```cpp
sdkbox::PluginFlurryAnalytics::setListener(this);
```

### 结束 Flurry Analytics (只在 Android 上有效)
当你不再使用 `FlurryAnalytics` 或你的游戏结束时, 必须要把 `FlurryAnalytics` 会话结束. 这个在 Android 上必须调用,但是在 iOS 上是可选的. 比如:
```cpp
// 这个只在 android 上有效, 但是你在 iOS 调用,也没有关系
sdkbox::PluginFlurryAnalytics::endSession();
```
