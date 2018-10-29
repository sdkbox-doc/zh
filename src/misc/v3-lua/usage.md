### 初始化 Misc

* 在你的代码中调用 `init()` 初始化插件, 一定要在使用插件功能之前初始化.
```lua
sdkbox.PluginMisc:init()
```

### 发送本地消息
```lua
-- 在 10 秒后收到消息
local nid = sdkbox.PluginMisc:localNotify("test title", "this a test notify content", 1000 * 10);
cc.log('Local Notification ID:' .. nid);
```

### 实现 MiscListner
* 接收消息的事件，需要实现 MiscListner.
```lua

sdkbox.PluginMisc.setListener(function(data)
    local event = args.event
    if "onHandleLocalNotify" == event then
    else
        cc.log('unknow event');
    end
end)

```
