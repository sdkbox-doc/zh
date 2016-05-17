### 初始化 Apteligent
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下：
```cpp
#include "PluginApteligent/PluginApteligent.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginApteligent::init();
}
```

### 注册追踪器 Breadcrumbs

```cpp
// leave a breadcrumb
sdkbox::PluginApteligent::leaveBreadcrumb("User tapped start button");

// perform all breadcrumb writes on a background thread
sdkbox::PluginApteligent::setAsyncBreadcrumbMode(true);
```


### 注册用户元数据

```
// Adding a Username
sdkbox::PluginApteligent::setUsername("MrsCritter");

// Adding Arbitrary User Metadata
sdkbox::PluginApteligent::setValueforKey("5", "Game Level");
```


### 注册用户流
```cpp
// Beginning a Userflow
sdkbox::PluginApteligent::beginUserflow("login");

// Ending a Userflow
sdkbox::PluginApteligent::endUserflow("login");

// Failing a Userflow
sdkbox::PluginApteligent::failUserflow("login");

// Cancelling a Userflow
sdkbox::PluginApteligent::cancelUserflow("login");
```

### 修改用户流的值
```cpp
int valueInCents = sdkbox::PluginApteligent::valueForUserflow("my_userflow");
valueInCents += 5;
sdkbox::PluginApteligent::setValueforUserflow(valueInCents, "my_userflow");

```

### 注册网络请求
```cpp
sdkbox::PluginApteligent::logNetworkRequest("GET", "http://www.abc123def456.com", 2.0, 1000, 100, 200);
```


### 过滤截获数据
```cpp
sdkbox::PluginApteligent::addFilter("www.gmail.com");
```

### 配置位置坐标
```cpp
// Beijing, China
sdkbox::PluginApteligent::updateLocation(39.9042, 116.4074);
```

### 其他任务
```cpp
// Allowing Users to Opt Out of Apteligent
sdkbox::PluginApteligent::setOptOutStatus(true);

// Changing the verbosity of Apteligent’s Logs
// sdkbox::CRLoggingLevelSilent  : Turns off all Apteligent log messages
// sdkbox::CRLoggingLevelError   : Only print errors. An error is an unexpected event that will result not capturing important data
// sdkbox::CRLoggingLevelWarning : (Default) Only print warnings. Currently warning messages are printed when calling Apteligent methods before initializing Apteligent.
// sdkbox::CRLoggingLevelInfo    : The most verbose level of logging
sdkbox::PluginApteligent::setLoggingLevel(sdkbox::CRLoggingLevelInfo);

// Send App Load Data
// You must set `"delay_sending_appload":true` in `sdkbox_config.json` first
sdkbox::PluginApteligent::sendAppLoadData();
```

### 实现 ApteligentListener
* 您可以实现 ApteligentListener 用来设置回调，比如当一个视频播放完成的时候。
```cpp
#include "PluginApteligent/PluginApteligent.h"
class MyClass : public sdkbox::ApteligentListener
{
private:
    void onCrashOnLastLoad() {} // not support on android
}
```
