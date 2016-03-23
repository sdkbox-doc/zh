### 初始化 Appnext
* 在你的代码合适的地方初始化插件, 我们建议你在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保你包含了对应的头文件:
```cpp
#include "PluginAppnext/PluginAppnext.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAppnext::init();
}
```

### 缓存插屏或者视频广告

```cpp
sdkbox::PluginAppnext::cacheAd("default");
sdkbox::PluginAppnext::cacheVideo("fullscreen");
```
**注意** : Appnext 的广告需要先缓存，再使用。


### 刷新插屏或者视频广告

```
sdkbox::PluginAppnext::refreshAds();
sdkbox::PluginAppnext::refreshVideo("fullscreen");
```
**NOTE** : 你需要在一个广告关闭时刷新它，否则下次不会显示广告。


### 显示插屏或者视频广告
```cpp
sdkbox::PluginAppnext::showAd("default");
sdkbox::PluginAppnext::showVideo("fullscreen");
```

### 隐藏插屏广告
```cpp
sdkbox::PluginAppnext::hideAd();
```

### 检查插屏或者视屏广告是否可以播放
```cpp
sdkbox::PluginAppnext::isAdReady();
sdkbox::PluginAppnext::isVideoReady("fullscreen");
```

### 接受 AppnextListner 事件 （可选）
* 让你的类继承 `AppnextListener`
```cpp
#include "PluginAppnext/PluginAppnext.h"
class MyClass : public sdkbox::AppnextListener
{
private:
    void onAdError(const std::string& msg) {}
    void onAdLoaded() {}
    void onAdOpened() {} // android 上没有回调
    void onAdClosed() {}
    void onAdClicked() {}

    void onVideoLoaded(const std::string& name) {} // ios 上没有回调
    void onVideoClicked(const std::string& name) {} // ios 上没有回调
    void onVideoClosed(const std::string& name) {} // ios 上没有回调
    void onVideoEnded(const std::string& name) {} // ios 上没有回调
    void onVideoError(const std::string& name, const std::string& msg) {} // ios 上没有回调
}
```
