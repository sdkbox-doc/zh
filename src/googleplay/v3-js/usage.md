
### 注册 Javascript 功能
你需要在使用 Google Play Games JS 前，先注册到 cocos2d-x.

这样做:
* 在 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 中包含如下头文件:
```cpp
#include "PluginGPGJS.hpp"
#include "PluginGPGJSHelper.h"
```

* 在 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 中调用如下代码:
```cpp
    sc->addRegisterCallback(register_all_PluginGPGJS);
    sc->addRegisterCallback(register_all_PluginGPGJS_helper);
```

### 初始化 Google Play Games
Google Play 是通过 `gpg.Builder` 这个类来初始化的.

这一个认证相关的代码，你可以直接拷贝粘贴来运行它:

```javascript

//Initialization
var config = new gpg.PlatformConfiguration();
config.SetClientID('777734739048-cdkbeieil19d6pfkavddrri5o19gk4ni.apps.googleusercontent.com');

new gpg.GameServices.Builder()
            .SetOnAuthActionStarted( function( result ) {
                // Auth started callback
            })
            .SetOnAuthActionFinished( function( result ) {
                // Auth finished callback
            })
            .SetLogging( gpg.LogLevel.INFO )	// Set Logging level
            .EnableSnapshots()					// Enable Snapshot (Saved Game) functionailty
            .Create( config, function( game_services ) {
                // 8
            } );
```

下面一步一步来操作.

###初始化
创建一个 `gpg.PlatformConfiguration` 类. 传入 client id, 这个只在 ios 上是需要的.

下一步就是创建一个 GameServices 类,它提供了访问 Googol Play Game 服务的接口.


#### Authorization 回调
GPG的 authentication 有两个回调 `AuthActionStarted` 和 `AuthActionFinished`

#### Auth 开始

```javascript
//result.AuthOperation indicates if user wants sign in or sign out
.SetOnAuthActionStarted(
    function( result ) {
        cc.log('on auth action started: ' + result.AuthOperation);
    })
```

#### Auth 结束

```javascript
.SetOnAuthActionFinished(
    function( result ) {
        cc.log('on auth action finished: ' + result.AuthOperation + ' ' + result.AuthStatus);
    })
```

#### 设置 Logging 等级
设置 Logging 等级是可选的步骤. 这是唯一的一个地方可以控制 Logging 等级的地方.


#### 启用 Saved Game
如果你想保存游戏数据到云服务器中, 就在初始化时设置它.

#### 创建
到这一步，authentication 之前的代码就差不多了.
然后 `Create` 函数就是真正的使用之前的设置去 authenticated, 通知是否成功，返回可访问的 GPG 类
GPG的交互都通过 `gpg.GameServices` 类来操作. 如果一切成功的话, 这个类会在 `Create` 的回调中返回。

### Authorization

所有的 Google Play Game 服务都需要用户先登录. 所以在 GPG 初始化后, 你应该让用户登录

```javascript
	game_services.StartAuthorizationUI();
```

### Achievements

成就是一个让用户有参与感很好的方法.你可以用游戏中的成就来鼓励用户去完成一些，平常他们不会去完成任务, 或让玩家去做与你的游戏本身风格不同的尝试.同时也是让玩家之间比较各自的游戏进度会是一个很容易的事.

比如你可以解锁 `gpg.GameServices.Achievements.Unlock`, 增加 `gpg.GameServices.Achievements.Increment`, 提示 `gpg.GameServices.Achievements.Reveal` 成就.

