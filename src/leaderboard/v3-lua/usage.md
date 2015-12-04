### 初始化 Leaderboard
* 修改 `Classes/AppDelegate.cpp` 包含如下头文件:
```lua
sdkbox.PluginLeaderboard:init();
sdkbox.IAP:init();
```

### 使用 Leaderboard
#### 提交分数
```lua
sdkbox.PluginLeaderboard:submitScore(leaderboardId, score);
```

#### 获取分数榜单
```lua
sdkbox.PluginLeaderboard:getLeaderboard(leaderboardId);
```

### 接收 Leaderboard 事件 (可选)

```lua
sdkbox.PluginLeaderboard:setListener(function(args)
    dump(args)
    if args.name == "onComplete" then
    elseif args.name == "onFail" then
    end
end)
```
