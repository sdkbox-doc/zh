### 注册 Javascript 函数
在 cocos2d-xjs 中使用 Achievement 函数, 您必须先注册他们.

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginAchievementJS.hpp"
#include "PluginAchievementJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保有如下调用:
```cpp
sc->addRegisterCallback(register_all_PluginAchievementJS);
sc->addRegisterCallback(register_all_PluginAchievementJS_helper);
```

### 初始化 Achievement
在初始化 Playphone 的 Achievement 之前，您需要做以下几件事:

  - 注册 Playphone 开发者账号 [Playphone Developer Portal](http://developer.playphone.com).
  - 创建游戏和相应的成就条目 [Playphone
   Developer Portal](https://developer.playphone.com/games).
  - 配置 Playphone 数据[Playphone plugin documentation](http://sdkbox- staging.github.io/en/plugins/playphone/v3 -cpp/#extra-steps).

* 在你的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginAchievement.init();
sdkbox.IAP.init();
```

### 使用 Achievement
#### 解锁 achievement
```javascript
sdkbox.PluginAchievement.unlock(achievementId);
```
