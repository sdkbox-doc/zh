### 修改 `AppDelegate.cpp`
* 修改 `Classes/AppDelegate.cpp` 包含以下头文件:
```lua
#include "PluginUnityAdsLua.hpp"
#include "PluginUnityAdsLuaHelper.h"
```

### 初始化 UnityAds
修改您的lua代码来初始化这个插件. 这个初始化,可以在任意地方,但是必须在您调用插件的功能接口之前.
```lua
sdkbox.PluginUnityAds:init()
```

### 显示插屏广告

```lua
local placement = ""
if (sdkbox.PluginUnityAds:isReady(placement)) then
    sdkbox.PluginUnityAds:show(placement)
else
    printf("unityads ad is not ready")
end
```

### 接收 UnityAds 事件 (可选)

```lua
local plugin = sdkbox.PluginUnityAds
plugin:setListener(function(args)
    local event = args.event -- event same with function name of UnityAdsListener
    dump(args, "unityads listener info:")
end)
plugin:init()
```
