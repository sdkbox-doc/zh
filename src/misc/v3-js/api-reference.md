## API 文档

### 方法
```javascript
sdkbox.PluginMisc.init();
```
>  初始化插件

```javascript
sdkbox.PluginMisc.setListener(listener);
```
> 设置 Listener

```javascript
sdkbox.PluginMisc.localNotify(title, content, delaymillisecond);
```
> 发送本地消息
@return 消息id


### Listeners
```javascript
onHandleLocalNotify (payloadJson);
```

