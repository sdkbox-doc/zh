# SDKBOX: 用安装器来安装sdkbox插件

## 准备运行 SDKBOX 安装器
在你能运行 SDKBOX 安装吕之前,你需要做下面几件事
* 确认你下载的 SDKBOX 安装器所在的路径 (你可以把安装器放在`/usr/local/bin`).
* 确认你下载的 SDKBOX 插件所在的路径.

## 用 SDKBOX 安装器安装一个插件
现在准备好去安装插件了吗?让我们开始吧!

### 在 Mac OS X 上安装
* 在命令行中, `cd` 到你的工程的根目录. 比如:
```sh
cd ~/MyGame
```

* 现在,您可以使用SDKBOX安装插件安装程序,注意你放置的位置安装程序和插件包. 比如:
```sh
sdkbox import iap
```

### What Next?
SDKBOX 安装程序 处理了大部分集成流程。然而,仍然有一些手动步骤,您必须完成。安装程序运行后输出一些你还需要完成的步骤,在插件的PDF有详细说明。比如运行上面的命令后,会得到如下结果:
```sh
$ sdkbox import iap
_______ ______  _     _ ______   _____  _     _
|______ |     \ |____/  |_____] |     |  \___/
______| |_____/ |    \_ |_____] |_____| _/   \_
Copyright (c) 2015 Chukong Technologies Inc. v0.5.7

Please reference the online documentation to finish the integration:
http://sdkbox-doc.github.io/en/plugins/iap/v3-cpp/
Installation Successful :)
```

### 安装器的其它命令参数.
 SDKBOX 安装器还有几种其它命令你可以用.你可以直接运行 `sdkbox` 或者带 `-h` 参数:
```sh
$ <path>/sdkbox
_______ ______  _     _ ______   _____  _     _
|______ |     \ |____/  |_____] |     |  \___/
______| |_____/ |    \_ |_____] |_____| _/   \_
Copyright (c) 2015 Chukong Technologies Inc. v0.5.7

usage: sdkbox [-h] [-v] [-p PROJECT] [-b PLUGIN] [--yes] [--dryrun]
              {import,restore,symbols,api}
```

| switch  | alternate switch  | what it does |
| :------------ |---------------:| :-----|
| -h      | --help          |show this help message and exit |
| -v      | --verbose       |specify verbosity level |
| -p PROJECT | --project PROJECT |path to project root (defaults to .) |
| -b PLUGIN | --plugin PLUGIN |specify path to plugin (defaults to .) |
|         | --dryrun        |test install before performing. |

### 保持一直使用的是最新版
SDKBOX安装程序自动检查更新.更新之前它会询问您的许可.这将允许你还保持当前版本或更新到最新版.
```sh
_______ ______  _     _ ______   _____  _     _
|______ |     \ |____/  |_____] |     |  \___/
______| |_____/ |    \_ |_____] |_____| _/   \_
Copyright (c) 2015 Chukong Technologies Inc. v0.5.6

A newer version of SDKBOX is available, would you like to update to v0.5.7?
Please type Yes, No or Quit Yes
updated SDKBOX v0.5.6 to v0.5.7 at sdkbox
```
