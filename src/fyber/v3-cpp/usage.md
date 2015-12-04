### 初始化 Fyber
* 在你的代码合适的地方初始化插件, 我们建议你在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 

```cpp
#include "PluginFyber/PluginFyber.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginFyber::init();
}
```

### 使用 Fyber
#### Offer Wall
使用显示 Offer Wall 
```cpp
sdkbox::PluginFyber::showOfferWall();
```

使用自定义的 __placementId__ 显示 Offer Wall 
```cpp
sdkbox::PluginFyber::showOfferWall("coins");
```

#### Rewarded Video
- iOS 参考 [rewarded-video-iOS](http://developer.fyber.com/content/ios/rewarded-video/introduction/existing-integration/)
- Android 参考 [rewarded-video-android](http://developer.fyber.com/content/android/rewarded-video/)

向服务器请求一个视频:
```cpp
sdkbox::PluginFyber::requestOffers();
```

向服务器请求一个 __placementId__ 的视频:
```
sdkbox::PluginFyber::requestOffers("coins");
```

显示奖励视频, 先调用 `requestOffers()`, 然后 `showOffers()`:
```cpp
sdkbox::PluginFyber::requestOffers();
sdkbox::PluginFyber::showOffers();
```

#### Interstitials
请求一个广告
```cpp
sdkbox::PluginFyber::requestInterstitial();
```

显示广告. 请先调用 `requestInterstitial` :
```cpp
sdkbox::PluginFyber::showInterstitial();
```

获取奖励
```cpp
sdkbox::PluginFyber::requestDeltaOfCoins();
```
或者:
```
sdkbox::PluginFyber::requestDeltaOfCoins("currencyId")
```

### 接收 Fyber 事件 (可选)

* 让你的类继承 `sdkbox::FyberListener`:
```cpp
#include "PluginFyber/PluginFyber.h"
class MyClass : public sdkbox::FyberListener
{
private:
	void onVirtualCurrencyConnectorFailed(int error,
	                                              const std::string& errorCode,
	                                              const std::string& errorMsg);
	void onVirtualCurrencyConnectorSuccess(double deltaOfCoins,
	                                               const std::string& currencyId,
	                                               const std::string& currencyName,
	                                               const std::string& transactionId);
	void onCanShowInterstitial(bool canShowInterstitial);
	void onInterstitialDidShow();
	void onInterstitialDismiss(const std::string& reason);
	void onInterstitialFailed();
	void onBrandEngageClientReceiveOffers(bool areOffersAvailable);
	void onBrandEngageClientChangeStatus(int status, const std::string& msg);
	void onOfferWallFinish(int status);
};
```

* 创建一个监听类来接收回调:
```cpp
sdkbox::PluginFyber::setListener(this);
```
