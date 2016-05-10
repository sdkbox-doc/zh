### 初始化 AdColony
* 在您的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginAdColony.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginAdColonyJS.hpp"
#include "PluginAdColonyJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保有如下调用:
```cpp
sc->addRegisterCallback(register_all_PluginAdColonyJS);
sc->addRegisterCallback(register_all_PluginAdColonyJS_helper);
```

### 显示广告
要在您想要显示广告的代码中,输入如下:
```cpp
sdkbox.PluginAdColony.show("video");
```
或:
```cpp
sdkbox.PluginAdColony.show("v4vc");
```

### 接收 AdColony 事件 (可选)
您可以接收 `AdColony` 的事件, 这样您可以在玩家观看完广告后给他相应的奖励.

* 创建一个监听:
```javascript
/**
 * data 的数据如下
 * data.name : 广告的名字 (在配置文件 sdkbox_config.json 中定义)
 * data.zoneID : 广告的 zoneID
 * data.shown : 标记广告是否显示了,或被用户关闭了
 * data.iapEnabled : 标记关联的广告是否是IAP
 * data.iapProductID : 广告的IAP对应的商品id
 * data.iapQuantity : 用户要付费商品的数量
 * data.iapEngagementType : 商品类型
 */

sdkbox.PluginAdColony.setListener({
		onAdColonyChange : function (data, available) {
				// 当AdColony完成加载调用
		},
		onAdColonyReward : function (data, currencyName, amount, success) {
				// 当AdColony的 v4vc 广告播放完毕后调用
		},
		onAdColonyStarted : function (data) {
				// 当广告开始播放调用
		},
		onAdColonyFinished : function (data) {
				// 当广告显示完毕后调用
		}
});
```
