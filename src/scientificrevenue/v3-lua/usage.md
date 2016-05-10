### 请参考 Scientific Revenue 官方文档

https://documentation.scientificrevenue.com/sdkbox-cocos2d-x/

官方联系邮箱 ted@scientificrevenue.com

### 初始化插件
```lua
sdkbox.ScientificRevenue:init()
```

### 设置定价会话参数
```lua
sdkbox.ScientificRevenue:sessionOptions(true, "en_US", true)
```

### 开始会话
```lua
sdkbox.ScientificRevenue:startSession("UserName");
```
