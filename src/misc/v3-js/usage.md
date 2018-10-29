### 初始化 Misc

调用 `init()` 可以初始化插件, 我们建议在 `app.js` 中初始化插件.
```javascript
sdkbox.PluginMisc.init();
```

### 发送一个本地消息

```javascript
// 10 秒后会收到一个消息
let nid = sdkbox.PluginMisc.localNotify("test title", "this a test notify content", 1000 * 10);
cc.log('Local Notification ID:' + nid);
```

### 实现 MiscListner

* 接收消息的事件，需要继承 MiscListener

```javascript

sdkbox.PluginMisc.setListener({
    onHandleLocalNotify :function (json) {
        cc.log(json);
    }
});

```
