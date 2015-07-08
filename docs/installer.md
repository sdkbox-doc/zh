
# SDKBOX 安装介绍

## 安装
__SDKBOX__ 提供了mac, windows版的命令行安装程序,你可以在cocos store中搜索 `sdkbox` ,并下载它

对于 `mac` 用户,推荐你把 __SDKBOX__ 安装程序放在 `/usr/local/bin` 目录下
对于 `windows` 用户,推荐你把 __SDKBOX__ 安装程序所在的目录加到系统环境变量中

为了叙述方便,下文中用 __SDKBOX__ 指代 __SDKBOX__ 安装器,


## 安装插件到工程中

### 安装到mac工程中
* 在命令行中, `cd` 到你的工程所在目录. 比如:
```
cd ~/MyGame
```

* 运行以下命令把IAP把集成到你的工程中,sdkbox会自动下载对应插件并安装到你的工程中
```
<path>/sdkbox import -b iap
```

### 安装到windows工程中
* 在命令行中, `cd` 到你的工程所在目录. 比如:
```
cd ~/MyGame
```

* 运行以下命令把IAP把集成到你的工程中,sdkbox会自动下载对应插件并安装到你的工程中
```
<path>/sdkbox.exe import -b iap
```

## 代码修改
插件安装好后,就可以参照插件的pdf文件调用 SDKBOX 接口, 同时 __SDKBOX__ 也会在命令行给出开发者需要修改的地方,命令行输出可能像以下这样:

```
$ sdkbox -b ../sdkbox-iap_cpp_v1.1/ import
 _______ ______  _     _ ______   _____  _     _
 |______ |     \ |____/  |_____] |     |  \___/
 ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright © 2015 Chukong Technologies Inc. v0.1

 Remaining Manual Steps:
 Android Integration:
 Step 2.5 - modify Cocos2dxActivity.java
 Step 2.5 - modify YourGameName.java
 Cocos2d-JS specific
 Step 3.2 - add appropriate headers for this plugin to your class.
 Step 3.2 - add appropriate call to initialize the Javascript callbacks.
 Step 3.2 - call sdkbox.IAP.init(); where appropriate in your code. We recommend to do this in the app.js
 Installation Successful :)
```

## __SDKBOX__ 更多用法
更多用法可以运行 `sdkbox -h`

```
$ <path>/sdkbox
 _______ ______  _     _ ______   _____  _     _
 |______ |     \ |____/  |_____] |     |  \___/
 ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright © 2015 Chukong Technologies Inc. v0.1

usage: sdkbox [-h] [-v] [-p PROJECT] [-b PLUGIN] [--yes] [--dryrun]
              {import,restore,symbols,api}
```

| switch  | alternate switch  | what it does |
| :------------ |---------------:| :-----|
| -h      | --help          |显示帮助信息 |
| -v      | --verbose       |显示更全的信息 |
| -p PROJECT | --project PROJECT |要集成的工程的根目录 (defaults to .) |
| -b PLUGIN | --plugin PLUGIN |插件的名字 (defaults to .) |
|         | --dryrun        |test install before performing. |

## 更新
__SDKBOX__ 可以自动检查更新,当有新版本时,会询问你是否要更新,比如可能会以下像这样:

```
 _______ ______  _     _ ______   _____  _     _
 |______ |     \ |____/  |_____] |     |  \___/
 ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright © 2015 Chukong Technologies Inc. v0.1

A newer version of SDKBOX is available, would you like to update to v0.5?
Please type Yes, No or Quit Yes
updated SDKBOX v0.1 to v0.5 at sdkbox
```
