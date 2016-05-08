### 注册 Javascript 函数
You need to register all the Youtube JS functions with cocos2d-x before using them.
您需要在使用之前，在 cocos2d-x 中注册所有的 Youtube JS 函数。

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，包含下列头文件：
```cpp
#include "PluginYoutubeJS.hpp"
#include "PluginYoutubeJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 文件，添加如下内容：
```cpp
sc->addRegisterCallback(register_all_PluginYoutubeJS);
sc->addRegisterCallback(register_all_PluginYoutubeJS_helper);
```

### 初始化 Youtube
* 通过在您的代码合适的位置调用 `init()` 方法来初始化这个插件。我们建议您在 `app.js` 中进行初始化。举例如下：
```javascript
sdkbox.PluginYoutube.init();
```

### 播放视频
用一个 youtube 视频 id 播放 youtube 视频，比如：

```javascript
sdkbox.PluginYoutube.playVideo("cdgQpa1pUUE", 0, true, true);
```

### 播放多段视频
有两种方法可以让您播放多段 youtube 视频

您可以像这样直接播放一个播放列表：
```javascript
sdkbox.PluginYoutube.playPlayList("7E952A67F31C58A3", 0, 0, true, true);
```

也可以像这样建立一个数组保存多段视频并且播放它们：
```javascript
var v = ["cdgQpa1pUUE","8aCYZ3gXfy8"];

sdkbox.PluginYoutube.playVideoList(v, 0, 0, true, true);
```

### 实现 YoutubeListener
* 您可以实现 YoutubeListener 用来设置回调，比如当一个视频播放完成的时候。
```javascript

sdkbox.PluginYoutube.setListener({
    onPlayEnds : function() { cc.log("Video finished playing");}
})

```
