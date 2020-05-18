### 初始化 HMS
在您的工程中合适的地方初始化插件.我们推荐在 `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()` 中.确保包含了相关的头文件:
```cpp
#include "PluginHMS/PluginHMS.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::HMS::init();
}
```

### 登录

HMS 提供了三种登录方式:

* Signing In with HUAWEI ID(ID Token)

```cpp
sdkbox::HMS::login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```cpp
sdkbox::HMS::login(2);
```

* Silently Signing In With HUAWEI ID

静默登录只能在上一次使用前两种方式已经登录成功的情况下，才能在静态登录下成功

```cpp
sdkbox::HMS::login(0);
```

> 以上三种登录方式, 不管成功还是失败, 最终都会触发 `onLogin` 事件.

HMS 帐号相关的 [文档](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### 登出

```
sdkbox::HMS::logout();
```

### 处理HMS事件
允许您接收 `HMS` 的事件.

* 继承这个类 `sdkbox::HMSListener`:
```cpp
    #include "PluginHMS/PluginHMS.h"
    class MyClass : public sdkbox::HMSListener
    {
    private:
        virtual void onLogin(int code, const std::string & msg) override;
    }
```

* 创建一个监听类来接收回调事件:
```cpp
sdkbox::HMS::setListener(listener);
```
