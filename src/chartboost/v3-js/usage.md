### 初始化 Chartboost
* 在你的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginChartboost.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含以下头文件:
```cpp
#include "PluginChartboostJS.hpp"
#include "PluginChartboostJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 调用以下函数:
```cpp
sc->addRegisterCallback(register_all_PluginChartboostJS);
sc->addRegisterCallback(register_PluginChartboostJs_helper);
```

### 显示广告
在你的代码中任何地方都可以显示广告:
```javascript
// To use the Chartboost predefined locations
sdkbox.PluginChartboost.show("Default");
// To use customized location
sdkbox.PluginChartboost.show("your_ad_name");
```

### 接收 Chartboost 事件 (可选)
你可以接收 `Chartboost` 事件, 当玩家观看了广告过,你可以在代码中做某些操作,比如奖励玩家.

* 创建一个监听 (用logging来显示返回内容):
```javascript
sdkbox.PluginChartboost.setListener({
    onChartboostCached : function (name) { cc.log("onChartboostCached " + name) },
    onChartboostShouldDisplay : function (name) { cc.log("onChartboostShouldDisplay " + name) },
    onChartboostDisplay : function (name) { cc.log("onChartboostDisplay " + name) },
    onChartboostDismiss : function (name) { cc.log("onChartboostDismiss " + name) },
    onChartboostClose : function (name) { cc.log("onChartboostClose " + name) },
    onChartboostClick : function (name) { cc.log("onChartboostClick " + name) },
    onChartboostReward : function (name, reward) { cc.log("onChartboostReward " + name + " reward " + reward) },
    onChartboostFailedToLoad : function (name, e) { cc.log("onChartboostFailedToLoad " + name + " load error " + e) },
    onChartboostFailToRecordClick : function (name, e) { cc.log("onChartboostFailToRecordClick " + name + " click error " + e) },
    onChartboostConfirmation : function () { cc.log("onChartboostConfirmation") },
    onChartboostCompleteStore : function () { cc.log("onChartboostCompleteStore") },
})
```
