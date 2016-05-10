### 注册 Javascript 函数
You need to register all the Apteligent JS functions with cocos2d-x before using them.
您需要在使用之前，在 cocos2d-x 中注册所有的 Apteligent JS 函数。

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，包含下列头文件：
```javascript
#include "PluginApteligentJS.hpp"
#include "PluginApteligentJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，添加如下内容：
```javascript
sc->addRegisterCallback(register_all_PluginApteligentJS);
sc->addRegisterCallback(register_all_PluginApteligentJS_helper);
```

### 注册追踪器 Breadcrumbs

```javascript
// leave a breadcrumb
sdkbox.PluginApteligent.leaveBreadcrumb("User tapped start button");

// perform all breadcrumb writes on a background thread
sdkbox.PluginApteligent.setAsyncBreadcrumbMode(true);
```


### 注册用户元数据
```
// Adding a Username
sdkbox.PluginApteligent.setUsername("MrsCritter");

// Adding Arbitrary User Metadata
sdkbox.PluginApteligent.setValueforKey("5", "Game Level");
```


### 注册用户流
```javascript
// Beginning a Userflow
sdkbox.PluginApteligent.beginUserflow("login");

// Ending a Userflow
sdkbox.PluginApteligent.endUserflow("login");

// Failing a Userflow
sdkbox.PluginApteligent.failUserflow("login");

// Cancelling a Userflow
sdkbox.PluginApteligent.cancelUserflow("login");
```

### 修改用户流的值
```javascript
int valueInCents = sdkbox.PluginApteligent.valueForUserflow("my_userflow");
valueInCents += 5;
sdkbox.PluginApteligent.setValueforUserflow(valueInCents, "my_userflow");

```

### 注册网络请求
```javascript
sdkbox.PluginApteligent.logNetworkRequest("GET", "http://www.abc123def456.com", 2.0, 1000, 100, 200);
```


### 过滤截获数据
```javascript
sdkbox.PluginApteligent.addFilter("www.gmail.com");
```

### 配置位置坐标
```javascript
// Beijing, China
sdkbox.PluginApteligent.updateLocation(39.9042, 116.4074);
```

### 其他任务
```javascript
// Allowing Users to Opt Out of Apteligent
sdkbox.PluginApteligent.setOptOutStatus(true);

// Changing the verbosity of Apteligent’s Logs
// sdkbox.PluginApteligent.LoggingLevel.Silent  : Turns off all Apteligent log messages
// sdkbox.PluginApteligent.LoggingLevel.Error   : Only print errors. An error is an unexpected event that will result not capturing important data
// sdkbox.PluginApteligent.LoggingLevel.Warning : (Default) Only print warnings. Currently warning messages are printed when calling Apteligent methods before initializing Apteligent.
// sdkbox.PluginApteligent.LoggingLevel.Info    : The most verbose level of logging
sdkbox.PluginApteligent.setLoggingLevel(sdkbox.PluginApteligent.LoggingLevel.Info);

// Send App Load Data
// You must set `"delay_sending_appload":true` in `sdkbox_config.json` first
sdkbox.PluginApteligent.sendAppLoadData();
```


### 实现 ApteligentListener
* 您可以实现 ApteligentListener 用来设置回调，比如当一个视频播放完成的时候。
```javascript

sdkbox.PluginApteligent.setListener({
    onCrashOnLastLoad : function() { } // not support on android
});

```
