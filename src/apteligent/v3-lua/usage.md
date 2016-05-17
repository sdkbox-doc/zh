### 初始化 Apteligent
* 修改您的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```lua
sdkbox.PluginApteligent:init()
```

### 注册追踪器 Breadcrumbs

```lua
-- leave a breadcrumb
sdkbox.PluginApteligent:leaveBreadcrumb("User tapped start button");

-- perform all breadcrumb writes on a background thread
sdkbox.PluginApteligent:setAsyncBreadcrumbMode(true)
```


### 注册用户元数据

```lua
-- Adding a Username
sdkbox.PluginApteligent:setUsername("MrsCritter")

-- Adding Arbitrary User Metadata
sdkbox.PluginApteligent:setValueforKey("5", "Game Level")
```


### 注册用户流

```lua
-- Beginning a Userflow
sdkbox.PluginApteligent:beginUserflow("login")

-- Ending a Userflow
sdkbox.PluginApteligent:endUserflow("login")

-- Failing a Userflow
sdkbox.PluginApteligent:failUserflow("login")

-- Cancelling a Userflow
sdkbox.PluginApteligent:cancelUserflow("login")
```

### 修改用户流的值
```lua
int valueInCents = sdkbox.PluginApteligent:valueForUserflow("my_userflow")
valueInCents += 5
sdkbox.PluginApteligent:setValueforUserflow(valueInCents, "my_userflow")

```

### 注册网络请求
```lua
sdkbox.PluginApteligent:logNetworkRequest("GET", "http://www.abc123def456.com", 2.0, 1000, 100, 200)
```


### 过滤截获数据
```lua
sdkbox.PluginApteligent:addFilter("www.gmail.com")
```

### 配置位置坐标
```lua
-- Beijing, China
sdkbox.PluginApteligent:updateLocation(39.9042, 116.4074)
```

### 其他任务
```lua
-- Allowing Users to Opt Out of Apteligent
sdkbox.PluginApteligent:setOptOutStatus(true)

-- Changing the verbosity of Apteligent’s Logs
-- sdkbox.PluginApteligent.LoggingLevel.Silent  : Turns off all Apteligent log messages
-- sdkbox.PluginApteligent.LoggingLevel.Error   : Only print errors. An error is an unexpected event that will result not capturing important data
-- sdkbox.PluginApteligent.LoggingLevel.Warning : (Default) Only print warnings. Currently warning messages are printed when calling Apteligent methods before initializing Apteligent.
-- sdkbox.PluginApteligent.LoggingLevel.Info    : The most verbose level of logging
sdkbox.PluginApteligent:setLoggingLevel(sdkbox.PluginApteligent.LoggingLevel.Info)

-- Send App Load Data
-- You must set `"delay_sending_appload":true` in `sdkbox_config.json` first
sdkbox.PluginApteligent:sendAppLoadData()
```

### 实现 ApteligentListener
* 您可以实现 ApteligentListener 用来设置回调，比如当一个视频播放完成的时候。
```lua

sdkbox.PluginApteligent.setListener(function(args)
    local event = args.event
    if "onCrashOnLastLoad" == event then -- not support on android
    end
end)

```
