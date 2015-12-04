### 初始化 Fyber
修改你的lua代码用 `init()` 初始化插件. 这个可以在任何地方调用,但是必须在你要想使用 Fyber 的功能之前.
```lua
sdkbox.PluginFyber:init();
```

### 使用 Fyber
#### Offer Wall
显示 Offer Wall 
```lua
sdkbox.PluginFyber:showOfferWall();
```

使用自定义的 __placementId__ 显示 Offer Wall 
```lua
sdkbox.PluginFyber:showOfferWall("coins");
```

#### Rewarded Video
- iOS 参考 [rewarded-video-iOS](http://developer.fyber.com/content/ios/rewarded-video/introduction/existing-integration/)
- Android 参考 [rewarded-video-android](http://developer.fyber.com/content/android/rewarded-video/)

向服务器请求一个视频:
```lua
sdkbox.PluginFyber:requestOffers();
```

向服务器请求一个 __placementId__ 的视频:
```
sdkbox.PluginFyber:requestOffers("coins");
```

显示奖励视频, 先调用 `requestOffers()`, 然后 `showOffers()`:
```lua
sdkbox.PluginFyber:requestOffers();
sdkbox.PluginFyber:showOffers();
```

#### Interstitials
请求一个广告
```lua
sdkbox.PluginFyber:requestInterstitial();
```

显示广告. 请先调用 `requestInterstitial` :
```lua
sdkbox.PluginFyber:showInterstitial();
```

获取奖励
```lua
sdkbox.PluginFyber:requestDeltaOfCoins();
```
或者
```
sdkbox.PluginFyber:requestDeltaOfCoins("currencyId")
```

### 接收 Fyber 事件 (可选)

```lua
sdkbox.PluginFyber:setListener(function(args)
    dump(args)
    if args.name == "onVirtualCurrencyConnectorFailed" then
    elseif args.name == "onVirtualCurrencyConnectorSuccess" then
    elseif args.name == "onCanShowInterstitial" then
    elseif args.name == "onInterstitialDidShow" then
    elseif args.name == "onInterstitialDismiss" then
    elseif args.name == "onInterstitialFailed" then
    elseif args.name == "onBrandEngageClientReceiveOffers" then
    elseif args.name == "onBrandEngageClientChangeStatus" then
    elseif args.name == "onOfferWallFinish" then
    end
end)
```
