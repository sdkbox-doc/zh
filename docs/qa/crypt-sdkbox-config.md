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


