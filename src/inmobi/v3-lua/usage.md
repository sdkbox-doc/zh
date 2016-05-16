### 修改 `AppDelegate.cpp`
* 修改 `Classes/AppDelegate.cpp` 包含以下头文件:
```lua
#include "PluginInMobiLua.hpp"
#include "PluginInMobiLuaHelper.h"
```

### 初始化 InMobi
修改你的lua代码来初始化这个插件. 这个初始化,可以在任意地方,但是必须在你调用插件的功能接口之前.
```lua
sdkbox.PluginInMobi:init()
```

### 显示插屏广告

```lua
local plugin = sdkbox.PluginInMobi
plugin:setListener(function(args)
    local event = args.event
    dump(args, "inmobi listener info:")
end)
plugin:init()

-- 手动加载广告
-- plugin:loadInterstitial();

-- 显示插屏广告
if plugin:isInterstitialReady() then
    print('inmobi interstitial ad is ready');
    plugin:showInterstitial();
else
    print('inmobi interstitial ad is not ready');
end
```

### 设置日志等级

```
plugin:setLogLevel(sdkbox.PluginInMobi.SBIMSDKLogLevel.kIMSDKLogLevelDebug);
```

### 设置用户数据

```
-- setting if need
print("inmobi plugin version:" .. plugin:getVersion());
plugin:setLogLevel(sdkbox.PluginInMobi.SBIMSDKLogLevel.kIMSDKLogLevelDebug);
plugin:addIdForType("test", sdkbox.PluginInMobi.SBIMSDKIdType.kIMSDKIdTypeLogin);
plugin:removeIdType(sdkbox.PluginInMobi.SBIMSDKIdType.kIMSDKIdTypeLogin);
plugin:setAge(18);
plugin:setAreaCode("area code");
plugin:setAgeGroup(sdkbox.PluginInMobi.SBIMSDKAgeGroup.kIMSDKAgeGroupBetween18And20);
plugin:setYearOfBirth(1989);
plugin:setEducation(sdkbox.PluginInMobi.SBIMSDKEducation.kIMSDKEducationHighSchoolOrLess);
plugin:setEthnicity(sdkbox.PluginInMobi.SBIMSDKEthnicity.kIMSDKEthnicityHispanic);
plugin:setGender(sdkbox.PluginInMobi.SBIMSDKGender.kIMSDKGenderMale);
plugin:setHouseholdIncome(sdkbox.PluginInMobi.SBIMSDKHouseholdIncome.kIMSDKHouseholdIncomeBelow5kUSD);
plugin:setIncome(4500);
plugin:setInterests("game");
plugin:setLanguage("zh-cn");
plugin:setLocation("cd", "sc", "usa");
plugin:setLocation(102, 348);
plugin:setNationality("nationality");
plugin:setPostalCode("618000");
```

### 接收 InMobi 事件 (可选)

```lua
local plugin = sdkbox.PluginInMobi
plugin:setListener(function(args)
    local event = args.event -- event same with function name of InMobiListener
    dump(args, "inmobi listener info:")
end)
plugin:init()
```
