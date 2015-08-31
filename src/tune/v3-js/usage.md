### 初始化 Tune
* 通过在您的代码合适的位置调用 `init()` 方法来初始化这个插件。我们建议您在 `app.js` 中进行初始化。举例如下：
```javascript
sdkbox.PluginTune.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginTuneJS.hpp"
#include "PluginTuneJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，添加如下内容：
```cpp
sc->addRegisterCallback(register_all_PluginTuneJS);
sc->addRegisterCallback(register_all_PluginTuneJS_helper);
```
这将注册 Javascript 回调函数。

### 使用 Tune
在初始化之后，您可以开始使用 Tune 插件的功能了。Tune 使用 __events__ 这个概念（就像 __MAT Native Event Types__一样）。您可以在您需要的地方将 __events__ 记入日志，并且在稍后通过基于 web 的报告阅读器查看它们。Tune 在文档中为这些 events 提供一种结构。举例如下：
```javascript
sdkbox.PluginTune.measureEventName("login");
sdkbox.PluginTune.measureEventId(0123456789);

var event = {};
event.eventName = "purchase";
event.refId = "RJ1357";
event.searchString = "sweet srisp red apples";
event.attribute1 = "srisp";
event.attribute2 = "red";
event.quantity = 3;
sdkbox.PluginTune.measureEvent(JSON.stringify(event));
```

### 捕捉 Tune 事件（可选）
您可以捕捉 `Tune` 事件，根据响应来执行操作。一个简单的例子如下：
```javascript
sdkbox.PluginTune.setListener({
  onEnqueuedAction: function(data) {},
  onSucceed: function(data) {},
  onFailed: function(data) {},
  onReceiveDeeplink: function(data, timeout) {},
  onFailDeeplink: function(errorString) {}
});
```
