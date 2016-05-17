### 初始化 Share
修改您的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```lua
sdkbox.PluginShare:init()
```

### 分享
在初始化之后，您可以开始使用 Share 插件的功能。在任何您想使用分享功能的地方调用 `share` 方法：
```lua
local shareInfo = {}
shareInfo.text = '#sdkbox(www.sdkbox.com) - the cure for sdk fatigue - from lua - '
shareInfo.title = "sdkbox";
shareInfo.image = "http://www.sdkbox.com/assets/images/logo.png";
shareInfo.link = "http://www.sdkbox.com";

//sdkbox.SocialPlatform.Platform_Select will show platforms list, let user select which platform want to share
//sdkbox.SocialPlatform.Platform_Twitter will share with twitter directly
//sdkbox.SocialPlatform.Platform_Facebook will share with facebook directly
shareInfo.platform = sdkbox.SocialPlatform.Platform_Select;
plugin:share(shareInfo)
```

所有 sdkbox.SocialPlatform 的可用值如下：

- Platform_Unknow
- Platform_Twitter
- Platform_Facebook
- Platform_Select
- Platform_All


所有 sdkbox.SocialShareState 的可用值如下：

- SocialShareStateNone
- SocialShareStateUnkonw
- SocialShareStateBegin
- SocialShareStateSuccess
- SocialShareStateFail
- SocialShareStateCancelled
- SocialShareStateSelectShow
- SocialShareStateSelected
- SocialShareStateSelectCancelled


### 捕获 Share 事件（可选）
该插件允许您捕获 `Share` 事件以帮助您根据返回的内容进行相应的操作。一个简单的例子如下：
```lua
local plugin = sdkbox.PluginShare
plugin:setListener(function(responsed)
	local event = responsed.event

    dump(responsed, "PluginShare share listener info:")
    if responsed.response.state == sdkbox.SocialShareState.SocialShareStateSuccess then
        print('share success')
    end

end)
plugin:init()
```
