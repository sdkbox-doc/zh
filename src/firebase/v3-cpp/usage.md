### 初始化 Firebase
* 在您的代码合适的地方初始化插件, 我们建议您在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 中完成初始化. 请确保您包含了对应的头文件:
```cpp
#include "PluginFirebase/PluginFirebase.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::Firebase::Analytics::init();
}
```

### 设置属性
在初始化完成之后, 你可以使用Firebase的功能接口, 以下在设置一些属性
```cpp
    sdkbox::Firebase::Analytics::setUserID("sdkbox_inter_test");
    sdkbox::Firebase::Analytics::setUserProperty("favorite_food", "hot pot");
    sdkbox::Firebase::Analytics::setScreenName("login", "");
```

### 统计事件

Firebase 提供了各种内置事件, 你可以使用内置事件，以更好的在 Firebase 后台展示统信息, 当然你也可以传入自定义事件

```cpp
    std::map<std::string, std::string> params;
    params[sdkbox::Firebase::Analytics::kFIRParameterItemID] = "id123456";
    params[sdkbox::Firebase::Analytics::kFIRParameterItemName] = "name123456";
    params[sdkbox::Firebase::Analytics::kFIRParameterItemCategory] = "category123456";
    params[sdkbox::Firebase::Analytics::kFIRParameterPrice] = "123.4";

    sdkbox::Firebase::Analytics::logEvent(sdkbox::Firebase::Analytics::kFIREventViewItem, params);
```
