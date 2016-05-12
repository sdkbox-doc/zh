### 注册 Javascript 函数
您需要在使用之前，在 cocos2d-x 中注册所有的 LeadBolt JS 函数。

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginLeadBoltJS.hpp"
#include "PluginLeadBoltJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，添加如下内容：
```cpp
sc->addRegisterCallback(register_all_PluginLeadBoltJS);
sc->addRegisterCallback(register_all_PluginLeadBoltJS_helper);
```

### 初始化 Leadbolt
通过在您的代码合适的位置调用 `init()` 方法来初始化这个插件。我们建议您在 `app.js` 中进行初始化。举例如下：
```javascript
sdkbox.PluginLeadBolt.init();
```

### 缓存广告数据
```javascript
sdkbox.PluginLeadbolt.loadModuleToCache("directdeal");
sdkbox.PluginLeadbolt.loadModuleToCache("rewardedvideo");
```
> 提示：LeadBolt 为了更好的用户体验，在使用前它会缓存广告数据。一旦缓存广告数据完成，您将能够看到这个广告。当缓存仍在进行中，广告是不可见的。

### 加载/显示广告
```javascript
sdkbox.PluginLeadbolt.loadModule("directdeal");
sdkbox.PluginLeadbolt.loadModule("rewardedvideo");
```

### 判断广告是否缓存完成
```javascript
sdkbox.PluginLeadbolt.isAdReady("directdeal");
sdkbox.PluginLeadbolt.isAdReady("rewardedvideo");
```

### 捕捉 LeadBolt 事件（可选）
该插件允许您捕捉 Leadbolt 广告事件，使您能可以根据返回的内容执行相应的操作。一个简单的例子如下：

```javascript
var plugin = sdkbox.PluginLeadBolt
plugin.setListener({
  onModuleLoaded: function(placement) {},
  onModuleClosed: function(placement) {},
  onModuleClicked: function(placement) {},
  onModuleCached: function(placement) {},
  onModuleFailed: function(placement, error, cached) {},
  onMediaFinished: function(viewCompleted) {}
})
plugin.init();
```
