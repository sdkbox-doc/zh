### 注册 Javascript 函数

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginBee7JS.hpp"
#include "PluginBee7JSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保有如下调用:
```cpp
sc->addRegisterCallback(register_all_PluginBee7JS);
sc->addRegisterCallback(register_all_PluginBee7JS_helper);
```

### 初始化 Bee7
* 在您的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginBee7.init();
```

### 使用 Bee7
#### 显示 Game Wall
```javascript
sdkbox.PluginBee7.showGameWall();
```

### 接收 Bee7 事件 (可选)

```javascript
sdkbox.PluginBee7.setListener({
	onAvailableChange: function(available) {},
	onVisibleChange: function(available) {},
	onGameWallWillClose: function() {},
	onGiveReward: function(bee7Points, virtualCurrencyAmount, appId, cappedReward,
						   campaignId, videoReward) {}
});
```
