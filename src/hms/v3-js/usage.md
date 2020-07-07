### 初始化 HMS
* 在您的代码合适的地方调用 `init()` 完成初始化. 我们推荐在 `app.js` 中完成初始化.比如:
```javascript
sdkbox.PluginHMS.init();
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
sdkbox.PluginHMS.login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```javascript
sdkbox.PluginHMS.login(2);
```

* Silently Signing In With HUAWEI ID

静默登录只能在上一次使用前两种方式已经登录成功的情况下，才能在静态登录下成功

```javascript
sdkbox.PluginHMS.login(0);
```

> 以上三种登录方式, 不管成功还是失败, 最终都会触发 `onLogin` 事件.

HMS 帐号相关的 [文档](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### 登出

```javascript
sdkbox.PluginHMS.logout();
```

### 请求托管在 HMS 的商品

托管商品是指在 HMS 管理后台配置的商品.

```javascript
sdkbox.PluginHMS.iapRequestProducts();
```
这个方法会触发 Listener 中的 `onIAPProducts` 方法

### 购买托管商品

```javascript
sdkbox.PluginHMS.iapPurchase("coin");
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
sdkbox.PluginHMS.iapPurchaseWithPrice(JSON.stringify(productInfo));
```
这个方法会触发 Listener 中的 `onIAPPurchase` 方法

### 请求拥有的商品

请求当前拥有的商品的购买记录, 包括 不可消费，订阅商品 和 非消费的可消费商品.

```javascript
sdkbox.PluginHMS.iapRequestOwnedPurchases();
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchases` 方法

### 消费商品

注意: 这里传的是 purchaseToken , 非不是商品名字或id

```javascript
sdkbox.PluginHMS.iapConsume(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPPConsume` 方法

### 请求所有的消费记录

请求用户所有的消费记录

```javascript
sdkbox.PluginHMS.iapRequestOwnedPurchaseRecords(purchaseToken);
```
这个方法会触发 Listener 中的 `onIAPOwnedPurchaseRecords` 方法

### 玩家信息

#### 获取玩家信息

将会触发 Listener 中的函数 `onPlayerInfo`
```javascript
sdkbox.PluginHMS.playerRequestInfo();
```

#### 获取玩家额外信息

这里主要是针对 未成年防沉迷 机制, 可以取得玩家是否未成年人，它的游戏时间等信息, 开发者利用这些信息对防沉迷作相应处理.

将会触发 Listener 中的函数 `onPlayerExtraInfo`

```javascript
sdkbox.PluginHMS.playerRequestInfo();
```

#### 提交游戏开始

提交玩家开始游戏事件

将会触发 Listener 中的函数 `onPlayerGameBegin`

```javascript
sdkbox.PluginHMS.playerSubmitGameBegin();
```

#### 提交游戏结束

提交玩家结束游戏事件

将会触发 Listener 中的函数 `onPlayerGameEnd`

```javascript
sdkbox.PluginHMS.playerSubmitGameEnd();
```

### 成就

#### 取成就列表

获取成就列表, 开发者可以使用返回的数据来自行展示

将会触发 Listener 中的函数 `onAchievementList`

```javascript
sdkbox.PluginHMS.achievementRequestList();
```

#### 显示成就

使用华为默认的成就显示列表

将会触发 Listener 中的函数 `onAchievementShow`

```javascript
sdkbox.PluginHMS.achievementShow();
```

#### 成就可见

将会触发 Listener 中的函数 `onAchievementVisualize`

```javascript
sdkbox.PluginHMS.achievementVisualize();
```

#### 增长成就

将会触发 Listener 中的函数 `onAchievementGrow`

```javascript
sdkbox.PluginHMS.achievementGrow();
```

#### 设置成就步骤

将会触发 Listener 中的函数 `onAchievementMakeSteps`

```javascript
sdkbox.PluginHMS.achievementMakeSteps();
```

#### 解锁成就

```javascript
sdkbox.PluginHMS.achievementReach();
```

### 事件

#### 增长事件

```javascript
sdkbox.PluginHMS.eventGrow(event, amount);
```

#### eventRequestList

将会触发 Listener 中的函数 `onEventList`
```javascript
sdkbox.PluginHMS.eventRequestList();
```

### 排行榜

#### 检查排行榜状态

在进行排行榜相关api前，开发者必检查玩家是否允许上传分数.

将会触发 Listener 中的函数 `onRankingSwitchStatus`
```javascript
sdkbox.PluginHMS.rankingRequestSwitchStatus();
```

将会触发 Listener 中的函数 `onRankingSetSwitchStatus`
```javascript
int status = 0;
// 0: allow open score in ranking
// 1: not allow open score in ranking

sdkbox.PluginHMS.rankingSetSwitchStatus(int status);
```

#### 提交分数

将会触发 Listener 中的函数 `onRankingSubmitScore`

```javascript
sdkbox.PluginHMS.rankingSubmitScore(rankingName, score, score_unit);
```

#### 显示排行榜

开发者自行显示

将会触发 Listener 中的函数 `onRankingList`

```javascript
bool realtime = true; // true, will request data from hms server; false, will use local cache data
sdkbox.PluginHMS.rankingRequestList(realtime, rankingName);
```

用华为默认列表显示
(此方式必须保证玩家终端EMUI为9.0及以上版本，且必须安装10.3及以上版本的华为应用助手。)

将会触发 Listener 中的函数 `onRankingShow`

```javascript
int timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.PluginHMS.rankingShow(timeDimension, rankingName);
```

#### 取分数

当前玩家的分数

将会触发 Listener 中的函数 `onRankingCurPlayerScore`

```javascript
int timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.PluginHMS.rankingRequestCurPlayerScore(rankingName, timeDimension);
```

取以玩家分数为中心的分数列表

将会触发 Listener 中的函数 `onRankingPlayerCenteredScores`

```javascript
int timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.PluginHMS.rankingRequestPlayerCenteredScores(rankingName, timeDimension, realtime);
```

### 存档

新增存档

将会触发 Listener 中的函数 `onArchiveAdd`

```javascript
sdkbox.PluginHMS.archiveAdd(playedTime, progress, description, supportCache,
                               bmBytes, bmBytesLen, bmBytesType,
                               dataBytes, dataBytesLen);
```

更新存档

将会触发 Listener 中的函数 `onArchiveUpdate`

```javascript
sdkbox.PluginHMS.archiveUpdate(archiveId,
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
sdkbox.PluginHMS.archiveLoad(archiveId, conflictPolicy);
```

### 浮标

如果你的游戏将在中国发行，那必须打开游戏浮标

```javascript
sdkbox.PluginHMS.buoyShow();
//or
sdkbox.PluginHMS.buoyHide();
```

### 广告

缓存广告

```javascript
sdkbox.PluginHMS.adCache(adName);
```

显示广告

```javascript
if (sdkbox.PluginHMS.adIsAvailable(adName)) {
    sdkbox.PluginHMS.adShow(adName);
}
```

隐藏广告

```javascript
sdkbox.PluginHMS.adHide(adName);
```

广告请求参数设置 (可选)

```javascript
/*
  * 广告内容类型:
  *   "W"->适合幼儿及以上年龄段观众的内容
  *  "PI"->适合少儿及以上年龄段观众的内容
  *   "J"->适合青少年及以上年龄段观众的内容
  *   "A"->仅适合成年观众众的内容
  *    ""->未明确广告分级
  */
sdkbox.PluginHMS.adSetAdContentClassification("A");

/*
  * 面向未达到法定承诺年龄用户的设置:
  *  0->不按面向未达到法定承诺年龄用户的方式来处理广告请求
  *  1->按面向未达到法定承诺年龄用户的方式来处理广告请求
  * -1->不确定是否按面向未达到法定承诺年龄用户的方式来处理广告请求
  */
sdkbox.PluginHMS.adSetTagForUnderAgeOfPromise(0);

/*
* 面向儿童的设置:
*  0->不根据 COPPA 的规定来处理广告请求
*  1->根据 COPPA 的规定来处理广告请求
* -1->不确定是否根据 COPPA 的规定来处理广告请求
*/
sdkbox.PluginHMS.adSetTagForChildProtection(0);

/*
* 是否只请求非个性化广告
*  0->请求个性化广告和非个性化广告（默认）;
*  1->只请求非个性化广告;
*/
sdkbox.PluginHMS.adSetNonPersonalizedAd(0);
```

奖励广告设置 (可选)

设置的奖励数据必须要URLEncode, 同时长度不超过1024个字符

```javascript
// 奖励广告定制数据
sdkbox.PluginHMS.adSetRewardData("cdata");

// 奖励广告用户 id
sdkbox.PluginHMS.adSetRewardUserId("uid666");
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
sdkbox.PluginHMS.setListener({
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

    // Ad
    onAdClose(code, errorOrJson) {
    }

    onAdFail(code, errorOrJson) {
    }

    onAdLeave(code, errorOrJson) {
    }

    onAdOpen(code, errorOrJson) {
    }

    onAdLoad(code, errorOrJson) {
    }

    onAdClick(code, errorOrJson) {
    }

    onAdImpression(code, errorOrJson) {
    }

    onAdReward(code, errorOrJson) {
    }

});
```
