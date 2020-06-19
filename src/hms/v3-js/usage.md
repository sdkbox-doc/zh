### 初始化 HMS
* 在您的代码合适的地方调用 `init()` 完成初始化. 我们推荐在 `app.js` 中完成初始化.比如:
```javascript
sdkbox.HMS.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```javascript
#include "PluginHMSJS.hpp"
#include "PluginHMSJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保调用了如下函数:
```javascript
sc->addRegisterCallback(register_all_PluginHMSJS);
sc->addRegisterCallback(register_all_PluginHMSJS_helper);
```

### 登录

HMS 提供了三种登录方式:

* Signing In with HUAWEI ID(ID Token)

```javascript
sdkbox.HMS.login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```javascript
sdkbox.HMS.login(2);
```

* Silently Signing In With HUAWEI ID

静默登录只能在上一次使用前两种方式已经登录成功的情况下，才能在静态登录下成功

```javascript
sdkbox.HMS.login(0);
```

> 以上三种登录方式, 不管成功还是失败, 最终都会触发 `onLogin` 事件.

HMS 帐号相关的 [文档](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### 登出

```javascript
sdkbox.HMS.logout();
```

### 请求托管在 HMS 的商品

托管商品是指在 HMS 管理后台配置的商品.

```javascript
sdkbox.HMS.iapRequestProducts();
```
这个方法会触发 Listener 中的 `onIAPProducts` 方法

### 购买托管商品

```javascript
sdkbox.HMS.iapPurchase("coin");
```
这个方法会触发 Listener 中的 `onIAPPurchase` 方法

### 购买非托管商品

非托管商品是指未在 HMS 后台配置商品, 但使用 HMS IAP 的来支付.

```javascript
let productInfo = {
  priceType: 0, // 0:consumable 1:non-consumable 2:subscription
  productName: 'product name',
  productId: 'product id',
  amount: '1.00',
  currency: 'CNY',
  country: 'CN',
  sdkChannel: '1', // sdkChannel size must be between 0 and 4
  serviceCatalog: 'X58',
  reservedInfor: '{"a": 1, "b":"s"}', // reservedInfor must be json string
  developerPayload: 'payload1'
};
sdkbox.HMS.iapPurchaseWithPrice(JSON.stringify(productInfo));
```
这个方法会触发 Listener 中的 `onIAPPurchase` 方法

### 请求拥有的商品

请求当前拥有的商品的购买记录, 包括 不可消费，订阅商品 和 非消费的可消费商品.

```javascript
sdkbox.HMS.iapRequestOwnedPurchases();
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchases` 方法

### 消费商品

注意: 这里传的是 purchaseToken , 非不是商品名字或id

```javascript
sdkbox.HMS.iapConsume(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPPConsume` 方法

### 请求所有的消费记录

请求用户所有的消费记录

```javascript
sdkbox.HMS.iapRequestOwnedPurchaseRecords(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchaseRecords` 方法

### 玩家信息

#### 获取玩家信息

将会触发 Listener 中的函数 `onPlayerInfo`
```javascript
sdkbox.HMS.playerRequestInfo();
```

#### 获取玩家额外信息

这里主要是针对 未成年防沉迷 机制, 可以取得玩家是否未成年人，它的游戏时间等信息, 开发者利用这些信息对防沉迷作相应处理.

将会触发 Listener 中的函数 `onPlayerExtraInfo`

```javascript
sdkbox.HMS.playerRequestInfo();
```

#### 提交游戏开始

提交玩家开始游戏事件

将会触发 Listener 中的函数 `onPlayerGameBegin`

```javascript
sdkbox.HMS.playerSubmitGameBegin();
```

#### 提交游戏结束

提交玩家结束游戏事件

将会触发 Listener 中的函数 `onPlayerGameEnd`

```javascript
sdkbox.HMS.playerSubmitGameEnd();
```

### 成就

#### 取成就列表

获取成就列表, 开发者可以使用返回的数据来自行展示

将会触发 Listener 中的函数 `onAchievementList`

```javascript
sdkbox.HMS.achievementRequestList();
```

#### 显示成就

使用华为默认的成就显示列表

将会触发 Listener 中的函数 `onAchievementShow`

```javascript
sdkbox.HMS.achievementShow();
```

#### 成就可见

将会触发 Listener 中的函数 `onAchievementVisualize`

```javascript
sdkbox.HMS.achievementVisualize();
```

#### 增长成就

将会触发 Listener 中的函数 `onAchievementGrow`

```javascript
sdkbox.HMS.achievementGrow();
```

#### 设置成就步骤

将会触发 Listener 中的函数 `onAchievementMakeSteps`

```javascript
sdkbox.HMS.achievementMakeSteps();
```

#### 解锁成就

```javascript
sdkbox.HMS.achievementReach();
```

### 事件

#### 增长事件

```javascript
sdkbox.HMS.eventGrow(event, amount);
```

#### eventRequestList

将会触发 Listener 中的函数 `onEventList`
```javascript
sdkbox.HMS.eventRequestList();
```

### 排行榜

#### 检查排行榜状态

在进行排行榜相关api前，开发者必检查玩家是否允许上传分数.

将会触发 Listener 中的函数 `onRankingSwitchStatus`
```javascript
sdkbox.HMS.rankingRequestSwitchStatus();
```

将会触发 Listener 中的函数 `onRankingSetSwitchStatus`
```javascript
int status = 0;
// 0: allow open score in ranking
// 1: not allow open score in ranking

sdkbox.HMS.rankingSetSwitchStatus(int status);
```

#### 提交分数

将会触发 Listener 中的函数 `onRankingSubmitScore`

```javascript
sdkbox.HMS.rankingSubmitScore(rankingName, score, score_unit);
```

#### 显示排行榜

开发者自行显示

将会触发 Listener 中的函数 `onRankingList`

```javascript
bool realtime = true; // true, will request data from hms server; false, will use local cache data
sdkbox.HMS.rankingRequestList(realtime, rankingName);
```

用华为默认列表显示
(此方式必须保证玩家终端EMUI为9.0及以上版本，且必须安装10.3及以上版本的华为应用助手。)

将会触发 Listener 中的函数 `onRankingShow`

```javascript
int timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.HMS.rankingShow(timeDimension, rankingName);
```

#### 取分数

当前玩家的分数

将会触发 Listener 中的函数 `onRankingCurPlayerScore`

```javascript
int timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.HMS.rankingRequestCurPlayerScore(rankingName, timeDimension);
```

取以玩家分数为中心的分数列表

将会触发 Listener 中的函数 `onRankingPlayerCenteredScores`

```javascript
int timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.HMS.rankingRequestPlayerCenteredScores(rankingName, timeDimension, realtime);
```

### 存档

新增存档

将会触发 Listener 中的函数 `onArchiveAdd`

```javascript
sdkbox.HMS.archiveAdd(playedTime, progress, description, supportCache,
                               bmBytes, bmBytesLen, bmBytesType,
                               dataBytes, dataBytesLen);
```

更新存档

将会触发 Listener 中的函数 `onArchiveUpdate`

```javascript
sdkbox.HMS.archiveUpdate(archiveId,
                          playedTime, progress, description,
                          bmBytes, bmBytesLen, bmBytesType,
                          dataBytes, dataBytesLen);
```

读存档

将会触发 Listener 中的函数 `onArchiveLoad`

```javascript
int conflictPolicy = 3;
//-1 -> hms willn't hand conflict, 
//1  -> hms will resolved conflict by played time, 
//2  -> hms will resolved conflict by progress,
//3  -> hms will resolved conflict by last update time
sdkbox.HMS.archiveLoad(archiveId, conflictPolicy);
```

### 浮标

如果你的游戏将在中国发行，那必须打开游戏浮标

```javascript
sdkbox.HMS.buoyShow();
//or
sdkbox.HMS.buoyHide();
```

### 处理HMS事件
您可以接收 `HMS` 事件, 不同事件对您的用户及 HMS 服务器做不同的处理.

所有的回调中都包含一个 code , 这值的含义可以参与如下 url :

* https://developer.huawei.com/consumer/cn/doc/development/HMS-References/game-return-code-v4
* https://developer.huawei.com/consumer/cn/doc/development/HMS-References/hms-error-code

这里单独列出常见的一些值的含义:

- 7020: 本地cache中没有数据
- 7022: 未实名或未成年人
- 7024: 手机中没有安装 "华为应用市场"
- 7218: 华为应用市场中的游戏服务未打开，或用户取消
- 7204: 需要安装应用助手最新版
- 7013: 未登录帐号 或 在调用 Archive 相关接口时报这个错，也可能是 sdkbox_config 中的 archive 未设置为 true

```javascript
sdkbox.HMS.setListener({
    // Account
    onLogin: function (code, msg) {
        // login event
    },

    // Player Info
    onPlayerInfo: function(code, errorOrJson) {
    },

    onPlayerExtraInfo: function(code, errorOrJson) {
    },

    onPlayerGameBegin: function(code, errorOrJson) {
    },

    onPlayerGameEnd: function(code, errorOrJson) {
    },

    // IAP
    onIAPReady: function(code, msg) {
        self.log('HMS Listener onIAPReady:' + code);
        cc.log(msg);
    },
    onIAPProducts: function(code, msg) {
        self.log('HMS Listener onIAPProducts:' + code);
        cc.log(msg);
    },
    onIAPPurchase: function(code, msg) {
        self.log('HMS Listener onIAPPurchase:' + code);
        cc.log(msg);
    },
    onIAPPConsume: function(code, msg) {
        self.log('HMS Listener onIAPPConsume:' + code);
        cc.log(msg);
    },
    onIAPOwnedPurchases: function(code, msg) {
        self.log('HMS Listener onIAPOwnedPurchases:' + code);
        cc.log(msg);
    },
    onIAPOwnedPurchaseRecords: function(code, msg) {
        self.log('HMS Listener onIAPOwnedPurchaseRecords:' + code);
        cc.log(msg);
    },

    // Achievement
    onAchievementList(code, errorOrJson) {
    }

    onAchievementShow(code, errorOrJson) {
    }

    onAchievementVisualize(code, errorOrJson) {
    }

    onAchievementGrow(code, errorOrJson) {
    }

    onAchievementMakeSteps(code, errorOrJson) {
    }

    // Event
    onEventList(code, errorOrJson) {
    }

    // Ranking
    onRankingSwitchStatus(code, errorOrJson) {
    }

    onRankingSetSwitchStatus(code, errorOrJson) {
    }

    onRankingSubmitScore(code, errorOrJson) {
    }

    onRankingShow(code, errorOrJson) {
    }

    onRankingList(code, errorOrJson) {
    }

    onRankingCurPlayerScore(code, errorOrJson) {
    }

    onRankingPlayerCenteredScores(code, errorOrJson) {
    }

    onRankingMoreScores(code, errorOrJson) {
    }

    onRankingTopScores(code, errorOrJson) {
    }

    // Archive
    onArchiveLimitThumbnailSize(code, errorOrJson) {
    }

    onArchiveLimitDetailsSize(code, errorOrJson) {
    }

    onArchiveAdd(code, errorOrJson) {
    }

    onArchiveShow(code, errorOrJson) {
    }

    onArchiveSummaryList(code, errorOrJson) {
    }

    onArchiveSelect(code, errorOrJson) {
    }

    onArchiveThumbnail(code, errorOrJson, coverData:Uint8Array) {
    }

    onArchiveUpdate(code, errorOrJson) {
    }

    onArchiveLoad(code, errorOrJson, contentData:Uint8Array) {
    }

    onArchiveRemove(code, errorOrJson) {
    }

    // Game Stats
    onGamePlayerStats(code, errorOrJson) {
    }

    onGameSummary(code, errorOrJson) {
    }


});
```
