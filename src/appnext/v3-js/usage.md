### 注册 Javascript 函数

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginAppnextJS.hpp"
#include "PluginAppnextJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保有如下调用:
```cpp
sc->addRegisterCallback(register_all_PluginAppnextJS);
sc->addRegisterCallback(register_all_PluginAppnextJS_helper);
```

### 初始化 Appnext
* 在你的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginAppnext.init();
```

### 缓存插屏或者视频广告

```cpp
sdkbox.PluginAppnext.cacheAd("default");
sdkbox.PluginAppnext.cacheVideo("fullscreen");
```
**注意** : Appnext 的广告需要先缓存，再使用。


### 刷新插屏或者视频广告

```
sdkbox.PluginAppnext.refreshAds();
sdkbox.PluginAppnext.refreshVideo("fullscreen");
```
**NOTE** : 你需要在一个广告关闭时刷新它，否则下次不会显示广告。


### 显示插屏或者视频广告
```cpp
sdkbox.PluginAppnext.showAd("default");
sdkbox.PluginAppnext.showVideo("fullscreen");
```

### 隐藏插屏广告
```cpp
sdkbox.PluginAppnext.hideAd();
```

### 检查插屏或者视屏广告是否可以播放
```cpp
sdkbox.PluginAppnext.isAdReady();
sdkbox.PluginAppnext.isVideoReady("fullscreen");
```


### 接受 AppnextListner 事件 （可选）

```javascript

sdkbox.PluginAppnext.setListener({
    onAdError : function(msg) { },
    onAdLoaded : function() { },
    onAdOpened : function() { }, // android 上没有回调
    onAdClosed : function() { },
    onAdClicked : function() { },

    onVideoLoaded : function(name) { },     // ios 上没有回调
    onVideoClicked : function(name) { },    // ios 上没有回调
    onVideoClosed : function(name) { },     // ios 上没有回调
    onVideoEnded : function(name) { },      // ios 上没有回调
    onVideoError : function(name, msg) { }  // ios 上没有回调
});

```
