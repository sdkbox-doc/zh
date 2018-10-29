### 初始化 AdMob
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下：
```cpp
#include "PluginAdMob/PluginAdMob.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAdMob::init();
}
```

### 缓存广告数据

```cpp
sdkbox::PluginAdMob::cache("home");
sdkbox::PluginAdMob::cache("gameover");
```
### 注意：AdMob 需要在使用前缓存广告数据，并且该插件不支持自动缓存。缓存广告数据可能会花费数分钟的时间，一旦缓存完成您将可以看到广告内容。在缓存期间，广告数据是不可用的状态。

### 显示广告
```cpp
sdkbox::PluginAdMob::show("home");
sdkbox::PluginAdMob::show("gameover");
```

### 隐藏广告
您不能隐藏插播式广告。
```cpp
sdkbox::PluginAdMob::hide("home");
```

### 检查广告数据可用性
```cpp
sdkbox::PluginAdMob::isAvailable("home");
sdkbox::PluginAdMob::isAvailable("gameover");
```

### 实现 AdMobListener
* 您可以实现 AdMobListener 用来设置回调，比如当一个视频播放完成的时候。
```cpp
#include "PluginAdMob/PluginAdMob.h"
class MyClass : public sdkbox::AdMobListener
{
private:
    void adViewDidReceiveAd(const std::string &name) {}
    void adViewDidFailToReceiveAdWithError(const std::string &name, const std::string &msg) {}
    void adViewWillPresentScreen(const std::string &name) {}
    void adViewDidDismissScreen(const std::string &name) {}
    void adViewWillDismissScreen(const std::string &name) {}
    void adViewWillLeaveApplication(const std::string &name) {}
    void reward(const std::string &name, const std::string &currency, double amount) {}
}
```
