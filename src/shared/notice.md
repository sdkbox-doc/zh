
<!--
## ~~从 China 服务器下载~~ 服务器已停止
如果你在中国, 并且下载插件的速度比较慢, 可以尝试使用位于中国的服务器来下载, 查询插件, 使用方法为在你的 `sdkbox import` 后加 `--server china` 及可, 比如:
```bash
sdkbox import xxx  --server china
```
xxx 为你的插件名字
-->

## 重点注意事项
如果您升级到了 Xcode7, 则需要以下额外步骤来确保插件工作正常:

#### 禁用应用程序安全传输策略
添加以下项到 plist:
```
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```
添加后的文件内容看起来就像这样：

![](../../imgs/ATS.png)


#### 禁止 Bitcode 支持
您必须禁止 __Bitcode__ 的支持，否则将会编译失败。

#### 游戏全屏配置
如果您的游戏不同时支持横竖屏，则必须在 Xcode 中选中 `Requires full screen`，否则将不会通过 Apple 的审核。

#### canOpenURL 白名单
取决于您使用哪些插件。需要在 `info.plist` 的 `LSApplicationQueriesSchemes` 下添加名单。
