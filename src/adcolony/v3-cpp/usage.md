### 初始化 AdColony
* 在您的代码合适的地方初始化插件, 我们建议您在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保您包含了对应的头文件:
```cpp
#include "PluginAdColony/PluginAdColony.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAdColony::init();
}
```

### 显示广告
在您想要显示广告的地方,输入如下代码:
```cpp
sdkbox::PluginAdColony::show("video");
```
或:
```cpp
sdkbox::PluginAdColony::show("v4vc");
```

### 接收 AdColony 事件 (可选)
您可以接收 `AdColony` 的事件, 这样您可以在玩家观看完广告后给他相应的奖励.

* 让您的类继承 `sdkbox::AdColonyListener`
```cpp
#include "PluginAdColony/PluginAdColony.h"
class MyClass : public sdkbox::AdColonyListener
{
private:
  void onAdColonyChange(const sdkbox::AdColonyAdInfo& info, bool available);
  void onAdColonyReward(const sdkbox::AdColonyAdInfo& info,
		const std::string& currencyName, int amount, bool success);
  void onAdColonyStarted(const sdkbox::AdColonyAdInfo& info);
  void onAdColonyFinished(const sdkbox::AdColonyAdInfo& info);
};
```

* 创建一个监听类来接收回调:
```cpp
sdkbox::PluginAdColony::setListener(this);
```
