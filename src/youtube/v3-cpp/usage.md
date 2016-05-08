### 初始化 Youtube
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下：
```cpp
#include "PluginYoutube/PluginYoutube.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginYoutube::init();
}
```

### 播放视频
用一个 youtube 视频 id 播放 youtube 视频，比如：

```cpp
sdkbox::PluginYoutube::playVideo("cdgQpa1pUUE", 0, true, true);
```
这段代码将播放下列 youtube 视频：
https://www.youtube.com/watch?v=cdgQpa1pUUE

### 播放多段视频
有两种方法可以让您播放多段 youtube 视频

您可以像这样直接播放一个播放列表：
```cpp
sdkbox::PluginYoutube::playPlayList("7E952A67F31C58A3", 0, 0, true, true);
```

也可以像这样建立一个 vector 保存多段视频并且播放它们：
```cpp
std::vector<std::string> v;
v.push_back( "cdgQpa1pUUE" );
v.push_back( "8aCYZ3gXfy8" );
v.push_back( "cdgQpa1pUUE" );

sdkbox::PluginYoutube::playVideoList(v, 0, 0, true, true);
```

### 实现 YoutubeListener
* 您可以实现 YoutubeListener 用来设置回调，比如当一个视频播放完成的时候。
```cpp
#include "PluginYoutube/PluginYoutube.h"
class MyClass : public sdkbox::YoutubeListener
{
private:
  void onPlayEnds( bool played_ok );
}
```
