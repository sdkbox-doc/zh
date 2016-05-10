### 修改 `AppDelegate.cpp`
* 修改 `Classes/AppDelegate.cpp` 包含以下头文件:
```lua
sdkbox.PluginAppnext:init()
```

### cache ad/video

```cpp
sdkbox.PluginAppnext:cacheAd("default")
sdkbox.PluginAppnext:cacheVideo("fullscreen")
```
**NOTE** : Appnext ads needs to be cached before use, auto-caching is not available with this plugin. It might take couple of minutes to cache ads, once cached you would be able to see the ads. While caching, ads are not available.


### 缓存插屏或者视频广告

```cpp
sdkbox.PluginAppnext:cacheAd("default")
sdkbox.PluginAppnext:cacheVideo("fullscreen")
```
**注意** : Appnext 的广告需要先缓存，再使用。


### 刷新插屏或者视频广告

```
sdkbox.PluginAppnext:refreshAds()
sdkbox.PluginAppnext:refreshVideo("fullscreen")
```
**NOTE** : 您需要在一个广告关闭时刷新它，否则下次不会显示广告。


### 显示插屏或者视频广告
```cpp
sdkbox.PluginAppnext:showAd("default")
sdkbox.PluginAppnext:showVideo("fullscreen")
```

### 隐藏插屏广告
```cpp
sdkbox.PluginAppnext:hideAd()
```

### 检查插屏或者视屏广告是否可以播放
```cpp
sdkbox.PluginAppnext:isAdReady()
sdkbox.PluginAppnext:isVideoReady("fullscreen")
```


### 接受 AppnextListner 事件 （可选）

```lua
sdkbox.PluginAppnext.setListener(function(args)
    local event = args.event
    if "onAdError" == event then
    elif "onAdLoaded" == event then
    elif "onAdOpened" == event then -- android 上没有回调
    elif "onAdClosed" == event then
    elif "onAdClicked" == event then

    elif "onVideoLoaded" == event then  -- ios 上没有回调
    elif "onVideoClicked" == event then -- ios 上没有回调
    elif "onVideoClosed" == event then  -- ios 上没有回调
    elif "onVideoEnded" == event then   -- ios 上没有回调
    elif "onVideoError" == event then   -- ios 上没有回调
    end
end)

```
