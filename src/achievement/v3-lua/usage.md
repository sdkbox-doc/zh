### 初始化 Achievement
在初始化 Playphone 的 Achievement 之前，您需要做以下几件事:

  - 注册 Playphone 开发者账号 [Playphone Developer Portal](http://developer.playphone.com).
  - 创建游戏和相应的成就条目 [Playphone
   Developer Portal](https://developer.playphone.com/games).
  - 配置 Playphone 数据[Playphone plugin documentation](http://sdkbox- staging.github.io/en/plugins/playphone/v3 -cpp/#extra-steps).

修改你的lua代码用 `init()` 初始化插件. 这个可以在任何地方调用,但是必须在你要想使用 Achievement 的功能之前.
```lua
sdkbox.PluginAchievement:init();
sdkbox.IAP:init();
```

### 使用 Achievement
#### 解锁 achievement
```lua
sdkbox.PluginAchievement:unlock(achievementId)
```
