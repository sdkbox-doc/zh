### 初始化 UnityAds
* 在您的代码合适的地方初始化插件, 我们建议您在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保您包含了对应的头文件:
```cpp
#include "PluginUnityAds/PluginUnityAds.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginUnityAds::init();
}
```

### 显示插屏广告

```cpp
std::string ad = "";
if (sdkbox::PluginUnityAds::isReady(ad)) {
    sdkbox::PluginUnityAds::show(ad);
} else {
    CCLOG("unityads is not ready");
}
```

### 接收 UnityAds 事件 (可选)

* 让您的类继承 `sdkbox::UnityAdsListener`
```cpp
#include "PluginUnityAds/PluginUnityAds.h"
class MyClass : public sdkbox::UnityAdsListener {
public:

  	 void unityAdsDidClick(const std::string& placementId) {
        CCLOG("unityads click %s", placementId.c_str());
    }

    void unityAdsPlacementStateChanged(const std::string& placementId,
                                PluginUnityAds::SBUnityAdsPlacementState oldState,
                                PluginUnityAds::SBUnityAdsPlacementState newState) {
        CCLOG("unityads state change %s %d->%d", placementId.c_str(), oldState, newState);
    }

    void unityAdsReady(const std::string& placementId) {
        CCLOG("unityads ready %s", placementId.c_str());
    }

    void unityAdsDidError(sdkbox::PluginUnityAds::SBUnityAdsError error, const std::string& message) {
        CCLOG("unityads error %d %s", error, message.c_str());
    }

    void unityAdsDidStart(const std::string& placementId) {
        CCLOG("unityads start %s", placementId.c_str());
    }

    void unityAdsDidFinish(const std::string& placementId, sdkbox::PluginUnityAds::SBUnityAdsFinishState state) {
        CCLOG("unityads finish %d %s", state, placementId.c_str());
    }

};
```

* 创建一个监听类来接收回调:
```cpp
sdkbox::PluginUnityAds::setListener(this);
```
