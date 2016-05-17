### 初始化 Bee7
* 在您的代码合适的地方初始化插件, 我们建议您在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保您包含了对应的头文件:

```cpp
#include "PluginBee7/PluginBee7.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginBee7::init();
}
```

### 使用 Bee7
#### 显示 Game Wall
```cpp
sdkbox::PluginBee7::showGameWall();
```

### 接收 Bee7 事件 (可选)

* 让您的类继承 `sdkbox::Bee7Listener`:
```cpp
#include "PluginBee7/PluginBee7.h"
class MyClass : public sdkbox::Bee7Listener
{
    void onAvailableChange(bool available) = 0;
    void onVisibleChange(bool available) = 0;
    void onGameWallWillClose() = 0;
    void onGiveReward(long bee7Points,
                      long virtualCurrencyAmount,
                      const std::string& appId,
                      bool cappedReward,
                      long campaignId,
                      bool videoReward) = 0;
};
```

* 创建一个监听类来接收回调:
```cpp
sdkbox::PluginBee7::setListener(this);
```
