### 初始化 Leaderboard
* 在你的代码合适的地方初始化插件, 我们建议你在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保你包含了对应的头文件:

```cpp
#include "PluginLeaderboard/PluginLeaderboard.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginLeaderboard::init();
     sdkbox::IAP::init();
}
```

### 使用 Leaderboard
#### 提交分数
```cpp
sdkbox::PluginLeaderboard::submitScore(leaderboardId, score);
```

#### 获取分数榜单
sdkbox::PluginLeaderboard::getLeaderboard(leaderboardId);


### 接收 Leaderboard 事件 (可选)

* 让你的类继承 `sdkbox::LeaderboardListener`:
```cpp
#include "PluginLeaderboard/PluginLeaderboard.h"
class MyClass : public sdkbox::LeaderboardListener
{
    void onComplete ( std::string leaderboard ) {}
    void onFail ( ) {}
};
```

* 创建一个监听类来接收回调:
```cpp
sdkbox::PluginLeaderboard::setListener(this);
```
