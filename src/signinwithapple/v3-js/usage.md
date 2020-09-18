### 初始化 SignInWithApple
* 在您的代码合适的地方调用 `init()` 完成初始化. 我们推荐在 `app.js` 中完成初始化.比如:
```javascript
sdkbox.PluginSignInWithApple.init();
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 包含如下头文件:
```javascript
#include "PluginSignInWithAppleJS.hpp"
#include "PluginSignInWithAppleJSHelper.h"
```

* 修改 `./frameworks/runtime-src/Classes/AppDelegate.cpp` 确保调用了如下函数:
```javascript
sc->addRegisterCallback(register_all_PluginSignInWithAppleJS);
sc->addRegisterCallback(register_all_PluginSignInWithAppleJS_helper);
```

### 初始化 SignInWithApple
修改您的 js 代码去初始插件, 初始化可以在任何地方来做,但是必须要在您想使用插件的功能之前.
```javascript
sdkbox.PluginSignInWithApple.init()
```

### 登录

登录

```javascript
sdkbox.PluginSignInWithApple.sign();
```

如果用户已经登录过，可以在应用启动时，调下如下:

```javascript
sdkbox.PluginSignInWithApple.signWithExistingAccount();
```

### 处理SignInWithApple事件
您可以接收 `SignInWithApple` 事件, 不同事件对您的用户及 SignInWithApple 服务器做不同的处理.

```javascript
sdkbox.PluginSignInWithApple.setListener({
    onAuthorizationDidComplete: function(authInfo) {},
    onAuthorizationCompleteWithError: function(authInfo) {},
    onAuthorizationStatus: function(authState) {},
});
```
