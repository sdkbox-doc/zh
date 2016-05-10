### 注册 Javascript 函数
You need to register all the SdkboxAds JS functions with cocos2d-x before using them.
您需要在使用之前，在 cocos2d-x 中注册所有的 SdkboxAds JS 函数。

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginSdkboxAdsJS.hpp"
#include "PluginSdkboxAdsJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，添加如下内容：
```cpp
sc->addRegisterCallback(register_all_PluginSdkboxAdsJS);
sc->addRegisterCallback(register_all_PluginSdkboxAdsJS_helper);
```

### 初始化 SdkboxAds
通过在您的代码合适的位置调用 `init()` 方法来初始化这个插件。我们建议您在 `app.js` 中进行初始化。举例如下：
```javascript
sdkbox.PluginSdkboxAds.init();
```

### 使用 SdkboxAds

请求显示一个在默认的 AdUnit 中的默认广告，并以此完成一次简单的集成测试：
```javascript
sdkbox.SdkboxAds.play()
```

请求显示默认 AdUnit 中的广告：
```javascript
sdkbox.SdkboxAds.play( zone_place_location, params );

// params is an object with string keys and values.
```
> 提示：每一个 AdUnit 都有自己的参数，可以参考每一个插件的文档。

请求显示一个指定的 AdUnit 中的广告：
```javascript
sdkbox.SdkboxAds.play( ad_unit_name, zone_place_location, params );
```

请求显示定义在 sdkbox\_config.json 的 Placement 中的广告：
```javascript
sdkbox.SdkboxAds.placement( placement_name );
```

更好的控制广告数据缓冲：
```javascript
sdkbox.SdkboxAds.cacheControl( ad_unit, cacheOpts );

// cacheOpts is an object with keys and values as strings.
```
> 缓冲的选项是由 AdUnit 指定的， 请参考每个插件的相关文档。

### SdkboxAds 事件
这个插件允许您捕捉事件。

```javascript
sdkbox.PluginSdkboxAds.setListener({
    onAdAction : function( ad_unit_id, zone_location_place_you_name_it, action_type),
    onRewardAction : function( ad_unit_id, zone_id, reward_amount, reward_succeed )
});
```

> 请参考本插件的 cpp 语言使用文档以获得 action_type 可取的值。
