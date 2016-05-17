### 注册 Leaderboard

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginLeaderboardJS.hpp"
#include "PluginLeaderboardJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保有如下调用:
```cpp
sc->addRegisterCallback(register_all_PluginLeaderboardJS);
sc->addRegisterCallback(register_all_PluginLeaderboardJS_helper);
```

### 初始化 Leaderboard
在您的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginLeaderboard.init();
sdkbox.IAP.init();
```

### 使用 Leaderboard
#### 提交分数
```javascript
sdkbox.PluginLeaderboard.submitScore(leaderboardId, score);
```

#### 获取分数榜单
```javascript
sdkbox.PluginLeaderboard.getLeaderboard(leaderboardId);
```

### 接收 Leaderboard 事件 (可选)

```javascript
sdkbox.PluginLeaderboard.setListener({
	onComplete: function(leaderboard) {},
	onFail: function() {}
});
```
