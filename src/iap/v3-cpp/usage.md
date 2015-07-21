### 初始化 IAP
在你的工程中合适的地方初始化插件.我们推荐在 `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()` 中.确保包含了相关的头文件:
```cpp
#include "PluginIAP/PluginIAP.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::IAP::init();
}
```

### 获取最新的价格
在你的游戏开始时,最好先从商店中取最新的商品价格信息.

在取最新的 IAP 数据, 只需要简单地调用 `sdkbox::IAP::refresh()`.

> `onProductRequestSuccess` 成功获取会收到这个事件.

> `onProductRequestFailure` 获取失败的话,会收到这个事件.

### 购买
购买只需要调用 `sdkbox::IAP::purchase(name)`

__注意:__ __name__ 是你在配置文件中 `items` 项的值, 而不是你在 iTunes 或 GooglePlay Store 中的商品名.

> `onSuccess` 购买成功会收到这个事件.

> `onFailure` 购买失败事件.

> `onCanceled` 用户取消了购买.

### 恢复购买
恢复购买调用 `sdkbox::IAP::restore()`.

> `onRestored` 恢复购买成功事件.

__注意:__ `onRestored` 可能会被多次触发

### 处理付费事件
允许你接收 `IAP` 的事件,这样你就可以对用户,IAP服务器做不同的处理.

* 继承这个类 `sdkbox::IAPListener`:
```cpp
    #include "PluginIAP/PluginIAP.h"
    class MyClass : public sdkbox::IAPListener
    {
    private:
        virtual void onSuccess(sdkbox::Product const& p) override;
        virtual void onFailure(sdkbox::Product const& p, const std::string &msg)
           override;
        virtual void onCanceled(sdkbox::Product const& p) override;
        virtual void onRestored(sdkbox::Product const& p) override;
        virtual void onProductRequestSuccess(std::vector<sdkbox::Product> const &products)
        override;
        virtual void onProductRequestFailure(const std::string &msg) override;
    }
```

* 创建一个监听类来接收回调事件:
```cpp
sdkbox::IAP::setListener(listener);
```
