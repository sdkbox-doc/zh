### 初始化 AgeCheq
* 在你的代码合适的地方初始化插件, 我们建议你在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保你包含了对应的头文件:
```cpp
#include "PluginAgeCheq/PluginAgeCheq.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAgeCheq::init();
}
```

### 使用 AgeCheq
在初始化完成后,你就可以使用 AgeCheq 的功能了, 在你的代码中需要的地方调用 `check` 或 `associateDate()`:
```cpp
sdkbox::PluginAgeCheq::check("1426");
sdkbox::PluginAgeCheq::associateData("1426", "ikfill");
```

### 接收 AgeCheq 事件 (可选)
你可以接收 AgeCheq 的事件,然后在程序做不同的处理与响应.一个简单的例子可能会如下:

* 让你的类继承 `sdkbox::AgeCheqListener`
```cpp
#include "PluginAgeCheq/PluginAgeCheq.h"
class MyClass : public sdkbox::AgeCheqListener
{
private:
  void checkResponse(const std::string& rtn, const std::string& rtnmsg,
          int apiversion, int checktype, bool appauthorized,
          bool appblocked, int parentverified, bool under13,
          bool under18, bool underdevage, int trials);

  void associateDataResponse(const std::string& rtn,
          const std::string& rtnmsg);
};
```

* 创建一个 __listener__ 来处理这些回调:
```cpp
sdkbox::PluginAgeCheq::setListener(this);
```
