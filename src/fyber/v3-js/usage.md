### 注册 Javascript 函数

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginFyberJS.hpp"
#include "PluginFyberJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保有如下调用:
```cpp
sc->addRegisterCallback(register_all_PluginFyberJS);
sc->addRegisterCallback(register_all_PluginFyberJS_helper);
```

### 初始化 Fyber
* 在你的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginFyber.init();
```

### 使用 Fyber
#### Offer Wall
显示 Offer Wall 
```javascript
sdkbox.PluginFyber.showOfferWall();
```

使用自定义的 __placementId__ 显示 Offer Wall 
```javascript
sdkbox.PluginFyber.showOfferWall("coins");
```

#### Rewarded Video
- iOS 参考 [rewarded-video-iOS](http://developer.fyber.com/content/ios/rewarded-video/introduction/existing-integration/)
- Android 参考 [rewarded-video-android](http://developer.fyber.com/content/android/rewarded-video/)

向服务器请求一个视频:
```javascript
sdkbox.PluginFyber.requestOffers();
```

向服务器请求一个 __placementId__ 的视频:
```javascript
sdkbox.PluginFyber.requestOffers("coins");
```

显示奖励视频, 先调用 `requestOffers()`, 然后 `showOffers()`:
```javascript
sdkbox.PluginFyber.requestOffers();
sdkbox.PluginFyber.showOffers();
```

#### Interstitials
请求一个广告
```javascript
sdkbox.PluginFyber.requestInterstitial();
```

显示广告. 请先调用 `requestInterstitial` :
```javascript
sdkbox.PluginFyber.showInterstitial();
```

获取奖励
```javascript
sdkbox.PluginFyber.requestDeltaOfCoins();
```
或者
```
sdkbox.PluginFyber.requestDeltaOfCoins("currencyId")
```

### 接收 Fyber 事件 (可选)

```javascript
sdkbox.PluginFyber.setListener({
	onVirtualCurrencyConnectorFailed: function(error, errorCode, errorMsg) {},
	onVirtualCurrencyConnectorSuccess: function(deltaOfCoins, currencyId, currencyName, transactionId) {},
	onCanShowInterstitial: function(canShowInterstitial) {},
	onInterstitialDidShow: function() {},
	onInterstitialDismiss: function(reason) {},
	onInterstitialFailed: function() {},
	onBrandEngageClientReceiveOffers: function(areOffersAvailable) {},
	onBrandEngageClientChangeStatus: function(status, msg) {},
	onOfferWallFinish: function(status) {}
});
```
