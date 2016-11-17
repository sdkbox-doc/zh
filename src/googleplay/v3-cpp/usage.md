

### 初始化 Google Play Games
在你代码合适的位置初始化插件.我们建议在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中初始化. 请确保你添加了对应的头文件:
```cpp
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginGPG::init();
}
```

### Authorization (认证)
所有的 Google Play Game 服务都要求用户登录, 在使用任何服务之前，都要保证用户已经登录成功了.
更多信息请见[官方文档](https://developers.google.com/games/services/cpp/GettingStartedNativeClient#concepts)

### Achevements (成就)
你需要联接游戏服务到你的游戏中，同时你的游戏要是 "已发布" 状态, 成就才有效.
更多信息请见[官方文档](https://developers.google.com/games/services/common/concepts/achievements)

### Leaderboards (排行榜)
你需要联接游戏服务到你的游戏中，同时你的游戏要是 "已发布" 状态, 排行榜才有效.
更多信息请见[官方文档](https://developers.google.com/games/services/common/concepts/leaderboards)

### Saved Games (存储游戏)
存储游戏功能需要在初始化阶段调用 `EnableSnapshots()` , 同时在 Google Play 开发者中心把它设置为启用状态.
更多信息请见[官方文档](https://developers.google.com/games/services/common/concepts/savedgames)

### Realtime multiplayer (实时多人)
你需要联接游戏服务到你的游戏中，同时你的游戏要是 "已发布" 状态, Realtime multiplayer才有效.
更多信息请见[官方文档](https://developers.google.com/games/services/common/concepts/realtimeMultiplayer)

### Turn-based multiplayer (回合多人)
你需要联接游戏服务到你的游戏中，同时你的游戏要是 "已发布" 状态, Turn-based multiplayer 才有效.
更多信息请见[官方文档](https://developers.google.com/games/services/common/concepts/turnbasedMultiplayer)

### Events and Quests (事件和任务)
你需要联接游戏服务到你的游戏中，同时你的游戏要是 "已发布" 状态, Events and Quests 才有效.
更多信息请见[官方文档](https://developers.google.com/games/services/common/concepts/quests)

### Player Statistics (玩家状态信息)
Player Stats 添加了有用的数据分析到你的游戏中.
更多信息请见[官方文档](https://developers.google.com/games/services/cpp/stats)

### Nearby Connections (附近联接)
Nearby Connections 让你的游戏支持本地多人，屏幕共享功能.
更多信息请见[官方文档](https://developers.google.com/games/services/cpp/nearby)
