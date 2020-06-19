### 初始化 HMS
在您的工程中合适的地方初始化插件.我们推荐在 `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()` 中.确保包含了相关的头文件:
```cpp
#include "PluginHMS/PluginHMS.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::HMS::init();
}
```

### 登录

HMS 提供了三种登录方式:

* Signing In with HUAWEI ID(ID Token)

```cpp
sdkbox::HMS::login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```cpp
sdkbox::HMS::login(2);
```

* Silently Signing In With HUAWEI ID

静默登录只能在上一次使用前两种方式已经登录成功的情况下，才能在静态登录下成功

```cpp
sdkbox::HMS::login(0);
```

> 以上三种登录方式, 不管成功还是失败, 最终都会触发 `onLogin` 事件.

HMS 帐号相关的 [文档](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### 登出

```cpp
sdkbox::HMS::logout();
```

### 请求托管在 HMS 的商品

托管商品是指在 HMS 管理后台配置的商品.

```cpp
sdkbox::HMS::iapRequestProducts();
```
这个方法会触发 Listener 中的 `onIAPProducts` 方法

### 购买托管商品

```cpp
sdkbox::HMS::iapPurchase("coin");
```
这个方法会触发 Listener 中的 `onIAPPurchase` 方法

### 购买非托管商品

非托管商品是指未在 HMS 后台配置商品, 但使用 HMS IAP 的来支付.

```cpp
const std::string productInfo = R"(
{
  "priceType": 0, //0:consumable 1:non-consumable 2:subscription
  "productName": "product name",
  "productId": "product id",
  "amount": "1.00",
  "currency": "CNY",
  "country": "CN",
  "sdkChannel": "1", // sdkChannel size must be between 0 and 4
  "serviceCatalog": "X58",
  "reservedInfor": "{\"a\": 1, \"b\":\"s\"}", // reservedInfor must be json string
  "developerPayload": "payload1"
}
)";
sdkbox::HMS::iapPurchaseWithPrice(productInfo);
```
这个方法会触发 Listener 中的 `onIAPPurchase` 方法

### 请求拥有的商品

请求当前拥有的商品的购买记录, 包括 不可消费，订阅商品 和 非消费的可消费商品.

```cpp
sdkbox::HMS::iapRequestOwnedPurchases();
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchases` 方法

### 消费商品

注意: 这里传的是 purchaseToken , 非不是商品名字或id

```cpp
sdkbox::HMS::iapConsume(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPPConsume` 方法

### 请求所有的消费记录

请求用户所有的消费记录

```cpp
sdkbox::HMS::iapRequestOwnedPurchaseRecords(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchaseRecords` 方法


### 玩家信息

#### 获取玩家信息

将会触发 Listener 中的函数 `onPlayerInfo`
```cpp
sdkbox::HMS::playerRequestInfo();
```

#### 获取玩家额外信息

这里主要是针对 未成年防沉迷 机制, 可以取得玩家是否未成年人，它的游戏时间等信息, 开发者利用这些信息对防沉迷作相应处理.

将会触发 Listener 中的函数 `onPlayerExtraInfo`

```cpp
sdkbox::HMS::playerRequestInfo();
```

#### 提交游戏开始

提交玩家开始游戏事件

将会触发 Listener 中的函数 `onPlayerGameBegin`

```cpp
sdkbox::HMS::playerSubmitGameBegin();
```

#### 提交游戏结束

提交玩家结束游戏事件

将会触发 Listener 中的函数 `onPlayerGameEnd`

```cpp
sdkbox::HMS::playerSubmitGameEnd();
```

### 成就

#### 取成就列表

获取成就列表, 开发者可以使用返回的数据来自行展示

将会触发 Listener 中的函数 `onAchievementList`

```cpp
sdkbox::HMS::achievementRequestList();
```

#### 显示成就

使用华为默认的成就显示列表

将会触发 Listener 中的函数 `onAchievementShow`

```cpp
sdkbox::HMS::achievementShow();
```

#### 成就可见

将会触发 Listener 中的函数 `onAchievementVisualize`

```cpp
sdkbox::HMS::achievementVisualize();
```

#### 增长成就

将会触发 Listener 中的函数 `onAchievementGrow`

```cpp
sdkbox::HMS::achievementGrow();
```

#### 设置成就步骤

将会触发 Listener 中的函数 `onAchievementMakeSteps`

```cpp
sdkbox::HMS::achievementMakeSteps();
```

#### 解锁成就

```cpp
sdkbox::HMS::achievementReach();
```

### 事件

#### 增长事件

```cpp
sdkbox::HMS::eventGrow(event, amount);
```

#### eventRequestList

将会触发 Listener 中的函数 `onEventList`
```cpp
sdkbox::HMS::eventRequestList();
```

### 排行榜

#### 检查排行榜状态

在进行排行榜相关api前，开发者必检查玩家是否允许上传分数.

将会触发 Listener 中的函数 `onRankingSwitchStatus`
```cpp
sdkbox::HMS::rankingRequestSwitchStatus();
```

将会触发 Listener 中的函数 `onRankingSetSwitchStatus`
```cpp
int status = 0;
// 0: allow open score in ranking
// 1: not allow open score in ranking

sdkbox::HMS::rankingSetSwitchStatus(int status);
```

#### 提交分数

将会触发 Listener 中的函数 `onRankingSubmitScore`

```cpp
sdkbox::HMS::rankingSubmitScore(rankingName, score, score_unit);
```

#### 显示排行榜

开发者自行显示

将会触发 Listener 中的函数 `onRankingList`

```cpp
bool realtime = true; // true, will request data from hms server; false, will use local cache data
sdkbox::HMS::rankingRequestList(realtime, rankingName);
```

用华为默认列表显示
(此方式必须保证玩家终端EMUI为9.0及以上版本，且必须安装10.3及以上版本的华为应用助手。)

将会触发 Listener 中的函数 `onRankingShow`

```cpp
int timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox::HMS::rankingShow(timeDimension, rankingName);
```

#### 取分数

当前玩家的分数

将会触发 Listener 中的函数 `onRankingCurPlayerScore`

```cpp
int timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox::HMS::rankingRequestCurPlayerScore(rankingName, timeDimension);
```

取以玩家分数为中心的分数列表

将会触发 Listener 中的函数 `onRankingPlayerCenteredScores`

```cpp
int timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox::HMS::rankingRequestPlayerCenteredScores(rankingName, timeDimension, realtime);
```

### 存档

新增存档

将会触发 Listener 中的函数 `onArchiveAdd`

```cpp
sdkbox::HMS::archiveAdd(playedTime, progress, description, supportCache,
                               bmBytes, bmBytesLen, bmBytesType,
                               dataBytes, dataBytesLen);
```

更新存档

将会触发 Listener 中的函数 `onArchiveUpdate`

```cpp
sdkbox::HMS::archiveUpdate(archiveId,
                          playedTime, progress, description,
                          bmBytes, bmBytesLen, bmBytesType,
                          dataBytes, dataBytesLen);
```

读存档

将会触发 Listener 中的函数 `onArchiveLoad`

```cpp
int conflictPolicy = 3;
//-1 -> hms willn't hand conflict, 
//1  -> hms will resolved conflict by played time, 
//2  -> hms will resolved conflict by progress,
//3  -> hms will resolved conflict by last update time
sdkbox::HMS::archiveLoad(archiveId, conflictPolicy);
```

### 浮标

如果你的游戏将在中国发行，那必须打开游戏浮标

```cpp
sdkbox::HMS::buoyShow();
//or
sdkbox::HMS::buoyHide();
```


### 处理HMS事件
允许您接收 `HMS` 的事件.

所有的回调中都包含一个 code , 这值的含义可以参与如下 url :

* https://developer.huawei.com/consumer/cn/doc/development/HMS-References/game-return-code-v4
* https://developer.huawei.com/consumer/cn/doc/development/HMS-References/hms-error-code

这里单独列出常见的一些值的含义:

7020: 本地cache中没有数据
7022: 未实名或未成年人
7024: 手机中没有安装 "华为应用市场"
7218: 华为应用市场中的游戏服务未打开，或用户取消
7204: 需要安装应用助手最新版
7013: 未登录帐号 或 在调用 Archive 相关接口时报这个错，也可能是 sdkbox_config 中的 archive 未设置为 true


* 继承这个类 `sdkbox::HMSListener`:
```cpp
#include "PluginHMS/PluginHMS.h"
class MyClass : public sdkbox::HMSListener
{
private:
  // Account
  virtual void onLogin(int code, const std::string &msg) override;

  // Player Info
  virtual void onPlayerInfo(int code, const std::string& errorOrJson) override;
  virtual void onPlayerExtraInfo(int code, const std::string& errorOrJson) override;
  virtual void onPlayerGameBegin(int code, const std::string& errorOrJson) override;
  virtual void onPlayerGameEnd(int code, const std::string& errorOrJson) override;

  // IAP
  virtual void onIAPReady(int code, const std::string& msg) override;
  virtual void onIAPProducts(int code, const std::string& errorOrJson) override;
  virtual void onIAPPurchase(int code, const std::string& errorOrJson) override;
  virtual void onIAPPConsume(int code, const std::string& errorOrJson) override;
  virtual void onIAPOwnedPurchases(int code, const std::string& errorOrJson) override;
  virtual void onIAPOwnedPurchaseRecords(int code, const std::string& errorOrJson) override;

  // Achievement
  virtual void onAchievementList(int code, const std::string& errorOrJson) override;
  virtual void onAchievementShow(int code, const std::string& errorOrJson) override;
  virtual void onAchievementVisualize(int code, const std::string& errorOrJson) override;
  virtual void onAchievementGrow(int code, const std::string& errorOrJson) override;
  virtual void onAchievementMakeSteps(int code, const std::string& errorOrJson) override;

  // Event
  virtual void onEventList(int code, const std::string& errorOrJson) override;

  // Ranking
  virtual void onRankingSwitchStatus(int code, const std::string& errorOrJson) override;
  virtual void onRankingSetSwitchStatus(int code, const std::string& errorOrJson) override;
  virtual void onRankingSubmitScore(int code, const std::string& errorOrJson) override;
  virtual void onRankingShow(int code, const std::string& errorOrJson) override;
  virtual void onRankingList(int code, const std::string& errorOrJson) override;
  virtual void onRankingCurPlayerScore(int code, const std::string& errorOrJson) override;
  virtual void onRankingPlayerCenteredScores(int code, const std::string& errorOrJson) override;
  virtual void onRankingMoreScores(int code, const std::string& errorOrJson) override;
  virtual void onRankingTopScores(int code, const std::string& errorOrJson) override;

  // Archive
  virtual void onArchiveLimitThumbnailSize(int code, const std::string& errorOrJson) override;
  virtual void onArchiveLimitDetailsSize(int code, const std::string& errorOrJson) override;
  virtual void onArchiveAdd(int code, const std::string& errorOrJson) override;
  virtual void onArchiveShow(int code, const std::string& errorOrJson) override;
  virtual void onArchiveSummaryList(int code, const std::string& errorOrJson) override;
  virtual void onArchiveSelect(int code, const std::string& errorOrJson) override;
  virtual void onArchiveThumbnail(int code, const std::string& errorOrJson, unsigned char* coverData, unsigned int coverDataLen) override;
  virtual void onArchiveUpdate(int code, const std::string& errorOrJson) override;
  virtual void onArchiveLoad(int code, const std::string& errorOrJson, unsigned char* contentData, unsigned int contentDataLen) override;
  virtual void onArchiveRemove(int code, const std::string& errorOrJson) override;

  // Game Stats
  virtual void onGamePlayerStats(int code, const std::string& errorOrJson) override;
  virtual void onGameSummary(int code, const std::string& errorOrJson) override;

}
```

* 创建一个监听类来接收回调事件:
```cpp
sdkbox::HMS::setListener(listener);
```
