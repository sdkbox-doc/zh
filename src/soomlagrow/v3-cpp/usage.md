### 初始化 SoomlaGrow
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下:
```cpp
#include "PluginSoomlaGrow/PluginSoomlaGrow.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginSoomlaGrow::init();
}
```

### 使用 SoomlaGrow 的 UserInsight 模块
在初始化完成后，你就可以使用 SoomlaGrow 的功能了，在任何你想使用的地方, 调用 `refreshInsight` 或 `getUserInsightInfo`:
```cpp
sdkbox::PluginSoomlaGrow::refreshInsight();
std::string jsonStr = sdkbox::PluginSoomlaGrow::getUserInsightInfo();
```

### 接收 SoomlaGrow 事件 (可选)
你可以接收 `SoomlaGrow` 事件,以便对不同事件做不同处理.一个简单的用法可以像下面这样:

* 让你的类继承 `sdkbox::SoomlaGrowListener`
```cpp
#include "PluginSoomlaGrow/PluginSoomlaGrow.h"
class MyClass : public sdkbox::SoomlaGrowListener
{
private:
    void onHighWayInitialized();
    void onHighWayConnected();
    void onHighWayDisconnected();
};
```

* 使用 __listener__ 来监听事件:
```cpp
sdkbox::PluginSoomlaGrow::setListener(this);
```
