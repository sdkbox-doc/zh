### 请参考 Scientific Revenue 官方文档

https://documentation.scientificrevenue.com/sdkbox-cocos2d-x/

官方联系邮箱 ted@scientificrevenue.com

在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下：
```cpp
#include "PluginScientificRevenue/PluginScientificRevenue.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::ScientificRevenue::getInstance()->init();
}
```

### 设置定价会话参数
```cpp
sdkbox::ScientificRevenue::getInstance()->sessionOptions(true, "en_US", true);
```

### 开始会话
```cpp
sdkbox::ScientificRevenue::getInstance()->startSession(UserName);
```
