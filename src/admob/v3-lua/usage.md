### 初始化 AdMob
* 修改您的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```lua
sdkbox.PluginAdMob:init()
```

### 缓存广告数据
```lua
sdkbox.PluginAdMob:cache("home")
sdkbox.PluginAdMob:cache("gameover")
```

### 显示广告
```lua
sdkbox.PluginAdMob:show("home")
sdkbox.PluginAdMob:show("gameover")
```

### 隐藏广告
You can not hide an interstitial ad
```lua
sdkbox.PluginAdMob:hide("home")
```

### 检查广告数据可用性
```lua
sdkbox.PluginAdMob:isAvailable("home")
sdkbox.PluginAdMob:isAvailable("gameover")
```

### 实现 AdMobListener
* 您可以实现 AdMobListener 用来设置回调，比如当一个视频播放完成的时候。
```lua

sdkbox.PluginAdMob.setListener(function(args)
    local event = args.event
    if "adViewDidReceiveAd" == event then
    elif "adViewDidFailToReceiveAdWithError" == event then
    elif "adViewWillPresentScreen" == event then
    elif "adViewDidDismissScreen" == event then
    elif "adViewWillDismissScreen" == event then
    elif "adViewWillLeaveApplication" == event then
    elif "reward" == event then
    end
end)

```
