### 初始化 Valuepotion
* 在您的代码合适的地方初始化插件, 我们建议您在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保您包含了对应的头文件:
```cpp
#include "PluginValuePotion/PluginValuePotion.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginValuePotion::init();
}
```

### 使用 Valuepotion

```cpp
sdkbox::PluginValuePotion::setTest(true);
sdkbox::PluginValuePotion::hasCachedInterstitial("default");

sdkbox::PluginValuePotion::trackEvent("test event");
sdkbox::PluginValuePotion::trackEvent("test event with value 23", 23);
sdkbox::PluginValuePotion::trackEvent("category", "event name", "label", 45);

sdkbox::PluginValuePotion::trackPurchaseEvent("test event", 56, "RMB", "order id", "product id");
sdkbox::PluginValuePotion::trackPurchaseEvent("test event", 67, "USD", "order id", "product id", "campaign id", "content id");
sdkbox::PluginValuePotion::trackPurchaseEvent("categroy", "event name", "label", 78, "ILY", "order id", "product id", "campaign id", "content id");

sdkbox::PluginValuePotion::userinfo("id", "user id");
sdkbox::PluginValuePotion::userinfo("serverid", "server id");
sdkbox::PluginValuePotion::userinfo("birth", "19991111"); //YYYYMMDD
sdkbox::PluginValuePotion::userinfo("gender", "M");
sdkbox::PluginValuePotion::userinfo("level", "9");
sdkbox::PluginValuePotion::userinfo("friends", "3");
sdkbox::PluginValuePotion::userinfo("accounttype", "facebook");
```

### 接收 ValuePotion 事件 (可选)

* 让您的类继承 `sdkbox::ValuePotionListener`
```cpp
#include "PluginValuePotion/PluginValuePotion.h"
class MyClass : public sdkbox::ValuePotionListener
{
private:
    virtual void onCacheInterstitial(const char *placement);

    virtual void onFailToCacheInterstitial(const char *placement, const char *errorMessage);

    virtual void onOpenInterstitial(const char *placement);

    virtual void onFailToOpenInterstitial(const char *placement, const char *errorMessage);

    virtual void onCloseInterstitial(const char *placement);

    virtual void onRequestOpenURL(const char *placement, const char *URL);

    virtual void onRequestPurchase(const char *placement, const char *name, const char *productId, int quantity, const char *campaignId, const char *contentId);

    virtual void onRequestRewards(const char *placement, std::vector<sdkbox::ValuePotionReward> rewards);
};
```

* 创建一个监听类来接收回调:
```cpp
sdkbox::PluginValuePotion::setListener(this);
```
