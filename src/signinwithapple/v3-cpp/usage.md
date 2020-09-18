### 初始化 SignInWithApple
在您的工程中合适的地方初始化插件.我们推荐在 `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()` 中.确保包含了相关的头文件:
```cpp
#include "PluginSignInWithApple/PluginSignInWithApple.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginSignInWithApple::init();
}
```

### 登录

Signing In with Apple

```cpp
sdkbox::PluginSignInWithApple::sign();
```

如果用户已经登录, 可以在应用启动时调用

```cpp
sdkbox::PluginSignInWithApple::signWithExistingAccount();
```

### 处理SignInWithApple事件
允许您接收 `SignInWithApple` 的事件.


* 继承这个类 `sdkbox::PluginSignInWithAppleListener`:
```cpp
#include "PluginSignInWithApple/PluginSignInWithApple.h"
class MyClass : public sdkbox::PluginSignInWithAppleListener
{
private:
  void onAuthorizationDidComplete(const std::string& authInfo) override;
  void onAuthorizationCompleteWithError(const std::string& authInfo) override;
  void onAuthorizationStatus(const std::string& authState) override;
}
```

* 创建一个监听类来接收回调事件:
```cpp
sdkbox::PluginSignInWithApple::setListener(listener);
```
