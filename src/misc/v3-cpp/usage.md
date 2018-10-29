### 初始化 Misc

在你的代码中初始化插件, 我们推荐在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中初始化. 请注意包含了相应的头文件:
```diff
+ #include "PluginMisc/PluginMisc.h"
  AppDelegate::applicationDidFinishLaunching() {
+      sdkbox::PluginMisc::init();
  }
```

### 发送本地消息

```cpp
// 10 秒后能收到消息
int nid = sdkbox::PluginMisc::localNotify("test title", "this a test notify content", 1000 * 10);
std::stringstream buf;
buf << "Local Notification:" << nid;
CCLOG(buf.str());
```

### 实现 MiscListner
* 要接收消息, 需要继承 MiscListener.
```cpp
#include "PluginMisc/PluginMisc.h"
class MyClass : public sdkbox::MiscListener
{
private:
    virtual void onHandleLocalNotify(const std::string& payloadJson) {
        // recevie local notification
        std::stringstream buf;
        buf << "onHandleLocalNotify:" << payloadJson;
        cocos2d::log("Log: %s", buf.str().c_str());
    };
}
```
