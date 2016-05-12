![](SDKBOX_logo.png)

# Google Analytics 插件文档

更多的信息，请访问我们的主页：[www.sdkbox.com](http://cocos2d-x.org/sdkbox)

## 集成 SDKBOX GoogleAnalytics

首先将 ```sdkbox_socialshare``` unity 包导入您的工程中。这将会在 Assets 目录下创建两个目录（Plugins 和 SDKBOX）。

## 使用 GoogleAnalytics 插件

To begin using GoogleAnalytics plugin, find the GoogleAnalytics prefab in the Assets/SDKBOX/googleanalytics directory.
在开始使用 GoogleAnalytics 之前，在 Assets/SDKBOX/socialshare 目录下找到 GoogleAnalytics prefab 。

![](ga1.png)

在您想使用 GoogleAnalytics package 的场景中创建一个 GoogleAnalytics prefab 的实例。在任何时候，您只需要一个 prefab 的实例。

![](ga2.png)

在 hierarchy 中选择 GoogleAnalytics 游戏对象，并且在您的 inspector pane 中您可以配置这个对象以完成安装。

## 配置 GoogleAnalytics 插件

![](ga3.png)

### 配置字段说明

<h5>iOS Tracking Code</h5>
这是您 GoogleAnalytics 帐号的追踪代号。您可以在两个平台使用相同的追踪代号，也可以分别使用不同的代号，这取决于您。

<h5>Android Tracking Code</h5>
这是您 GoogleAnalytics 帐号的追踪代号。您可以在两个平台使用相同的追踪代号，也可以分别使用不同的代号，这取决于您。


## GoogleAnalytics API

<h6>
在初始化时，显示的开始一个分析会话。
</h6>
```
public static void startSession();
```

<h6>
终止一个会话。您通常不需要手动终止一个会话，如果您需要这么做， 您可以调用这个方法。
</h6>
```
static void stopSession();
```

<h6>
手动请求信息发送到服务器。默认情况下，数据在 Android 平台下每5分钟使用 Google Analytics SDK 发送到服务器。
</h6>
```
static void dispatchHits();
```

<h6>
更改信息发送到服务器的周期时间，设置其为期待的秒数。
</h6>
```
static void dispatchPeriodically(int seconds);
```

<h6>
停止周期性发送信息到服务器。
接下来如果想恢复发送，那么需要手动调用 `dispatchPeriodically` 或者 `dispatchHits` 。
</h6>
```
static void stopPeriodicalDispatch();
```

<h6>
为这次追踪会话设置用户 ID 。
</h6>
```
static void setUser(string userID);
```

<h6>
Set value for custom dimension.
定制规格。
</h6>
```
static void setDimension(int index, string value);
```

<h6>
Set value for custom metric.
定制
</h6>
```
static void setMetric(int index, string value);
```

<h6>
Log screen info. title is the title of a screen. Screens are logical units
inside your app you'd like to identify at analytics panel.
记录屏幕信息。标题是屏幕的标题。

</h6>
```
static void logScreen(string title);
```

<h6>
记录事件。
</h6>
```
static void logEvent(string eventCategory, string eventAction, string eventLabel, int value);
```

<h6>
记录一个异常。这仅仅支持 app 内部事件。
</h6>
```
static void logException(string exceptionDescription, bool isFatal);
```

<h6>
测量应用程序时间
</h6>
```
static void logTiming(string timingCategory, int timingInterval, string timingName, string timingLabel);
```

<h6>
记录一个社交事件。
</h6>
```
static void logSocial(string socialNetwork, string socialAction, string socialTarget);
```

<h6>
测试性运行，跟踪的事件不会被真正的发送给真实的服务器帐号。
</h6>
```
static void setDryRun(bool enable);
```

<h6>
当使用 google 内部的广告供应商时候，允许追踪广告事件。
</h6>
```
static void enableAdvertisingTracking(bool enable);
```

<h6>
根据追踪 ID XX-YYYYYYYY-Z 创建一个 google analytics 追踪器。
如果这个追踪器已经存在，那么不会有新的追踪器被创建。在任何情况下，与追踪 id 关联的追踪器将被设置成分析方法的默认追踪器。
</h6>
```
static void createTracker(string trackerId);
```

<h6>
 * 根据 trackerId 激活一个追踪器。如果这个追踪器不存在，
 * 那么调用将无任何作用。
</h6>
```
static void enableTracker(string trackerId);
```

