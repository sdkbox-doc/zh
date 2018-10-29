## API 文档

### 方法
```lua
sdkbox.PluginMisc:init()
```
>  初始化插件

```lua
sdkbox.PluginMisc:setListener(listener)
```
> 设置 Listener

```lua
sdkbox.PluginMisc:localNotify(title, content, delaymillisecond);
```
> 发送本地消息
@return 消息id


### Listeners
```lua
onHandleLocalNotify (payloadJson);
```
