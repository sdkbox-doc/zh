### 初始化 Leadbolt
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下：
```cpp
#include "PluginLeadBolt/PluginLeadBolt.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginLeadBolt::init();
}
```

### 缓存广告数据
```cpp
sdkbox::PluginLeadbolt::loadModuleToCache("directdeal");
sdkbox::PluginLeadbolt::loadModuleToCache("rewardedvideo");
```
> 提示：LeadBolt 为了更好的用户体验，在使用前它会缓存广告数据。一旦缓存广告数据完成，您将能够看到这个广告。当缓存仍在进行中，广告是不可见的。

### 加载/显示广告
```cpp
sdkbox::PluginLeadbolt::loadModule("directdeal");
sdkbox::PluginLeadbolt::loadModule("rewardedvideo");
```

### 判断广告是否缓存完成
```cpp
sdkbox::PluginLeadbolt::isAdReady("directdeal");
sdkbox::PluginLeadbolt::isAdReady("rewardedvideo");
```

### 捕捉 LeadBolt 事件（可选）
该插件允许您捕捉 Leadbolt 广告事件，使您能可以根据返回的内容执行相应的操作。比如在奖励式广告中，onMediaFinished 事件就允许您对看完这个广告的用户进行奖励。

* 允许您的类继承 `sdkbox::LeadBoltListener`
```cpp
#include "PluginLeadBolt/PluginLeadBolt.h"

class LBListener : public sdkbox::LeadBoltListener {
public:

    void onModuleLoaded(const std::string& placement);
    void onModuleClosed(const std::string& placement);
    void onModuleClicked(const std::string& placement);
    void onModuleCached(const std::string& placement);
    void onModuleFailed(const std::string& placement, const std::string& error, bool iscached);
    void onMediaFinished(bool viewCompleted);

};
```

* 创建一个 __listener__ 处理回调：
```cpp
sdkbox::PluginLeadBolt::setListener(this);
```
