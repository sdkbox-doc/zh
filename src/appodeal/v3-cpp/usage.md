### 初始化 Appodeal
* 在你的代码合适的地方初始化插件, 我们建议你在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保你包含了对应的头文件:
```cpp
#include "PluginAppodeal/PluginAppodeal.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAppodeal::init();
}
```

### 使用 Appodeal
```cpp
// 设置用户 id
sdkbox::PluginAppodeal::setUserVkId("user id");

// 缓冲所有类型的广告
sdkbox::PluginAppodeal::cacheAd(sdkbox::PluginAppodeal::AdType::AppodealAdTypeAll);

// 显示广告
sdkbox::PluginAppodeal::showAd(sdkbox::PluginAppodeal::ShowStyle::AppodealShowStyleInterstitial);
```

### 接收 Appodeal events (可选)

* 让你的类继承 `sdkbox::AppodealListener`
```cpp
#include "PluginAppodeal/PluginAppodeal.h"
class ADListener : public sdkbox::AppodealListener {
public:
    virtual void onBannerDidLoadAd();
    virtual void onBannerDidFailToLoadAd();
    virtual void onBannerDidClick();
    virtual void onBannerPresent();

    virtual void onInterstitialDidLoadAd();
    virtual void onInterstitialDidFailToLoadAd();
    virtual void onInterstitialWillPresent();
    virtual void onInterstitialDidDismiss();
    virtual void onInterstitialDidClick();

    virtual void onVideoDidLoadAd();
    virtual void onVideoDidFailToLoadAd();
    virtual void onVideoDidPresent();
    virtual void onVideoWillDismiss();
    virtual void onVideoDidFinish();
};
```

* 创建一个监听类来接收回调:
* ```cpp
sdkbox::PluginAppodeal::setListener(this);
```
