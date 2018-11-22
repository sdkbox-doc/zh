### 注册 Javascript 函数
您需要在使用之前，在 cocos2d-x 中注册所有的 AdMob JS 函数。

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginAdMobJS.hpp"
#include "PluginAdMobJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，添加如下内容：
```cpp
sc->addRegisterCallback(register_all_PluginAdMobJS);
sc->addRegisterCallback(register_all_PluginAdMobJS_helper);
```

### Initialize AdMob
### 初始化 AdMob
通过在您的代码合适的位置调用 `init()` 方法来初始化这个插件。我们建议您在 `app.js` 中进行初始化。举例如下：
```javascript
sdkbox.PluginAdMob.init();
```

### 缓存广告数据
```javascript
sdkbox.PluginAdMob.cache("home");
sdkbox.PluginAdMob.cache("gameover");
```

### 显示广告
```javascript
sdkbox.PluginAdMob.show("home");
sdkbox.PluginAdMob.show("gameover");
```

### 隐藏广告
您不能隐藏插播式广告。
```javascript
sdkbox.PluginAdMob.hide("home");
```

### 检查广告数据可用性
```javascript
sdkbox.PluginAdMob.isAvailable("home");
sdkbox.PluginAdMob.isAvailable("gameover");
```

### 实现 AdMobListener
* 您可以实现 AdMobListener 用来设置回调，比如当一个视频播放完成的时候。
```javascript

sdkbox.PluginAdMob.setListener({
    adViewDidReceiveAd : function(name) { },
    adViewDidFailToReceiveAdWithError : function(name, msg) { },
    adViewWillPresentScreen : function(name) { },
    adViewDidDismissScreen : function(name) { },
    adViewWillDismissScreen : function(name) { },
    adViewWillLeaveApplication : function(name) { },
    reward(name, currency, amount)
});

```
