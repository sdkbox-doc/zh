### 初始化 Bee7
修改您的lua代码用 `init()` 初始化插件. 这个可以在任何地方调用,但是必须在您要想使用 Bee7 的功能之前.
```lua
sdkbox.PluginBee7:init();
```

### 使用 Bee7
#### 显示 Game Wall
```lua
sdkbox.PluginBee7:showGameWall()
```

### 接收 Bee7 事件 (可选)

```lua
sdkbox.PluginBee7:setListener(function(args)
    dump(args)
    if args.name == "onAvailableChange" then
    elseif args.name == "onVisibleChange" then
    elseif args.name == "onGameWallWillClose" then
    elseif args.name == "onGiveReward" then
    end
end)
```
