### 初始化 AdColony
* 在您的代码合适的地方初始化插件, 我们建议您在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保您包含了对应的头文件:
```cpp
#include "PluginAdColony/PluginAdColony.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAdColony::init();
}
```

### 显示广告
在您想要显示广告的地方,输入如下代码:
```cpp
sdkbox::PluginAdColony::show("video");
```
或:
```cpp
sdkbox::PluginAdColony::show("v4vc");
```

### 接收 AdColony 事件 (可选)
您可以接收 `AdColony` 的事件, 这样您可以在玩家观看完广告后给他相应的奖励.

* 让您的类继承 `sdkbox::AdColonyListener`
```cpp
#include "PluginAdColony/PluginAdColony.h"
class MyClass : public sdkbox::AdColonyListener
{
private:

    /*
     * Interstitial Callback
     */
    void adColonyInterstitialDidLoad(const std::string& interstitial);
    void adColonyInterstitialDidFailToLoad(const std::string& error);
    void adColonyInterstitialWillOpen(const std::string& interstitial);
    void adColonyInterstitialDidClose(const std::string& interstitial);
    void adColonyInterstitialExpired(const std::string& interstitial);
    void adColonyInterstitialWillLeaveApplication(const std::string& interstitial);
    void adColonyInterstitialDidReceiveClick(const std::string& interstitial);
    void adColonyInterstitialIapOpportunity(const std::string& interstitial, const std::string& iapProductID, int engagement);

    /*
     * Banner Callback
     */
    void adColonyAdViewDidLoad(const std::string& adView);
    void adColonyAdViewDidFailToLoad(const std::string& error);
    void adColonyAdViewWillLeaveApplication(const std::string& adView);
    void adColonyAdViewWillOpen(const std::string& adView);
    void adColonyAdViewDidClose(const std::string& adView);
    void adColonyAdViewDidReceiveClick(const std::string& adView);

    /*
     * Rewards Callback
     */
    void adColonyReward(const std::string name, const std::string& currencyName, int amount, bool success);

};
```

* 创建一个监听类来接收回调:
```cpp
sdkbox::PluginAdColony::setListener(this);
```
