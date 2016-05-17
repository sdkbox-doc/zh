### 初始化 Youtube
* 修改您的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```lua
sdkbox.PluginYoutube:init()
```

### 播放视频
用一个 youtube 视频 id 播放 youtube 视频，比如：

```lua
sdkbox.PluginYoutube:playVideo("cdgQpa1pUUE", 0, true, true);
```

### 播放多段视频
有两种方法可以让您播放多段 youtube 视频

您可以像这样直接播放一个播放列表：
```lua
sdkbox.PluginYoutube:playVideo("cdgQpa1pUUE", 0, true, true);
```

也可以像这样建立一个数组保存多段视频并且播放它们：
```lua
v = {"cdgQpa1pUUE","8aCYZ3gXfy8"};

sdkbox.PluginYoutube.playVideoList(v, 0, 0, true, true);
```

### 实现 YoutubeListener
* 您可以实现 YoutubeListener 用来设置回调，比如当一个视频播放完成的时候。
```lua

sdkbox.PluginYoutube.setListener(function(name, args)
    if "onPlayEnds" == name then
      print("Video Finished")
    end
end)

```
