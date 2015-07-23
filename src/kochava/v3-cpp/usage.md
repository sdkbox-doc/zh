### 初始化 Kochava
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下：
```cpp
#include "PluginKochava/PluginKochava.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginKochava::init();
}
```

### 追踪事件
Kochava 提供了对 __custom__, __spatial__, __referral__ 事件的追踪功能。

* 追踪一个 __custom__ 事件：
```cpp
sdkbox::PluginKochava::trackEvent("<EVENT>", "<VALUE>");
```

* 通过提供世界上的地名与位置，追踪一个 __spatial__ 事件：
```cpp
sdkbox::PluginKochava::spatialEvent("<TITLE>", <X>, <Y>, <Z>);
```

* 追踪一个 __referral__ 事件（也被称作深链接）：
```cpp
sdkbox::PluginKochava::sendDeepLink("<URI>", "<YOUR APP>");
```
__Note:__ 在 Android 平台上，该函数的第二个参数（__<YOUR APP>__）不会被使用。您可以只提供地一个参数 __<URI>__ 。

### 捕捉 Kochava 事件（可选）
您可以轮询并且捕捉 Kochava 事件， 让您在一个参考点或者归属地数据从服务器返回时得到通知，也可以让您在一个用户穿过信标边界时得到通知。比如，当一个用户在星巴克附近时，或者走向星巴克时。下面是用 __lambda__ 函数实现一个简单例子：
```cpp
auto callback = [](const std::map<std::string, std::string>* attribution)
{
  if (attribution)
  {
      typedef std::map<std::string, std::string> map_type;
      const map_type& m = * attribution;

      for (map_type::const_iterator it = m.begin(); it != m.end(); ++it)
      {
          const map_type::value_type& kv = * it;
          printf("%s -> %s", kv.first.c_str(), kv.second.c_str());
      }
  }
};

sdkbox::PluginKochava::setAttributionCallback(callback);
```
 __Note__: 请求属性数据将会消耗一点时间，您可以采用轮询的方式调用 `getAttributionData()` ，直到您得到不是 **null** 的数据。
