### 注册 Javascript 函数

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginAppodealJS.hpp"
#include "PluginAppodealJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保有如下调用:
```cpp
sc->addRegisterCallback(register_all_PluginAppodealJS);
sc->addRegisterCallback(register_all_PluginAppodealJS_helper);
```

### 初始化 Appodeal
* 在你的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化, 比如:
```javascript
sdkbox.PluginAppodeal.init();
```

### 使用 Appodeal
```js
plugin.setUserVkId("user id");
plugin.cacheAd(15);
```

### 接收 Appodeal events (可选)

```javascript
var plugin = sdkbox.PluginAppodeal
plugin.setListener({
    onBannerDidLoadAd: function() { cc.log("onBannerDidLoadAd") },
    onBannerDidFailToLoadAd: function() { cc.log("onBannerDidFailToLoadAd") },
    onBannerDidClick: function() { cc.log("onBannerDidClick") },
    onBannerPresent: function() { cc.log("onBannerPresent") },
    onInterstitialDidLoadAd: function() { cc.log("onInterstitialDidLoadAd") },
    onInterstitialDidFailToLoadAd: function() { cc.log("onInterstitialDidFailToLoadAd") },
    onInterstitialWillPresent: function() { cc.log("onInterstitialWillPresent") },
    onInterstitialDidDismiss: function() { cc.log("onInterstitialDidDismiss") },
    onInterstitialDidClick: function() { cc.log("onInterstitialDidClick") },
    onVideoDidLoadAd: function() { cc.log("onVideoDidLoadAd") },
    onVideoDidFailToLoadAd: function() { cc.log("onVideoDidFailToLoadAd") },
    onVideoDidPresent: function() { cc.log("onVideoDidPresent") },
    onVideoWillDismiss: function() { cc.log("onVideoWillDismiss") },
    onVideoDidFinish: function() { cc.log("onVideoDidFinish") }
})
plugin.init()
```
