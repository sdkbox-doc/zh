### 初始化 Tune
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。`init()` 以及 `mesaureSession()` 函数将会被调用。举例如下：
```cpp
#include "PluginTune/PluginTune.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginTune::init();
     sdkbox::PluginTune::measureSession();
}
```

### 使用 Tune
在初始化之后，您可以开始使用 Tune 插件的功能了。Tune 使用 __events__ 这个概念（就像 __MAT Native Event Types__一样）。您可以在您需要的地方将 __events__ 记入日志，并且在稍后通过基于 web 的报告阅读器查看它们。Tune 在文档中为这些 events 提供一种结构。举例如下：
```cpp
{
    PluginTune::measureEventName("purchase");
    PluginTune::measureEventId(1122334455);
		TuneEvent event;
    event.eventName = "purchase2";
    event.refId     = "RJ1357";
    event.searchString = "sweet crisp red apples";
    event.attribute1 = "crisp";
    event.attribute2 = "red";
    event.quantity = 3;
    PluginTune::measureEvent(event);
}
```
需要注意的是，在 __event__ `PluginTune::measureEvent(event)` 被调用之后，我们的事件将会被记入日志。