更多信息请参见: [Achievements 文档](https://developers.google.com/games/services/common/concepts/achievements)

### Leaderboards

游戏排行榜是一个有趣的方式来驱动你的玩家之间竞争, 游戏中资深的玩家会想在公共榜的榜首, 更多的普通玩家就会想与他们的朋友之间比较。

比如，有取排行榜的接口 `gpg.GameServices.Leaderboards.Fetch`, 有以页的形式取玩家分数的接口 `gpg.GameServices.Leaderboards.FetchScorePage`, 等.

更多信息请参见: [Leaderboards 文档](https://developers.google.com/games/services/common/concepts/leaderboards)

### Saved Games

Saved Games服务给你一个方便的方式来保存玩家的比赛进展到谷歌的服务器。你的游戏可以检索已保存的游戏数据允许玩家从任何设备在他们最后的保存点继续游戏。Saved Games服务可以同步一个玩家的游戏数据跨多个设备。

更多信息请参见: [Saved Games 文档](https://developers.google.com/games/services/common/concepts/savedgames)

### Real-time multiplayer

您的游戏可以使用Google Play游戏服务中的实时多人API，在单个游戏会话中将多个玩家连接在一起，并在连接的玩家之间传输数据消息。使用实时多人API可以帮助简化您的游戏开发工作，因为API代表您处理以下任务：

* 管理网络连接以创建和维护实时多人游戏室（虚拟构造，实现在同一游戏会话中的多个玩家之间的网络通信，并且允许玩家彼此直接发送数据）。
* 提供选择用户界面, 邀请玩家加入房间，随机寻找玩家进行自动匹配，或两者的组合。
* 在实时多人游戏的生命周期内，在Google Play游戏服务服务器上存储参与者和房间状态信息。
* 向玩家发送房间邀请和更新。通知会显示在玩家登录的所有设备上（除非已禁用）。

更多信息请参见: [Real-time Multiplayer 文档](https://developers.google.com/games/services/common/concepts/realtimeMultiplayer)

### Turn-based multiplayer

在基于回合的多人游戏中，在多个玩家之间传递共享一个状态，并且在一个回合中只有一个玩家具有修改共享状态的许可。 玩家根据由游戏确定的游戏顺序异步轮流。 您的游戏可以使用Google Play游戏服务提供的回合制多人API来管理以下任务：

* 邀请玩家加入回合制多人游戏比赛，随机寻找玩家与您的游戏匹配，或两者的组合。 Google Play游戏服务可让您在比赛中最多容纳8位参与者。
* 将参与者和匹配状态信息存储在Google服务器上，并在基于回合的匹配生命周期内与所有参与者异步分享更新的匹配数据。
* 发送匹配邀请并向玩家发送通知。 通知会显示在玩家登录的所有设备上（除非禁用）。

更多信息请参见: [Turn-based Multiplayer 文档](https://developers.google.com/games/services/common/concepts/turnbasedMultiplayer)

### Player Statistics

获取和设置各种玩家相关数据。例如，取得当前登录的玩家的信息 “gpg.GameServices.Players.FetchSelf”，或由id来匹配的玩家信息 “gpg.GameServices.Players.Fetch”。此外，玩家统计可以获得一些有趣的信息，例如玩家的平均会话长度，上次玩的天数或他在游戏上购买的数量。
更多信息请参见: [Player Stats 文档](https://developers.google.com/games/services/cpp/stats)


### Events and Quests

Google Play Game 事件服务允许你收集玩家在游戏中的数据并存储在Google的服务器中分析。 你可以灵活地定义你的游戏应该收集什么玩家数据; 这可能包括以下指标：

* 玩家使用特定的项目
* 玩家达到一定水平
* 玩家执行一些特定的游戏动作

您可以根据事件数据的反馈来决定如何改进您的游戏。 例如，您可以调整游戏中某些级别的难度级别，玩家发现太难以完成。

例如，你可以接受一个任务`gpg.GameServices.Quests.Accept`或在一个任务上声明里程碑`gpg.GameServices.Quests.AcceptMilestone`。

更多信息请参见: [Events and Quests 文档](https://developers.google.com/games/services/common/concepts/quests)

### Nearby Connections

Nearby Connections可以让你的游戏有本地多人和屏幕投射功能.
更多信息请参见: [Nearby 文档](https://developers.google.com/games/services/cpp/nearby)
