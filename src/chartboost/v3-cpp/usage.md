### 初始化 Chartboost
* 在你的代码合适的地方初始化插件, 我们建议你在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保你包含了对应的头文件:
```cpp
#include "PluginChartboost/PluginChartboost.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginChartboost::init();
}
```

### 显示广告
在你的代码中,想显示广告的地方加下以下代码:
```cpp
// To use the Chartboost predefined locations
sdkbox::PluginChartboost::show(sdkbox::CB_Location_Default);
// To use customized location
sdkbox::PluginChartboost::show("your_ad_name");
```

### 接收 Chartboost 事件 (可选)
你可以接收 `Chartboost` 事件, 当玩家观看了广告过,你可以在代码中做某些操作,比如奖励玩家.

* 让你的类继承 `sdkbox::ChartboostListener`
```cpp
#include "PluginChartboost/PluginChartboost.h"
class MyClass : public sdkbox::ChartboostListener
{
public:
      void onChartboostCached(const std::string& name);
      void onChartboostShouldDisplay(const std::string& name);
      void onChartboostDisplay(const std::string& name);
      void onChartboostDismiss(const std::string& name);
      void onChartboostClose(const std::string& name);
      void onChartboostClick(const std::string& name);
      void onChartboostReward(const std::string& name, int reward);
      void onChartboostPauseClickForConfirmation();
};
```

* 创建一个 __listener__ 来处理回调:
```cpp
sdkbox::PluginChartboost::setListener(this);
```
