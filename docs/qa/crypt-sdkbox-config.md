# 保护你的 sdkbox_config.json 文件

## 前提条件
- 插件版本 >= 2.4.1.1
- sdkbox 命令行 >= 1.0.2.2

## SDKBox 内置的保护措施

### 1. 加密 sdkbox_config.json

```bash
# 加密
sdkbox encrypt -i sdkbox_config.json -o sdkbox_config.json --key your_key

# 解密
sdkbox decrypt -i sdkbox_config.json -o sdkbox_config.json --key your_key
```

### 2. 设置秘钥

```c++
// AppDelegate.cpp
#include <sdkbox/Sdkbox.h>


sdkbox::init("", "your_key"); // 第一个参数必须为空 ""
sdkbox::IAP::init();
sdkbox::PluginAdMob::init();
```

## 自己加密方案

```c++
// AppDelegate.cpp
#include <sdkbox/Sdkbox.h>

std::string content = __decrypt__("your_encrypt_content");
sdkbox::setConfig(content); // @content 为未加密的 'sdkbox_config.json' 内容
sdkbox::IAP::init();
sdkbox::PluginAdMob::init();
```


## 使用 Cocos Creator 的保存措施

基本思路: `Cocos Crator` 本身是提供 JS 源码的加密支持的. 但是对 Cocos2dx 引擎的 Res 目录并没有加密, 而 sdkbox_config.json 就是放在不会加密的 Res 目录下的. 所以我们需要把 sdkbox_config.json 移到 Creator 工程的 assert 目录, 并把 sdkbox_config.json 变为一个 js 文件. 然后在开发代码中 require 这个 js 文件, 再把它传给 sdkbox .

具体步骤如下:

* 修改 `AppDelegate.cpp` , 如下:

```cpp
...
#include "SDKBoxJSHelper.h"
...

bool AppDelegate::applicationDidFinishLaunching()
{
    ...

    jsb_register_all_modules();
    se->addRegisterCallback(register_all_SDKBoxJS_helper);

    ...

    return true;
}

```

* 把 `jsb-link/res/sdkbox_config.json` 移动并改名为 `assets/SDKBox/sdkbox_config.js`.
* 在 `assets/SDKBox/sdkbox_config.js` 第一行加入 `module.exports =` 语句

```js
module.exports =
{
    "android": {
        "iap": {
            ...
        }
        ...
    },
    "ios": {
        "iap": {
            ...
        }
        ...
    }
}

```

* 在开发代码中加载 sdkbox_config.js , 并把值传给sdkbox

```js
const sdkbox_config = require('../SDKBox/sdkbox_config')
...
sdkbox.setConfig(JSON.stringify(sdkbox_config)); // 在插件初始化之前调用
...
sdkbox.PluginXXX.init();
...
```
