### 初始化 SdkboxAds
修改您的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```lua
sdkbox.PluginSdkboxAds:init();
```

### 使用 SdkboxAds

请求显示一个在默认的 AdUnit 中的默认广告，并以此完成一次简单的集成测试：
```javascript
sdkbox.SdkboxAds:play()
```

请求显示默认 AdUnit 中的广告：
```lua
sdkbox.SdkboxAds:play( zone_place_location, params );

// params is an object with string keys and values.
```
> 提示：每一个 AdUnit 都有自己的参数，可以参考每一个插件的文档。

请求显示一个指定的 AdUnit 中的广告：
```lua
sdkbox.SdkboxAds:play( ad_unit_name, zone_place_location, params );
```

请求显示定义在 sdkbox\_config.json 的 Placement 中的广告：
```lua
sdkbox.SdkboxAds:placement( placement_name );
```

更好的控制广告数据缓冲：
```lua
sdkbox.SdkboxAds:cacheControl( ad_unit, cacheOpts );

// cacheOpts is an object with keys and values as strings.
```
> 缓冲的选项是由 AdUnit 指定的， 请参考每个插件的相关文档。

### SdkboxAds 事件
这个插件允许您捕捉事件。

```lua
sdkbox.PluginSdkboxAds:setListener(function(args)
    if "onAdAction" == args.name then
        local ad_unit_id = args.ad_unit_id;
        local ad_name = args.ad_name;
        local ad_action_type = args.ad_action_type;
    elseif "onRewardAction" ==  args.name then
        local ad_unit_id = args.ad_unit_id;
        local ad_name = args.ad_name;
        local reward_amount = args.reward_amount;
        local reward_success = args.reward_success;
    end
end)
```
