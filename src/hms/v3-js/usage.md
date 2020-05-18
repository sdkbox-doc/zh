### 初始化 HMS
* 在您的代码合适的地方调用 `init()` 完成初始化. 我们推荐在 `app.js` 中完成初始化.比如:
```javascript
sdkbox.HMS.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```cpp
#include "PluginHMSJS.hpp"
#include "PluginHMSJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保调用了如下函数:
```cpp
sc->addRegisterCallback(register_all_PluginHMSJS);
sc->addRegisterCallback(register_all_PluginHMSJS_helper);
```

### 登录

HMS 提供了三种登录方式:

* Signing In with HUAWEI ID(ID Token)

```javascript
sdkbox.HMS.login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```javascript
sdkbox.HMS.login(2);
```

* Silently Signing In With HUAWEI ID

静默登录只能在上一次使用前两种方式已经登录成功的情况下，才能在静态登录下成功

```javascript
sdkbox.HMS.login(0);
```

> 以上三种登录方式, 不管成功还是失败, 最终都会触发 `onLogin` 事件.

HMS 帐号相关的 [文档](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### 登出

```javascript
sdkbox.HMS.logout();
```

### 处理HMS事件
您可以接收 `HMS` 事件, 不同事件对您的用户及 HMS 服务器做不同的处理.
```javascript
sdkbox.HMS.setListener({
    onLogin : function (code, msg) {
        // login event
    }
});
```
