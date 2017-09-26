### 初始化 SdkboxAds
* 修改您的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```lua
sdkbox.PluginSdkboxPlay:init();
```

### 使用 SdkboxPlay


#### 介绍
SdkboxPlay 插件 是一个针对 Google Play 以及 Game Center 社交服务的抽象。针对每个平台，在通用的 API 下访问 Leaderboards 以及 Achievements 插件。
为了能适用于两个插件平台，SdkboxPlay 在实现上做了一些权衡，具体细节将在文档的相关部分描述。

##### Achievements

Achievements 插件在不同的开发者平台上有不同的定义。
以下是在 GooglePlay 以及 GameCenter 下 Achievements 插件一些概念上的不同：
* Google Play 区分普通成就以及可累积的成就。Google 保持对可累计成就的进度持续追踪。而普通成就只能达成一次。
* 在 Game Center 下 Achievements 所有的成就都是可累计成就， 但是 Game Center 并不持续跟踪这些成就的进度。这些成就将在游戏过程中被达成。并且这些成就可以被重复解锁多次。
* Google Play 有新解锁成就的概念（第一次解锁），而Game Center则有可周期性解锁的成就。这两个概念是互补的。

为了使以上概念统一， SdkboxPlay API 做了如下设计：

* 允许您定义非累计式的成就。对于 iOS 平台来说，就是将累计值设为100的累计式的成就，因为这表明这个成就即将被解锁（并只解锁一次）。
* 允许您定义累计式的成就。在 GooglePlay 平台下，累计式插件可以在 app 控制台定义自己的解锁值。
* 为了保持一致，建议您定义 Google Play 下的成就的解锁值为100。这个值也是 Game Center 下的成就解锁值。

##### Leaderboards

Leaderboards 插件在不同的开发者平台上有不同的定义。
为了简单，当前的 SdkboxPlay 实现不允许定义组队排行榜。但是对于两个平台您都可以定义任意数量的排行榜。
尽管 GooglePlay 和 GameCenter 都可以采用相同的方式定义排行榜，但是在运行是二者还是有区别的：

* Google Play 会为每一个排行榜创建三种时间表的排行：每天，每周以及全时间段的排行。
* Game Center 则只会创建一个时间表的排行。

这一点不同在下面的回调方法中也将会看到。

#### 使用

调用 `sdkbox::SdkboxPlay::init()` 将会配置在 sdkox\_config.json 文件中定义的排行榜以及成就系统。

首先，为了连接一个游戏服务平台必须调用下列方法：

```lua
sdkbox.PluginSdkboxPlay:signin();
```

如果连接成功，您将可以通过下列 API 来使用 SdkboxPlay：

##### Leaderboards

```lua
sdkbox.PluginSdkboxPlay:submitScore( leaderboard_name, score )
```

这个方法发送一个更新请求给排行榜。排行榜的名字必须是在配置文件中所定义的。
如果该请求发送给一个不存在的排行榜，那么该请求将不起任何作用。
是否存储这个更新请求的值，取决与开发者控制台配置（比如：总是存储最新的分数，或者总是存储最高分）。
这个方法还将触发下面的毁掉方法：

```lua
sdkbox.PluginSdkboxPlay:onScoreSubmitted(
        leaderboard_name,
        score,
        maxScoreAllTime,
        maxScoreWeek,
        maxScoreToday )
```

对于 iOS 来说，仅有一个时间表排行，所以后面3个参数都是 false 。

```lua
sdkbox.PluginSdkboxPlay:showLeaderboard( leaderboard_name );
```

这个方法请求显示排行榜信息。这将会在不同平台下显示平台特有的 UI 。对于 iOS 来说，显示排行榜与显示成就的 UI 并没有什么区别，所以这个方法在 iOS 下只是会显示排行榜的视图。

##### Achievements

```lua
sdkbox.PluginSdkboxPlay:unlockAchievement( achievement_name );
```

解锁一个非累计式的成就。这在 iOS 平台上， 将会发送一个请求给 Game Center 使得一个累计式成就直接达到100点从而解锁。
如果这个成就在配置文件中定义的不正确（错误的 ID），或者 SdkboxPlay 认为成就的类型不正确（是在Google Play下的累计式成就）,那么这个方法就会静默失败。
如果该方法成功，那么就会触发一个监听事件：onAchievementUnlocked( const std::string& achievement_name, bool newlyUnlocked) 。

```lua
sdkbox.PluginSdkboxPlay:incrementAchievement( achievement_name, increment );
```

增加累计式成就的解锁点数。
如果这个成就在配置文件里定义不正确（错误的或者已经存在的 ID ），或者 SdkboxPlay 认为成就的类型不正确，那么这个方法就会静默失败。
如果这个方法调用成功，它将触发下列两个回调事件：

* 如果这个累计式成就还没有达到解锁的点数，那么就触发 `onIncrementalAchievementStep( const std::string& achievement_name, int step )` 。
* 如果这个累计式成就达到点数第一次被解锁，那么就触发 `onIncrementalAchievementUnlocked( const std::string& achievement_name, bool newlyUnlocked)` 。

```lua
sdkbox.PluginSdkboxPlay:showAchievements( );
```

这个方法显示默认的成就视图。这个视图将只显示公开的成就。针对不同的平台显示特定的信息。比如该成就是否解锁，剩余的解锁步骤（仅适用于 Google Play ）平台，总共获得的经验值等等。

##### 游戏数据云保存

```cpp
sdkbox.PluginSdkboxPlay:loadAllGameData();
```

加载所有保存在云中的数据(iOS中用iCloud, Android中用Google Drive 来存储).

```cpp
sdkbox.PluginSdkboxPlay:saveGameDataBinary(name, data, length);
```

保存 Lua string.


### SdkboxPlay 事件
该插件允许您捕捉事件。

```lua
sdkbox.PluginSdkboxPlay:setListener(function(args)
    if "onConnectionStatusChanged" == args.name then
        local status = args.status;

    elseif "onScoreSubmitted" ==  args.name then
        local leaderboard_name = args.leaderboard_name;
        local score= args.score;
        local maxScoreAllTime= args.maxScoreAllTime;
        local maxScoreWeek= args.maxScoreWeek;
        local maxScoreToday= args.maxScoreToday;

    elseif "onIncrementalAchievementUnlocked" ==  args.name then
        local achievement_name = args.achievement_name;

    elseif "onIncrementalAchievementStep" ==  args.name then
        local achievement_name = args.achievement_name;
        local step = args.step;

    elseif "onAchievementUnlocked" ==  args.name then
        local achievement_name = args.achievement_name;
        local newlyUnlocked = args.newlyUnlocked;

    end
end)
```
