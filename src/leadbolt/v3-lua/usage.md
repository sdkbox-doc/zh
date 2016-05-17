### 初始化 Leadbolt
修改您的 Lua 代码， 调用 `init()` 初始化插件。初始化可以放在代码的任何位置，但是，必须在使用插件功能之前完成。
```lua
sdkbox.PluginLeadBolt:init()
```

### 缓存广告数据
```lua
sdkbox.PluginLeadbolt:loadModuleToCache("directdeal");
sdkbox.PluginLeadbolt:loadModuleToCache("rewardedvideo");
```
> 提示：LeadBolt 为了更好的用户体验，在使用前它会缓存广告数据。一旦缓存广告数据完成，您将能够看到这个广告。当缓存仍在进行中，广告是不可见的。

### 加载/显示广告
```lua
sdkbox.PluginLeadbolt:loadModule("directdeal");
sdkbox.PluginLeadbolt:loadModule("rewardedvideo");
```

### 判断广告是否缓存完成
```lua
if plugin:isAdReady('directdeal') then
    plugin:loadModule('directdeal')
else
    print('leadbolt ad is not ready')
end
```

### 捕捉 LeadBolt 事件（可选）
该插件允许您捕捉 Leadbolt 广告事件，使您能可以根据返回的内容执行相应的操作。比如在奖励式广告中，onMediaFinished 事件就允许您对看完这个广告的用户进行奖励。
```lua
sdkbox.PluginLeadBolt:setListener(function(args)
	local event = args.event
	if "onModuleLoaded" == event then
	elif "onModuleClosed" == event then
	elif "onModuleClicked" == event then
	elif "onModuleCached" == event then
	elif "onModuleFailed" == event then
	elif "onMediaFinished" == event then
	end
end)
```
