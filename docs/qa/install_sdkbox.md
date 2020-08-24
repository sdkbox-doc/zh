[&#171; SDKBOX Home](http://sdkbox.com)

<h1>安装SDKBox</h1>

SDKBox 是可以分成安装器与插件两部分, 插件部分是运行在手机端, 也就是开发者最后的应用中, 安装器部分是将插件集成到开发者工程的工具.
我们在安装器部分提供了两种方式一种是命令行方式(一般称之为 `SDKBox Installer`), 一种是GUI方式(GUI现在是CocosCreator的一个插件, 所以一般称之为 `SDKBox GUI For Creator`).

以下将介绍如何将 `SDKBox Installer` 和 `SDKBox GUI For Creator` 安装到你的电脑中 (Windows, macOS).

## SDKBox Helper (可选)

这是一个帮助工具, 主要是用来方便安装 `SDKBox Installer`, `SDKBox GUI For Creator` (当然, 你可以不使用它, 以下也会提供方式来集成, 以你自己的方式来作选择).

* [SDKBoxHelper Windows](https://github.com/hugohuang1111/sdkboxhelper/releases/download/v0.0.5/sdkboxhelper.exe)
* [SDKBoxHelper Mac](https://github.com/hugohuang1111/sdkboxhelper/releases/download/v0.0.5/sdkboxhelper)

## SDKBox Installer

有如下几个方式, 请选择其中一种即可:

* 在命令行中运行 `sdkboxhelper` 来安装 `SDKBox Installer`
* 在命令行中运行 Python2 脚本 `python -c """import urllib; s = urllib.urlopen('https://raw.githubusercontent.com/sdkbox-doc/en/master/install/install.py').read(); exec(s)"""` 来安装 `SDKBox Installer`
* 手动下载 [SDKBox Installer](http://download.sdkbox.com/installer/v1/sdkbox_installer.zip) 包, 然后解压到 `~/.sdkbox/bin` 路径 (Windows 上路径为 `C:\Users\${UserName}\.sdkbox\bin`), 再添加 `~/.sdkbox/bin` 到环境变量 PATH 即可.

__Note__:

* 安装完成后, 新开一个命令窗口, 运行 `sdkbox -h` 来检查是否安装成功. 在某些时候, 如果环境变量确定已添加, 还是报 `command not find` 之类的错误, 可能需要重启.
* `SDKBox Installer` 是基于 Python 2.7 , 所以请保证 python 2.7 已安装. 命令行中输入 `python --version` 查看.

## SDKBox GUI For Creator

有如下几个方式, 任选其中即可:

* 在命令行中运行 `sdkboxhelper -t creator -p path/to/creator_project` 就可以在 `path/to/creator_project` 这个 creator 工程中安装 SDKBox 插件. (`path/to/creator_project` 应该是你的真实的工程路径)

* 手动下载 `SDKBox GUI For Creator` , [地址](http://sdkbox.anysdk.com/gui/creator/sdkbox-1.4.1.zip)
    - 全局安装: 解压 `SDKBox GUI For Creator` 到 `~/.CocosCreator/packages` (Windows上路径为 `C:\Users\${UserName}\.CocosCreator\packages`)
    - 工程安装: 解压 `SDKBox GUI For Creator` 到 `${CocosCreator Project}/packages`

__Note__:

* Cocos Creator 从版本 1.4.0 到 2.4.1 是内置有 `SDKBox GUI For Creator`, 不需要再安装.

* `SDKBox GUI For Creator` 最终还是会调用 `SDKBox Installer` 来实现安装.

* 如果安装完成后, `扩展` 菜单中没有出现 `SDKBox` 项, 那你可以需要重启 Coocs Creator.

* 安装完成后的目录树应该和以下类似:
```
packages
|--sdkbox
    |--app
    |--main.js
    |--package.json
```

