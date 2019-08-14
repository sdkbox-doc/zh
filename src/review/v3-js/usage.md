### 注册 Javascript 函数
在使用 Review js接口前，您要先把它注册到js环境中.

像这样做:
* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginReviewJS.hpp"
#include "PluginReviewJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 调用如下函数:
```cpp
sc->addRegisterCallback(register_all_PluginReviewJS);
sc->addRegisterCallback(register_all_PluginReviewJS_helper);
```

### 初始化Initialize Review
在您的代码中调用 `init()` 完成初始化.我们建议在 `app.js` 中初始化.比如:
```javascript
sdkbox.PluginReview.init();
```

### 设置 Review (可选)
如果您不要使用默认的提示字串,您可以设置自己的字串

`注意:` 如果您在 `sdkbox.config` 中把 `tryPromptWhenInit` 项设置为真,那必须在 `init()` 之前调用以下函数
```cpp
sdkbox.PluginReview.setCustomPromptTitle("custom title");
sdkbox.PluginReview.setCustomPromptMessage("custom message");
sdkbox.PluginReview.setCustomPromptCancelButtonTitle("custom cancel");
sdkbox.PluginReview.setCustomPromptRateButtonTitle("custom rate");
sdkbox.PluginReview.setCustomPromptRateLaterButtonTitle("custom rate later");
```

如果您的 `sdkbox.config` 中把 `tryPromptWhenInit` 项为 false, 那您可以调用 `tryToShowPrompt` 尝试提示用户评价您的应用,
如果所有的限制条件都满足,那提示框就会显示
```cpp
sdkbox.PluginReview.show();
```

您也可以强制显示评价提示框
```cpp
sdkbox.PluginReview.show(true);
```

如果您的 `sdkbox.config` 中的 `UserEventLimit` 项大于0的话，那您需要自已增加用户事件记数
```cpp
sdkbox.PluginReview.userDidSignificantEvent(true);
```

### 接收 Review 的事件 (可选)
您可以接收 Review 事件,然后对不同的事件，做不同的处理.一个的简单的用法可能会像这样:
```javascript
var plugin = sdkbox.PluginReview
plugin.setListener({
  onDisplayAlert: function(data) {cc.log("didDisplayAlert")},
  onDeclineToRate: function(data) { cc.log("didDeclineToRate") },
  onRate: function(data) { cc.log("didToRate") },
  onRemindLater: function(data) { cc.log("didToRemindLater") }
})
plugin.init()
```
