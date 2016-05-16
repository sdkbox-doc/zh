### 初始化 Achievement
在初始化 Playphone 的 Achievement 之前，您需要做以下几件事:

  - 注册 Playphone 开发者账号 [Playphone Developer Portal](http://developer.playphone.com).
  - 创建游戏和相应的成就条目 [Playphone
   Developer Portal](https://developer.playphone.com/games).
  - 配置 Playphone 数据[Playphone plugin documentation](http://sdkbox- staging.github.io/en/plugins/playphone/v3 -cpp/#extra-steps).

在你的代码合适的地方初始化插件, 我们建议你在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 

```cpp
#include "PluginAchievement/PluginAchievement.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAchievement::init();
     sdkbox::IAP::init();
}
```

### 使用 Achievement
#### 解锁 achievement
```cpp
sdkbox::PluginAchievement::unlock(achievementId);
```
