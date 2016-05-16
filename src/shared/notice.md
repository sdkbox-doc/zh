## 重点注意事项
如果您升级到了 Xcode7, 则需要以下额外步骤来确保插件工作正常:

#### 禁用应用程序安全传输
添加以下项到 plist:
```
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```
#### 禁止 Bitcode 支持
您必须禁止 __Bitcode__ 的支持，否则将会编译失败

#### 游戏全屏配置
如果您的游戏不同时支持横竖屏，则必须在 Xcode 中选中 `Requires full screen`，否则将不会通过 Apple 的审核.

#### canOpenURL 白名单
取决于您使用哪些插件。需要在 `info.plist` 的 `LSApplicationQueriesSchemes` 下添加名单.
