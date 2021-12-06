# 本地使用 SDKBox 的方法

## 简介

有一些工程可能因为各种原因, 需要继续使用 SDKBox. 下面介绍一下, 如何本地使用 SDKBox 安装插件. 

## 步骤

### 下载插件
- 所有已安装过的插件都会在 `~/.sdkbox/plugins` (Windows 上就是类似的个人目录 `%HOME%/.sdkbox/plugins`) .
- 如果有需要, 你也可以预先自己下载插件保留备份.
    1. 浏览网页 `http://download.sdkbox.com/installer/v1/manifest.json`
    2. 用 `bundle` 的值, 替换 `http://download.sdkbox.com/installer/v1/BUNDLE_NAME` 中的 `BUNDLE_NAME`, 就可以得到插件(以 iap 为例)的下载路径, `http://download.sdkbox.com/installer/v1/sdkbox-iap_v2.7.7.0.tar.gz` .
    3. 下载, 备份

### 安装插件

- 在命令行中, 输入 `sdkbox import /local/path/to/plugin -p /project/path`

### 本地安装的例子:

- 安装本地插件到 creator2 的导出工程中

`sdkbox import ~/.sdkbox/plugins/sdkbox-iap_v2.7.7.0 -p ./build/jsb-link`

```bash
hugo@hugodeMacBook-Pro creatorTest % sdkbox import ~/.sdkbox/plugins/sdkbox-iap_v2.7.7.0 -p ./build/jsb-link
  _______ ______  _     _ ______   _____  _     _
  |______ |     \ |____/  |_____] |     |  \___/
  ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright (c) 2016-2020 SDKBOX Inc. v1.4.6.1
 Please reference the online documentation to finish the integration:
http://sdkbox-doc.github.io/en/plugins/iap/v3-js/
 Installation Successful :)
 > Log file = /Users/hugo/.sdkbox/log/sdkbox-log-2021-12-06.sdkbox.temp
```

- 安装本地插件到 creator3 的导出工程中

`sdkbox import /Users/hugo/Downloads/sdkbox-iap_v2.7.7.0.tar.gz -p /Users/hugo/Documents/work/t/creator3Test --nohelp`

```bash
hugo@hugodeMacBook-Pro cocos2dxTest % sdkbox import /Users/hugo/Downloads/sdkbox-iap_v2.7.7.0.tar.gz -p /Users/hugo/Documents/work/t/creator3Test --nohelp
  _______ ______  _     _ ______   _____  _     _
  |______ |     \ |____/  |_____] |     |  \___/
  ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright (c) 2016-2020 SDKBOX Inc. v1.4.6.1
 > Log file = /Users/hugo/.sdkbox/log/sdkbox-log-2021-12-06-4.sdkbox.temp
```

- 安装本地插件到 cocos2dx 的工程中

`sdkbox import ~/.sdkbox/plugins/sdkbox-admob_v2.7.6.1 -p .`

```bash
hugo@hugodeMacBook-Pro cocos2dxTest % sdkbox import ~/.sdkbox/plugins/sdkbox-admob_v2.7.6.1 -p .
  _______ ______  _     _ ______   _____  _     _
  |______ |     \ |____/  |_____] |     |  \___/
  ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright (c) 2016-2020 SDKBOX Inc. v1.4.6.1
 Please reference the online documentation to finish the integration:
http://sdkbox-doc.github.io/en/plugins/admob/v3-cpp/

  1. iOS:
  > Replace `ca-app-pub-3940256099942544~1458002511` with `proj.ios_mac/ios/Info.plist` file;
  > Replace `ca-app-pub-3940256099942544~1458002511` with your publish id with `sdkbox_config.json` file;

  2. Android:
  > Replace `ca-app-pub-3940256099942544~3347511713` with your publish id with `AndroidManifest.xml` file;
  > Replace `ca-app-pub-3940256099942544~3347511713` with your publish id with `sdkbox_config.json` file;

 Installation Successful :)
 > Log file = /Users/hugo/.sdkbox/log/sdkbox-log-2021-12-06-3.sdkbox.temp
```

