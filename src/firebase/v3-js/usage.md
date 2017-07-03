### 注册 Javascript 函数

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginFirebaseJS.hpp"
#include "PluginFirebaseJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保有如下调用:
```cpp
    sc->addRegisterCallback(register_all_PluginFirebaseJS);
    sc->addRegisterCallback(register_all_PluginFirebaseJS_helper);
```

### 初始化 Firebase
* 在您的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.firebase.Analytics.init();
```

### 统计事件

```javascript
const evt = {}
evt[sdkbox.firebase.Analytics.Param.kFIRParameterItemID] = 'id123456';
evt[sdkbox.firebase.Analytics.Param.kFIRParameterItemName] = 'name123456';
evt[sdkbox.firebase.Analytics.Param.kFIRParameterItemCategory] = 'category123456';
evt[sdkbox.firebase.Analytics.Param.kFIRParameterPrice] = '123.4';
sdkbox.firebase.Analytics.logEvent(sdkbox.firebase.Analytics.Event.kFIREventViewItem, evt);
```
