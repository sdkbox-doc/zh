## 游戏存档

SDKBoxPlay 支持 iOS/Google的游戏云存档功能. 开发者可以使用此接口存储用户的游戏数据.

### iOS 云存储

* 玩家自己的 iCloud 帐号必须是开启状态
* 开发者在对应的工程的必须把 iCloud [打开](https://developer.apple.com/library/content/documentation/DataManagement/Conceptual/CloudKitQuickStart/EnablingiCloudandConfiguringCloudKit/EnablingiCloudandConfiguringCloudKit.html#//apple_ref/doc/uid/TP40014987-CH2-SW2)

### 用法

#### 加载所有的游戏数据

```cpp
sdkbox::PluginSdkboxPlay::loadAllData();
```

#### 加载某一项游戏数据

```cpp
sdkbox::PluginSdkboxPlay::loadGameData("key2");
```

#### 保持数据

```cpp
sdkbox::PluginSdkboxPlay::saveGameData("key1", "{\"game_name\": \"sdkbox go\", \"stage\": 3}");
```

iOS 存档[官方文档](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/GameKit_Guide/SavedGames/SavedGames.html)

Android 存档[官方文档](https://developers.google.com/games/services/common/concepts/savedgames)
