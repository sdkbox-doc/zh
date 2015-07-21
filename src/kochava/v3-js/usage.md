### 初始化 Kochava
* 通过在您的代码合适的位置调用 `init()` 方法来初始化这个插件。我们建议您在 `app.js` 中进行初始化。举例如下：
```javascript
sdkbox.PluginKochava.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginKochavaJS.hpp"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，添加如下内容：
```cpp
sc->addRegisterCallback(register_all_PluginKochavaJS);
```
这将注册 Javascript 回调函数。

### 追踪事件
Kochava 提供了对 __custom__, __spatial__, __referral__ 事件的追踪功能。

* 追踪一个 __custom__ 事件：
```javascript
sdkbox.PluginKochava.trackEvent("<EVENT>", "<VALUE>");
```

* 通过提供世界上的地名与位置，追踪一个 __spatial__ 事件：
```javascript
sdkbox.PluginKochava.spatialEvent("<TITLE>", <X>, <Y>, <Z>);
```

* 追踪一个 __referral__ 事件（也被称作深链接）：
```javascript
sdkbox.PluginKochava.sendDeepLink("<URI>", "<YOUR APP>");
```
__Note:__ 在 Android 平台上，该函数的第二个参数（__<YOUR APP>__）不会被使用。您可以只提供地一个参数 __<URI>__ 。
