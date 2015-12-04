### Initialize AgeCheq
* 在你的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginAgeCheq.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 在其中包含如下头文件:
```cpp
#include "PluginAgeCheqJS.hpp"
#include "PluginAgeCheqJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 在其中调下如下代码:
```cpp
sc->addRegisterCallback(register_all_PluginAgeCheqJS);
sc->addRegisterCallback(register_all_PluginAgeCheqJS_helper);
```

### 使用 AgeCheq
在初始化后,你就可以使用 AgeCheq 的功能了. 在你的代码任意使用 `check` 功能:
```cpp
sdkbox.PluginAgeCheq.check("agecheqPin");
```

### 接收 AgeCheq 事件 (可选)
你可以接收 AgeCheq 的事件,并对不同的事件做不同的响应. 一个简单的例子可能会如下:
```javascript
sdkbox.PluginAgeCheq.init();
sdkbox.PluginAgeCheq.setListener({
    checkResponse : function (rtn, rtnmsg, apiversion, checktype, appauthorized, appblocked, parentverified, under13, under18, underdevage, trials) {
        cc.log("checkResponse rtn:" + rtn + " rtnmsg:" + rtnmsg
            + " apiversion:" + apiversion + " checktype:" + checktype
            + " appauthorized:" + appauthorized + " appblocked:" + appblocked
            + " parentverified:" + parentverified + " under13:" + under13
            + " under18:" + under18 + " underdevage:" + underdevage + " trials:" + trials);
    },
    associateDataResponse : function (rtn, rtnmsg) {
        cc.log("associateDataResponse rtn:" + rtn + " rtnmsg:" + rtnmsg);
    }
})
sdkbox.PluginAgeCheq.check("agecheqPin");
```
