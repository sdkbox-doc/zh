[&#171; SDKBOX Home](http://sdkbox.com)

<h1>Gameroom Plugin</h1>

## 前言
Facebook Gaemroom 是一个基于 **Windows** 的游戏娱乐平台，提供了数千种游戏下载以及丰富多彩的玩家社区，并且还提供游戏发行等服务。

Gameroom SDK 是官方提供的让游戏开发者接入 Gameroom 的 SDK， 但现在该 **SDK 仍然处于 Beta** 状态。

SDKBOX 为了更好的服务于广大游戏开发者，率先提供了对于 Gameroom SDK的封装，推出了 SDKBOX Gameroom Plugin，实现了对这一 SDK API 接口的统一以及优化，更便于集成至 Cocos2d-x 以及其他引擎。 

## 集成指南

### 与 Cocos2d-x 3.x 版本集成
*   [The C++ version](./v3-cpp.md)
*   [The Javascript version](./v3-js.md)

### 与 Cocos Creator 集成
<!--*   [Integration with Cocos Creator](./v3-cc)-->

>   Cocos Creator 现在还没有真正发布支持 Gameroom Plugin 的版本，但是 beta 测试已经在顺利进行中，不久将会发布正是支持该插件的版本。


## 样例工程

[A demo project on github](https://github.com/sdkbox/sdkbox-sample-gameroom)

## 已完成的功能

现在，SDKBOX Gameroom Plugin 已经完成了下列功能：

*   user login
*   *feed shared (function test normally but the returned value is always 0)*
*   IAP
    *   IAP with product ID
    *   IAP with a URL link
    *   *purchase premium version or license (function test failed in Gameroom SDK)*
*   *App Events (crash in Gameroom SDK when no user login)*
*   App Request
    *    send requests to fixed person
    *    send requests to chosen person via a Facebook dialog

>   用斜体标明的功能是仍然存在问题的功能，已经向 Facebook 反馈，并请求帮助。


