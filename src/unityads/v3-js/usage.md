### 注册 Javascript 函数

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginUnityAdsJS.hpp"
#include "PluginUnityAdsJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保有如下调用:
```cpp
sc->addRegisterCallback(register_all_PluginUnityAdsJS);
sc->addRegisterCallback(register_all_PluginUnityAdsJS_helper);
```

### 初始化 UnityAds
* 在您的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginUnityAds.init();
```

### 显示插屏广告

```javascript
const placementId = '';
if (sdkbox.PluginUnityAds.isReady(placementId)) {
    sdkbox.PluginUnityAds.show(placementId);
} else {
    cc.log('unityads is not ready');
}
```

### 接收 UnityAds 事件 (可选)

```javascript
var plugin = sdkbox.PluginUnityAds
plugin.setListener({
    unityAdsDidClick: function(placementId) {
        console.log('unityAdsDidClick ' + placementId);
    },
    unityAdsPlacementStateChanged: function(placementId, oldState, newState) {
        console.log('unityAdsPlacementStateChanged:' + placementId + ' oldState:' + oldState + " newState:" + newState);
    },
    unityAdsReady: function(placementId) {
        console.log('unityAdsReady ' + placementId);
    },
    unityAdsDidError: function(error, message) {
        console.log('unityAdsDidError:' + error + ' message:' + message);
    },
    unityAdsDidStart: function(placementId) {
        console.log('unityAdsDidStart=' + placementId);
    },
    unityAdsDidFinish: function(placementId, state) {
        console.log('unityAdsDidFinish ' + placementId + ' state:' + state);
    }
})
plugin.init();
```
