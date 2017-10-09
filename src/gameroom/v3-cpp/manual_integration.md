### 手动集成

如果你想手动集成 Gameroom 插件，你需要一步步的完成下列多种配置。这些步骤比较复杂，我们并不推荐你手动集成插件。

1.  找到 Visual Studio Solution 文件并且打开它。对于被 `cocos` 创建的 Cpp 工程，你可以在 `./proj.win32` 子目录下找到这个文件。为了便于下面的描述，我们将 `proj.win32` 这个目录命名为**项目目录**。

2.  解压 Gameroom 插件包，你会得到一个目录，我们把这个目录称作**插件目录**。

3.  拷贝头文件。对于 Cpp 工程，你需要拷贝**插件目录**下的 `win32/include/*.h` 文件到**项目目录**的 `include` 文件夹下。

4.  拷贝**插件目录**下的 `win32/libs/*.lib` 库文件到**项目目录**下的 `libs` 文件夹下。 

5.  部署 Facebook Gameroom SDK 文件。

    a.  拷贝**插件目录**下的 `sdk/fbg` 头文件目录到你的**项目目录**下的 `include` 子文件夹下。 

    b.  拷贝**插件目录**下的 `sdk/libs/*.lib` 库文件到你的**项目目录**下的 `libs` 子文件夹下。

6.  修改 Visual Studio 配置：

    a.  为编译器添加头文件目录，依次单击：项目 -> 属性 -> 配置属性 -> VC++ 目录 -> 包含目录 （单击编辑，添加新项）。

    然后添加 `$(solutiondir)include` 。

    b.  添加库文件目录，依次单击：项目 -> 属性 -> 配置属性 -> VC++ 目录 -> 库目录（单击编辑，添加新项）。

    然后添加 `$(solutiondir)libs` 。

    c.  链接库文件，依次单击：项目 -> 属性 -> 配置属性 -> 链接器 -> 输入 -> 附加依赖项 （单击编辑，添加新项）。

    然后添加 `GameroomPlugin32.lib` 以及 `LibFBGPlatform32.lib` 。

    **对于 `debug` 版本，请添加 `GamerommPlugin32.debug.lib`** 。

7.  打开**项目目录**子文件夹 `/Classes` 中的 `AppDelegate.cpp` 文件，准备为其打代码补丁。

8.  **接下来打补丁的步骤也可以使用 `patch` 工具完成**。对于 Cpp 工程，请使用**插件目录**下的 `AppDelegate.cpp3.15.patch` 文件。

```
patch AppDelegate.cpp ./plugin-dir/path/AppDelegate.cpp3.15.patch
```

-   在 `USING_NS_CC` 之前，添加 SDKBOX 头文件：

```
#ifdef SDKBOX_ENABLED
#include "PluginGameroom.h"
#endif
```

-   在 `AppDelegate` 类的构造与析构函数里，重定向 STDOUT 至一个文件，因为 Facebook SDK 没有提供任何 log API 。 

```
AppDelegate::AppDelegate()
{
    freopen("fbg.log", "w", stdout);
}
AppDelegate::~AppDelegate()
{
    ...
    fclose(stdout);
}
```

-   在函数 `applicationDidFinishLaunching` 开始，初始化 SDKBOX Gameroom 插件：

```
#ifdef SDKBOX_ENABLED
    sdkbox::PluginGameroom::init("your_app_id");
#endif
```

-   在条件语句 `if (!glview)` 之后，添加以下代码：

```
#if (CC_TARGET_PLATFORM == CC_PLATFORM_WIN32) || (CC_TARGET_PLATFORM == CC_PLATFORM_MAC) || (CC_TARGET_PLATFORM == CC_PLATFORM_LINUX)
    const wchar_t title[]{ L"Facebook Gameroom" };
    auto parentWin = FindWindow(NULL, title);

    // set dpi for app.
    auto res_dpi = SetProcessDPIAware();

    RECT rect;
    GetWindowRect(parentWin, &rect);
    glview = GLViewImpl::createWithRect("cocos_sample_cpp", Rect(0, 0, rect.right - rect.left - 20, rect.bottom - rect.top - 100), 1.0f, true);
    director->setOpenGLView(glview);
    auto currentWin = Director::getInstance()->getOpenGLView()->getWin32Window();
    SetParent(currentWin, parentWin);
#else
    glview = GLViewImpl::create("cocos_sample_cpp");
    director->setOpenGLView(glview);
#endif
```

