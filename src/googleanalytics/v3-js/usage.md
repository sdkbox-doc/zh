### 初始化 Google Analytics
* 通过在您的代码合适的位置调用 `init()` 方法来初始化这个插件。我们建议您在 `app.js` 中进行初始化。举例如下：
```javascript
sdkbox.PluginGoogleAnalytics.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginGoogleAnalyticsJS.hpp"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，添加如下内容：
```cpp
sc->addRegisterCallback(register_all_PluginGoogleAnalyticsJS);
```
这将注册 Javascript 回调函数。
