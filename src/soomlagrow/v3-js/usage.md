### 注册 Javascript 函数
在使用 SoomlaGrow js接口前，你要先把它注册到js环境中.

像这样做:
* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginSoomlaGrowJS.hpp"
#include "PluginSoomlaGrowJSHelper.hpp"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 调用如下函数:
```cpp
sc->addRegisterCallback(register_all_PluginSoomlaGrowJS);
sc->addRegisterCallback(register_all_PluginSoomlaGrowJS_helper);
```

### 初始化Initialize SoomlaGrow
在你的代码中调用 `init()` 完成初始化.我们建议在 `app.js` 中初始化.比如:
```javascript
sdkbox.PluginSoomlaGrow.init();
```

### 使用 SoomlaGrow 的 User Insigiht 模块
在完成初始化后，SoomlaGrow会自动记录，你程序中的 `IAP`, `Facebook` 插件的使用情况.同时你还可以在你的代码中调用 `refreshInsight`, 'getUserInsightInfo' 接口:
```javascript
sdkbox.PluginSoomlaGrow.refreshInsight()
sdkbox.PluginSoomlaGrow.getUserInsightInfo()
```

### 接收 SoomlaGrow 的事件 (可选)
你可以接收 SoomlaGrow 事件,然后对不同的事件，做不同的处理.一个的简单的用法可能会像这样:
```javascript
sdkbox.PluginSoomlaGrow.setListener({
            onHighWayInitialized: function(data) {cc.log("onHighWayInitialized")},
            onHighWayConnected: function(data) { cc.log("onHighWayConnected") },
            onHighWayDisconnected: function(data) { cc.log("onHighWayDisconnected") }
            })
sdkbox.PluginSoomlaGrow.init()
```
