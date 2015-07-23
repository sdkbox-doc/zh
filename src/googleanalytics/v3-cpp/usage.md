### 初始化 Google Analytics
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下：
```cpp
#include "PluginGoogleAnalytics/PluginGoogleAnalytics.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginGoogleAnalytics::init();
}
```
