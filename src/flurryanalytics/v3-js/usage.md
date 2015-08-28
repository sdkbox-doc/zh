### 初始化 Flurry Analytics
* 在你的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginFlurryAnalytics.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含以下头文件:
```cpp
#include "PluginFlurryAnalyticsJS.hpp"
#include "PluginFlurryAnalyticsJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 调用以下函数:
```cpp
sc->addRegisterCallback(register_all_PluginFlurryAnalyticsJS);
sc->addRegisterCallback(register_PluginFlurryAnalyticsJS_helper);
```

### 使用 Flurry Analytics
在初始化完成后,你就可以使用 Flurry Analytics 提供的功能了. 在你的代码中任意地方,使用 `logevent`:
```javascript
sdkbox.PluginFlurryAnalytics.logEvent("test event2 js", JSON.stringify({"eKey1":"eVal1", "eKey2":"eVal2"}));
```

### 接收 Flurry Analytics 事件 (可选)
你可以接收 `FlurryAnalytics` 事件, 然后对不同事件做不同的程序响应,一个简单的例子可以会像这样:
```javascript
sdkbox.PluginFlurryAnalytics.init();
sdkbox.PluginFlurryAnalytics.setListener({
    flurrySessionDidCreateWithInfo:function(info) {
        var jsonInfo = JSON.parse(info)
        console.log("session started")
        console.log("APIKey :" + jsonInfo.apiKey + " session id :" + jsonInfo.sessionId);
        sdkbox.PluginFlurryAnalytics.logEvent("test event2 js", JSON.stringify({"eKey1":"eVal1", "eKey2":"eVal2"}));
    }
});
sdkbox.PluginFlurryAnalytics.startSession();
```

### 结束 Flurry Analytics (只在 Android 上有效)
当你不再使用 `FlurryAnalytics` 或你的游戏结束时, 必须要把 `FlurryAnalytics` 会话结束. 这个在 Android 上必须调用,但是在 iOS 上是可选的. 比如:
```javascript
// 这个只在 android 上有效, 但是你在 iOS 调用,也没有关系
sdkbox.PluginFlurryAnalytics.endSession();
```
