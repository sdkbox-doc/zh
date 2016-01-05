### 注册 Javascript 函数

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginInMobiJS.hpp"
#include "PluginInMobiJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保有如下调用:
```cpp
sc->addRegisterCallback(register_all_PluginInMobiJS);
sc->addRegisterCallback(register_all_PluginInMobiJS_helper);
```

### 初始化 InMobi
* 在你的代码中合适的地方调用 `init()`, 我们建议在 `app.js` 初始化,比如:
```javascript
sdkbox.PluginInMobi.init();
```

### 显示插屏广告

```javascript
// 手动加载广告
sdkbox.PluginInMobi.loadInterstitial();

// 显示插屏广告
if (sdkbox.PluginInMobi.isInterstitialReady()) {
    console.log('inmobi interstitial ad is ready');
    sdkbox.PluginInMobi.showInterstitial();
} else {
    console.log('inmobi interstitial ad is not ready');
}
```

### 设置日志等级

```
sdkbox.PluginInMobi.setLogLevel(sdkbox.PluginInMobi.SBIMSDKLogLevel.kIMSDKLogLevelDebug);
```

### 设置用户数据

```
sdkbox.PluginInMobi.addIdForType("test", sdkbox.PluginInMobi.SBIMSDKIdType.kIMSDKIdTypeLogin);
sdkbox.PluginInMobi.removeIdType(sdkbox.PluginInMobi.SBIMSDKIdType.kIMSDKIdTypeLogin);
sdkbox.PluginInMobi.setAge(18);
sdkbox.PluginInMobi.setAreaCode("area code");
sdkbox.PluginInMobi.setAgeGroup(sdkbox.PluginInMobi.SBIMSDKAgeGroup.kIMSDKAgeGroupBetween18And20);
sdkbox.PluginInMobi.setYearOfBirth(1989);
sdkbox.PluginInMobi.setEducation(sdkbox.PluginInMobi.SBIMSDKEducation.kIMSDKEducationHighSchoolOrLess);
sdkbox.PluginInMobi.setEthnicity(sdkbox.PluginInMobi.SBIMSDKEthnicity.kIMSDKEthnicityHispanic);
sdkbox.PluginInMobi.setGender(sdkbox.PluginInMobi.SBIMSDKGender.kIMSDKGenderMale);
sdkbox.PluginInMobi.setHouseholdIncome(sdkbox.PluginInMobi.SBIMSDKHouseholdIncome.kIMSDKHouseholdIncomeBelow5kUSD);
sdkbox.PluginInMobi.setIncome(4500);
sdkbox.PluginInMobi.setInterests("game");
sdkbox.PluginInMobi.setLanguage("zh-cn");
sdkbox.PluginInMobi.setLocation("cd", "sc", "usa");
sdkbox.PluginInMobi.setLocation(102, 348);
sdkbox.PluginInMobi.setNationality("nationality");
sdkbox.PluginInMobi.setPostalCode("618000");
```

### 接收 InMobi 事件 (可选)

```javascript
var plugin = sdkbox.PluginInMobi
plugin.setListener({
    bannerDidFinishLoading: function() { console.log('bannerDidFinishLoading'); },
    bannerDidFailToLoadWithError: function(code, description) { console.log('bannerDidFailToLoadWithError code:' + code + ' desc:' + description); },
    bannerDidInteractWithParams: function(params) { console.log('bannerDidInteractWithParams'); },
    userWillLeaveApplicationFromBanner: function() { console.log('userWillLeaveApplicationFromBanner'); },
    bannerWillPresentScreen: function() { console.log('bannerWillPresentScreen'); },
    bannerDidPresentScreen: function() { console.log('bannerDidPresentScreen'); },
    bannerWillDismissScreen: function() { console.log('bannerWillDismissScreen'); },
    bannerDidDismissScreen: function() { console.log('bannerDidDismissScreen'); },
    bannerRewardActionCompletedWithRewards: function(rewards) { console.log('bannerRewardActionCompletedWithRewards'); },
    interstitialDidFinishLoading: function() { console.log('interstitialDidFinishLoading'); },
    interstitialDidFailToLoadWithError: function(code, description) { console.log('interstitialDidFailToLoadWithError code:' + code + ' desc:' + description); },
    interstitialWillPresent: function() { console.log('interstitialWillPresent'); },
    interstitialDidPresent: function() { console.log('interstitialDidPresent'); },
    interstitialDidFailToPresentWithError: function(code, description) { console.log('interstitialDidFailToPresentWithError code:' + code + ' desc:' + description); },
    interstitialWillDismiss: function() { console.log('interstitialWillDismiss'); },
    interstitialDidDismiss: function() { console.log('interstitialDidDismiss'); },
    interstitialDidInteractWithParams: function(params) { console.log('interstitialDidInteractWithParams'); },
    interstitialRewardActionCompletedWithRewards: function(rewards) { console.log('interstitialRewardActionCompletedWithRewards'); },
    userWillLeaveApplicationFromInterstitial: function() { console.log('userWillLeaveApplicationFromInterstitial'); }
})
plugin.init();
```
