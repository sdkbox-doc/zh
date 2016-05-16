### 初始化 Vungle
* 通过在您的代码合适的位置调用 `init()` 方法来初始化这个插件。我们建议您在 `app.js` 中进行初始化。举例如下：
```javascript
sdkbox.PluginVungle.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginVungleJS.hpp"
#include "PluginVungleJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，添加如下内容：
```cpp
sc->addRegisterCallback(register_all_PluginVungleJS);
sc->addRegisterCallback(register_all_PluginVungelJS_helper);
```
这将注册 Javascript 回调函数。

### 显示广告
无论 __video__ 还是 __reward__ 类型的广告，可以在任何您想显示它们的地方加入代码：
```javascript
sdkbox.PluginVungle.show("video");
sdkbox.PluginVungle.show("reward");
```

### 捕捉 Vungle 事件（可选）
您可以捕捉 `Vungle` 事件来执行一些操作，比如在玩家观看了视频广告后给其发放奖励。

* 创建一个 __listener__ 用于事件回调 (通过写入事件日志举例如下)：
```javascript
sdkbox.PluginVungle.setListener({
    onVungleCacheAvailable : function() { cc.log("onVungleCacheAvailable") },
    onVungleStarted : function() { cc.log("onVungleStarted") },
    onVungleFinished : function() { cc.log("onVungleFinished") },
    onVungleAdViewed : function(isComplete) { cc.log("onVungleAdViewed" + isComplete) },
    onVungleAdReward : function(adName) { cc.log("onVungleAdReward:" + adName) }
})
```
